Written to `simulations/quest/golden/listen-support-variate-R5-2026-03-15.md`.

---

## R5 — listen-support Variations Summary

**Baseline:** R4 V-05 scores 98.18 under v5 (C-18 + C-19 both FAIL). All 5 variations inherit the full R4 V-05 mechanism set.

**Three single-axis variations (how to close C-18 and C-19):**

| | Axis | C-18 mechanism | C-19 gate |
|-|------|---------------|-----------|
| **V-01** | Output format | Compact `Cell ID` (`SRE-P1`) at all 3 levels: matrix row header → STEP 3B column → body headline `*(Cell: XX-P#)*` | 4-item standalone block |
| **V-02** | Lifecycle emphasis | VM Row IDs retained from R4 V-05; body *metadata subline* cites VM Row ID (2/3 nodes — C-18 PARTIAL expected) | 5-item standalone blocking gate naming artifacts by section name |
| **V-03** | Phrasing register | Semantic `REG-ID` scheme (`REG-SRE-SETUP`) at all 3 levels: matrix row → STEP 3B column → body headline `*(Reg: REG-xxx-TYPE)*` | 3-item gate (minimum pass) |

**Two combined variations:**

| | Combination | C-18 | C-19 | Predicted composite |
|-|-------------|------|------|---------------------|
| **V-04** | V-01 Cell IDs + V-02 5-item gate | Chain complete | 5-item blocking, artifact-named | 100 |
| **V-05** | R4 V-05 base + VM Row ID headline annotation + 5-item blocking gate | Chain complete | 5-item blocking, artifact-named, explicit blocking declaration | 100 |

**Key design decision exposed:** V-02 isolates whether the VM Row ID in a *metadata subline* satisfies C-18 or not. V-04/V-05 close the ambiguity by putting the ID in the body headline itself. The R5 scorecard will confirm whether `*(VM: ...)` at headline vs `VM Row: ...` at metadata subline produces different C-18 rulings.
