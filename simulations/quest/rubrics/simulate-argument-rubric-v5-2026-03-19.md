Here is the complete v5 rubric. Summary of what changed:

---

## v5 delta

**Three new aspirational criteria (C-18, C-19, C-20)** extracted from the three R4 excellence signals:

| ID | Pattern | Enforcement |
|----|---------|------------|
| C-18 | critical-path-pre-commitment | Phase 0 names 2-3 CP steps; Phase 4 close checks whether P1 faults landed on them. The audit loop between fault severity and structural priority is the pass condition — not just a verdict. |
| C-19 | named-specialist-handoff | Named roles (Logician / Reviewer / Chair) with explicit closure language at the form-ID/validity boundary. Anonymous gates pass C-17 but fail C-19 — identity is the enforcement mechanism. |
| C-20 | advocate-commitment-gap | Gap fields written as "Needed X, found only Y" where X was pre-committed in Phase 0. UNSUPPORTED-GEN faults must trace to a named Phase 0 generalization. An assertion-only gap ("no empirical support") fails. |

**Boundary cases:** Each new criterion is non-redundant with its nearest neighbors — C-18 vs C-11/C-16, C-19 vs C-17, C-20 vs C-10/C-13 — with explicit separation statements.

**Score formula:** `aspirational_pass / 12 * 10` (pool: 9 → 12). Golden threshold unchanged.
fication target; C-16 requires a count-derived H0 verdict. C-18 requires a *priority map* pre-committed before reading, with a post-trace accountability check connecting P1 severity to CP flags -- a structural audit loop, not just a verdict.
- C-19 is not a duplicate of C-17: C-17 requires temporal separation between form naming and validity checks (any mechanism). C-19 requires *named specialist identities* as the enforcement mechanism -- the separation must be via role boundaries, not anonymous gates or sub-section labels alone.
- C-20 is not a duplicate of C-10/C-13: C-10 requires the fault be non-obvious and reviewer-worthy. C-13 requires a fault-class verdict at close. C-20 requires the Gap *field* to be written as a commitment-relative account -- "needed the pre-committed load-bearing claim X, found only Y" -- so that UNSUPPORTED-GEN is structurally derived from the Phase 0 commitment, not asserted independently.

**Score formula:** `aspirational_pass / 12 * 10` (pool grows from 9 to 12). Golden threshold unchanged.

---

## Criteria Summary

- **C-01--C-05** essential correctness/coverage
- **C-06--C-08** recommended depth/format
- **C-09** detects term drift pinpointed to a C-ID
- **C-10** ensures the P1/P2 fault is non-obvious and reviewer-worthy
- **C-11** *(R1)* falsification target in Phase 0 sharpens structural fault detection
- **C-12** *(R1)* inline reviewer hook inside every WEAK/BROKEN verdict
- **C-13** *(R1, tightened in v3)* fault-pattern closure names a structural fault class, not a depth tier
- **C-14** *(R2)* enumerated Class column makes C-13 mechanical at insertion time
- **C-15** *(R2)* reviewer depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) with domain comparison per WEAK/BROKEN step
- **C-16** *(R3)* null-hypothesis binary verdict -- H0 in Phase 0, mechanically derived reject/fail-to-reject at Phase 4 close
- **C-17** *(R3)* dedicated form-identification sub-pass before validity checks -- pre-commitment, not post-hoc labeling
- **C-18** *(R4)* critical-path pre-commitment -- Phase 0 names load-bearing steps; Phase 4 audits whether P1 faults landed on them
- **C-19** *(R4)* named specialist handoff -- named role identities with closure language enforce temporal separation via identity
- **C-20** *(R4)* advocate-commitment gap accounts -- Gap fields say "needed X, found only Y" relative to Phase 0 pre-committed assumptions

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
| C-07 | **AMEND section provides ordered, actionable fixes** | depth | recommended | AMEND contains exactly 3 fixes ordered P1 -> P2 -> P3. Each fix references the F-ID or C-ID it addresses and specifies what claim, evidence, or definition change would close the gap -- not just "add more evidence." |
| C-08 | **Artifact written with complete frontmatter** | format | recommended | Output file contains YAML frontmatter with all six required fields: skill, topic, date, claims_mapped (integer), broken_steps (integer), p1_count (integer). Values are consistent with the body (claims_mapped equals the row count in the Claim Map table). |

---

## Aspirational Criteria (10 pts)

