## Corps-Rob R8 Scorecard

### Scoring Formula
- Essential (C-01–C-05): pass fraction × 60
- Recommended (C-06–C-08): pass fraction × 30
- Aspirational (C-09–C-29): each criterion × 5 pts
- Dependency chain: C-25 → C-28 → C-29 (each requires prior pass)

---

## V-01 — Schema Grafted into RULE AUDIT-SUITE

Builds on R7 V-02 (which had C-26 but not C-25/C-28/C-29). Installs TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c) into the Triage Note Compliance section of the RULE AUDIT-SUITE, adding TRIAGE NOTE AUDIT RESULT block with per-condition enumeration.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage identity | PASS | `## Stage:` header + ROLE field in format |
| C-02 Role-loaded perspective | PASS | Role Concern section + role-specific calibration |
| C-03 ROB document format | PASS | Labeled findings, verdict, TPM block present |
| C-04 Actionable findings 2x | PASS | Minimum 2 per stage, owner + resolution required |
| C-05 Go/No-Go TPM | PASS | `### Go/No-Go` section with GO/NO-GO/GO WITH CONDITIONS |
| C-06 Cross-stage coherence | FAIL | No cross-referencing instruction across stages |
| C-07 Risk register TPM | PASS | Table with Severity, Likelihood, Mitigation, Status columns |
| C-08 Exec-office cascade | PASS | S-office mission by name required, abstract refs rejected |
| C-09 Inter-stage blocker | FAIL | No blocker detection instruction |
| C-10 Cross-cutting theme | FAIL | No theme elevation instruction |
| C-11 Conditional verdict | FAIL | No enumerated conditions instruction |
| C-12 Severity discrimination | PASS | MOST CRITICAL → HIGH / LEAST CRITICAL → LOW enforces spread |
| C-13 Risk register status | PASS | Status column: OPEN / WATCH / MITIGATED with 2+ required |
| C-14 Pre-finding calibration | PASS | Calibration Block; TRIAGE NOTE required when uniform |
| C-15 Update protocol | FAIL | No risk register update cadence section |
| C-16 Role-lens pre-declaration | PASS | `### Role Concern` + ROLE CONCERN field before Calibration |
| C-17 Enforcement audit | PASS | RULE AUDIT-SUITE audits calibration, role concern, triage note compliance |
| C-18 Universal triage note | PASS | "All three field labels required; present in every stage unconditionally" |
| C-19 Zero-deviation declaration | PASS | RULE ZERO-STATE + `CALIBRATION COMPLIANCE: ALL STAGES PASS`, `ROLE CONCERN GAPS: NONE`, `TRIAGE NOTE GAPS: NONE` |
| C-20 Enforcement audit table | FAIL | Audit sections are labeled prose/list, not Stage/Pre-Commitment/Declared/Honored/Deviation table |
| C-21 Named triage vocabulary | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR as explicit named fields |
| C-22 Role-concern gap scan | PASS | Role Concern Compliance section in RULE AUDIT-SUITE |
| C-23 Triage note gap scan | PASS | Triage Note Compliance section in RULE AUDIT-SUITE |
| C-24 Multi-type audit suite | PASS | Three independent sections: Calibration, Role Concern, Triage Note Compliance |
| C-25 Field-level triage audit | PASS | TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c) in Triage Note Compliance section; C-21+C-23 pass |
| C-26 Named rule + anti-patterns | PASS | RULE AUDIT-SUITE with ANTI-PATTERN-1 (merged) and ANTI-PATTERN-2 (repeated); C-24 passes |
| C-27 Gap-scan absence = format error | FAIL | Sections required in RULE AUDIT-SUITE but no "format error" / "FORMAT VIOLATION" language |
| C-28 Named field-level schema | PASS | TRIAGE NOTE AUDIT SCHEMA with labeled (a)/(b)/(c) in Triage Note Compliance section; C-25 passes |
| C-29 Enumerated condition zero-state | PASS | TRIAGE NOTE AUDIT RESULT block enumerates `(a) Section absent: NONE`, `(b) Named field missing: NONE`, `(c) Placeholder content: NONE`; C-25+C-28 pass |

