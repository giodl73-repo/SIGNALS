Written. Here is the complete v9 rubric:

---

```markdown
---
skill: simulate-argument
version: v9
date: 2026-03-19
pool: 24
golden_threshold: 96
---

# simulate-argument Rubric — v9

## v9 delta

**Three new aspirational criteria (C-30, C-31, C-32)** extracted from R9 excellence
signals — the first round where all five variations achieved a perfect 21/21 score.

| ID | Pattern | Enforcement |
|----|---------|------------|
| C-30 | scope-column-gen-registry-accountability | The Gen-registry in Phase 0 must include a Scope column for each Gen-ID entry, stating the population or domain to which the generalization applies. UNSUPPORTED-GEN Gap fields must address scope coverage — specifying what scope was claimed and why the evidence falls short of that scope — not merely flag the absence of supporting evidence for the generalization. A Gap field that writes "no evidence provided for Gen-NN" without addressing the scope dimension does not pass C-30. |
| C-31 | falsification-target-step3-close-loop | Phase 4 Step 3 must explicitly name the closest matching fault by F-ID and fault class, directly bridging the Phase 0 falsification target to the fault record. The closing must take the form: "The Phase 0 falsification target [was / was not] met — closest fault: F-NN [CLASS]." A Step 3 that states the H0 or inertia verdict without naming a specific fault by F-ID does not pass C-31. |
| C-32 | numbered-protocol-labeled-substeps-phase4 | Phase 4 closing must be structured as a numbered 5-step protocol with explicitly labeled sub-steps (e.g., "Step 1: Fault class distribution", "Step 2: H0 binary verdict", "Step 3: Falsification target close", "Step 4: CP audit", "Step 5: Generalization accountability"). An unstructured narrative closing or a partially labeled Phase 4 closing does not pass. V-05 canonical form is the reference implementation. |

**Boundary cases:**
- C-30 is not a duplicate of C-20: C-20 requires Gap fields to cite Gen-ID and state the shortfall. C-30 requires the Gen-registry to include a Scope column and Gap fields to address the scope dimension specifically. Satisfies C-20, fails C-30 if scope is not named.
- C-31 is not a duplicate of C-16: C-16 requires the binary H0 verdict from fault counts (Step 2). C-31 requires Step 3 to name the closest fault by F-ID and class, completing the Phase 0→fault-record loop. States H0 verdict without F-ID → fails C-31.
- C-32 is not a duplicate of C-07: C-07 governs Phase 5 repair plan ordering. C-32 governs Phase 4 closing structure. Different phases; C-07 pass does not imply C-32 pass.

**Score formula:** `aspirational_pass / 24 * 10` (pool grows from 21 to 24).
Golden threshold unchanged at 96.
```

---

**What changed:**

| # | New criterion | Source signal | Enforcement anchor |
|---|---------------|--------------|-------------------|
| C-30 | scope-column gen-registry accountability | V-03, V-04 | Gen-registry Scope column; UNSUPPORTED-GEN Gaps must name claimed scope and why evidence falls short |
| C-31 | falsification-target Step-3 close-loop | V-01, V-04 | Phase 4 Step 3 must name the closest fault by F-ID and class; H0 verdict alone does not close the loop |
| C-32 | numbered-protocol labeled-substeps Phase 4 | V-05 | Phase 4 closing must be a numbered 5-step protocol with labeled sub-steps; V-05 is the canonical reference |

