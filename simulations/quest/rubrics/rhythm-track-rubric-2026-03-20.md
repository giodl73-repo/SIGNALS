Rubric written to `simulations/quest/rubrics/rhythm-track-rubric-2026-03-20.md`.

**5 essential** (all must pass):
- C-01: Dependency map table produced with D-ID rows
- C-02: Every dependency has a Phase 3 verification block with SATISFIED/PARTIAL/VIOLATED
- C-03: P1 violations correctly surfaced and counted
- C-04: Track integrity status (SOUND/PARTIAL/BROKEN) is consistent with findings
- C-05: Artifact written with all required frontmatter fields

**3 recommended**:
- C-06: Transfer types classified correctly (Definition/Structural/Empirical/Causal)
- C-07: AMEND gives targeted, paper-specific fixes (not generic)
- C-08: Critical path identifies which D-IDs block the next submission

**2 aspirational**:
- C-09: IMPLICITLY distinguished from YES/NO in citation checks
- C-10: MODIFIED dependencies get justification assessment

The key failure modes are empty dependency tables (MODULE.md not read), P1 count mismatches between Phase 4 and frontmatter, and generic fixes that don't name paper + section.
ng Phase 3 verification block with: Is it cited? (YES/NO/IMPLICITLY), Is it used in correct form? (YES/NO/MODIFIED), Verdict (SATISFIED/PARTIAL/VIOLATED). No dependency is skipped. |
| C-03 | **P1 violations correctly surfaced** | correctness | essential | Any dependency where a later paper contradicts or ignores a structural result from an earlier paper is labeled P1. If no P1 violations exist the output explicitly states "P1 violations: 0". The count in Phase 5 matches the P1-labeled entries in Phase 4. |
| C-04 | **Track integrity status is consistent** | correctness | essential | Phase 5 states SOUND, PARTIAL, or BROKEN, and this status is consistent with the Phase 4 findings: BROKEN requires at least one P1 violation; PARTIAL requires at least one P2 gap and no P1; SOUND requires no P1 and no P2. |
| C-05 | **Artifact written with correct frontmatter** | format | essential | Artifact written to `signals/rhythm/track/{topic}-track-{date}.md`. Frontmatter contains all required fields: skill, topic, date, papers_checked, p1_violations, track_integrity. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Transfer types classified correctly** | depth | recommended | Each dependency row in Phase 2 assigns one of the four transfer types: Definition, Structural, Empirical, Causal. The classification matches the nature of what transfers (e.g., a formula is Definition, a mathematical framework is Structural, a measured number is Empirical, a mechanism is Causal). |
| C-07 | **AMEND section gives targeted, actionable fixes** | depth | recommended | Phase 6 contains three fixes ranked P1, P2, P3. Each fix names the specific paper section to change and the exact change needed (e.g., "Add citation to P01b in P02 §3.1" not "improve citations"). P1 fix addresses the highest-severity violation found in Phase 4. |
| C-08 | **Critical path is identified** | coverage | recommended | Phase 5 lists the specific D-IDs (or states "none") that must be resolved before the next paper in the track can be submitted. The list is non-empty when P1 or P2 violations exist. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Implicit vs explicit citation distinguished** | depth | aspirational | Phase 3 verification blocks use IMPLICITLY (not just YES/NO) when a dependency is used in spirit but not cited by paper name or section. At least one IMPLICIT finding is explored with a note on whether implicit use is sufficient or whether an explicit citation is needed. |
| C-10 | **Modification justification assessed** | behavior | aspirational | For any dependency verified as MODIFIED, Phase 3 assesses whether the modification is justified (YES/NO/NOT ADDRESSED) and explains the implication — e.g., whether the modification extends, narrows, or contradicts the original result. |

---

## Scoring Example

```
Essential (5 criteria):  C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 FAIL
Recommended (3 criteria): C-06 PASS, C-07 PASS, C-08 FAIL
Aspirational (2 criteria): C-09 FAIL, C-10 FAIL

essential_pass = 4/5
recommended_pass = 2/3
aspirational_pass = 0/2

Composite = (4/5 * 60) + (2/3 * 30) + (0/2 * 10)
          = 48 + 20 + 0 = 68

Golden? NO — not all essential pass (C-05 failed)
```

---

## Failure Modes to Watch

- **Empty dependency table**: skill ran but MODULE.md was not read or had no dependency annotations — C-01 fails
- **Verdicts without verification blocks**: Phase 4 register present but Phase 3 blocks missing — C-02 fails
- **P1 count mismatch**: frontmatter `p1_violations` differs from P1-labeled rows in Phase 4 — C-03 and C-05 fail
- **Inconsistent integrity status**: SOUND declared despite PARTIAL or VIOLATED entries — C-04 fails
- **Generic fixes**: "Improve citation consistency" instead of naming paper, section, and change — C-07 fails