**Aspirationals passing (15):** C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-28, C-29

```
composite = 60 + 20 + (15 × 5) = 60 + 20 + 75 = 155
```

---

## V-02 — Preamble-Level Schema Declaration

Moves TRIAGE NOTE AUDIT SCHEMA to run-level preamble before any stage runs. Post-stage TRIAGE NOTE GAPS section references the pre-declared schema. Two post-stage sections: TRIAGE NOTE GAPS + ROLE CONCERN GAPS. No RULE AUDIT-SUITE.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Stage header + ROLE field |
| C-02 | PASS | Calibration block with role-specific spread |
| C-03 | PASS | Labeled findings, verdict, TPM block |
| C-04 | PASS | Min 2 per stage, owner + resolution |
| C-05 | PASS | Go/No-Go in TPM |
| C-06 | FAIL | No cross-stage referencing instruction |
| C-07 | PASS | Risk Register table with Status |
| C-08 | PASS | S-office mission by name required |
| C-09 | FAIL | Not addressed |
| C-10 | FAIL | Not addressed |
| C-11 | FAIL | Not addressed |
| C-12 | PASS | MOST CRITICAL/LEAST CRITICAL enforces spread |
| C-13 | PASS | Status column present |
| C-14 | PASS | Calibration Block; uniform-spread TRIAGE NOTE required |
| C-15 | FAIL | No update protocol |
| C-16 | FAIL | No Role Concern section in stage format |
| C-17 | PASS | TRIAGE NOTE GAPS audits compliance with the triage note pre-commitment |
| C-18 | PASS | Three fields unconditionally required |
| C-19 | PASS | RULE ZERO-STATE + `TRIAGE NOTE GAPS: NONE` required |
| C-20 | FAIL | No structured table format for audit |
| C-21 | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR |
| C-22 | PASS | ROLE CONCERN GAPS post-stage section |
| C-23 | PASS | TRIAGE NOTE GAPS post-stage section |
| C-24 | FAIL | Only 2 post-stage sections (needs ≥3) |
| C-25 | PASS | TRIAGE NOTE GAPS applies preamble schema with (a)/(b)/(c) per stage; C-21+C-23 pass |
| C-26 | FAIL | No RULE AUDIT-SUITE with anti-patterns; C-24 fails |
| C-27 | FAIL | No "format error" language; C-22/C-23 pass but C-27 requires escalation language |
| C-28 | PASS | TRIAGE NOTE AUDIT SCHEMA declared in preamble — strongest C-28 separation; C-25 passes |
| C-29 | PASS | TRIAGE NOTE AUDIT RESULT enumerates all three conditions; C-25+C-28 pass |

**Aspirationals passing (12):** C-12, C-13, C-14, C-17, C-18, C-19, C-21, C-22, C-23, C-25, C-28, C-29

```
composite = 60 + 20 + (12 × 5) = 60 + 20 + 60 = 140
```

---

## V-03 — RULE CONDITION-ENUM as Run-Level Enforcement

