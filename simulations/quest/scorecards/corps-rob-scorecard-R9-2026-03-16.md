Scorecard written to `simulations/quest/scorecards/corps-rob-scorecard-R9-2026-03-16.md`.

---

## Summary

**All 5 essentials pass** across all variations. Rankings:

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | V-05 (Full R9 Stack) | **205** (max) |
| 2 | V-04 (Carry Forward + Conditional Verdict) | **185** |
| 3 | V-01 / V-02 / V-03 (tied) | **180** |

**Key scoring mechanics:**
- V-01 scores 180 (not 175) because C-06 is **recommended-tier** -- adding it completes 3/3 recommended = +10 pts, not +5.
- V-04 reaches 185 by also completing 3/3 recommended (C-06) plus one aspirational (C-11).
- V-05 reaches the maximum 205 by completing all tiers: 3/3 recommended + 23/23 aspirational.

**4 new patterns extracted from V-05:**

1. **RULE CARRY-FORWARD** -- per-stage carry blocks as mandatory labeled artifacts (not prose cross-references)
2. **RULE SYNTHESIS as non-audit** -- explicitly declared outside RULE AUDIT-SUITE scope to protect ANTI-PATTERN integrity
3. **RULE CONDITIONAL-ITEM vs RULE CONDITION-ENUM disambiguation** -- prevents conflation at generation time
4. **RULE AUDIT-TABLE additive-not-replacement** -- table above AUDIT RESULT block, preserving C-29

```json
{"top_score": 205, "all_essential_pass": true, "new_patterns": ["RULE CARRY-FORWARD: per-stage carry blocks as mandatory labeled artifacts with CARRY: NONE zero-state, making cross-stage references verifiable structural artifacts rather than incidental prose observations", "RULE SYNTHESIS as a non-audit first-class document section between stages and audit suite -- declared non-audit to protect RULE AUDIT-SUITE scope diversity from ANTI-PATTERN triggers", "RULE CONDITIONAL-ITEM declared explicitly distinct from RULE CONDITION-ENUM: prevents model conflation of conditional verdict enumeration (numbered what/owner/ref items) with audit schema result enumeration (a/b/c conditions)", "RULE AUDIT-TABLE: table-above-block pattern inserts stage-per-row scannability above the AUDIT RESULT block without replacing it -- additive not replacement, preserving C-29 enumerated condition zero-state"]}
```
pread |
| C-13 Risk register status | PASS | Status column: OPEN / WATCH / MITIGATED with 2+ required |
| C-14 Pre-finding calibration | PASS | Calibration Block; TRIAGE NOTE required when spread uniform |
| C-15 Update protocol | FAIL | No Update Protocol block in TPM |
| C-16 Role-lens pre-declaration | PASS | `### Role Concern` + ROLE CONCERN field before Calibration |
| C-17 Enforcement audit | PASS | Three independent post-stage audit sections in RULE AUDIT-SUITE |
| C-18 Universal triage note | PASS | All three fields unconditionally required in every stage |
| C-19 Zero-deviation declaration | PASS | RULE ZERO-STATE + explicit zero-state lines in all audit sections |
| C-20 Enforcement audit table | FAIL | No stage-per-row table; audit sections remain prose/list format |
| C-21 Named triage vocabulary | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR as labeled fields |
| C-22 Role-concern gap scan | PASS | Role Concern Compliance section in post-stage audit suite |
| C-23 Triage note gap scan | PASS | Triage Note Compliance section in post-stage audit suite |
| C-24 Multi-type audit suite | PASS | Three independent sections: Calibration, Role Concern, Triage Note |
| C-25 Field-level triage audit | PASS | TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c); AUDIT RESULT enumerates per-condition |
| C-26 Named rule + anti-patterns | PASS | RULE AUDIT-SUITE with ANTI-PATTERN-1 (merged) and ANTI-PATTERN-2 (repeated) |
| C-27 Gap-scan absence = format error | PASS | RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION for both sections |
| C-28 Named field-level schema | PASS | TRIAGE NOTE AUDIT SCHEMA + ROLE CONCERN AUDIT SCHEMA in run-level preamble |
| C-29 Enumerated condition zero-state | PASS | AUDIT RESULT block enumerates each condition as individually clean |
| C-30 Preamble schema + named reference | PASS | Both schemas in run-level preamble before stages; post-stage sections reference "preamble declaration applies" |
| C-31 Rule citation anchors in headers | PASS | Section headers include [RULE CONDITION-ENUM applies] and [RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION] |

