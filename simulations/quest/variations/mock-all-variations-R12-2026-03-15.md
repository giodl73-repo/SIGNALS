`simulations/quest/golden/mock-all-variate-R12-2026-03-15.md` written.

---

## Round 12 Summary

**Two new criteria this round: C-26 and C-27 (denominator 17 -> 19)**

| C | What it requires | Chain it enables |
|---|-----------------|-----------------|
| C-26 | Inertia gap skeleton cells contain namespace-specific content at table construction time -- not "TBD" deferred to ROLE 2 | Unlocks C-10 and C-17: next steps and vocabulary can be derived from the table row directly |
| C-27 | ROLE 1 stop-gate enumerates the table's own column header names verbatim | Side-effect cascade: gate cannot be written before columns are declared, so C-11 and C-14 auto-pass |

**Variation axis assignments:**

| Variation | Single/Combined | Axis | C-26 | C-27 | Predicted |
|-----------|----------------|------|------|------|-----------|
| V-01 | Single | Role sequence -- skill pre-seeds skeleton cells in template | PASS | FAIL | 18/19 |
| V-02 | Single | Output format -- verbatim column headers in stop-gate | UNCERTAIN | PASS | 17-18/19 |
| V-03 | Single | Phrasing register -- conversational descriptive | PARTIAL | FAIL | ~15/19 |
| V-04 | Combined | Template seeds + verbatim gate (ceiling) | PASS | PASS | 19/19 |
| V-05 | Combined | Verbatim gate + explicit column-declaration lifecycle step | UNCERTAIN | PASS | 18-19/19 |

**Key diagnostic from V-03:** tests the floor -- a conversational skill that does not pass C-26 or C-27 confirms both criteria require explicit structural choices beyond natural prose.

**C-26 winning form (V-01/V-04):** the skill itself provides the seed phrases; the model reads them into cells rather than inventing them. This is "authored at classification time" in the strongest possible sense.

**C-27 winning form (V-02/V-04/V-05):** declare column names canonically, then write the gate to name those exact strings. Structural self-reference created by construction, not by discipline.
