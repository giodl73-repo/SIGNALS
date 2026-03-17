# campaign-validate Rubric — v2

> Updated after R1 scoring (V-01: 93, V-02: 98). Three new aspirational criteria added from
> excellence signals EX-1, EX-3, EX-4. C-10 criterion notes updated with EX-2 guidance.

---

## Quick Reference

**5 essential** (all must pass for golden):
- **C-01** — All 5 sub-skills represented (review-design, review-users, review-customers, listen-feedback, listen-adoption). Common failure: listen-adoption silently skipped.
- **C-02** — Findings ranked by *adoption impact*, not severity. A chasm-blocking P2 outranks a cosmetic P1.
- **C-03** — Explicit go/no-go verdict. "It depends" without a condition fails.
- **C-04** — Top 3 blockers attributed to source sub-skill (trivially passes on go verdicts).
- **C-05** — Artifact written to `simulations/{topic}/validate-{date}.md`.

**3 recommended** (needed to reach composite >= 80):
- **C-06** — Cross-signal synthesis: at least one pattern/tension linking 2+ sub-skills. Concatenation fails.
- **C-07** — Per-sub-skill labeled sections for navigability.
- **C-08** — Severity tiers (P1/P2/P3 or equivalent), not flat list.

**5 aspirational** (bonus points above baseline):
- **C-09** — Adoption impact quantified per finding (e.g., "blocks chasm crossing").
- **C-10** — Remediation paths for each top blocker.
- **C-11** *(new v2)* — Table-format per sub-skill as completeness gate.
- **C-12** *(new v2)* — Adoption Impact as a dedicated column separate from Severity.
- **C-13** *(new v2)* — Explicit artifact confirmation string emitted after write.

Golden threshold: all 5 essential pass + composite >= 80.

---

## Essential Criteria (weight: 60 points total)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | All 5 sub-skills represented | completeness | Output explicitly invokes and reports findings from all five sub-skills: review-design, review-users, review-customers, listen-feedback, listen-adoption. Each must have distinct content — shared content between listen-feedback and listen-adoption is a fail signal. |
| C-02 | Ranked by adoption impact | correctness | Findings are sorted by adoption impact, not severity. Adoption impact is the primary sort key. A P2 finding that blocks chasm crossing ranks above a P1 cosmetic finding. Severity-first ranking fails this criterion. |
| C-03 | Explicit go/no-go verdict | correctness | Output includes a go/no-go readiness signal as a named field or prominent section. Verdict is unambiguous (not "it depends" without a condition). |
| C-04 | Top blockers attributed to sub-skill | correctness | If verdict is no-go or conditional, output lists top 3 specific blockers, each attributed to the sub-skill that surfaced it. If verdict is go, this criterion passes trivially. |
| C-05 | Artifact written to disk | behavior | Output is written to `simulations/{topic}/validate-{date}.md` following the signal artifact naming convention. File must exist after skill run. |

---

## Recommended Criteria (weight: 30 points total)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Cross-signal synthesis | depth | Brief identifies at least one pattern or tension appearing across 2+ sub-skills (e.g., a usability finding from review-users confirmed by a support-ticket prediction from listen-feedback). Not just a concatenation of sub-skill outputs. |
| C-07 | Per-sub-skill labeled sections | format | Each sub-skill's findings appear under a clearly labeled heading. Reader can navigate directly to review-design findings, listen-adoption findings, etc. without reading the whole document. |
| C-08 | Finding severity differentiation | depth | Findings use consistent severity tiers (P1/P2/P3, blocking/major/minor, or equivalent). High-severity findings visually distinct from low-severity. Not a flat undifferentiated list. |

---