**Aspirationals passing (18):** C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31

```
composite = (5/5 x 60) + (3/3 x 30) + (18 x 5)
          = 60 + 30 + 90
          = 180
```

---

## V-02 -- Enforcement Format Richness (Update Protocol + Audit Table)

Adds (1) Update Protocol block in TPM stage (C-15) and (2) RULE AUDIT-TABLE requiring stage-per-row tables above each AUDIT RESULT block (C-20). No RULE CARRY-FORWARD. C-30 and C-31 preserved.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage identity | PASS | `## Stage:` headers + ROLE field |
| C-02 Role-loaded perspective | PASS | Role Concern section + role-specific calibration |
| C-03 ROB document format | PASS | Labeled findings, verdict, TPM block present |
| C-04 Actionable findings 2x | PASS | Min 2 per stage, owner + resolution required |
| C-05 Go/No-Go TPM | PASS | `### Go/No-Go` with explicit verdict |
| C-06 Cross-stage coherence | FAIL | No RULE CARRY-FORWARD; no cross-stage referencing instruction |
| C-07 Risk register TPM | PASS | Risk Register table with Status column |
| C-08 Exec-office cascade | PASS | S-office mission by name required |
| C-09 Inter-stage blocker | FAIL | No SYNTHESIS section |
| C-10 Cross-cutting theme | FAIL | No SYNTHESIS section |
| C-11 Conditional verdict | FAIL | No RULE CONDITIONAL-ITEM |
| C-12 Severity discrimination | PASS | Calibration block enforces HIGH-to-LOW spread |
| C-13 Risk register status | PASS | Status column present with OPEN/WATCH/MITIGATED |
| C-14 Pre-finding calibration | PASS | Calibration Block with MOST/LEAST CRITICAL |
| C-15 Update protocol | PASS | Update Protocol block in TPM with TRIGGER EVENTS, UPDATE OWNER, REVISIT CADENCE; C-13 passes |
| C-16 Role-lens pre-declaration | PASS | ROLE CONCERN field before Calibration |
| C-17 Enforcement audit | PASS | Three independent post-stage audit sections |
| C-18 Universal triage note | PASS | All three fields unconditionally required |
| C-19 Zero-deviation declaration | PASS | RULE ZERO-STATE + explicit zero-state lines |
| C-20 Enforcement audit table | PASS | RULE AUDIT-TABLE: Stage/Pre-Commitment/Honored/Deviation table above each AUDIT RESULT block; AUDIT RESULT block preserved beneath; C-17 passes |
| C-21 Named triage vocabulary | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR |
| C-22 Role-concern gap scan | PASS | Role Concern Compliance section present |
| C-23 Triage note gap scan | PASS | Triage Note Compliance section present |
| C-24 Multi-type audit suite | PASS | Three independent sections with distinct scopes |
| C-25 Field-level triage audit | PASS | (a)/(b)/(c) conditions checked per stage |
| C-26 Named rule + anti-patterns | PASS | RULE AUDIT-SUITE with ANTI-PATTERN-1 and ANTI-PATTERN-2 |
| C-27 Gap-scan absence = format error | PASS | RULE BOOKEND-AUDIT FORMAT VIOLATION language |
| C-28 Named field-level schema | PASS | Both named schemas in run-level preamble |
| C-29 Enumerated condition zero-state | PASS | Per-condition AUDIT RESULT enumeration preserved beneath table |
| C-30 Preamble schema + named reference | PASS | Schemas in preamble; "preamble declaration applies" in section headers |
| C-31 Rule citation anchors in headers | PASS | Section headers include [RULE CONDITION-ENUM applies], [RULE AUDIT-TABLE applies], [RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION] |

**Aspirationals passing (20):** C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31

