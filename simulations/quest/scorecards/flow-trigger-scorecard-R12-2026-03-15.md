format not explicitly rendered in shown text. C-21 passes, no breach format visible → weak pass.
- V-04/V-05: Inherit EC-03 breach token definition from R11 V-05 base (`[PROHIBITION BREACH: Role N | name]` + CLOSURE CHECK counter). PASS.

**C-25 — Named lifecycle gate with typed exit conditions**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | PARTIAL | PARTIAL | PARTIAL | **PASS** | **PASS** |

- V-01/V-02/V-03: Phase 0 named; job statement references "Status: SATISFIED" but exit conditions are not a numbered list (EC-01…EC-N) with typed Status column. No explicit EXIT SIGNAL statement issued. PARTIAL.
- V-04/V-05: 8-column registry carries typed Status values per EC row; EXIT SIGNAL derives from "N/N SATISFIED" aggregate. PASS.

**C-26 — INERTIA CONTRAST embedded rationale**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | FAIL | FAIL | FAIL | **PASS** | **PASS** |

- V-01/V-02/V-03: No INERTIA CONTRAST section or equivalent contrast-column mechanism.
- V-04: Inline "Weaker alternative" + "Failure mode" columns in 8-column registry satisfy C-26 via C-29 mechanism (≥2 mechanisms with named failure modes).
- V-05: Standalone INERTIA CONTRAST section opens with "anonymous prohibition" (C-30 rationale) and "anonymous artifact gap" (C-31 rationale), plus retains inline contrast columns. Named section with ≥2 mechanisms and concrete failure modes. PASS.

**C-27 — Computable Phase 0 exit signal**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | PARTIAL | PARTIAL | PARTIAL | **PASS** | **PASS** |

- V-01/V-02/V-03: "Status: SATISFIED" mentioned in Phase 0 job description; no typed Status column with aggregate count. PARTIAL.
- V-04/V-05: Status column (column 3 in 8-column registry); "N/N SATISFIED" aggregate in EXIT SIGNAL statement. Recomputable by column scan. PASS.

**C-28 — Per-obligation refutation conditions**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | FAIL | FAIL | FAIL | **PASS** | **PASS** |

- V-01/V-02/V-03: No "Violated if:" clauses in Phase 0 artifact sections. FM-40 fires for missing activation anchor (a Phase 0 structure violation), but that is not the same as a co-located refutation condition per obligation.
- V-04/V-05: "Violated if" is column 4 in the 8-column registry; string-detectable breach condition per row. PASS.

**C-29 — INERTIA CONTRAST as typed inline columns**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | FAIL | FAIL | FAIL | **PASS** | **PASS** |

- V-01/V-02/V-03: Separate artifact tables; no "Weaker alternative" / "Failure mode" columns in ARTIFACT MANIFEST or any Phase 0 registry.
- V-04/V-05: Columns 5 ("Weaker alternative") and 6 ("Failure mode") defined in 8-column registry header; all mechanism rows carry non-empty values in both columns.

**C-30 — Temporally-anchored prohibition activation events (new)**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | **PASS** | FAIL | FAIL | **PASS** | **PASS** |

- V-01: PROHIBITION CONTRACTS table has "Activation Event" column. PROH-01 cites EC-04; PROH-02 cites EC-03. FM-40 in catalog. Effective period determinable by reading Phase 0 registry. PASS.
- V-02: Manifest axis only; prohibition table lacks Activation Event column.
- V-03: Ordering axis; no Activation Event column.
- V-04: "Activation Event" is column 7 in 8-column registry; prohibition rows carry EC-ID activation anchors. PASS.
- V-05: Lifecycle emphasis implements temporal anchor; INERTIA CONTRAST opens with "anonymous prohibition" failure mode, making the rationale for the anchor non-separable from its declaration. PASS.

**C-31 — Role-attributed artifact production mandate (new)**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| | FAIL | **PASS** | PARTIAL | PARTIAL | **PASS** |

- V-01: ARTIFACT MANIFEST has columns ART-ID \| Artifact \| Purpose — no Producing Role or Production Phase.
- V-02: ARTIFACT MANIFEST adds "Producing Role" + "Production Phase" as named columns; CLOSURE CHECK attributes gaps to named roles ("ART-02 (EXCLUSION LOG) — Role 1 (Auditor): ABSENT"). Both manifest fields explicit. PASS.
- V-03: Role definitions in production order create implicit role-artifact binding but "Producing Role" is not a manifest column or inline typed label. PARTIAL per C-31 pass condition ("explicit manifest fields").
- V-04: "Producing Role" is column 8 in the 8-column registry; artifact rows carry role attribution. "Production Phase" is implicit (all Phase 0 artifacts are produced in Phase 0) — not a separate named column. PARTIAL: role explicit, phase implicit.
- V-05: INERTIA CONTRAST opens with "anonymous artifact gap" failure mode naming both role AND phase as required fields. This forces the manifest to carry both explicitly as named fields. CLOSURE CHECK references role for artifact attribution. PASS.

---

