v17 written to `simulations/quest/rubrics/scout-inertia-rubric-v17-2026-03-17.md`.

---

## v16 → v17 summary

**Two new criteria extracted from R16 scorecard:**

| # | Criterion | Source signal | Confirmed by |
|---|-----------|---------------|--------------|
| A-40 | **Engineering-register locus noun in compound failure noun** | V-02's `STRUCTURAL FAULTS` scoring note: "FAULTS is a technically more precise locus noun — fault = specific defect plane vs. weakness = general vulnerable zone"; engineering fault taxonomy terms (FAULTS, FAILURE PLANES, FRACTURE ZONES) are distinguishable from general vulnerability vocabulary (WEAKNESSES, GAPS, VULNERABILITIES) within A-38-passing forms | R16 V-02 |
| A-41 | **Architectural-scope TYPE component in compound failure noun** | V-01 and V-02 both use STRUCTURAL as the TYPE component; scoring note "TYPE=structural (architectural/systemic category)" explicitly classifies STRUCTURAL as an architectural scope category, distinguishing it from event-descriptor TYPEs (FAILURE, ERROR, DEFECT) used in V-03/V-04 compound nouns | R16 V-01 and V-02 |

**Ceiling: 250 → 260**

**New implication chains:**
- `A-40 implies A-38 implies A-34 implies A-26 implies A-10 and A-14`
- `A-41 implies A-38 implies A-34 implies A-26 implies A-10 and A-14`
- A-40 and A-41 are **independent of each other**: `STRUCTURAL WEAKNESSES` satisfies A-41 (architectural TYPE) but fails A-40 (general locus). `STRUCTURAL FAULTS` satisfies both.

**R17 target**: A variation using `STRUCTURAL FAULTS` as the compound failure noun satisfies A-40 (FAULTS = engineering locus) and A-41 (STRUCTURAL = architectural TYPE) simultaneously, achieving 260/260 on the full scaffold.