```
composite = (5/5 x 60) + (2/3 x 30) + (20 x 5)
          = 60 + 20 + 100
          = 180
```

---

## V-03 -- Synthesis Section (Blockers + Cross-Cutting Themes)

Adds RULE SYNTHESIS: mandatory SYNTHESIS section after stages and before Post-Stage Audit Suite, containing BLOCKERS and CROSS-CUTTING THEMES subsections. Both subsections use RULE ZERO-STATE. SYNTHESIS declared as a summary-level artifact (not audit section), preserving RULE AUDIT-SUITE compliance. No RULE CARRY-FORWARD.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage identity | PASS | `## Stage:` headers + ROLE field |
| C-02 Role-loaded perspective | PASS | Role Concern section + role-specific calibration |
| C-03 ROB document format | PASS | Labeled findings, verdict, TPM block present |
| C-04 Actionable findings 2x | PASS | Min 2 per stage, owner + resolution |
| C-05 Go/No-Go TPM | PASS | Explicit Go/No-Go verdict |
| C-06 Cross-stage coherence | FAIL | No RULE CARRY-FORWARD; stages write independently |
| C-07 Risk register TPM | PASS | Risk Register table with Status |
| C-08 Exec-office cascade | PASS | S-office mission by name required |
| C-09 Inter-stage blocker | PASS | SYNTHESIS/BLOCKERS subsection: upstream stage, finding ID, downstream stage impact explicitly required; BLOCKERS: NONE zero-state covers clean case |
| C-10 Cross-cutting theme | PASS | SYNTHESIS/CROSS-CUTTING THEMES: document-level theme name, 2+ stage citations, severity elevation explanation; CROSS-CUTTING THEMES: NONE zero-state covers clean case |
| C-11 Conditional verdict | FAIL | No RULE CONDITIONAL-ITEM declared |
| C-12 Severity discrimination | PASS | MOST CRITICAL/LEAST CRITICAL enforces spread |
| C-13 Risk register status | PASS | Status column present |
| C-14 Pre-finding calibration | PASS | Calibration Block with spread declaration |
| C-15 Update protocol | FAIL | No Update Protocol block in TPM |
| C-16 Role-lens pre-declaration | PASS | ROLE CONCERN field before Calibration |
| C-17 Enforcement audit | PASS | Three independent post-stage audit sections |
| C-18 Universal triage note | PASS | All three fields unconditionally required |
| C-19 Zero-deviation declaration | PASS | RULE ZERO-STATE applied in audit sections and SYNTHESIS subsections |
| C-20 Enforcement audit table | FAIL | No RULE AUDIT-TABLE; audit sections remain prose/list |
| C-21 Named triage vocabulary | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR |
| C-22 Role-concern gap scan | PASS | Role Concern Compliance section |
| C-23 Triage note gap scan | PASS | Triage Note Compliance section |
| C-24 Multi-type audit suite | PASS | SYNTHESIS not an audit section per RULE SYNTHESIS declaration; three audit sections remain distinct and independent |
| C-25 Field-level triage audit | PASS | (a)/(b)/(c) conditions enumerated |
| C-26 Named rule + anti-patterns | PASS | RULE AUDIT-SUITE with ANTI-PATTERN-1 and ANTI-PATTERN-2 |
| C-27 Gap-scan absence = format error | PASS | RULE BOOKEND-AUDIT FORMAT VIOLATION language |
| C-28 Named field-level schema | PASS | Both named schemas in run-level preamble |
| C-29 Enumerated condition zero-state | PASS | Per-condition AUDIT RESULT enumeration |
| C-30 Preamble schema + named reference | PASS | Preamble schemas; "preamble declaration applies" in section headers |
| C-31 Rule citation anchors in headers | PASS | Section headers include rule citations |

**Aspirationals passing (20):** C-09, C-10, C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31

```
composite = (5/5 x 60) + (2/3 x 30) + (20 x 5)
          = 60 + 20 + 100
          = 180
```

---

## V-04 -- Carry Forward + Conditional Verdict Enumeration

