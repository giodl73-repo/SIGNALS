## campaign-decide R18 — Scoring Report

**Rubric**: v17 (max 108.0) | **Variations**: V-01 through V-05

---

### All Variations: 107.5 / 108.0 (tied)

All five variations pass all Essential (60.0) and Recommended (30.0) criteria. Aspirational score is 17.5/18.0 across the board — the single deduction is **C-23 FAIL** on all variants: the Phase 1b FINDING REGISTER uses a bare `Note` column header, which C-23 explicitly lists as a generic placeholder. This is an inherited R17 V-05 baseline issue, not variation-specific.

The R18 variation axes (PRE-COMMITMENT block, challenge register, evidence density closure) are not yet captured by any existing criterion — they surface as **C-45** and **C-46** candidates.

---

### Rankings (by structural innovation depth)

| Rank | Var | Score | Notes |
|------|-----|-------|-------|
| 1 | V-05 | 107.5 | All three R18 axes — most complete lifecycle chain |
| 2 | V-04 | 107.5 | PRE-COMMITMENT + density closure (C-45 + C-46 candidates, confirmed non-interacting) |
| 3 | V-01 | 107.5 | PRE-COMMITMENT block only — C-45 candidate isolated |
| 4 | V-03 | 107.5 | Density closure only — C-46 candidate isolated |
| 5 | V-02 | 107.5 | Challenge register — no new criterion candidate |

---

### Excellence Signals (from V-05)

**1 — Complete document-lifecycle accountability chain**

V-05 closes all unanchored positions in document lifecycle simultaneously:

| Position | Structural artifact |
|----------|-------------------|
| Document start | PRE-COMMITMENT block — plain-form prior lock before schema |
| Preamble | SCHEMA PREAMBLE temporal annotations in column headers (C-43) |
| Phase entry | `[min: N]` evidence count annotation in header (C-44) |
| Phase close | Density closure `Evidence density: [actual] of [min]` (C-46) |
| Phase 5 header | Named fill-forward directive (C-39/C-41) |

No lifecycle position is structurally unanchored.

**2 — Schema-free prior lock (C-45 candidate)**

PRE-COMMITMENT block appears *before* SCHEMA PREAMBLE, so hypotheses are committed before any column structure is visible. This forecloses schema-conformance pressure shaping hypothesis content — a failure mode C-13 cannot prevent (C-13 only requires `Prior Confidence` inside Phase 0 rows, which can still be written while reading the schema). V-05 traces the chain: PRE-COMMITMENT → Phase 0 transcription → Phase 5 calibration delta, making accountability verifiable at three structural points.

**3 — Header-entry / footer-close evidence count audit pair (C-46 candidate)**

C-44 (header `[min: N]`) paired with the density closure annotation creates a two-point audit per evidence phase. C-44 alone requires reading the table body to verify the minimum was met. The density annotation creates a structural confirmation artifact at close time — under-population is detectable without body-reading at *either* point. V-04 confirmed C-45 and C-46 are independent and additive with no interaction degradation.

---

### C-23 Fix Path

Rename Phase 1b FINDING REGISTER `Note` column → `Response Strategy Note` or `RS-Note` to make the semantic explicit in the header. Only barrier to 108.0/108.0.

---

```json
{"top_score": 107.5, "all_essential_pass": true, "new_patterns": ["PRE-COMMITMENT block positioned before SCHEMA PREAMBLE captures plain-form analyst priors before any schema column structure is visible, creating a schema-free prior lock that prevents schema-conformance pressure from shaping hypothesis content — C-45 candidate", "Evidence density closure annotation per phase (Evidence density: [actual count] of [min] — gate clears when actual >= min) creates a structural footer-close confirmation artifact that pairs with the C-44 header-entry minimum annotation, enabling under-population detection at both phase entry and phase close without reading the table body — C-46 candidate"]}
```