Adds RULE CONDITION-ENUM as a named run-level rule with VIOLATION [AGGREGATE-NONE] label. TRIAGE NOTE AUDIT SCHEMA declared inline in the post-stage TRIAGE NOTE GAPS section (not preamble). Two post-stage sections: TRIAGE NOTE GAPS + ROLE CONCERN GAPS. No RULE AUDIT-SUITE.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Standard stage format |
| C-02 | PASS | Calibration block with role spread |
| C-03 | PASS | Findings, verdict, TPM block |
| C-04 | PASS | Min 2 per stage |
| C-05 | PASS | Go/No-Go present |
| C-06 | FAIL | No cross-stage referencing |
| C-07 | PASS | Risk Register with Status |
| C-08 | PASS | S-office mission required |
| C-09 | FAIL | Not addressed |
| C-10 | FAIL | Not addressed |
| C-11 | FAIL | Not addressed |
| C-12 | PASS | Spread enforcement via Calibration Block |
| C-13 | PASS | Status column present |
| C-14 | PASS | Calibration Block with uniform-spread guard |
| C-15 | FAIL | No update protocol |
| C-16 | FAIL | No Role Concern section in stage format |
| C-17 | PASS | TRIAGE NOTE GAPS audits pre-commitment |
| C-18 | PASS | Three fields unconditionally required |
| C-19 | PASS | RULE ZERO-STATE; TRIAGE NOTE GAPS: NONE required |
| C-20 | FAIL | No structured table |
| C-21 | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR |
| C-22 | PASS | ROLE CONCERN GAPS section |
| C-23 | PASS | TRIAGE NOTE GAPS section |
| C-24 | FAIL | Only 2 post-stage sections |
| C-25 | PASS | TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c) in TRIAGE NOTE GAPS; C-21+C-23 pass |
| C-26 | FAIL | RULE CONDITION-ENUM is not RULE AUDIT-SUITE; no multi-type audit anti-patterns |
| C-27 | FAIL | No format error language for absent sections |
| C-28 | PASS | TRIAGE NOTE AUDIT SCHEMA is a named schema artifact within TRIAGE NOTE GAPS section; co-located but named and declared before application; C-25 passes |
| C-29 | PASS | TRIAGE NOTE AUDIT RESULT enumerates per condition; RULE CONDITION-ENUM explicitly prohibits aggregate NONE; C-25+C-28 pass |

**Aspirationals passing (12):** C-12, C-13, C-14, C-17, C-18, C-19, C-21, C-22, C-23, C-25, C-28, C-29

```
composite = 60 + 20 + (12 × 5) = 60 + 20 + 60 = 140
```

Note: RULE CONDITION-ENUM is a stronger reliability mechanism for C-29 than V-02's prose instruction, but both produce the same score — the output criterion is the same. RULE CONDITION-ENUM's value is predictive (reduces degradation probability), not additive to the current rubric.

---

## V-04 — Symmetric Schema Coverage

Applies named-schema + enumerated-AUDIT RESULT pattern to BOTH gap sections: ROLE CONCERN AUDIT SCHEMA (a)/(b) + TRIAGE NOTE AUDIT SCHEMA (a)/(b)/(c). RULE BOOKEND-AUDIT with "absence = format error" language. Role Concern block required in each stage. Two post-stage sections only; no RULE AUDIT-SUITE.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Stage format with headers |
| C-02 | PASS | Role Concern + calibration in stages |
| C-03 | PASS | Findings, verdict, TPM block |
| C-04 | PASS | Min 2 per stage |
| C-05 | PASS | Go/No-Go present |
| C-06 | FAIL | No cross-stage referencing |
| C-07 | PASS | Risk Register with Status |
| C-08 | PASS | S-office mission required |
| C-09 | FAIL | Not addressed |
| C-10 | FAIL | Not addressed |
| C-11 | FAIL | Not addressed |
| C-12 | PASS | Spread via MOST CRITICAL/LEAST CRITICAL |
| C-13 | PASS | Status column present |
| C-14 | PASS | Calibration Block |
| C-15 | FAIL | No update protocol |
| C-16 | PASS | Role Concern block required first in each stage |
| C-17 | PASS | Both post-stage sections audit pre-commitments |
| C-18 | PASS | Three triage fields unconditionally |
| C-19 | PASS | RULE ZERO-STATE; NONE required in both sections |
| C-20 | FAIL | No Stage/Pre-Commitment/Declared/Honored/Deviation table |
| C-21 | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR |
| C-22 | PASS | ROLE CONCERN GAPS section with ROLE CONCERN AUDIT SCHEMA |
| C-23 | PASS | TRIAGE NOTE GAPS section with TRIAGE NOTE AUDIT SCHEMA |
| C-24 | FAIL | Only 2 post-stage sections (ROLE CONCERN GAPS + TRIAGE NOTE GAPS) |
| C-25 | PASS | TRIAGE NOTE AUDIT SCHEMA (a)/(b)/(c) in TRIAGE NOTE GAPS; C-21+C-23 pass |
| C-26 | FAIL | No RULE AUDIT-SUITE anti-patterns; C-24 fails |
| C-27 | PASS | RULE BOOKEND-AUDIT: "absence = format error" / "FORMAT VIOLATION" for both sections; C-22+C-23 pass |
| C-28 | PASS | TRIAGE NOTE AUDIT SCHEMA named and declared in section header; C-25 passes |
| C-29 | PASS | TRIAGE NOTE AUDIT RESULT with per-condition enumeration; ROLE CONCERN AUDIT RESULT also enumerated; C-25+C-28 pass |

