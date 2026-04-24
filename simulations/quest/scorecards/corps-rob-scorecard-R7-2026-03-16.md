## Scorecard: corps-rob Round 7

---

### Criteria Reference

| Weight | Criteria | Max pts |
|--------|----------|---------|
| Essential (5) | C-01 through C-05 | 60 |
| Recommended (3) | C-06 through C-08 | 30 |
| Aspirational (19) | C-09 through C-27 | 95 |
| **Total** | | **185** |

---

### V-01 -- Triage Note Field-Level Compliance Audit

Primary axis: **C-25**. Upgrades TRIAGE NOTE GAPS from section-presence check to three-condition field-level schema with TRIAGE NOTE AUDIT RESULT enumeration block.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Stage headers present in format spec |
| C-02 | PASS | Role loading from org.yaml / .roles/ required |
| C-03 | PASS | Full ROB format with findings, verdicts, TPM sections |
| C-04 | PASS | Minimum 2 findings per stage explicitly stated |
| C-05 | PASS | Go/No-Go in TPM stage |
| C-06 | FAIL | No cross-stage coherence instruction |
| C-07 | PASS | Risk register table with ID, Severity, Likelihood, Mitigation, Status; min 3 rows, 1 HIGH |
| C-08 | PASS | "at least one finding must name a specific S-office mission by name" |
| C-09 | FAIL | No inter-stage blocker detection mechanism |
| C-10 | FAIL | No cross-cutting theme section |
| C-11 | FAIL | No CONDITIONS: numbered items or N/A in verdict block |
| C-12 | PASS | Calibration block enforces HIGH/LOW spread; severity must match planned spread |
| C-13 | PASS | Status column (OPEN/WATCH/MITIGATED) in risk register |
| C-14 | PASS | MOST CRITICAL / LEAST CRITICAL / PLANNED SPREAD block; uniform requires note |
| C-15 | FAIL | No Update Protocol in TPM stage |
| C-16 | FAIL | No ROLE CONCERN block before Calibration in stage format |
| C-17 | FAIL | No enforcement audit of pre-commitment artifacts |
| C-18 | PASS | Triage Note mandatory in every stage; all three fields unconditionally required |
| C-19 | PASS | RULE ZERO-STATE declared; applies to all audit sections |
| C-20 | FAIL | No enforcement audit (C-17 fails; C-20 not scoreable) |
| C-21 | PASS | HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR named field labels |
| C-22 | PASS | ROLE CONCERN GAPS post-stage section present; "mandatory" language |
| C-23 | PASS | TRIAGE NOTE GAPS post-stage section present |
| C-24 | FAIL | Only 2 post-stage audit sections (TRIAGE NOTE GAPS + ROLE CONCERN GAPS); third section absent |
| C-25 | PASS | TRIAGE NOTE AUDIT SCHEMA with (a)/(b)/(c); zero-state requires TRIAGE NOTE AUDIT RESULT block enumerating all three conditions -- not just "NONE" |
| C-26 | FAIL | No RULE AUDIT-SUITE with labeled anti-pattern declarations |
| C-27 | FAIL | Sections called "mandatory" and "incomplete" on omission but no "format error" / "format violation" language |