*Scored as aspirational_pass / 12 * 10. All twelve criteria are equal weight.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Term drift detected and pinpointed** | depth | aspirational | At least one validity check reports "DRIFT: [description]" and the AMEND section's P3 fix names the specific definition claim (C-ID) where drift originates and proposes a stable replacement wording. |
| C-10 | **Fault exposes a structural weakness reviewers would flag** | behavior | aspirational | At least one P1 or P2 fault identifies a gap that is non-obvious (not a missing citation on a trivially true premise) and that a domain reviewer would plausibly raise. The Gap field explains *why* the inference fails, not just *that* it fails. |
| C-11 | **Falsification target stated before tracing begins** | depth | aspirational | Phase 0 (or equivalent preamble) contains an explicit best-case statement of the argument -- what it would look like if fully sound -- so the trace has a concrete target to disprove rather than only a vague mandate to find faults. The statement is referenced or refuted in at least one fault in the register. |
| C-12 | **Inline reviewer hook present on every WEAK/BROKEN verdict** | behavior | aspirational | Every STEP block whose verdict is WEAK or BROKEN includes a parenthetical or tagged line asking "Would a domain reviewer flag this?" with a YES/NO answer and one-sentence justification. The hook is inside the STEP block, not added retroactively in AMEND. |
| C-13 | **Fault pattern synthesized against Phase 0 at close** | depth | aspirational | Phase 4 (Fault Register) or a closing synthesis section explicitly asks whether the accumulated fault pattern confirms or refutes the Phase 0 best-case statement. The answer names the dominant fault class using structural vocabulary (e.g., definitional drift, unsupported generalization, circular dependency, invalid logical form). Naming only a depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) or confirming Phase 0 without a class name does not pass. |
| C-14 | **Fault class taxonomy column in Fault Register** | depth | aspirational | The Fault Register contains a `Class` column. Every row carries exactly one of four codes: DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM. Phase 4 closing identifies the dominant fault class by citing the most frequent code in the column -- no post-hoc invented label required. |
| C-15 | **Reviewer depth tier annotated per WEAK/BROKEN step** | behavior | aspirational | Every STEP block whose verdict is WEAK or BROKEN includes a reviewer depth classification (OBVIOUS / NOTABLE / SIGNIFICANT) with a one-sentence domain comparison explaining why a specialist would rate the gap at that tier. The tier tag also appears in the Fault Register Gap field for the corresponding fault. |
| C-16 | **Null-hypothesis binary verdict at Phase 4 close** | depth | aspirational | Phase 0 states an explicit null hypothesis of the form "This argument is structurally sound and requires no revision" (or equivalent). Phase 4 closing delivers a binary verdict mechanically derived from fault counts: at least one P1 fault -> "H0 is rejected"; zero P1 faults -> "H0 is not rejected". The closing also states an inertia defensibility conclusion ("Inertia is [defensible/not defensible]"). A prose judgment that reaches the same conclusion without deriving it from counts does not pass. |
| C-17 | **Dedicated form-identification sub-pass before validity checks** | depth | aspirational | Phase 3 contains a dedicated sub-pass, section, or column that names the logical form of each inference claim *before* the validity checks (consistency check, DRIFT check, reviewer flag) are run. At least 50% of inference steps show evidence of form naming preceding validity results. A logical form label appearing only inside or after a verdict does not pass -- temporal separation is required. |
| C-18 | **Critical-path pre-commitment with post-trace audit** | depth | aspirational | Phase 0 (or equivalent preamble) explicitly nominates 2-3 inference steps as most load-bearing ("critical path") before tracing begins. Phase 2 or the Claim Map marks those steps with a CP flag or equivalent. Phase 4 closing contains a dedicated accountability check: for each CP-flagged step, state whether a P1 fault landed on it. A trace that only counts P1 faults without connecting them to pre-committed CP steps does not pass -- the audit loop between fault severity and structural priority is the new requirement. |
| C-19 | **Named specialist handoff with closure language** | behavior | aspirational | Phase 3 assigns form identification and validity checking to distinct named roles (e.g., Logician, Empirical Reviewer, Committee Chair) and includes an explicit closure statement at the transition boundary -- e.g., "The Logician's pass is closed. All forms committed. The Empirical Reviewer begins." The named roles must be different identities (cannot co-execute), and the closure statement must appear at the handoff point, not as a general preamble. An anonymous gate ("complete 3A before 3B") or a role label with no closure language does not pass. |
| C-20 | **Advocate-commitment gap accounts in Fault Register** | behavior | aspirational | Gap fields in the Fault Register are written as commitment-relative structural accounts: "Needed [X pre-committed as load-bearing in Phase 0], found only [Y]." For every UNSUPPORTED-GEN fault, the Gap field names the specific generalization that was pre-committed as a load-bearing assumption and explains what evidence the paper provides instead. A Gap field that only asserts failure ("no empirical support") without tracing back to a Phase 0 commitment does not pass. |

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
C-18 critical-path pre-commitment + audit [PASS / FAIL]
C-19 named specialist handoff             [PASS / FAIL]
C-20 advocate-commitment gap accounts     [PASS / FAIL]

essential_pass    = /5
recommended_pass  = /3
aspirational_pass = /12

composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/12 * 10)
composite = ___

golden = all essential PASS AND composite >= 80  [YES / NO]
```
