---

# corps-committee -- Prompt Variations R18

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | C-49 only — BEFORE YOU START cites `C-46 miss` + explicit pair list | Pre-flight names the current governing criterion and enumerates `C-42, C-43, C-44, C-45, or any later pair`; FAILS template ends at C-45 — no C-46/C-47/C-48 entries (C-50 absent) |
| **V-02** | C-50 only — FAILS template gains C-46/C-47/C-48 entries | Template carries all three new CORRECT entries; BEFORE YOU START retains `C-44 miss` with stale pair list `C-42, C-43, or any later pair` (C-49 absent) |
| **V-03** | Output format — Phase 3 prose blocks instead of table rows | Neither C-49 nor C-50; tests whether table format is load-bearing for C-01–C-48 criteria; STANCE/CITE/RESPONDS-TO labels preserved as named fields within prose blocks |
| **V-04** | Combination: C-50 full + C-49 partial | Template has C-46/C-47/C-48 (C-50 satisfied); pre-flight cites `C-46 miss` but keeps old pair list `C-42, C-43, or any later pair` — citation correct, enumeration imprecise |
| **V-05** | Full integration: C-49 precise + C-50 full | Pre-flight cites `C-46 miss` AND lists `C-44, C-45` explicitly; template carries C-46/C-47/C-48 entries; both new criteria fully satisfied; all prior criteria inherited from R17 V-05 |

## Key Differentiators Per Variation

| | BEFORE YOU START C-47 line | FAILS template ceiling | Phase 3 format |
|---|---|---|---|
| V-01 | `C-42, C-43, C-44, C-45 ... C-46 miss` | C-45 | table |
| V-02 | `C-42, C-43 ... C-44 miss` | **C-48** | table |
| V-03 | `C-42, C-43 ... C-44 miss` | C-45 | **prose** |
| V-04 | `C-42, C-43 ... C-46 miss` (stale list) | **C-48** | table |
| V-05 | `C-42, C-43, C-44, C-45 ... C-46 miss` | **C-48** | table |

## Two New Axes Introduced (C-49, C-50)

**C-49 precision gap** (V-04 vs V-05): V-04's pre-flight cites `C-46 miss` — correct criterion — but the pair list reads `C-42, C-43, or any later pair`, requiring inference. V-05 explicitly names `C-44, C-45` so the pair list self-documents without relying on `any later pair` as a catch-all. A reviewer following V-04's halt would look for a C-46 violation (correct) but would need to reconstruct which pairs require entries from the rubric history rather than reading them off the pre-flight directly.

**C-50 recursion** (V-01/V-03 vs V-02/V-04/V-05): V-01 and V-03 carry no FAILS entries for the R17 triplet (C-46/C-47/C-48). A reviewer encountering a missing ICB section, a stale template pre-flight, or a missing preamble pre-flight has no canonical citation in the FAILS template. V-02, V-04, V-05 all carry entries for all three — a C-46, C-47, or C-48 violation can be cited by label from the template directly.

**V-05 is the only variation where both mechanisms are simultaneously satisfied** — citation names the correct governing criterion, pair list is explicit, and template is current through the C-46/C-47/C-48 triplet.

Written to: `simulations/quest/golden/corps-committee-variate-R18-2026-03-17.md`