**Aspirationals passing (14):** C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-25, C-27, C-28, C-29

```
composite = 60 + 20 + (14 × 5) = 60 + 20 + 70 = 150
```

---

## V-05 — Full R8 Stack

Stacks all R8 axes: preamble schemas for both dimensions (TRIAGE NOTE AUDIT SCHEMA + ROLE CONCERN AUDIT SCHEMA), RULE ZERO-STATE, RULE CONDITION-ENUM, RULE BOOKEND-AUDIT (format violation), RULE AUDIT-SUITE with ANTI-PATTERN-1/2. Three post-stage RULE AUDIT-SUITE sections each cite RULE CONDITION-ENUM and RULE BOOKEND-AUDIT inline.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Stage format with headers |
| C-02 | PASS | Role Concern section + calibration per stage |
| C-03 | PASS | Labeled findings, verdict, TPM block |
| C-04 | PASS | Min 2 per stage, owner + resolution |
| C-05 | PASS | Go/No-Go present |
| C-06 | FAIL | No cross-stage referencing instruction |
| C-07 | PASS | Risk Register with Status column |
| C-08 | PASS | S-office mission required by name |
| C-09 | FAIL | Not addressed |
| C-10 | FAIL | Not addressed |
| C-11 | FAIL | Not addressed |
| C-12 | PASS | MOST CRITICAL → HIGH, LEAST CRITICAL → LOW enforces spread |
| C-13 | PASS | Status: OPEN / WATCH / MITIGATED with 2+ distinct values |
| C-14 | PASS | Calibration Block; uniform-spread TRIAGE NOTE required |
| C-15 | FAIL | No update protocol for risk register |
| C-16 | PASS | Role Concern section required first in every stage |
| C-17 | PASS | Calibration Compliance section audits calibration pre-commitment |
| C-18 | PASS | "All three field labels required; present in every stage unconditionally" + placeholder triggers Condition (c) |
| C-19 | PASS | RULE ZERO-STATE + labeled NONE on all three audit sections |
| C-20 | FAIL | Audit sections use labeled list/AUDIT RESULT blocks, not Stage/Pre-Commitment/Declared/Honored/Deviation table |
| C-21 | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR named fields |
| C-22 | PASS | Role Concern Compliance section in RULE AUDIT-SUITE |
| C-23 | PASS | Triage Note Compliance section in RULE AUDIT-SUITE |
| C-24 | PASS | Three independent sections: Calibration, Role Concern, Triage Note Compliance |
| C-25 | PASS | Triage Note Compliance applies preamble TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c); cross-references preamble by name; C-21+C-23 pass |
| C-26 | PASS | RULE AUDIT-SUITE with ANTI-PATTERN-1 (merged) and ANTI-PATTERN-2 (repeated); C-24 passes |
| C-27 | PASS | RULE BOOKEND-AUDIT declares "absence = FORMAT VIOLATION" for both sections; cited again inside Role Concern Compliance and Triage Note Compliance headers; C-22+C-23 pass |
| C-28 | PASS | Both TRIAGE NOTE AUDIT SCHEMA and ROLE CONCERN AUDIT SCHEMA declared in preamble — maximum separation from application; post-stage sections reference by name "preamble declaration applies"; C-25 passes |
| C-29 | PASS | TRIAGE NOTE AUDIT RESULT and ROLE CONCERN AUDIT RESULT both enumerate per-condition; RULE CONDITION-ENUM explicitly prohibits aggregate NONE; C-25+C-28 pass |