Pool: 21 → 24. Formula: `aspirational_pass / 24 * 10`.
sification target in Phase 0 sharpens structural fault detection
- **C-12** *(R1)* inline reviewer hook inside every WEAK/BROKEN verdict
- **C-13** *(R1, tightened v3)* fault-pattern closure names a structural fault class, not a depth tier
- **C-14** *(R2)* enumerated Class column makes C-13 mechanical at insertion time
- **C-15** *(R2)* reviewer depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) with domain comparison per WEAK/BROKEN step
- **C-16** *(R3)* null-hypothesis binary verdict — H0 in Phase 0, mechanically derived reject/fail-to-reject at Phase 4 close
- **C-17** *(R3)* dedicated form-identification sub-pass before validity checks — pre-commitment, not post-hoc labeling
- **C-18** *(R4)* critical-path pre-commitment — Phase 0 names load-bearing steps; Phase 4 audits whether P1 faults landed on them
- **C-19** *(R4)* named specialist handoff — named role identities with closure language enforce temporal separation via identity
- **C-20** *(R4)* advocate-commitment gap accounts — Gap fields say "needed X, found only Y" relative to Phase 0 pre-committed generalizations
- **C-21** *(R5)* advocate phase 3 gen-anchoring — Phase 3 best readings cite Phase 0 Gen-IDs, creating Phase 0->Phase 3->Phase 4 chain
- **C-22** *(R5)* logician global binding — Logician's closure names all downstream specialists and prohibits reclassification globally
- **C-23** *(R5)* CP audit three-way verdict — CONFIRMED/DISCONFIRMED/CONFIRMED-ELSEWHERE per CP step; third category is required
- **C-24** *(R6)* advocate form-independent gen-anchoring — Gen-ID anchor trigger fires on content of best reading, not Logician's form label; two-field check required
- **C-25** *(R6)* logician cross-phase immutability — reclassification prohibition extends to phases; Phase 4 INVALID-FORM derives from Phase 3A committed form only
- **C-26** *(R6)* CP audit forced adjacency search — DISCONFIRMED requires documented Step 2 adjacency search; passive omission does not pass
- **C-27** *(R7)* advocate named form-type trigger enumeration — Advocate block explicitly names causal inference and analogy as trigger form types; closure attests enumerated-label scan; generic assertion without named types does not pass
- **C-28** *(R7)* logician cross-phase derivation double-lock — C-25 requires both Logician closure phase-language AND Phase-4 row-level `Derives from: FORM [C-ID]` derivation references; neither element alone suffices
- **C-29** *(R7)* unconditional CP adjacency with Gen-ID provenance — Step 2 runs for every CP step unconditionally; CONFIRMED-ELSEWHERE verdicts must name the Gen-ID anchor from Phase 3; conditional Step-2 procedure does not pass
- **C-30** *(R9)* scope-column gen-registry accountability — Gen-registry includes a Scope column per Gen-ID; UNSUPPORTED-GEN Gaps address scope coverage, not merely absence of evidence
- **C-31** *(R9)* falsification-target Step-3 close-loop — Phase 4 Step 3 names the closest fault by F-ID and class, completing the Phase 0 prediction->fault-record loop; H0 verdict alone does not pass
- **C-32** *(R9)* numbered-protocol labeled-substeps Phase 4 — Phase 4 closing is a numbered 5-step protocol with explicitly labeled sub-steps; unstructured or partially labeled closing does not pass

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
| C-07 | **Phase 5 repair instructions** | format | recommended | Phase 5 repair plan orders faults P1->P2->P3, references F-ID, C-ID, and Class for each, and provides exact repair instructions sufficient to re-run Phase 3. |
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
| C-21 | **Advocate Phase 3 gen-anchoring** | depth | Phase 3 best readings cite Phase 0 Gen-IDs via a two-field check: `Generalization assumed: YES/NO` followed by `Gen-ID anchor: Gen-NN`. This creates a traceable Phase 0->Phase 3->Phase 4 provenance chain. |
| C-22 | **Logician global binding** | depth | The Logician's closure names all downstream specialists by role and states: "No subsequent specialist may reclassify logical structure." Both all-downstream naming and the explicit prohibition must be present. |
| C-23 | **CP audit three-way verdict** | depth | Phase 4 closing step 4 uses all three verdict categories: CONFIRMED, DISCONFIRMED, and CONFIRMED-ELSEWHERE. The third category (CONFIRMED-ELSEWHERE) must appear at least once and be explained. |
| C-24 | **Advocate form-independent gen-anchoring** | depth | The gen-scan trigger fires on the semantic content of the best reading — whether the assumption extends beyond the studied population — not on the Logician's form label. A two-field check is required: `Generalization assumed: YES/NO` followed by `Gen-ID anchor`. Causal inference and analogy steps that assume universal mechanism applicability must trigger the anchor regardless of form label. A best reading that cites Gen-ID only when the Logician labeled the step "inductive generalization" does not pass. |
| C-25 | **Logician cross-phase immutability** | depth | The Logician's closure explicitly states that no subsequent *phase* may reclassify logical structure. Phase 4 verdicts of INVALID-FORM must derive from the Phase 3A committed form; re-examination of form assignment at Phase 4 is structurally prohibited. A closure that names specialists but does not extend the prohibition to phases does not pass. |
| C-26 | **CP audit forced adjacency search** | depth | Before DISCONFIRMED may be written in the Phase 4 CP audit, the analyst must complete and document a Step 2 adjacency search — identifying which non-CP step the fault landed on (or confirming none). DISCONFIRMED is an active documented conclusion, not a passive absence of evidence. A CP audit that writes DISCONFIRMED without documenting the adjacency search does not pass. |
| C-27 | **Advocate named form-type trigger enumeration** | depth | The Advocate block explicitly enumerates causal inference and argument-from-analogy as form types whose key assumptions may posit universal applicability and must therefore trigger the content-conditional gen scan. The Advocate closure attests that steps bearing the enumerated labels received the same generalization scan as steps labeled "inductive generalization." A generic assertion that "every inference step" receives the scan, without naming specific form types, does not pass even if C-24 is satisfied. |
| C-28 | **Logician cross-phase derivation double-lock** | depth | Satisfying C-25 requires two simultaneously present elements: (1) the Logician's closure explicitly states "no subsequent *phase* may reclassify logical structure," AND (2) each Phase-4 INVALID-FORM row carries an explicit `Derives from: FORM [C-ID]` derivation reference tracing back to the Phase-3A committed form label. A Phase-4 INVALID-FORM row with a derivation reference but no Logician closure phase-extension language does not pass. A Logician closure with phase-extension language but no Phase-4 row-level derivation references does not pass. Both elements must be present. |
| C-29 | **Unconditional CP adjacency with Gen-ID provenance** | depth | Step 2 of the CP audit adjacency search must run unconditionally — even when Step 1 concludes CONFIRMED, Step 2 must execute and document which non-CP step(s) were examined (or explicitly confirm none). When the adjacency search identifies an UNSUPPORTED-GEN fault on an adjacent step, the CONFIRMED-ELSEWHERE verdict must name the Gen-ID anchor from Phase 3 (e.g., "CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM"). A CP audit where Step 2 runs only when Step 1 is not CONFIRMED does not pass C-29 even if all DISCONFIRMED verdicts have adjacency documentation. |
| C-30 | **Scope-column gen-registry accountability** | depth | The Gen-registry in Phase 0 must include a Scope column for each Gen-ID entry, stating the population or domain to which the generalization applies. UNSUPPORTED-GEN Gap fields must address scope coverage — specifying what scope was claimed and why the evidence falls short of that scope — not merely flag the absence of supporting evidence. A Gap field that writes "no evidence provided for Gen-NN" without addressing the scope dimension does not pass C-30 even if C-20 is satisfied. |
| C-31 | **Falsification-target Step-3 close-loop** | depth | Phase 4 Step 3 must explicitly name the closest matching fault by F-ID and fault class, directly bridging the Phase 0 falsification target to the fault record. The closing must take the form: "The Phase 0 falsification target [was / was not] met — closest fault: F-NN [CLASS]." A Step 3 that states the H0 or inertia verdict without naming a specific fault by F-ID does not pass C-31 even if C-16 is satisfied. |
| C-32 | **Numbered-protocol labeled-substeps Phase 4** | format | Phase 4 closing must be structured as a numbered 5-step protocol with explicitly labeled sub-steps (e.g., "Step 1: Fault class distribution", "Step 2: H0 binary verdict", "Step 3: Falsification target close", "Step 4: CP audit", "Step 5: Generalization accountability"). An unstructured narrative closing or a partially labeled Phase 4 closing does not pass. V-05 canonical form is the reference implementation. |
