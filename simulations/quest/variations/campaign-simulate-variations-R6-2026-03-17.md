Written to `simulations/quest/golden/campaign-simulate-variate-R6-2026-03-17.md`.

---

# campaign-simulate -- Round 6 Variations

**Three new axes, all sharing a common structural pattern:** each upgrades a prose or checkbox obligation in R5 V-05 into a named verification table.

## Axis assignments

| Axis | Label | What it upgrades | Structural mechanism |
|------|-------|-----------------|---------------------|
| A | Remediation Quality Gate | Pre-output checklist bullet "Remediation entries match template" | Per-remediation table: Verb / Target / Location / Conformance |
| B | Entity Coverage Matrix | Sub-skill sentinel rows (C-16) | Per-entity matrix: COVERED / CLEAN / SKIPPED -- extends C-16 from sub-skill to entity granularity |
| C | Post-Synthesis Blast Radius Re-Assessment | Cross-skill synthesis gate output orphaned from ranked table | Propagates pattern Combined Blast Radius back into findings; produces revised ranked table |

## Variation assignments

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | A only | Remediation Quality Gate table makes vague verbs and missing locations structurally visible the way Type Vocabulary Verification makes type drift visible |
| V-02 | B only | Entity Coverage Matrix surfaces silently skipped entities that sub-skill sentinel rows can't detect |
| V-03 | C only | Blast Radius Re-Assessment Gate closes the feedback loop between synthesis output and ranked output -- without it, P-ID "Combined Blast Radius" is a finding with no effect on the primary deliverable |
| V-04 | A + B | Covers both output-quality (remediation) and input-coverage (entity) silent failure modes in one pass |
| V-05 | A + B + C | Full combination; all of R5 V-05 architecture forward; no compliance requirement satisfied by prose alone |

## New rubric candidates surfaced

- **C-26 (potential)**: Remediation Quality Gate produces a per-remediation verification table — upgrades "All Remediation entries match template" from checklist bullet (process) to named table (structure). Same prose-to-structure upgrade relation as C-17/C-22/C-24.
- **C-27 (potential)**: Entity Coverage Matrix makes entity-level examination completeness verifiable — extends C-16's sub-skill sentinel rule down to entity granularity. An entity row showing SKIPPED is equivalent to a missing sub-skill row.
- **C-28 (potential)**: Blast Radius Re-Assessment Gate propagates cross-skill pattern elevations back into the ranked table — findings in patterns carry "(ELEVATED by P-ID)" in Blast Rationale. C-24 gates on pattern extraction; C-28 gates on pattern propagation.