### Full Criterion Matrix

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 | P | P | P | P | P |
| C-10 | P | P | P | P | P |
| C-11 | P | P | P | P | P |
| C-12 | P | P | P | P | P |
| C-13 | P | P | P | P | P |
| C-14 | P | P | P | P | P |
| C-15 | P | P | P | P | P |
| C-16 | P | P | P | P | P |
| C-17 | P | P | P | P | P |
| C-18 | P | P | P | P | P |
| C-19 | ~P | ~P | ~P | ~P | ~P |
| C-20 | ~P | ~P | ~P | ~P | ~P |
| C-21 | P | P | P | P | P |
| C-22 | P | P | P | P | P |
| C-23 | P | P | P | P | P |
| C-24 | ~P | ~P | ~P | P | P |
| C-25 | ~P | ~P | ~P | P | P |
| C-26 | F | F | F | P | P |
| C-27 | ~P | ~P | ~P | P | P |
| C-28 | F | F | F | P | P |
| C-29 | F | F | F | P | P |
| C-30 | **P** | F | F | **P** | **P** |
| C-31 | F | **P** | ~P | ~P | **P** |

*P = PASS, ~P = PARTIAL (0.5), F = FAIL*

---

### Aspirational Point Totals

| Variation | PASS | PARTIAL | FAIL | Weighted (of 23) |
|-----------|------|---------|------|------------------|
| V-01 | 14 | 5 | 4 | 14 + 2.5 = **16.5** |
| V-02 | 14 | 5 | 4 | 14 + 2.5 = **16.5** |
| V-03 | 13 | 6 | 4 | 13 + 3.0 = **16.0** |
| V-04 | 20 | 3 | 0 | 20 + 1.5 = **21.5** |
| V-05 | 21 | 2 | 0 | 21 + 1.0 = **22.0** |

---

### Composite Scores

| Rank | Variation | Essential | Recommended | Aspirational | **Composite** | Golden? |
|------|-----------|-----------|-------------|-------------|--------------|---------|
| 1 | **V-05** | 60.00 | 30.00 | 9.57 | **99.57** | YES |
| 2 | **V-04** | 60.00 | 30.00 | 9.35 | **99.35** | YES |
| 3 | V-01 | 60.00 | 30.00 | 7.17 | **97.17** | YES |
| 3 | V-02 | 60.00 | 30.00 | 7.17 | **97.17** | YES |
| 5 | V-03 | 60.00 | 30.00 | 6.96 | **96.96** | YES |

Aspirational formula: `weighted_asp / 23 × 10`. All variations: all essential PASS, composite ≥ 80.

---

### Key Discriminators

**V-04 vs V-05 (9.35 vs 9.57):** C-31 is the sole difference.
- V-04: `Producing Role` column 8 in registry; `Production Phase` implicit (Phase 0 context). PARTIAL.
- V-05: INERTIA CONTRAST opening with "anonymous artifact gap" failure mode names both role and phase as required fields, forcing the manifest to carry both explicitly. PASS.

**V-01 vs V-02 (both 97.17):** Symmetric: V-01 gains C-30/loses C-31; V-02 gains C-31/loses C-30. Neither satisfies both new criteria.

**V-03 (96.96):** Loses both new criteria (C-30 FAIL, C-31 only PARTIAL) and gains nothing that V-01/V-02 don't have.

**V-04/V-05 gap from V-01–V-03:** Building on the R11 V-05 7-column registry foundation provides 6 criteria (C-24, C-25, C-26, C-27, C-28, C-29) that all flip from PARTIAL/FAIL to PASS — a 4.5-point aspirational swing in a single structural decision.

---

### Excellence Signals from V-05

**Signal 1 — Dual-criterion rationale anchor via INERTIA CONTRAST opening.**
V-04 implements both C-30 and C-31 mechanisms but the rationale for each is not co-located with the mechanisms — a future variation could weaken one mechanism while preserving the other without encountering a rationale-level signal. V-05 opens the INERTIA CONTRAST with both "anonymous prohibition" and "anonymous artifact gap" failure modes, creating a single section that motivates both criteria simultaneously. Removing either mechanism now produces a visible gap between the INERTIA CONTRAST claim and the manifest structure.

**Signal 2 — Named failure mode as structural completeness forcing function.**
"Anonymous artifact gap" (missing artifact traceable to no owner) names the failure state for C-31. To fix "anonymous" requires identifying both who (role) and when (phase). The named failure mode therefore forces the manifest to carry *both* `Producing Role` and `Production Phase` as explicit fields — not just the role. This is what converts V-04's C-31 PARTIAL into V-05's PASS: the failure mode description enforces field completeness at definition time rather than requiring a separate completeness check.

**Signal 3 — Zero-new-fail at 22/23.**
V-05 has no FAIL criteria for the first time in R12 variations. The two remaining PARTIAL criteria (C-19 and C-20) are Phase 5/6 structural issues unaddressed by any Phase 0 variation — they represent the current ceiling for Phase 0-only changes. V-05 has reached the maximum achievable score without modifying Phase 5 verdict blocks or Phase 6 closure templates.

---

```json
{"top_score": 99.57, "all_essential_pass": true, "new_patterns": ["INERTIA CONTRAST as simultaneous dual-criterion rationale anchor: opening with both C-30 and C-31 failure modes from a single section ensures neither criterion's rationale can be silently dropped in future variations — extends single-criterion co-location to multi-criterion scale", "Named failure mode as structural completeness forcing function: explicitly naming 'anonymous artifact gap' forces the manifest to carry BOTH producing role AND production phase (fixing anonymous requires naming both fields), converting C-31 from PARTIAL to PASS and showing that failure mode names can drive field-level completeness of the implementing mechanism"]}
```
