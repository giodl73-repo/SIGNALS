Saved to `simulations/quest/rubrics/prove-prototype-rubric-v10-variate-R10-2026-03-15.md`.

---

## Round 10 — prove-prototype (v10, 232 pts)

**Why R9-V-03 fails both C-31 and C-32 simultaneously:**

- **C-31 gap**: R9-V-03 lists "inertia competitor identification" in FRAMER's Must NOT Write column, but a column entry is not an explicit routing declaration. C-31's criterion description requires the prohibition to state the content "must NOT appear in DESIGN and must reside exclusively in CALIBRATE." Without routing language, a role-label scan detects that FRAMER excluded it but cannot verify CALIBRATE is the required destination.

- **C-32 gap**: R9-V-03's CALIBRATE COMPLETE says "inertia competitor identified, B-00 committed, outperform threshold stated" — the three labels are present, but B-00 is a label without its value. C-32 requires "B-00 committed with its value" so a scan-only auditor can confirm the triple without reading the container body.

---

**Variation map:**

| Variation | Axis | Key Change | Hypothesis |
|-----------|------|------------|------------|
| **V-01** | C-31 (single) | FRAMER prohibition adds routing text: "prohibited in DESIGN — belongs exclusively in CALIBRATE" in three locations | Routing language alone satisfies C-31 independent of CALIBRATE structure |
| **V-02** | C-32 (single) | CALIBRATE COMPLETE embeds: `inertia competitor identified = "[name]", B-00 committed = [value], outperform threshold stated = [condition]` | Value embedding alone satisfies C-32 independent of FRAMER prohibition |
| **V-03** | Lifecycle emphasis (single) | CALIBRATE header enumerates three single-function responsibilities as a numbered list | Enumerated header makes the three-element audit contract visible before Phase 4 is read |
| **V-04** | C-31 + C-32 (combined) | V-01 routing language + V-02 value embedding, both applied | Both C-31 and C-32 can be satisfied simultaneously without regression |
| **V-05** | C-31 + C-32 + C-30 (combined) | V-04 + three-column table in Phase 7 | R10 ceiling attempt: 225+ pts |

**R10 ceiling candidate**: V-05 targets all three new/reinforced criteria (C-31, C-32, C-30) simultaneously. V-04 is the safe baseline — if V-05 shows regression, V-04 isolates the cause to Phase 7.
