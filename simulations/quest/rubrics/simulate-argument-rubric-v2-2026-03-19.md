Done. Here's what changed in v2:

**Three new aspirational criteria from R1 excellence signals:**

| ID | Pattern | What it enforces |
|----|---------|-----------------|
| C-11 | falsification-target | Phase 0 best-case statement — concrete target to disprove before tracing starts |
| C-12 | inline-reviewer-hook | "Would a domain reviewer flag this?" inside every WEAK/BROKEN STEP block at detection time |
| C-13 | fault-pattern-closure | Phase 4 closing synthesis: does the fault pattern confirm or refute Phase 0? |

**Score sheet update:** aspirational pool grows from 2 to 5 criteria. Formula changes from `aspirational_pass/2 * 10` to `aspirational_pass/5 * 10` — same 10-point ceiling, higher bar to reach it. Golden threshold (`all essential PASS AND composite >= 80`) is unchanged.
if X then Y" — named logical forms (modus ponens, abduction, etc.) make the trace reviewable
- **C-07** validates AMEND is ordered and specific, not vague ("add evidence")
- **C-08** checks frontmatter consistency — `claims_mapped` must match actual row count
- **C-09** detects term drift pinpointed to a C-ID
- **C-10** ensures the P1/P2 fault is non-obvious and reviewer-worthy
- **C-11** *(new)* falsification target in Phase 0 sharpens structural fault detection over surface corrections
- **C-12** *(new)* inline reviewer hook inside every WEAK/BROKEN verdict operationalizes C-10 at detection time
- **C-13** *(new)* fault-pattern closure at Phase 4 forces structural synthesis across faults rather than a disconnected list

---

## Essential Criteria (60 pts)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Claim map present and populated** | correctness | essential | Output contains a Claim Map table with at least 6 rows. Each row has a C-ID, claim text, and a valid type (premise / inference / empirical / definition / conclusion). |
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

*Scored as aspirational_pass / 5 * 10. All five criteria are equal weight.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Term drift detected and pinpointed** | depth | aspirational | At least one validity check reports "DRIFT: [description]" and the AMEND section's P3 fix names the specific definition claim (C-ID) where drift originates and proposes a stable replacement wording. |
| C-10 | **Fault exposes a structural weakness reviewers would flag** | behavior | aspirational | At least one P1 or P2 fault identifies a gap that is non-obvious (not a missing citation on a trivially true premise) and that a domain reviewer would plausibly raise. The Gap field explains *why* the inference fails, not just *that* it fails. |
| C-11 | **Falsification target stated before tracing begins** | depth | aspirational | Phase 0 (or equivalent preamble) contains an explicit best-case statement of the argument — what it would look like if fully sound — so the trace has a concrete target to disprove rather than only a vague mandate to find faults. The statement is referenced or refuted in at least one fault in the register. |
| C-12 | **Inline reviewer hook present on every WEAK/BROKEN verdict** | behavior | aspirational | Every STEP block whose verdict is WEAK or BROKEN includes a parenthetical or tagged line asking "Would a domain reviewer flag this?" with a YES/NO answer and one-sentence justification. The hook is inside the STEP block, not added retroactively in AMEND. |
| C-13 | **Fault pattern synthesized against Phase 0 at close** | depth | aspirational | Phase 4 (Fault Register) or a closing synthesis section explicitly asks whether the accumulated fault pattern confirms or refutes the Phase 0 best-case statement. The answer names the dominant fault class (e.g., definitional drift, unsupported generalization, circular dependency) rather than listing faults again. |

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
C-01 claim map present/populated          [PASS / FAIL]
C-02 dependency graph complete            [PASS / FAIL]
C-03 section coverage satisfied           [PASS / FAIL]
C-04 every inference step traced          [PASS / FAIL]
C-05 fault register matches verdicts      [PASS / FAIL]

C-06 logical forms named                  [PASS / FAIL]
C-07 AMEND ordered + actionable           [PASS / FAIL]
C-08 artifact frontmatter complete        [PASS / FAIL]

C-09 term drift detected                  [PASS / FAIL]
C-10 structural weakness exposed          [PASS / FAIL]
C-11 falsification target present         [PASS / FAIL]
C-12 inline reviewer hook on WEAK/BROKEN  [PASS / FAIL]
C-13 fault pattern synthesized at close   [PASS / FAIL]

essential_pass    = /5
recommended_pass  = /3
aspirational_pass = /5

composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)
composite = ___

golden = all essential PASS AND composite >= 80  [YES / NO]
```
