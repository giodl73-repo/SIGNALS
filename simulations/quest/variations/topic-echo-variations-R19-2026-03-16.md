Written to `simulations/quest/golden/topic-echo-variate-R19-2026-03-16.md`.

---

## Round 19 Variations: `topic:echo`

Five complete prompt bodies targeting C-58, C-59, C-60. Each builds on R18 V-05 (335/335 under v18).

### Variation axes

| # | Axis | New Declaration | C-58 | C-59 | C-60 | v19 |
|---|------|----------------|:----:|:----:|:----:|:---:|
| V-01 | A only | `GATE-TOKEN-REGISTRY` before Step 0 | PASS | FAIL | FAIL | 340 |
| V-02 | B only | `MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX` (extends MANIFEST-COMPLETE format) | FAIL | PASS | FAIL | 340 |
| V-03 | C only | `CROSS-LAYER CITATION CONSISTENCY PROTOCOL` (Step 9) | FAIL | FAIL | PASS | 340 |
| V-04 | A+B | Registry + extended manifest token | PASS | PASS | FAIL | 345 |
| **V-05** | **A+B+C** | All three + GT-04 in registry | **PASS** | **PASS** | **PASS** | **350** |

### What each axis does

**Axis A (C-58) -- GATE-TOKEN-REGISTRY:** A four-row table (`GT-01..GT-04`) declared at heading level before Step 0, listing each gate token's canonical name, step location, and prerequisite criterion. Token completeness becomes diff-detectable: reviewer diffs the registry against emitted tokens rather than scanning the full artifact. Applies the C-44/C-52 traversal-free completeness contract to the token layer itself.

**Axis B (C-59) -- MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX:** Extends the TOKEN CONTENT REQUIREMENT's MANIFEST-COMPLETE format to carry `(confirming artifact INLINE in all [Q] rows)` after the TYPE-C count. The terminal manifest token now self-certifies both citation accounting (C-52) and inline-evidence presence (C-57) from token text alone -- no manifest table consultation needed for either condition.

**Axis C (C-60) -- Step 9 Cross-Layer Check:** A new post-manifest step producing a per-citation-pair table: Citation-ID | Belief-Ref-artifact (from STILL-LIVE FILTER) | Status-Cell-artifact (from manifest STATUS) | MATCH/MISMATCH. `CROSS-CITATION-CONSISTENT` (GT-04) emitted only when all rows MATCH; any MISMATCH is a hard gate. Closes the gap where C-54 and C-57 each verify one reference direction but no prior criterion verifies both directions name the same source.

### V-05 structural coherence

The three R19 declarations form a coherent closure-layer contract at the token/registry layer:
- Token **set** auditable by registry (C-58)
- Terminal manifest token self-certifying for the **full** closure layer (C-59)
- Cross-layer evidence references verified **per pair** (C-60)