Adds RULE CARRY-FORWARD (C-06) combined with RULE CONDITIONAL-ITEM (C-11). RULE CONDITIONAL-ITEM declared explicitly distinct from RULE CONDITION-ENUM to prevent model conflation. Conditional verdicts enumerate conditions as numbered items before Rationale (what/owner/ref). No SYNTHESIS, no Update Protocol, no RULE AUDIT-TABLE.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage identity | PASS | `## Stage:` headers + ROLE field |
| C-02 Role-loaded perspective | PASS | Role Concern section + role-specific calibration |
| C-03 ROB document format | PASS | Labeled findings, verdict, TPM block present |
| C-04 Actionable findings 2x | PASS | Min 2 per stage, owner + resolution |
| C-05 Go/No-Go TPM | PASS | Explicit Go/No-Go verdict |
| C-06 Cross-stage coherence | PASS | RULE CARRY-FORWARD: mandatory per-stage CARRY FORWARD sections; 5 carry sites in 6-stage run guarantees >= 2 named cross-stage references |
| C-07 Risk register TPM | PASS | Risk Register table with Status |
| C-08 Exec-office cascade | PASS | S-office mission by name required |
| C-09 Inter-stage blocker | FAIL | No SYNTHESIS section; carry forward references upstream findings but does not produce a dedicated blocker artifact |
| C-10 Cross-cutting theme | FAIL | No SYNTHESIS section; no document-level theme elevation |
| C-11 Conditional verdict | PASS | RULE CONDITIONAL-ITEM: APPROVED/GO WITH CONDITIONS must enumerate >= 2 numbered items with what/owner/ref before Rationale; declared distinct from RULE CONDITION-ENUM |
| C-12 Severity discrimination | PASS | Calibration block enforces spread |
| C-13 Risk register status | PASS | Status column present |
| C-14 Pre-finding calibration | PASS | Calibration Block |
| C-15 Update protocol | FAIL | No Update Protocol block in TPM |
| C-16 Role-lens pre-declaration | PASS | ROLE CONCERN field before Calibration |
| C-17 Enforcement audit | PASS | Three independent post-stage audit sections |
| C-18 Universal triage note | PASS | All three fields unconditionally required |
| C-19 Zero-deviation declaration | PASS | RULE ZERO-STATE + explicit zero-state lines |
| C-20 Enforcement audit table | FAIL | No RULE AUDIT-TABLE; audit sections remain prose/list |
| C-21 Named triage vocabulary | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR |
| C-22 Role-concern gap scan | PASS | Role Concern Compliance section |
| C-23 Triage note gap scan | PASS | Triage Note Compliance section |
| C-24 Multi-type audit suite | PASS | Three independent sections |
| C-25 Field-level triage audit | PASS | (a)/(b)/(c) conditions |
| C-26 Named rule + anti-patterns | PASS | RULE AUDIT-SUITE with ANTI-PATTERN-1 and ANTI-PATTERN-2 |
| C-27 Gap-scan absence = format error | PASS | RULE BOOKEND-AUDIT FORMAT VIOLATION language |
| C-28 Named field-level schema | PASS | Both named schemas in preamble |
| C-29 Enumerated condition zero-state | PASS | Per-condition AUDIT RESULT enumeration |
| C-30 Preamble schema + named reference | PASS | Preamble schemas; named references in sections |
| C-31 Rule citation anchors in headers | PASS | Section headers include rule citations |

**Aspirationals passing (19):** C-11, C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31

```
composite = (5/5 x 60) + (3/3 x 30) + (19 x 5)
          = 60 + 30 + 95
          = 185
```

---

## V-05 -- Full R9 Stack

