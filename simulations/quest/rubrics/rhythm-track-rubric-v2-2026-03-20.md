Done. Here's the complete updated rubric:

---

# Rubric — rhythm-track v2

## Criteria Summary

| Tier | Count | Points | Criteria |
|------|-------|--------|----------|
| Essential | 5 | 60 (12 each) | C-01 through C-05 |
| Recommended | 3 | 30 (10 each) | C-06 through C-08 |
| Aspirational | 6 | 30 (5 each) | C-09 through C-14 |
| **Total** | **14** | **120** | |

**Golden**: all 5 essential must PASS. `Composite = (essential/5 * 60) + (recommended/3 * 30) + (aspirational/6 * 30)`

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Dependency map table produced** | coverage | Phase 2 table with D-ID rows; empty (not missing) if no annotations found. |
| C-02 | **Every dependency has a verification block** | coverage | One block per D-ID: cited? (YES/NO/IMPLICITLY), correct form? (YES/NO/MODIFIED), Verdict. No skips. |
| C-03 | **P1 violations correctly surfaced** | correctness | P1-labeled entries in Phase 4 match count in Phase 5 and frontmatter. "P1 violations: 0" stated explicitly when none. |
| C-04 | **Track integrity status is consistent** | correctness | BROKEN/PARTIAL/SOUND status follows from findings: BROKEN >= 1 P1; PARTIAL >= 1 P2 and no P1; SOUND = no P1 and no P2. |
| C-05 | **Artifact written with correct frontmatter** | format | All fields present: skill, topic, date, papers_checked, p1_violations, track_integrity. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Transfer types classified correctly** | depth | Each dependency row assigns one of Definition / Structural / Empirical / Causal matching the nature of what transfers. |
| C-07 | **AMEND gives targeted, actionable fixes** | depth | Three fixes ranked P1/P2/P3, each naming paper + section + exact change. |
| C-08 | **Critical path identified** | coverage | Phase 5 lists D-IDs blocking next submission; non-empty when P1 or P2 violations exist. |

---

## Aspirational Criteria (30 pts total)

**Original (v1):**

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-09 | **Implicit vs explicit citation distinguished** | IMPLICITLY used in Phase 3 with a note on whether implicit use is sufficient. |
| C-10 | **Modification justification assessed** | MODIFIED dependencies assessed YES/NO/NOT ADDRESSED with implication explained. |

**New (v2 — from R1 excellence signals):**

| ID | Criterion | Signal Source | Pass Condition |
|----|-----------|---------------|----------------|
| C-11 | **Count reconciliation is structural** | V-02 reconciliation step; V-04 reconciliation table | P1/P2 counts reconciled via a dedicated step or table before Phase 5 — not merely instructed. The number is written down and carried forward; a reader cannot arrive at a different count by re-reading. |
| C-12 | **Integrity derivation shown explicitly** | V-02 "show your work"; V-04 IF-THEN derivation | Phase 5 states premises (P1 count, P2 count) and rule applied (e.g., "P1 = 2 > 0 → BROKEN"). Status verifiable from Phase 5 alone without re-reading Phase 4. |
| C-13 | **NOT ADDRESSED for unjustified modification** | V-03 NOT ADDRESSED vs N/A | Modification justification uses NOT ADDRESSED (not just N/A) when the paper neither confirms nor denies the justification — three-way distinction that N/A collapses. |
| C-14 | **AMEND handles P1=0 edge case** | V-02 and V-04 edge case handling | When P1 = 0, Fix 1 explicitly escalates to highest-severity P2 gap and states this. Without it, AMEND is structurally incomplete for clean tracks. |

---

