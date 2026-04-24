Reading the v7 rubric and R7 scorecard to extract the three new excellence patterns before writing v8.

The three R7 excellence signals map to C-27, C-28, C-29:

- **named-form-type-trigger-examples** → C-27: advocate must enumerate specific form types (causal inference, analogy), not assert generically
- **logician-cross-phase-derivation-double-lock** → C-28: C-25 requires BOTH closure phase-language AND row-level `Derives from` reference in Phase 4; V-02 proved neither alone suffices
- **unconditional-cp-adjacency-with-gen-id-notes** → C-29: Step 2 runs unconditionally even when Step 1 = CONFIRMED; CONFIRMED-ELSEWHERE must name the Gen-ID anchor from Phase 3

Pool grows 18→21. Formula: `aspirational_pass / 21 * 10`. Golden threshold unchanged at 96.

```markdown
---
skill: simulate-argument
version: v8
date: 2026-03-19
pool: 21
golden_threshold: 96
---

# simulate-argument Rubric — v8

## v8 delta

**Three new aspirational criteria (C-27, C-28, C-29)** extracted from R7 excellence
signals — the first round where one variation (V-05) achieved 18/18 aspirational and
all five variations scored golden.

| ID | Pattern | Enforcement |
|----|---------|------------|
| C-27 | advocate-named-form-type-trigger-enumeration | The Advocate block must explicitly enumerate causal inference and argument-from-analogy as form types that trigger the content-conditional generalization scan. A generic assertion that "every inference step" or "all inference steps" receives the scan does not pass — the enumeration must name the specific form types and explain why their key assumptions may posit universal applicability. The Advocate closure must attest that steps bearing the enumerated labels received the same generalization scan as steps labeled "inductive generalization." A variation that passes C-24 via a general assertion without named form types does not pass C-27. |
| C-28 | logician-cross-phase-derivation-double-lock | Satisfying C-25 requires two simultaneously present elements: (1) the Logician's closure explicitly states "no subsequent *phase* may reclassify logical structure," AND (2) each Phase-4 INVALID-FORM row carries an explicit `Derives from: FORM [C-ID]` derivation reference tracing back to the Phase-3A committed form label. A Phase-4 INVALID-FORM row with a derivation reference but no closure phase-extension language does not pass. A Logician closure with phase-extension language but no Phase-4 row-level derivation references does not pass. Both elements must be present simultaneously. |
| C-29 | unconditional-cp-adjacency-with-gen-id-provenance | Step 2 of the CP audit adjacency search must run unconditionally — even when Step 1 concludes CONFIRMED, Step 2 must execute and document which non-CP step(s) were examined (or explicitly confirm none were found). When the adjacency search identifies an UNSUPPORTED-GEN fault on an adjacent step, the CONFIRMED-ELSEWHERE verdict must name the Gen-ID anchor from Phase 3 (e.g., "CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM"). A CP audit where Step 2 runs only when Step 1 is not CONFIRMED (conditional procedure) does not pass C-29 even if all DISCONFIRMED verdicts have adjacency documentation. |

**Boundary cases:**
- C-27 is not a duplicate of C-24: C-24 requires the gen-scan trigger to be content-conditional rather than form-label-conditional. C-27 requires the Advocate block to explicitly enumerate the form types that carry content-conditional risk (causal inference, analogy), with closure attestation. A variation that fires the scan on semantic content using only a generic instruction passes C-24 but fails C-27.
- C-28 is not a duplicate of C-25: C-25 requires the Logician closure to state that no subsequent phase may reclassify logical structure. C-28 requires that the Phase-4 INVALID-FORM rows also carry explicit row-level derivation references to the Phase-3A committed form. A variation with the Logician closure phase-language but no Phase-4 derivation rows passes C-25 but fails C-28. Both elements must be present simultaneously for C-28.
- C-29 is not a duplicate of C-26: C-26 requires DISCONFIRMED to be written only after a documented adjacency search. C-29 requires Step 2 to run unconditionally — even for CONFIRMED steps — and requires CONFIRMED-ELSEWHERE verdicts to carry Gen-ID provenance from Phase 3. A variation where Step 2 runs only before DISCONFIRMED verdicts passes C-26 but fails C-29.

**Score formula:** `aspirational_pass / 21 * 10` (pool grows from 18 to 21).
Golden threshold unchanged at 96.

---

## Criteria Summary

- **C-01--C-05** essential correctness/coverage
- **C-06--C-08** recommended depth/format
- **C-09** detects term drift pinpointed to a C-ID
- **C-10** ensures the P1/P2 fault is non-obvious and reviewer-worthy
- **C-11** *(R1)* falsification target in Phase 0 sharpens structural fault detection
- **C-12** *(R1)* inline reviewer hook inside every WEAK/BROKEN verdict
- **C-13** *(R1, tightened v3)* fault-pattern closure names a structural fault class, not a depth tier
- **C-14** *(R2)* enumerated Class column makes C-13 mechanical at insertion time
- **C-15** *(R2)* reviewer depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) with domain comparison per WEAK/BROKEN step
- **C-16** *(R3)* null-hypothesis binary verdict — H0 in Phase 0, mechanically derived reject/fail-to-reject at Phase 4 close
- **C-17** *(R3)* dedicated form-identification sub-pass before validity checks — pre-commitment, not post-hoc labeling
- **C-18** *(R4)* critical-path pre-commitment — Phase 0 names load-bearing steps; Phase 4 audits whether P1 faults landed on them
- **C-19** *(R4)* named specialist handoff — named role identities with closure language enforce temporal separation via identity
- **C-20** *(R4)* advocate-commitment gap accounts — Gap fields say "needed X, found only Y" relative to Phase 0 pre-committed generalizations
- **C-21** *(R5)* advocate phase 3 gen-anchoring — Phase 3 best readings cite Phase 0 Gen-IDs, creating Phase 0→Phase 3→Phase 4 chain
- **C-22** *(R5)* logician global binding — Logician's closure names all downstream specialists and prohibits reclassification globally
- **C-23** *(R5)* CP audit three-way verdict — CONFIRMED/DISCONFIRMED/CONFIRMED-ELSEWHERE per CP step; third category is required
- **C-24** *(R6)* advocate form-independent gen-anchoring — Gen-ID anchor trigger fires on content of best reading, not Logician's form label; two-field check required
- **C-25** *(R6)* logician cross-phase immutability — reclassification prohibition extends to phases; Phase 4 INVALID-FORM derives from Phase 3A committed form only
- **C-26** *(R6)* CP audit forced adjacency search — DISCONFIRMED requires documented Step 2 adjacency search; passive omission does not pass
- **C-27** *(R7)* advocate named form-type trigger enumeration — Advocate block explicitly names causal inference and analogy as trigger form types; closure attests enumerated-label scan; generic assertion without named types does not pass
- **C-28** *(R7)* logician cross-phase derivation double-lock — C-25 requires both Logician closure phase-language AND Phase-4 row-level `Derives from: FORM [C-ID]` derivation references; neither element alone suffices
- **C-29** *(R7)* unconditional CP adjacency with Gen-ID provenance — Step 2 runs for every CP step unconditionally; CONFIRMED-ELSEWHERE verdicts must name the Gen-ID anchor from Phase 3; conditional Step-2 procedure does not pass

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
| C-06 | **Logical form vocabulary** | depth | recommended | Logician names form from an enumerated vocabulary (modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism, argument from analogy, inductive generalization, inference to the best explanation, causal inference, etc.) in each FORM block. Ad-hoc or post-hoc labels do not pass. |
| C-07 | **Phase 5 repair instructions** | format | recommended | Phase 5 repair plan orders faults P1→P2→P3, references F-ID, C-ID, and Class for each, and provides exact repair instructions sufficient to re-run Phase 3. |
| C-08 | **Frontmatter complete** | format | recommended | All six frontmatter fields present and populated: skill, topic, date, claims_mapped, broken_steps, p1_count. |

---

## Aspirational Criteria (10 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Term drift detected** | depth | DRIFT check in 3B-CRITIC names the drifted term, the originating C-ID where the term was defined, and the shift observed. AMEND P3 DEF-DRIFT in the Fault Register names the originating C-ID and proposes a stable replacement. |
| C-10 | **Non-obvious fault surfaced** | depth | The P1 or P2 fault identified is not surface-level. It requires structural analysis (form examination, assumption exposure, generalization scope) that a non-expert reviewer would miss. The fault-pattern closure explains why the fault is non-obvious. |
| C-11 | **Falsification target pre-committed** | depth | Phase 0 includes at least one explicit falsification target (H0 or structural pre-commitment). Phase 4 returns to every Phase 0 pre-commitment and audits the outcome. |
| C-12 | **Inline reviewer hook present** | format | Inside every WEAK or BROKEN VERDICT block, the Reviewer or Chair includes an inline flag: "As committee chair, would I flag this in a written review? YES/NO" with a one-sentence justification. |
| C-13 | **Fault-pattern closure names structural class** | depth | The Phase 4 closing step names the dominant fault class using a structural code (e.g., UNSUPPORTED-GEN, INVALID-FORM, DEF-DRIFT, SCOPE-OVERREACH) — not a depth tier (OBVIOUS/NOTABLE/SIGNIFICANT). |
| C-14 | **Enumerated Class column in Fault Register** | format | The Fault Register includes a Class column populated with enumerated fault codes. Phase 4 step 1 counts per code and names the dominant class. |
| C-15 | **Reviewer depth tier with domain comparison** | depth | For every WEAK or BROKEN step, the Chair assigns a depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) and provides a one-sentence domain comparison explaining the tier assignment. |
| C-16 | **Null-hypothesis binary verdict** | depth | Phase 0 states an explicit H0. Phase 4 step 2 derives a binary verdict (REJECT H0 / FAIL TO REJECT H0) from fault counts. Phase 4 step 3 states the H0 verdict alongside the inertia verdict. |
| C-17 | **Dedicated form-identification sub-pass** | depth | The Logician (3A) completes a dedicated form-identification sub-pass that pre-commits to a form label for each inference step before any validity checks run. Re-labeling at Phase 4 is not permitted. |
| C-18 | **Critical-path pre-commitment and audit** | depth | Phase 0 names the load-bearing (critical-path) steps. Phase 4 closing step 4 audits per CP step: prediction + trace outcome + three-way verdict (CONFIRMED/DISCONFIRMED/CONFIRMED-ELSEWHERE) + structural risk distribution sentence. |
| C-19 | **Named specialist handoff with closure language** | format | All specialists make first-person identity commitments with closure language. The Logician simultaneously names all downstream specialists and prohibits reclassification in a single closure statement. |
| C-20 | **Advocate commitment gap accounting** | depth | The Gen-registry in Phase 0 pre-commits generalizations with Gen-IDs. The Advocate's Gap field states "needed X (Gen-NN), found only Y" relative to the pre-committed generalization. Phase 4 step 5 audits generalization accountability per Gen-ID. |
| C-21 | **Advocate Phase 3 gen-anchoring** | depth | Phase 3 best readings cite Phase 0 Gen-IDs via a two-field check: `Generalization assumed: YES/NO` followed by `Gen-ID anchor: Gen-NN`. This creates a traceable Phase 0→Phase 3→Phase 4 provenance chain. |
| C-22 | **Logician global binding** | depth | The Logician's closure names all downstream specialists by role and states: "No subsequent specialist may reclassify logical structure." Both all-downstream naming and the explicit prohibition must be present. |
| C-23 | **CP audit three-way verdict** | depth | Phase 4 closing step 4 uses all three verdict categories: CONFIRMED, DISCONFIRMED, and CONFIRMED-ELSEWHERE. The third category (CONFIRMED-ELSEWHERE) must appear at least once and be explained. |
| C-24 | **Advocate form-independent gen-anchoring** | depth | The gen-scan trigger fires on the semantic content of the best reading — whether the assumption extends beyond the studied population — not on the Logician's form label. A two-field check is required: `Generalization assumed: YES/NO` followed by `Gen-ID anchor`. Causal inference and analogy steps that assume universal mechanism applicability must trigger the anchor regardless of form label. A best reading that cites Gen-ID only when the Logician labeled the step "inductive generalization" does not pass. |
| C-25 | **Logician cross-phase immutability** | depth | The Logician's closure explicitly states that no subsequent *phase* may reclassify logical structure. Phase 4 verdicts of INVALID-FORM must derive from the Phase 3A committed form; re-examination of form assignment at Phase 4 is structurally prohibited. A closure that names specialists but does not extend the prohibition to phases does not pass. |
| C-26 | **CP audit forced adjacency search** | depth | Before DISCONFIRMED may be written in the Phase 4 CP audit, the analyst must complete and document a Step 2 adjacency search — identifying which non-CP step the fault landed on (or confirming none). DISCONFIRMED is an active documented conclusion, not a passive absence of evidence. A CP audit that writes DISCONFIRMED without documenting the adjacency search does not pass. |
| C-27 | **Advocate named form-type trigger enumeration** | depth | The Advocate block explicitly enumerates causal inference and argument-from-analogy as form types whose key assumptions may posit universal applicability and must therefore trigger the content-conditional gen scan. The Advocate closure attests that steps bearing the enumerated labels received the same generalization scan as steps labeled "inductive generalization." A generic assertion that "every inference step" receives the scan, without naming specific form types, does not pass even if C-24 is satisfied. |
| C-28 | **Logician cross-phase derivation double-lock** | depth | Satisfying C-25 requires two simultaneously present elements: (1) the Logician's closure explicitly states "no subsequent *phase* may reclassify logical structure," AND (2) each Phase-4 INVALID-FORM row carries an explicit `Derives from: FORM [C-ID]` derivation reference tracing back to the Phase-3A committed form label. A Phase-4 INVALID-FORM row with a derivation reference but no Logician closure phase-extension language does not pass. A Logician closure with phase-extension language but no Phase-4 row-level derivation references does not pass. Both elements must be present. |
| C-29 | **Unconditional CP adjacency with Gen-ID provenance** | depth | Step 2 of the CP audit adjacency search must run unconditionally — even when Step 1 concludes CONFIRMED, Step 2 must execute and document which non-CP step(s) were examined (or explicitly confirm none). When the adjacency search identifies an UNSUPPORTED-GEN fault on an adjacent step, the CONFIRMED-ELSEWHERE verdict must name the Gen-ID anchor from Phase 3 (e.g., "CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM"). A CP audit where Step 2 runs only when Step 1 is not CONFIRMED does not pass C-29 even if all DISCONFIRMED verdicts have adjacency documentation. |
```