All six failing R8 V-05 criteria added simultaneously to the R8 V-05 base: RULE CARRY-FORWARD (C-06), RULE SYNTHESIS with BLOCKERS + THEMES (C-09, C-10), RULE CONDITIONAL-ITEM (C-11), Update Protocol in TPM (C-15), RULE AUDIT-TABLE in each audit section (C-20). Each addition occupies a structurally distinct location. C-30 and C-31 explicitly preserved.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage identity | PASS | `## Stage:` headers + ROLE field |
| C-02 Role-loaded perspective | PASS | Role Concern section + role-specific calibration |
| C-03 ROB document format | PASS | Labeled findings, verdict, TPM block present |
| C-04 Actionable findings 2x | PASS | Min 2 per stage, owner + resolution |
| C-05 Go/No-Go TPM | PASS | Explicit Go/No-Go verdict |
| C-06 Cross-stage coherence | PASS | RULE CARRY-FORWARD: per-stage carry sections before Calibration; 5 carry sites in 6-stage run; CARRY: NONE zero-state when nothing carries |
| C-07 Risk register TPM | PASS | Risk Register table with Status |
| C-08 Exec-office cascade | PASS | S-office mission by name required |
| C-09 Inter-stage blocker | PASS | SYNTHESIS/BLOCKERS: upstream stage, finding ID, downstream stage, impact stated; BLOCKERS: NONE zero-state |
| C-10 Cross-cutting theme | PASS | SYNTHESIS/CROSS-CUTTING THEMES: document-level theme name, stage citations with finding IDs, severity elevation explanation; CROSS-CUTTING THEMES: NONE zero-state |
| C-11 Conditional verdict | PASS | RULE CONDITIONAL-ITEM (explicitly distinct from RULE CONDITION-ENUM): >= 2 numbered items per conditional verdict, each with what/owner/ref before Rationale |
| C-12 Severity discrimination | PASS | Calibration block enforces HIGH-to-LOW spread |
| C-13 Risk register status | PASS | Status column with OPEN/WATCH/MITIGATED |
| C-14 Pre-finding calibration | PASS | Calibration Block with MOST/LEAST CRITICAL |
| C-15 Update protocol | PASS | Update Protocol block in TPM: TRIGGER EVENTS, UPDATE OWNER, REVISIT CADENCE; C-13 passes |
| C-16 Role-lens pre-declaration | PASS | ROLE CONCERN field before Calibration |
| C-17 Enforcement audit | PASS | Three independent post-stage audit sections |
| C-18 Universal triage note | PASS | All three fields unconditionally required in every stage |
| C-19 Zero-deviation declaration | PASS | RULE ZERO-STATE applied across audit sections, SYNTHESIS subsections, and CARRY FORWARD |
| C-20 Enforcement audit table | PASS | RULE AUDIT-TABLE: Stage/Pre-Commitment/Honored/Deviation table above each AUDIT RESULT block; AUDIT RESULT block preserved beneath (C-29 not voided); C-17 passes |
| C-21 Named triage vocabulary | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR |
| C-22 Role-concern gap scan | PASS | Role Concern Compliance section |
| C-23 Triage note gap scan | PASS | Triage Note Compliance section |
| C-24 Multi-type audit suite | PASS | SYNTHESIS not an audit section per RULE SYNTHESIS declaration; three audit sections remain independent |
| C-25 Field-level triage audit | PASS | (a)/(b)/(c) conditions; AUDIT RESULT block preserved beneath table |
| C-26 Named rule + anti-patterns | PASS | RULE AUDIT-SUITE with ANTI-PATTERN-1 and ANTI-PATTERN-2 |
| C-27 Gap-scan absence = format error | PASS | RULE BOOKEND-AUDIT: FORMAT VIOLATION language for both sections |
| C-28 Named field-level schema | PASS | Both named schemas in run-level preamble with labeled (a)/(b)/(c) |
| C-29 Enumerated condition zero-state | PASS | Per-condition AUDIT RESULT enumeration preserved beneath RULE AUDIT-TABLE tables |
| C-30 Preamble schema + named reference | PASS | Both schemas in preamble before stages; post-stage sections reference "preamble declaration applies"; no addition touches preamble |
| C-31 Rule citation anchors in headers | PASS | Section headers cite [RULE CONDITION-ENUM applies], [RULE AUDIT-TABLE applies], [RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]; no addition removes these |

**Aspirationals passing (23 / 23):** C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31

```
composite = (5/5 x 60) + (3/3 x 30) + (23 x 5)
          = 60 + 30 + 115
          = 205
```

---

## Rankings