**Essential**: 5/5 → 60 | **Recommended**: 2/3 (C-07, C-08) → 20 | **Aspirational**: 8 (C-12, C-13, C-14, C-18, C-19, C-21, C-22, C-23, C-25 = wait -- that's 9)

Recount: C-12 + C-13 + C-14 + C-18 + C-19 + C-21 + C-22 + C-23 + C-25 = 9 passing aspirational × 5 = 45

Wait -- C-25 requires C-21 and C-23 to both pass. Both pass. C-24 fails but C-24 is not a prerequisite for C-25.

**Aspirational**: 9 × 5 = 45

**V-01 composite: 60 + 20 + 45 = 125**

---

### V-02 -- Named Audit Rule with Anti-Pattern Specification

Primary axis: **C-26**. RULE AUDIT-SUITE expressed as a named format rule with ANTI-PATTERN-1 [MERGED SECTION] and ANTI-PATTERN-2 [REPEATED DIMENSION] as labeled first-class declarations.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Stage headers present |
| C-02 | PASS | Role loading from org.yaml / .roles/ |
| C-03 | PASS | ROB format with findings, verdicts, TPM sections |
| C-04 | PASS | Min 2 findings per stage |
| C-05 | PASS | Go/No-Go in TPM |
| C-06 | FAIL | No cross-stage coherence instruction |
| C-07 | PASS | Risk register table with all required columns |
| C-08 | PASS | "at least one finding must name a specific S-office mission by name" |
| C-09 | FAIL | No blocker detection |
| C-10 | FAIL | No cross-cutting theme section |
| C-11 | FAIL | Verdict block has Rationale but no CONDITIONS: numbered items or N/A |
| C-12 | PASS | Calibration block with spread matching enforcement |
| C-13 | PASS | Status column present |
| C-14 | PASS | MOST CRITICAL / LEAST CRITICAL / PLANNED SPREAD; uniform note required |
| C-15 | FAIL | No Update Protocol in TPM |
| C-16 | PASS | "### Role Concern / ROLE CONCERN:" block appears before Calibration in every stage |
| C-17 | PASS | Calibration Compliance post-stage section audits whether actual spread honored declared spread; names the pre-commitment, checks each stage, flags deviations |
| C-18 | PASS | Triage Note mandatory in every stage with three required fields |
| C-19 | PASS | RULE ZERO-STATE; each audit section requires explicit zero-state |
| C-20 | FAIL | Calibration Compliance is a list with zero-state, not a named-column table (Stage / Pre-Commitment / Declared / Honored / Deviation) |
| C-21 | PASS | HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR field labels |
| C-22 | PASS | Role Concern Compliance post-stage section present |
| C-23 | PASS | Triage Note Compliance post-stage section present |
| C-24 | PASS | Three independent sections: Calibration Compliance + Role Concern Compliance + Triage Note Compliance -- distinct pre-commitment scopes |
| C-25 | FAIL | Triage Note Compliance checks (a) section absent and (b) missing field labels but not (c) placeholder content; zero-state is "TRIAGE NOTE GAPS: NONE" not three-condition enumeration |
| C-26 | PASS | RULE AUDIT-SUITE named with ANTI-PATTERN-1 [MERGED SECTION] and ANTI-PATTERN-2 [REPEATED DIMENSION] as labeled declarations; C-24 passes |
| C-27 | FAIL | No "absence = format error" language for gap-scan sections |

**Essential**: 5/5 → 60 | **Recommended**: 2/3 (C-07, C-08) → 20 | **Aspirational**: C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24, C-26 = 12 × 5 = 60

**V-02 composite: 60 + 20 + 60 = 140**

---

### V-03 -- Gap-Scan Absence as Format Error

Primary axis: **C-27**. RULE BOOKEND-AUDIT declares both ROLE CONCERN GAPS and TRIAGE NOTE GAPS absence as FORMAT VIOLATION with explicit "absence = format error" language.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Stage headers present |
| C-02 | PASS | Role loading from org.yaml / .roles/ |
| C-03 | PASS | Full ROB format |
| C-04 | PASS | Min 2 findings per stage |
| C-05 | PASS | Go/No-Go in TPM |
| C-06 | FAIL | No cross-stage coherence instruction |
| C-07 | PASS | Risk register table with all required columns |
| C-08 | PASS | "at least one finding must name a specific S-office mission by name" |
| C-09 | FAIL | No blocker detection |
| C-10 | FAIL | No cross-cutting theme section |
| C-11 | FAIL | No CONDITIONS block in verdict |
| C-12 | PASS | Calibration block enforces spread |
| C-13 | PASS | Status column present |
| C-14 | PASS | MOST CRITICAL / LEAST CRITICAL / PLANNED SPREAD |
| C-15 | FAIL | No Update Protocol |
| C-16 | PASS | ROLE CONCERN block before Calibration in every stage |
| C-17 | PASS | CALIBRATION ERRORS post-stage section audits whether actual findings honored declared spread |
| C-18 | PASS | Triage Note mandatory with all three fields |
| C-19 | PASS | RULE ZERO-STATE applies to all gap-check sections |
| C-20 | FAIL | Calibration Errors is a list, not a named-column table; C-17 passes but enforcement artifact format is list-only |
| C-21 | PASS | HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR field labels |
| C-22 | PASS | ROLE CONCERN GAPS section present; RULE BOOKEND-AUDIT format error declaration |
| C-23 | PASS | TRIAGE NOTE GAPS section present; RULE BOOKEND-AUDIT format error declaration |
| C-24 | PASS | Three sections: ROLE CONCERN GAPS + TRIAGE NOTE GAPS + CALIBRATION ERRORS -- distinct scopes |
| C-25 | FAIL | TRIAGE NOTE GAPS describes three conditions (a/b/c) in scan instructions but zero-state is plain "TRIAGE NOTE GAPS: NONE" -- no three-condition TRIAGE NOTE AUDIT RESULT enumeration block |
| C-26 | FAIL | No RULE AUDIT-SUITE with labeled anti-pattern declarations |
| C-27 | PASS | RULE BOOKEND-AUDIT: "omission of this section after stages have run is a FORMAT VIOLATION. 'absence = format error'" for BOTH gap-scan sections; C-22 and C-23 both pass |

**Essential**: 5/5 → 60 | **Recommended**: 2/3 (C-07, C-08) → 20 | **Aspirational**: C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24, C-27 = 12 × 5 = 60

**V-03 composite: 60 + 20 + 60 = 140**

---

### V-04 -- Field-Level Triage Compliance + Format Error Language

Primary axes: **C-25 + C-27**. RULE TRIAGE-AUDIT (three-condition schema + three-condition zero-state) + RULE BOOKEND-AUDIT ("absence = format error" for both gap-scan sections).

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Stage headers present |
| C-02 | PASS | Role loading from org.yaml / .roles/ |
| C-03 | PASS | Full ROB format |
| C-04 | PASS | Min 2 findings per stage |
| C-05 | PASS | Go/No-Go in TPM |
| C-06 | FAIL | No cross-stage coherence instruction |
| C-07 | PASS | Risk register table with all required columns |
| C-08 | PASS | Named S-office mission requirement |
| C-09 | FAIL | No blocker detection |
| C-10 | FAIL | No cross-cutting theme section |
| C-11 | FAIL | No CONDITIONS block in verdict |
| C-12 | PASS | Calibration block with spread enforcement |
| C-13 | PASS | Status column in risk register |
| C-14 | PASS | MOST CRITICAL / LEAST CRITICAL / PLANNED SPREAD; uniform note required |
| C-15 | FAIL | No Update Protocol in TPM |
| C-16 | PASS | ROLE CONCERN block required before Calibration; PASSES/FAILS criteria explicit |
| C-17 | PASS | CALIBRATION ERRORS section checks declared spread vs. actual; zero-state required |
| C-18 | PASS | TRIAGE NOTE mandatory with all three fields unconditionally |
| C-19 | PASS | RULE ZERO-STATE; three-condition zero-state block explicitly required |
| C-20 | FAIL | No named-column enforcement audit table (C-17 satisfies via list format) |
| C-21 | PASS | HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR field labels; referenced in RULE TRIAGE-AUDIT's Condition (b) |
| C-22 | PASS | ROLE CONCERN GAPS present; "[RULE BOOKEND-AUDIT: absence = format error]" |
| C-23 | PASS | TRIAGE NOTE GAPS present; "[RULE BOOKEND-AUDIT: absence = format error]" |
| C-24 | PASS | Three sections: Role Concern Gaps + Triage Note Gaps + Calibration Errors -- distinct scopes |
| C-25 | PASS | RULE TRIAGE-AUDIT: (a)/(b)/(c) checked per stage; zero-state requires TRIAGE NOTE AUDIT RESULT block with all three conditions enumerated (not just "NONE"); C-21 and C-23 both pass |
| C-26 | FAIL | No RULE AUDIT-SUITE with labeled anti-pattern declarations |
| C-27 | PASS | RULE BOOKEND-AUDIT: "FORMAT ERROR. Absence = format error" for both sections using error language; C-22 and C-23 both pass |

**Essential**: 5/5 → 60 | **Recommended**: 2/3 (C-07, C-08) → 20 | **Aspirational**: C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24, C-25, C-27 = 13 × 5 = 65

**V-04 composite: 60 + 20 + 65 = 145**

---

### V-05 -- Full R7 Stack on R6 V-05 Base

Primary axes: **C-25 + C-26 + C-27** (RULES O, P, Q) on RULES A-N base covering all v2-v7 aspirational criteria.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Stage headers present |
| C-02 | PASS | Role loading from org.yaml / .roles/ |
| C-03 | PASS | Full ROB format |
| C-04 | PASS | Min 2 findings per stage (RULES A + D apply) |
| C-05 | PASS | Go/No-Go in TPM |
| C-06 | PASS | CROSS-STAGE COHERENCE instruction with typed format: `[stage] F-N: confirm/escalate/contradict -- [one sentence]`; "Aim for at least 2 cross-stage references" |
| C-07 | PASS | Risk register table with all required columns |
| C-08 | PASS | Mission Cascade table: named S-office mission → program → artifact/alignment |
| C-09 | FAIL | Cross-stage coherence uses "escalate" but no explicit hard-blocker detection mechanism with upstream stage + blocking finding ID + downstream impact required |
| C-10 | FAIL | No Synthesis or cross-cutting Themes section |
| C-11 | PASS | RULE B: conditional verdicts require numbered items (what/owner/finding ID); unconditional writes `CONDITIONS: N/A` |
| C-12 | PASS | RULE A: severity discrimination; at least 1 HIGH per stage, 1 below-HIGH across run |
| C-13 | PASS | RULE C: Status column; 2+ distinct values required |
| C-14 | PASS | RULE D: Calibration Block; uniform spread requires justification Triage Note |
| C-15 | PASS | RULE E: Update Protocol table (Trigger Events / Owner Role / Revisit Cadence); all fields topic-specific |
| C-16 | PASS | RULE F: ROLE CONCERN block as first named section in each stage; generic descriptions cited as violations |
| C-17 | PASS | RULE H: Enforcement Audit section required after final stage; covers Calibration Block spreads, Update Protocol, ROLE CONCERN declarations |
| C-18 | PASS | RULE G: Triage Note mandatory in every stage; all three fields unconditionally required |
| C-19 | PASS | RULE I: zero-state declaration on every audit / gap-check section when clean |
| C-20 | PASS | RULE J: Enforcement Audit must be a named-column table (Stage / Pre-Commitment Declared / Honored / Deviation); prose does not qualify |
| C-21 | PASS | RULE K: exactly HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR as field labels; prose without labels violates |
| C-22 | PASS | RULE L + RULE Q: ROLE CONCERN GAPS required; "absence = FORMAT ERROR" under RULE Q |
| C-23 | PASS | RULE M + RULE Q: TRIAGE NOTE GAPS required; "absence = FORMAT ERROR" under RULE Q |
| C-24 | PASS | RULE N: three independent sections (ROLE CONCERN GAPS + TRIAGE NOTE GAPS + CALIBRATION ERRORS); distinct scopes; RULE N cites RULE H, RULE L, RULE M as prerequisites |
| C-25 | PASS | RULE O: three-condition schema (a/b/c) applied per stage; clean zero-state requires TRIAGE NOTE AUDIT RESULT block enumerating all three; "TRIAGE NOTE GAPS: NONE alone does not satisfy RULE O"; C-21 and C-23 both pass |
| C-26 | PASS | RULE P: RULE AUDIT-SUITE printed as named rule with ANTI-PATTERN-1 [MERGED SECTION] and ANTI-PATTERN-2 [REPEATED DIMENSION] as labeled, independently-addressable compliance blockers; C-24 passes |
| C-27 | PASS | RULE Q: "absence = format error" for both ROLE CONCERN GAPS and TRIAGE NOTE GAPS using error language; "Language such as 'strongly recommended' does not satisfy RULE Q"; C-22 and C-23 both pass |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 (C-06, C-07, C-08) → 30 | **Aspirational**: C-11 through C-27 except C-09 and C-10 = 17 × 5 = 85

**V-05 composite: 60 + 30 + 85 = 175**

---

### Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 | V-05 -- Full R7 stack | 60 | 30 | 85 (17/19) | **175** |
| 2 | V-04 -- C-25 + C-27 | 60 | 20 | 65 (13/19) | **145** |
| 3= | V-02 -- C-26 | 60 | 20 | 60 (12/19) | **140** |
| 3= | V-03 -- C-27 | 60 | 20 | 60 (12/19) | **140** |
| 5 | V-01 -- C-25 | 60 | 20 | 45 (9/19) | **125** |

V-02 and V-03 are tied at 140 with distinct aspirational profiles: V-02 holds C-26 where V-03 holds C-27; neither has both.

---

### Differential Analysis

**V-04 vs V-02/V-03 (+5):** V-04 adds C-25 over V-03 (three-condition schema + enumerated zero-state via RULE TRIAGE-AUDIT) and C-25 over V-02 (V-02 only checks a and b, not c; zero-state not enumerated). The gain is one aspirational criterion -- field-level depth in the zero-state declaration.

**V-05 vs V-04 (+30):** V-05 gains across all three scoring pools:
- Recommended: gains C-06 (cross-stage coherence with typed format) -- +10
- Aspirational: gains C-11 (RULE B -- conditional itemization), C-15 (RULE E -- Update Protocol), C-17 (RULE H -- Enforcement Audit), C-20 (RULE J -- table format), C-26 (RULE P -- anti-patterns) -- +25

**V-01 weakness:** Building C-25 as the primary axis but not including ROLE CONCERN blocks (C-16), enforcement audit (C-17), or a third post-stage audit section (C-24) means V-01 scores below even the R6 retroactive baselines. It isolates the C-25 mechanism but strips surrounding structure.

---

### Excellence Signals from V-05

**Signal 1: Typed cross-stage reference format.** `[stage] F-N: confirm/escalate/contradict -- [sentence]` turns coherence from an advisory preference into a structural artifact. The typed verbs (confirm/escalate/contradict) encode the semantics of cross-stage relationship into the reference itself, making escalation chains scannable without re-reading prose.

**Signal 2: Rule-to-rule dependency declarations.** Each rule in V-05 explicitly names its prerequisites: "RULE M and RULE K must both pass for RULE O to be scoreable", "RULE N must pass for RULE P to be scoreable." This turns the rule set into a dependency graph that is self-documenting -- a reader can determine which criteria are gated without consulting the rubric.

**Signal 3: Anti-patterns as first-class labeled rule elements.** ANTI-PATTERN-1 [MERGED SECTION] and ANTI-PATTERN-2 [REPEATED DIMENSION] are independently addressable labels within RULE P -- not prose rationale. A model following these rules can mechanically check "did my output trigger ANTI-PATTERN-1?" rather than interpreting prose. This shifts compliance from judgment-based to pattern-check.

**Signal 4: Seventeen integrated rules vs. layered prose.** Encoding every structural requirement as a named, numbered RULE makes the full spec a coherent artifact: cross-referenceable, dependency-ordered, self-checking. Single-axis variations (V-01 through V-04) accumulate isolated mechanisms; V-05's rule architecture integrates them into a system where each element knows its dependencies and its dependents.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["rule-to-rule dependency declarations make prerequisite chains traceable within the rule text itself (RULE O depends on RULE M and RULE K)", "anti-patterns as labeled first-class rule elements (ANTI-PATTERN-1, ANTI-PATTERN-2) make compliance mechanical rather than interpretive"]}
```