**Aspirationals passing (16):** C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29

```
composite = 60 + 20 + (16 × 5) = 60 + 20 + 80 = 160
```

---

## Summary Table

| Variation | Essential | Rec | Aspirational (count) | Composite | Rank |
|-----------|-----------|-----|---------------------|-----------|------|
| V-05 | 60 | 20 | 80 (16) | **160** | 1 |
| V-01 | 60 | 20 | 75 (15) | **155** | 2 |
| V-04 | 60 | 20 | 70 (14) | **150** | 3 |
| V-02 | 60 | 20 | 60 (12) | **140** | 4 |
| V-03 | 60 | 20 | 60 (12) | **140** | 4 |

All variations pass all 5 essential criteria and both contributing recommended criteria (C-07, C-08). C-06 fails in all — no variation includes cross-stage coherence instruction.

### V-05 vs. V-01 Delta (+5 pts)

V-05 gains C-27 over V-01 because RULE BOOKEND-AUDIT uses explicit "FORMAT VIOLATION" / "absence = format error" language — which C-27's pass condition requires word-for-word. V-01's RULE AUDIT-SUITE mandates the sections but uses "required" language only, not format-error escalation.

### V-04 vs. V-01 Delta (−5 pts)

V-04 gains C-27 (+5) but loses C-24 and C-26 (−10) by omitting RULE AUDIT-SUITE. Two post-stage sections can deliver C-27 but cannot satisfy the three-section diversity requirement of C-24, which gates C-26.

---

## Excellence Signals (V-05)

**1. Preamble schema + post-stage reference pattern**
Both TRIAGE NOTE AUDIT SCHEMA and ROLE CONCERN AUDIT SCHEMA are declared at run level before stages begin. Each post-stage section cites the preamble by name ("preamble declaration applies"). The schema is visibly separate from its application — the model cannot conflate declaration with use. This makes C-28 unambiguous for both dimensions simultaneously.

**2. Rule citation anchors inside section headers**
Every post-stage section in V-05 contains inline rule citations (`[RULE CONDITION-ENUM applies]`, `[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]`). Named rules are checkable at output generation time; prose instructions are not. A model generating the section can see the constraint without re-reading the preamble.

**3. Format-violation escalation on both gap sections**
RULE BOOKEND-AUDIT escalates absence of either gap section from "missing improvement" to "FORMAT VIOLATION" — the same category as a missing stage header. This changes the model's compliance calculus: optional improvements are routinely dropped under length pressure; format violations are not. C-27 requires this escalation language to be printed, and V-05 prints it twice per section (in the rule declaration and again in the section header).

**4. Symmetric mechanism generalization**
Applying named-schema + AUDIT RESULT enumeration to ROLE CONCERN GAPS as well as TRIAGE NOTE GAPS proves the pattern is format-level (not triage-specific). The ROLE CONCERN AUDIT RESULT block provides a parallel enumerated zero-state that strengthens C-29's mechanism beyond triage notes — and seeds a potential C-30 signal (named schema generalization).

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["preamble schema with post-stage named reference — schema declared once at run level, each audit section references it by name rather than redeclaring inline", "rule citation anchors in section headers — each post-stage section header cites the named rules it applies, making compliance checkable at output time without re-reading the preamble"]}
```