| Rank | Variation | Score | Delta from Baseline (170) |
|------|-----------|-------|--------------------------|
| 1 | V-05 (Full R9 Stack) | **205** | +35 |
| 2 | V-04 (Carry Forward + Conditional Verdict) | **185** | +15 |
| 3 | V-01 (RULE CARRY-FORWARD only) | **180** | +10 |
| 3 | V-02 (Update Protocol + Audit Table) | **180** | +10 |
| 3 | V-03 (Synthesis Section) | **180** | +10 |

Note on V-01 scoring: C-06 is recommended-tier (not aspirational), so adding it completes the recommended tier from 2/3 to 3/3 (+10 pts), not merely adding 5 aspirational pts. V-02 and V-03 each add two aspirational criteria (+10 pts) but remain at 2/3 recommended.

---

## Excellence Signals -- V-05

**1. Structural non-interference across six simultaneous additions.**
Each addition occupies a distinct document location: CARRY FORWARD before Calibration per stage, RULE CONDITIONAL-ITEM only in the Verdict block, Update Protocol inside TPM after Risk Register, SYNTHESIS between stages and audit suite, RULE AUDIT-TABLE inside each existing audit section. No two additions touch the same section. The full stack composes without conflict because structural locations were chosen to be independent.

**2. Named rules prevent collapse under generation pressure.**
Each addition is declared as a named run-level rule (RULE CARRY-FORWARD, RULE SYNTHESIS, RULE CONDITIONAL-ITEM, RULE AUDIT-TABLE) with its own violation pattern. Named rules with labeled violations are checkable at output time -- every new structural requirement can be audited by name, not inferred from output structure.

**3. Additive-not-replacement pattern preserves downstream criteria.**
RULE AUDIT-TABLE inserts the stage-per-row table above the AUDIT RESULT block rather than replacing it. C-29 (enumerated condition zero-state) is explicitly preserved: "AUDIT RESULT block beneath the table (RULE CONDITION-ENUM applies)." New additions never silently void prior-round criteria.

**4. Carry blocks as the foundation for conditional verdict chains.**
RULE CARRY-FORWARD and RULE CONDITIONAL-ITEM reinforce each other structurally: upstream unresolved findings appear as named carry entries -> unresolved carries become the items in conditional verdict enumerations. The escalation path from finding to carry to verdict condition is a verifiable artifact chain, not a prose observation.

**5. SYNTHESIS declared as non-audit to protect RULE AUDIT-SUITE.**
RULE SYNTHESIS explicitly declares SYNTHESIS as a summary-level analysis artifact, not an audit section, so it does not count toward RULE AUDIT-SUITE's three required sections and cannot trigger ANTI-PATTERN-1 or ANTI-PATTERN-2. Without this declaration, adding SYNTHESIS risks the model counting it as one of the three audit sections, collapsing scope diversity.

**6. RULE CONDITION-ENUM / RULE CONDITIONAL-ITEM disambiguation.**
Both rules involve enumeration but govern different constructs: RULE CONDITION-ENUM governs audit schema result blocks; RULE CONDITIONAL-ITEM governs conditional verdict items. The spec names the distinction explicitly `[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]`. Without this, a model might apply audit-schema (a/b/c) patterns instead of the numbered-item verdict format.

---

```json
{"top_score": 205, "all_essential_pass": true, "new_patterns": ["RULE CARRY-FORWARD: per-stage carry blocks as mandatory labeled artifacts with CARRY: NONE zero-state, making cross-stage references verifiable structural artifacts rather than incidental prose observations", "RULE SYNTHESIS as a non-audit first-class document section between stages and audit suite -- declared non-audit to protect RULE AUDIT-SUITE scope diversity from ANTI-PATTERN triggers", "RULE CONDITIONAL-ITEM declared explicitly distinct from RULE CONDITION-ENUM: prevents model conflation of conditional verdict enumeration (numbered what/owner/ref items) with audit schema result enumeration (a/b/c conditions)", "RULE AUDIT-TABLE: table-above-block pattern inserts stage-per-row scannability above the AUDIT RESULT block without replacing it -- additive not replacement, preserving C-29 enumerated condition zero-state"]}
```
