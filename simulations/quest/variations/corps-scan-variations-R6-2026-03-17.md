Written to `simulations/quest/golden/corps-scan-variate-R6-2026-03-17.md`.

---

## Variate R6 -- corps-scan

Five complete prompt variations targeting the v6 rubric (270 pts, 27 criteria).

### New criteria treated as structural invariants across all variations

| Criterion | How applied in R6 |
|-----------|-------------------|
| **C-23** detected-from: in YAML | Explicit IVR triple in all variations (IVR-3B/IVR-P3-B/IVR-4B); repair says "traceability must appear in the YAML itself" |
| **C-24** Pivot candidates enumerated | Dedicated IVR triple in all variations; VIOLATION block explicitly names the "YES/POSSIBLE/NO table without rejection reasons" anti-pattern |
| **C-25** Phase-scoped labels | All triples labeled IVR-1A/IVR-2B/IVR-P1-A/IVR-P2-D etc. Meta-rule counts them to verify completeness |
| **C-26** Meta-rule closing constraint set | Preamble in every variation: "Any directive not expressed as a labeled IVR triple is advisory only. 14 labeled triples -- count to verify." |
| **C-27** Conditional advance instruction | Every Completion Test ends with "Advance to X: only if all YES. If any NO: resolve before continuing." |

### Variation axes

| Variation | Axis | Key hypothesis |
|-----------|------|----------------|
| **V-01** | Inertia framing | Status-quo competitor (Confluence/recall) named at each phase makes traceability discipline feel motivated |
| **V-02** | Lifecycle emphasis | Formal ENTRY/EXIT contracts per phase make C-27 structural by construction |
| **V-03** | Phrasing register (conversational imperative) | Direct commands lower activation energy; tests whether model internalizes constraints in a colloquial register |
| **V-04** | Inertia framing + lifecycle emphasis | WHY (inertia context) + HOW (entry/exit contracts) -- highest compliance hypothesis |
| **V-05** | Role sequence + inertia framing | 4-role with dedicated Inertia Auditor (ROLE 2) that primes the scan with "manual gaps" before the Repo Archaeologist runs |

V-05 adds ROLE 2 (Inertia Auditor) as the structural novelty -- this role enumerates C-24 pivot rejection reasons with inertia framing before the inventory phase, and its ROLE 2 gap check (IVR-3D) creates a cross-role traceability loop.