**Scoring change from v1**: aspirational bucket expanded from 10 pts (2 criteria) to 30 pts (6 criteria); max score is now 120.
plicit citation distinguished** | depth | aspirational | Phase 3 verification blocks use IMPLICITLY (not just YES/NO) when a dependency is used in spirit but not cited by paper name or section. At least one IMPLICIT finding is explored with a note on whether implicit use is sufficient or whether an explicit citation is needed. |
| C-10 | **Modification justification assessed** | behavior | aspirational | For any dependency verified as MODIFIED, Phase 3 assesses whether the modification is justified (YES/NO/NOT ADDRESSED) and explains the implication — e.g., whether the modification extends, narrows, or contradicts the original result. |
| C-11 | **Count reconciliation is structural, not instructional** | correctness | aspirational | The P1 (and P2) count is mechanically reconciled via a dedicated reconciliation step, summary row, or table before Phase 5 — not merely instructed ("count your P1 rows"). The reconciled number is written down and explicitly carried into Phase 5 and the frontmatter. A reader following the output cannot arrive at a different count by re-reading. |
| C-12 | **Integrity derivation shown explicitly** | transparency | aspirational | Phase 5 shows the derivation logic, not just the conclusion. The output states the premise (P1 count, P2 count) and the rule applied (e.g., "P1 = 2 > 0 -> BROKEN") so the status can be verified without re-reading Phase 4. A reader can confirm the status is correct from Phase 5 alone. |
| C-13 | **NOT ADDRESSED used for unjustified modification** | behavior | aspirational | When modification justification is assessed (C-10), the output uses NOT ADDRESSED (not just YES/NO/N/A) when the paper neither confirms nor denies the justification for the change. This three-way distinction — justified, unjustified, not addressed — surfaces a third epistemic state that N/A collapses. |
| C-14 | **AMEND handles P1=0 edge case explicitly** | depth | aspirational | When no P1 violations exist, Fix 1 in Phase 6 explicitly targets the highest-severity P2 gap and states this: e.g., "No P1 violations found -- Fix 1 addresses highest-severity P2 gap." Without this, Fix 1 is vacuous or omitted when the track is clean, leaving the AMEND section structurally incomplete for well-formed tracks. |

---

## Scoring Example

```
Essential (5):     C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 FAIL
Recommended (3):   C-06 PASS, C-07 PASS, C-08 FAIL
Aspirational (6):  C-09 PASS, C-10 FAIL, C-11 PASS, C-12 FAIL, C-13 FAIL, C-14 FAIL

essential_pass = 4/5
recommended_pass = 2/3
aspirational_pass = 2/6

Composite = (4/5 * 60) + (2/3 * 30) + (2/6 * 30)
          = 48 + 20 + 10 = 78

Golden? NO -- not all essential pass (C-05 failed)
```

R1 golden ceiling (all criteria pass):

```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 6/6

Composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 30) = 120
Golden? YES
```

---

## Failure Modes to Watch

- **Empty dependency table**: skill ran but MODULE.md was not read or had no dependency annotations -- C-01 fails
- **Verdicts without verification blocks**: Phase 4 register present but Phase 3 blocks missing -- C-02 fails
- **P1 count mismatch**: frontmatter `p1_violations` differs from P1-labeled rows in Phase 4 -- C-03 and C-05 fail
- **Count drift without reconciliation**: model counted correctly in Phase 3 but re-counted differently in Phase 5 -- C-03 fails, C-11 fails
- **Inconsistent integrity status**: SOUND declared despite PARTIAL or VIOLATED entries -- C-04 fails
- **Status asserted without derivation**: integrity status correct but Phase 5 shows no premises or rule -- C-12 fails
- **Generic fixes**: "Improve citation consistency" instead of naming paper, section, and change -- C-07 fails
- **Vacuous Fix 1 on clean tracks**: AMEND section present but Fix 1 is empty or "no violations found" with no P2 escalation -- C-14 fails

---

## R1 Excellence Signals (basis for C-11 through C-14)

| New Criterion | Signal Source | Observation |
|---------------|---------------|-------------|
| C-11 | V-02 reconciliation step; V-04 reconciliation table | Structural enforcement (dedicated step/table with carry-forward instruction) pushed C-03 from PARTIAL to PASS in V-02 and V-04; mere instruction to "count rows" left V-01 and V-03 at PARTIAL |
| C-12 | V-02 "show your work"; V-04 IF-THEN derivation | Making the derivation logic visible lets a reader verify the integrity status from Phase 5 alone without re-reading Phase 4 |
| C-13 | V-03 NOT ADDRESSED vs N/A | Three-way distinction (YES / NO / NOT ADDRESSED) surfaces when a paper neither confirms nor denies modification justification -- collapses to N/A without this signal |
| C-14 | V-02 and V-04 P1=0 edge case | Both golden variations explicitly escalated Fix 1 to the highest-severity P2 gap when P1 = 0; without this, AMEND is incomplete for structurally sound tracks |
