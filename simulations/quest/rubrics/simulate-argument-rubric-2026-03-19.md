Rubric written to `simulations/quest/rubrics/simulate-argument-rubric-2026-03-19.md`.

**Design rationale:**

- **C-01/C-02** lock the claim map structure — without a valid directed graph the whole trace is meaningless
- **C-03** enforces the "every section contributes" requirement from the spec
- **C-04** is the core of the skill — every inference must have a full STEP block (logical form + 3 checks + verdict)
- **C-05** closes the loop: verdicts must propagate into the fault register with no silent gaps
- **C-06** pushes beyond restating "if X then Y" — named logical forms (modus ponens, abduction, etc.) make the trace reviewable
- **C-07** validates AMEND is ordered and specific, not vague ("add evidence")
- **C-08** checks frontmatter consistency — `claims_mapped` must match actual row count
- **C-09/C-10** are the bar-raisers: term drift pinpointed to a C-ID, and the P1/P2 fault is non-obvious and reviewer-worthy
im text and a valid type (premise / inference / empirical / definition / conclusion). Minimum 6 claims. |
| C-02 | **Dependency graph is complete** | correctness | essential | Every claim with type=inference lists at least one C-ID in Depends on. Every C-ID referenced as a dependency exists in the table. No dangling references. |
| C-03 | **Section coverage satisfied** | coverage | essential | At least one claim is drawn from each major section of the source paper. If the paper has N sections, at least N distinct sections are represented across all claims. |
| C-04 | **Every inference step is traced** | correctness | essential | For every claim with type=inference, a STEP block exists with: logical form (named or stated), all three validity checks answered (YES/WEAK/NO or YES/CITED/ASSUMED/UNSUPPORTED/YES/DRIFT), and a verdict of SOUND, WEAK, or BROKEN. |
| C-05 | **Fault register matches verdicts** | correctness | essential | Every claim whose STEP verdict is BROKEN or WEAK appears in the Fault Register with a non-empty Gap, Fix required, and Severity (P1/P2/P3). No BROKEN/WEAK steps are absent from the register. |

---

## Recommended Criteria (30 pts)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Logical forms are named, not just restated** | depth | recommended | Each STEP block names a logical structure (e.g., modus ponens, abduction, analogy, inductive generalization) rather than only writing "if X and Y then Z". At least 50% of inference steps have a named form. |
| C-07 | **AMEND section provides ordered, actionable fixes** | depth | recommended | AMEND contains exactly 3 fixes ordered P1 → P2 → P3. Each fix references the F-ID or C-ID it addresses and specifies what claim, evidence, or definition change would close the gap — not just "add more evidence." |
| C-08 | **Artifact written with complete frontmatter** | format | recommended | Output file contains YAML frontmatter with all five required fields: skill, topic, date, claims_mapped (integer), broken_steps (integer), p1_count (integer). Values are consistent with the body (claims_mapped equals the row count in the Claim Map table). |

---

## Aspirational Criteria (10 pts)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Term drift detected and pinpointed** | depth | aspirational | At least one validity check reports "DRIFT: [description]" and the AMEND section's P3 fix names the specific definition claim (C-ID) where drift originates and proposes a stable replacement wording. |
| C-10 | **Fault exposes a structural weakness reviewers would flag** | behavior | aspirational | At least one P1 or P2 fault identifies a gap that is non-obvious (not a missing citation on a trivially true premise) and that a domain reviewer would plausibly raise. The Gap field explains *why* the inference fails, not just *that* it fails. |

---

## Disqualifying Conditions

Output scores zero if any of the following are true:

- Claim map has fewer than 6 rows.
- No STEP blocks are present (phase 3 skipped entirely).
- Fault Register is absent or empty when at least one WEAK/BROKEN verdict exists.
- AMEND is absent.

---

## Score Sheet Template

```
C-01 claim map present/populated      [PASS / FAIL]
C-02 dependency graph complete        [PASS / FAIL]
C-03 section coverage satisfied       [PASS / FAIL]
C-04 every inference step traced      [PASS / FAIL]
C-05 fault register matches verdicts  [PASS / FAIL]

C-06 logical forms named              [PASS / FAIL]
C-07 AMEND ordered + actionable       [PASS / FAIL]
C-08 artifact frontmatter complete    [PASS / FAIL]

C-09 term drift detected              [PASS / FAIL]
C-10 structural weakness exposed      [PASS / FAIL]

essential_pass = /5
recommended_pass = /3
aspirational_pass = /2

composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
composite = ___

golden = all essential PASS AND composite >= 80  [YES / NO]
```
