Done. Here's the R20 output:

---

**Written**: `simulations/quest/golden/org-scan-variate-R20-2026-03-16.md`

## Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Lifecycle emphasis | C-73 preamble manifest — `PREAMBLE DECLARATION MANIFEST` block publishes an explicit count (10 total: 2 named protocols + 8 schemas) before GROUP A; any constraint absent from the count is a C-73 violation detectable without reading phase bodies |
| **V-02** | Output format | C-71 phase footer compliance tokens — every `PHASE OUTPUTS` block carries named `MET / NOT MET` tokens for all 8 floor-constrained criteria in GROUP A and 6 in GROUP B; creates a second independent verification path for every floor criterion |
| **V-03** | Phrasing register | C-72 schema-first reference as named convention — 8 phase instruction sites carry `"[data type] declared in [SCHEMA NAME] (see PREAMBLE SCHEMA DECLARATIONS — [list] not restated here per schema-first reference pattern)"` annotations; re-enumeration in any instruction is a structurally detectable named violation |
| **V-04** | Role sequence | C-70 TABLE F gate-blocking — gate checklist grows to 8 items; `GATE TOKEN PROTOCOL` defines a separate `TABLE F FAIL STRING` named constant distinct from the generic `FAIL TOKEN`; TABLE F non-compliance produces the named string, independently identifiable without parsing `FAIL TOKEN` reason fields |
| **V-05** | Combined | All four new criteria together — preamble manifest declares what must exist (C-73), named convention annotations reference it by name throughout phases (C-72), footer compliance tokens confirm what was produced (C-71), TABLE F FAIL STRING enforces transport manifest at gate time (C-70); every criterion C-67–C-73 is verifiable from three independent locations: preamble, instruction annotation, footer token |

**New criteria coverage distribution**:
- C-70 (TABLE F gate-blocking): V-04 + V-05
- C-71 (footer MET/NOT MET tokens): V-02 + V-05
- C-72 (named convention in phase instructions): V-03 + V-05
- C-73 (preamble declaration count manifest): V-01 + V-05

V-05 is the only variation that achieves all four simultaneously.