## Aspirational Criteria (weight: 5 points each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Adoption impact quantified per finding | depth | Each ranked finding includes an estimated adoption impact magnitude — e.g., "blocks innovator segment (5%)", "chasm risk: high — majority will not cross without X". Magnitude is specific, not generic. |
| C-10 | Remediation paths for top blockers | depth | Each top blocker includes a concrete remediation suggestion pointing to a design decision the team can make. Not just "fix this" — specifies what change would resolve the blocker and which sub-skill result supports it. |
| C-11 | Table-format per sub-skill as completeness gate | format | Each sub-skill's findings are presented in a structured table (not prose), so that a missing sub-skill appears as an empty table rather than invisible absent text. The table skeleton is present even if the sub-skill found nothing — making omission detectable, not silent. |
| C-12 | Adoption Impact as dedicated column separate from Severity | format | Severity and Adoption Impact appear as distinct columns or fields in the findings output. A finding can be P3 severity and high adoption impact; the two axes are never merged. This structural separation prevents rank-by-severity errors at the layout level. |
| C-13 | Explicit artifact confirmation string | behavior | After writing the artifact, the skill emits a confirmation line: "Artifact written: simulations/{topic}/validate-{date}.md". The confirmation string is machine-detectable, closing the C-05 verification loop with a positive signal rather than relying on absence of error. |

---

## Criterion Notes

**C-01 — all 5 must appear**: A common failure mode is skipping listen-adoption because the
model conflates it with listen-feedback. Pass requires both listen sub-skills visibly present
with distinct content.

**C-02 — adoption impact is the sort key**: Findings ranked by severity alone (P1 first) is
NOT sufficient. The ranking must reflect adoption impact — a P2 finding that blocks the chasm
crossing outranks a P1 cosmetic issue.

**C-04 — trivial pass on go**: If the brief reaches a go verdict, C-04 passes automatically.
The criterion only activates on no-go or "go with conditions" outcomes.

**C-06 — synthesis vs concatenation**: The brief fails C-06 if it simply lists Section 1 =
review-design output, Section 2 = review-users output, etc. Synthesis means drawing a
connection across sections: "X surfaced in review-users is confirmed by Y in listen-feedback."

**C-10 — remediation as structured column (EX-2)**: The strongest implementations embed
remediation inside the blocker table as a dedicated column, not as separate prose. When
remediation is a column, every row demands a cell — the structure forces completeness.
Prose remediation sections pass C-10 but risk being skipped; columnar remediation is the
preferred pattern (see V-02 vs V-01 in R1 scoring).

**C-11 — table skeleton forces completeness (EX-1)**: The criterion is met when the table
structure is pre-defined with sub-skill labels as row or section headers, so a skipped
sub-skill produces a visibly empty table rather than no table at all. V-02 demonstrated this:
"table-per-sub-skill structure makes omission visually obvious as a blank table."

**C-12 — orthogonal axes (EX-3)**: The column separation communicates the distinction at the
layout level, before any cell is read. A finding ranked P3 severity / high adoption impact is
correctly ranked higher than a P1 cosmetic — but only if the reader can see both dimensions.
Merged fields (e.g., "P2 — high adoption impact" in one cell) pass C-08 but fail C-12.

**C-13 — confirmation as detection signal (EX-4)**: The confirmation string is not just
informational — it is a detectable artifact. Automated scoring and pipeline validation can
grep for "Artifact written:" to confirm the write step executed without inspecting the
filesystem. This closes the loop on C-05 with a positive signal.

---

## Scoring Model

| Tier | Criteria | Points | Max |
|------|----------|--------|-----|
| Essential | C-01 through C-05 | 12 pts each | 60 |
| Recommended | C-06 through C-08 | 10 pts each | 30 |
| Aspirational | C-09 through C-13 | 5 pts each | 25 |
| **Total** | | | **115** |

Golden: all 5 essential pass + composite >= 80.
Composite > 100 is achievable when all aspirational criteria pass.

---

## Example Pass/Fail Patterns

| Pattern | Essential | Recommended | Composite | Golden? |
|---------|-----------|-------------|-----------|---------|
| All 5 sub-skills, go verdict, ranked findings, synthesis | 5/5 | 3/3 | 100 | YES |
| Missing listen-adoption, rest good | 4/5 | 3/3 | 78 | NO — C-01 fails |
| All 5 present, findings NOT ranked by adoption impact | 4/5 | 2/3 | 72 | NO — C-02 fails |
| All 5, ranked, verdict present, blockers listed, no synthesis | 5/5 | 1/3 | 70 | NO — composite < 80 |
| All 5, ranked, verdict, blockers, synthesis, severity tiers | 5/5 | 3/3 | 100 | YES |
| V-02 pattern: tables + columns + confirmation + remediation col | 5/5 | 3/3 + C-11/C-12/C-13 | 113 | YES |
