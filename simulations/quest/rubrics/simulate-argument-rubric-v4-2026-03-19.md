Done. Here's what changed in v4:

**Two new aspirational criteria from R3 excellence signals:**

| ID | Pattern | Source | What it enforces |
|----|---------|--------|-----------------|
| C-16 | null-hypothesis-verdict | V-03 | Phase 0 states explicit H0; Phase 4 close delivers binary verdict *mechanically derived* from P1 count + inertia defensibility statement |
| C-17 | form-identification-sub-pass | V-02, V-03 | Dedicated sub-pass names logical form *before* validity checks run — temporal separation prevents post-hoc form assignment |

**Boundary cases explicitly stated:**
- C-16 is not a duplicate of C-11/C-13: the new requirement is count-driven derivation ("at least one P1 → H0 rejected") and an explicit inertia verdict, not just prose synthesis
- C-17 is not a duplicate of C-06: C-06 requires forms exist somewhere; C-17 requires they precede validity checks — temporal constraint, not presence constraint

**Score formula:** `aspirational_pass / 9 * 10` (pool grows from 7 to 9). Golden threshold unchanged.
1 → reject), delivering a binary sentence plus an inertia defensibility statement. The count-driven derivation and the inertia verdict are the new requirements.

**Why C-17 is not a duplicate of C-06:** C-06 requires named logical forms appear somewhere in the output (at least 50% of steps). C-17 requires form naming to occur as a dedicated phase or column pass *before* the validity checks — a temporal constraint, not just a presence constraint. Post-hoc form labeling passes C-06 but fails C-17.

**Score formula:** `aspirational_pass / 9 * 10` (pool grows from 7 to 9). Golden threshold unchanged.

**Criteria summary:**
- **C-01–C-05** essential correctness/coverage
- **C-06–C-08** recommended depth/format
- **C-09** detects term drift pinpointed to a C-ID
- **C-10** ensures the P1/P2 fault is non-obvious and reviewer-worthy
- **C-11** *(R1)* falsification target in Phase 0 sharpens structural fault detection
- **C-12** *(R1)* inline reviewer hook inside every WEAK/BROKEN verdict
- **C-13** *(R1, tightened in v3)* fault-pattern closure names a structural fault class, not a depth tier
- **C-14** *(R2)* enumerated Class column makes C-13 mechanical at insertion time
- **C-15** *(R2)* reviewer depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) with domain comparison per WEAK/BROKEN step
- **C-16** *(R3)* null-hypothesis binary verdict — H0 in Phase 0, mechanically derived reject/fail-to-reject at Phase 4 close
- **C-17** *(R3)* dedicated form-identification sub-pass before validity checks — pre-commitment, not post-hoc labeling

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
| C-08 | **Artifact written with complete frontmatter** | format | recommended | Output file contains YAML frontmatter with all six required fields: skill, topic, date, claims_mapped (integer), broken_steps (integer), p1_count (integer). Values are consistent with the body (claims_mapped equals the row count in the Claim Map table). |

---

## Aspirational Criteria (10 pts)

*Scored as aspirational_pass / 9 * 10. All nine criteria are equal weight.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Term drift detected and pinpointed** | depth | aspirational | At least one validity check reports "DRIFT: [description]" and the AMEND section's P3 fix names the specific definition claim (C-ID) where drift originates and proposes a stable replacement wording. |
| C-10 | **Fault exposes a structural weakness reviewers would flag** | behavior | aspirational | At least one P1 or P2 fault identifies a gap that is non-obvious (not a missing citation on a trivially true premise) and that a domain reviewer would plausibly raise. The Gap field explains *why* the inference fails, not just *that* it fails. |
| C-11 | **Falsification target stated before tracing begins** | depth | aspirational | Phase 0 (or equivalent preamble) contains an explicit best-case statement of the argument — what it would look like if fully sound — so the trace has a concrete target to disprove rather than only a vague mandate to find faults. The statement is referenced or refuted in at least one fault in the register. |
| C-12 | **Inline reviewer hook present on every WEAK/BROKEN verdict** | behavior | aspirational | Every STEP block whose verdict is WEAK or BROKEN includes a parenthetical or tagged line asking "Would a domain reviewer flag this?" with a YES/NO answer and one-sentence justification. The hook is inside the STEP block, not added retroactively in AMEND. |
| C-13 | **Fault pattern synthesized against Phase 0 at close** | depth | aspirational | Phase 4 (Fault Register) or a closing synthesis section explicitly asks whether the accumulated fault pattern confirms or refutes the Phase 0 best-case statement. The answer names the dominant fault class using structural vocabulary (e.g., definitional drift, unsupported generalization, circular dependency, invalid logical form). Naming only a depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) or confirming Phase 0 without a class name does not pass. |
| C-14 | **Fault class taxonomy column in Fault Register** | depth | aspirational | The Fault Register contains a `Class` column. Every row carries exactly one of four codes: DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM. Phase 4 closing identifies the dominant fault class by citing the most frequent code in the column — no post-hoc invented label required. |
| C-15 | **Reviewer depth tier annotated per WEAK/BROKEN step** | behavior | aspirational | Every STEP block whose verdict is WEAK or BROKEN includes a reviewer depth classification (OBVIOUS / NOTABLE / SIGNIFICANT) with a one-sentence domain comparison explaining why a specialist would rate the gap at that tier. The tier tag also appears in the Fault Register Gap field for the corresponding fault. |
| C-16 | **Null-hypothesis binary verdict at Phase 4 close** | depth | aspirational | Phase 0 states an explicit null hypothesis of the form "This argument is structurally sound and requires no revision" (or equivalent). Phase 4 closing delivers a binary verdict mechanically derived from fault counts: at least one P1 fault → "H0 is rejected"; zero P1 faults → "H0 is not rejected". The closing also states an inertia defensibility conclusion ("Inertia is [defensible/not defensible]"). A prose judgment that reaches the same conclusion without deriving it from counts does not pass. |
| C-17 | **Dedicated form-identification sub-pass before validity checks** | depth | aspirational | Phase 3 contains a dedicated sub-pass, section, or column that names the logical form of each inference claim *before* the validity checks (consistency check, DRIFT check, reviewer flag) are run. At least 50% of inference steps show evidence of form naming preceding validity results. A logical form label appearing only inside or after a verdict does not pass — temporal separation is required. |

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
C-14 fault class taxonomy column present  [PASS / FAIL]
C-15 reviewer depth tier annotated        [PASS / FAIL]
C-16 null-hypothesis binary verdict       [PASS / FAIL]
C-17 form-identification sub-pass         [PASS / FAIL]

essential_pass    = /5
recommended_pass  = /3
aspirational_pass = /9

composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/9 * 10)
composite = ___

golden = all essential PASS AND composite >= 80  [YES / NO]
```
