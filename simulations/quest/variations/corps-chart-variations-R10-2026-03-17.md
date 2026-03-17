Here are the 5 variations for Round 10, targeting the three new rubric criteria:

---

## Variation Summary

| ID | Axis | New Criteria | Hypothesis |
|----|------|--------------|------------|
| **V-01** | BEFORE-PRODUCE back-reference (single) | C-26 | FORMAT CONTRACT is read once at document head; by PRODUCE time, 1,000+ tokens have elapsed and schema constraints may have faded. A labeled `BEFORE PRODUCING: re-read FORMAT CONTRACT schema (N)` directive immediately before each governed PRODUCE command converts schema compliance from recall into per-step active reference. Closes the temporal gap between DISQUALIFY-IF and VERIFY. Baseline: R9 V-01 (no ROLE-NAME LOCK, no vocab blocks). |
| **V-02** | Key Roles as explicit fifth CHECK site (single) | C-27 | C-21 enumerated four mandatory CHECK sites; Key Roles was the ungoverned fifth role-consuming column. V-02 explicitly lists it as the fifth mandatory site inside the ROLE-NAME LOCK block's site enumeration, with a dedicated labeled `CHECK [SITE 5 -- KEY ROLES]` instruction at the headcount table command. Baseline: R9 V-02 (four-field Rebuttal, ROLE-NAME LOCK). |
| **V-03** | Per-cell row-by-row role-lock (single) | C-28 | Column-level CHECK instructions apply once at instruction time; memory-decay within a multi-row table produces compliance-drift where early rows comply but later rows introduce novel names. V-03 adds "verify before populating the next row -- do not complete the table and verify after" for both DRI/Owner and Key Roles columns. Baseline: R9 V-03 (strict mandatory DRI/Owner). |
| **V-04** | C-26 + C-27 (combination) | C-26, C-27 | Two orthogonal extensions: C-26 fires at every PRODUCE command (temporal coverage), C-27 adds the fifth governed column (spatial coverage). DRI/Owner per-cell is the open variable. Baseline: R9 V-04 (FORMAT CONTRACT DISQUALIFY-IF + four-field Rebuttal + vocab blocks). |
| **V-05** | C-26 + C-27 + C-28 full integration | C-26, C-27, C-28 + all prior | Maximum stack on R9 V-05. Adds: labeled BEFORE-PRODUCE at every schema-governed command, Key Roles as enumerated fifth site in ROLE-NAME LOCK block, per-cell directives for DRI/Owner **and** Key Roles. Three non-overlapping failure modes closed: format-evasion (C-26), role-site coverage gap (C-27), within-table row-drift (C-28). |

**Key design decision in all variations**: C-26's BEFORE PRODUCING directive names the specific schema by number and label (e.g., `schema (1) -- HEADCOUNT BY AREA`) and explicitly states what condition will not be met -- making it a confirmation of non-violation rather than a generic re-read instruction. C-27's fifth-site enumeration appears inside the ROLE-NAME LOCK block itself, so the site list is co-located with the role list it governs. C-28's per-cell language uses the exact "before populating the next row -- do not complete the table and verify after" formulation that the rubric evidence identified as the mechanism.
