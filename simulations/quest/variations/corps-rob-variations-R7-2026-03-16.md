Written to `simulations/quest/golden/corps-rob-variate-R7-2026-03-16.md`.

---

## Variate R7 -- corps-rob

**R7 focus**: The three new v7 criteria (C-25, C-26, C-27) were present incidentally in R6 but never the primary axis.

---

### Variation Axes Selected

| Axis | Used In | Target |
|------|---------|--------|
| Triage Note field-level compliance -- three-condition schema, zero-state enumerates all conditions | V-01 | C-25 |
| Named audit rule with labeled anti-pattern declarations (ANTI-PATTERN-1, ANTI-PATTERN-2) | V-02 | C-26 |
| Gap-scan absence as format error -- both sections carry "absence = format error" language | V-03 | C-27 |
| Field-level triage compliance + format error language -- two gap-scan protocol criteria | V-04 | C-25, C-27 |
| Full R7 stack on R6 V-05 base -- RULES A-N + RULES O, P, Q | V-05 | C-25, C-26, C-27 |

---

### V-01 -- Triage Note Field-Level Compliance Audit (C-25)

Upgrades R6 V-02's TRIAGE NOTE GAPS from section-presence checking to field-level compliance. The key mechanism: the zero-state block must enumerate all three conditions explicitly -- `(a) NONE / (b) NONE / (c) NONE` -- rather than just "TRIAGE NOTE GAPS: NONE". That single-line zero-state confirms only that no stages were missing their section; the three-condition enumeration confirms no field was missing and no placeholder survived.

### V-02 -- Named Audit Rule with Anti-Pattern Specification (C-26)

Upgrades R6 V-03's RULE AUDIT-SUITE from a named rule with prose rationale to a named rule with **two labeled anti-pattern declarations**: ANTI-PATTERN-1 (MERGED SECTION) and ANTI-PATTERN-2 (REPEATED DIMENSION). The anti-patterns are first-class rule elements -- addressable by label -- not prose embedded in the requirement description.

### V-03 -- Gap-Scan Absence as Format Error (C-27)

Extends R6 V-01's format error declaration (which covered only ROLE CONCERN GAPS) to cover **both** mandatory gap-scan sections. Both sections carry explicit format error declarations: "absence = format error" language in the format specification, not advisory language. RULE BOOKEND-AUDIT is the enforcement vehicle.

### V-04 -- Field-Level Triage + Format Error Language (C-25 + C-27)

Natural pairing: C-27 enforces that the gap-scan sections exist (format error on absence); C-25 enforces that TRIAGE NOTE GAPS checks at the right granularity when it does exist. RULE BOOKEND-AUDIT carries the format errors; RULE TRIAGE-AUDIT carries the three-condition schema. C-22 and C-23 follow as structural prerequisites.

### V-05 -- Full R7 Stack (C-25 + C-26 + C-27 on RULES A-N base)

RULES A-N from R6 V-05 (all C-11--C-24) plus:
- **RULE O** (C-25): three-condition schema + enumerated zero-state in TRIAGE NOTE GAPS
- **RULE P** (C-26): RULE AUDIT-SUITE with ANTI-PATTERN-1 and ANTI-PATTERN-2 as named declarations
- **RULE Q** (C-27): format error declarations on both gap-scan sections, using error/violation language

Theoretical maximum under v7: **185 points** (60 essential + 30 recommended + 95 aspirational).
