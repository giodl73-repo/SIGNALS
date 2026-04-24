## simulate-argument — Round 9 Scorecard

**All five variations score 21/21 (10.0/10.0, golden).** First round where every variation achieves a perfect score.

---

### Scores

| Variation | Pass | Score | Golden? |
|-----------|------|-------|---------|
| V-01 (inertia-first) | 21/21 | 10.0 | YES |
| V-02 (Reviewer-first) | 21/21 | 10.0 | YES |
| V-03 (expanded Phase 0) | 21/21 | 10.0 | YES |
| V-04 (V-01 + V-03) | 21/21 | 10.0 | YES |
| V-05 (distillation) | 21/21 | 10.0 | YES |

---

### Key Finding: V-02 Boundary Confirmed

The predicted C-19/C-21 failures for V-02 did not materialize. **Evidence-first ordering (Reviewer before Advocate) passes all 21 criteria.**

- **C-19** is enforced by closure language and identity commitment, not by physical role sequencing. The Logician's closure names all downstream specialists and seals the prohibition — the order specialists run in does not break this contract.
- **C-21** is enforced by the two-field check (`Generalization assumed` + `Gen-ID anchor`) pointing back to Phase 0, which exists regardless of whether the Advocate saw the Critic's work first.

**Design implication**: evidence-first skill architectures are structurally valid. C-19 and C-21 are sequencing-agnostic.

---

### Excellence Signals (candidates for v9 rubric)

1. **`scope-column-gen-registry-accountability`** (V-03, V-04) — Scope column on Gen-registry; UNSUPPORTED-GEN Gaps must address scope coverage, not just existence of generalization. Candidate C-30.
2. **`falsification-target-step3-close-loop`** (V-01, V-04) — Phase 4 Step 3 names the closest matching fault by F-ID and class, bridging the Phase 0 prediction to the fault record. Candidate C-30 or C-16 tightening.
3. **`numbered-protocol-labeled-substeps-phase4`** (V-05) — Phase 4 closing as a numbered 5-step protocol with labeled sub-steps. Usability enhancement; V-05 is the preferred canonical form for the skill update.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["scope-column-gen-registry-accountability", "falsification-target-step3-close-loop", "evidence-first-ordering-boundary-confirmed"]}
```
." Phase 4 step 3 closes the loop: "The Phase 0 falsification target [was / was not] met." |
| V-02 | **PASS** | Phase 0 H0 serves as structural pre-commitment; Phase 4 step 2 derives binary verdict from fault counts. |
| V-03 | **PASS** | Phase 0 has dedicated "Falsification target" sentence: "H0 is falsified if [inference step type] fails -- specifically, if [fault class] is found at P1 severity." |
| V-04 | **PASS** | Phase 0 falsification target (Pass 1, refined Pass 2): "H0 is falsified if [inference type] fails -- specifically, if [fault class] is found at P1 severity on [C-ID once known]." Phase 4 step 3 names the closest fault by F-ID and class. |
| V-05 | **PASS** | Phase 0 H0 as structural pre-commitment; Phase 4 Step 3 inertia verdict derived from Step 2 fault count. |

### C-12 -- Inline reviewer hook inside every WEAK/BROKEN verdict

All variations: **PASS** -- "As committee chair, would I flag this in a written review? YES/NO" present in every 3C WEAK or BROKEN VERDICT block.

### C-13 -- Fault-pattern closure names structural fault class, not depth tier

All variations: **PASS** -- Phase 4 closing Step 1 names dominant fault class by enumerated code (UNSUPPORTED-GEN / DEF-DRIFT / CIRCULAR-DEP / INVALID-FORM).

### C-14 -- Enumerated Class column in Fault Register

All variations: **PASS** -- Class column present with exactly one enumerated code per row.

### C-15 -- Reviewer depth tier with domain comparison per WEAK/BROKEN step

All variations: **PASS** -- every WEAK/BROKEN 3C verdict carries Depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) and domain comparison sentence.

### C-16 -- Null-hypothesis binary verdict

All variations: **PASS** -- Phase 0 states H0; Phase 4 Step 2 derives binary verdict (REJECT H0 / FAIL TO REJECT H0) from P1 fault count; Phase 4 Step 3 states H0 verdict alongside inertia verdict.

### C-17 -- Dedicated form-identification sub-pass (3A) before validity checks

All variations: **PASS** -- Phase 3A (THE LOGICIAN) runs as isolated form-identification pass; no validity evaluation or advocacy intermixed.

### C-18 -- Critical-path pre-commitment; Phase 4 audits CP fault landing

All variations: **PASS** -- Phase 0 names load-bearing steps (TBD revised after Phase 2); CP? flags in Claim Map; Phase 4 CP priority audit per CP step with three-way verdict and risk distribution sentence.

### C-19 -- Named specialist handoff with closure language enforcing temporal separation

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Logician closure names Advocate, Empirical Reviewer, and Committee Chair. All specialists close with first-person identity commitments. Canonical ordering. |
| **V-02** | **PASS** | Logician closure: "The Advocate, the Empirical Reviewer, and the Committee Chair are bound to these forms. No subsequent specialist and no subsequent phase may reclassify..." All specialists make first-person identity commitments under role names. Reversed ordering (Critic before Advocate) does not break C-19. **Boundary confirmed: C-19 is enforced by closure language and identity commitment, not by physical role sequencing.** |
| V-03 | **PASS** | Logician closure names all three downstream specialists. All first-person commitments present. |
| V-04 | **PASS** | Same canonical closure language. |
| V-05 | **PASS** | Logician closure: "The Advocate, Reviewer, and Chair are bound to these forms. No subsequent specialist and no subsequent phase may reclassify logical structure committed here." All specialists close under role identity. |

### C-20 -- Advocate commitment gap accounting

All variations: **PASS** -- UNSUPPORTED-GEN Gap fields cite Phase 0 Gen-ID and state the evidential shortfall with the "Advocate required Gen-NN... Reviewer found only..." format.

### C-21 -- Advocate Phase 3 gen-anchoring (Phase 0 -> Phase 3 -> Phase 4 chain)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Two-field check: `Generalization assumed: YES/NO` + `Gen-ID anchor: Gen-NN from Phase 0`. |
| **V-02** | **PASS** | Two-field check present in Advocate block despite Advocate running after Critic. Phase 0 Gen-IDs pre-committed before all specialists; Advocate cites them through `Gen-ID anchor` field. Phase 0->Phase 3->Phase 4 chain intact. **Boundary confirmed: evidence-first ordering does not break gen-anchoring provenance.** |
| V-03 | **PASS** | Two-field check present; Gen-registry includes Scope column, enriching the chain. |
| V-04 | **PASS** | Two-field check present; Gen-registry with Scope column. |
| V-05 | **PASS** | Two-field check present. |

### C-22 -- Logician global binding

All variations: **PASS** -- Logician closure names all three downstream specialists by role and explicitly prohibits reclassification ("No subsequent specialist may reclassify logical structure").

### C-23 -- CP audit three-way verdict (CONFIRMED / DISCONFIRMED / CONFIRMED-ELSEWHERE)

All variations: **PASS** -- CONFIRMED-ELSEWHERE is instantiated with format `CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM`.

### C-24 -- Advocate form-independent gen-anchoring (trigger on content, not form label)

All variations: **PASS** -- Advocate instruction states the scan is form-independent; applies to all inference steps regardless of Logician label; two-field check present.

### C-25 -- Logician cross-phase immutability (reclassification prohibition extends to phases)

All variations: **PASS** -- every Logician closure includes "No subsequent specialist and no subsequent phase may reclassify logical structure committed here." R8 V-04 failure (specialist-only closure lacking phase-extension language) not repeated in any R9 variation.

### C-26 -- CP audit forced adjacency search (DISCONFIRMED requires documented Step 2)

All variations: **PASS** -- DISCONFIRMED verdict requires listing the full dependency chain per the Phase 4 closing protocol; undocumented DISCONFIRMED does not pass.

---

### New Criteria -- C-27, C-28, C-29

#### C-27 -- Advocate named form-type trigger enumeration

**Rule**: Advocate block must explicitly name causal inference AND argument-from-analogy as trigger form types; closure must attest both labels received the same scan as "inductive generalization." Generic assertion without named types in the attestation sentence fails even if C-24 is satisfied.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Advocate closure: "A step labeled 'causal inference' whose best reading assumes the studied mechanism operates universally, and a step labeled 'argument from analogy' whose best reading extends the analogy's scope beyond the studied population, each received the same generalization scan as a step labeled 'inductive generalization.'" Both labels in the equivalence-attestation sentence. |
| V-02 | **PASS** | Same attestation sentence -- both form types named explicitly in the "same scan as inductive generalization" construction. |
| V-03 | **PASS** | Same attestation sentence in Advocate closure. |
| V-04 | **PASS** | Same attestation sentence. |
| V-05 | **PASS** | "A step labeled 'causal inference'... and a step labeled 'argument from analogy'... each received the same generalization scan as a step labeled 'inductive generalization.'" Both labels present in equivalence-attestation sentence. |

R8 V-01 failure (generic form-independent language without named labels) not repeated in any R9 variation. The attestation pattern is canonically locked.

#### C-28 -- Logician cross-phase derivation double-lock

**Rule**: Both elements required simultaneously -- (1) Logician closure with phase-extension language AND (2) Phase-4 INVALID-FORM rows carry `Derives from: FORM [specific-C-ID]`. Neither element alone suffices.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Element 1: Logician closure "no subsequent specialist and no subsequent phase may reclassify." Element 2: Fault Register derivation line requires specific `FORM [C-ID]`. Both present. |
| V-02 | **PASS** | Element 1: same full Logician closure. Element 2: "Derives from: FORM [C-ID] committed in Phase 3A as [Logician's committed form]" -- specific block C-ID. Both present. |
| V-03 | **PASS** | Element 1: full Logician phase-language. Element 2: derivation format with specific FORM [C-ID] confirmed. Both present. |
| V-04 | **PASS** | Element 1: full Logician phase-language (V-04 does not repeat R8's specialist-only mistake). Element 2: Fault Register derivation with specific FORM [C-ID]. Both confirmed. |
| V-05 | **PASS** | Element 1: "No subsequent specialist and no subsequent phase may reclassify logical structure committed here." Element 2: "Every INVALID-FORM row requires an immediate derivation line below it" + `Derives from: FORM [C-ID] committed in Phase 3A as [form]`. Both elements confirmed. |

R8 failures (V-02 generic attribution, V-04 specialist-only closure) not repeated. Double-lock is canonically enforced across all five.

#### C-29 -- Unconditional CP adjacency with Gen-ID provenance

**Rule**: Step 2 runs unconditionally for every CP step regardless of Step 1. CONFIRMED-ELSEWHERE verdict must embed the Gen-ID anchor inline in the verdict string.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | "Step 2 runs unconditionally for every CP step regardless of Step 1 result." CONFIRMED-ELSEWHERE: "CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM." Gen-ID inline. |
| V-02 | **PASS** | Same unconditional Step 2 language. Same CONFIRMED-ELSEWHERE verdict string with Gen-ID parenthetical. |
| V-03 | **PASS** | Step 2 labeled "(unconditional -- runs for every CP step)." CONFIRMED-ELSEWHERE format with Gen-ID inline in verdict string. R8 V-03 failure (Gen-ID in body text only, absent from verdict string) is not repeated -- V-03 here carries Gen-ID directly in the verdict string. |
| V-04 | **PASS** | Same unconditional Step 2. Verdict string: `CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM`. |
| V-05 | **PASS** | "Sub-step B runs unconditionally for every CP step regardless of sub-step A result." Rule (1): "CONFIRMED-ELSEWHERE must embed the Gen-ID anchor in the verdict string -- fault ID alone does not pass." Verdict format confirmed. |

R8 V-03 failure (body-text Gen-ID, absent from verdict string) not repeated. Gen-ID provenance is inline in all five verdict strings.

---

## Aspirational Pool Summary (C-09--C-29)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| C-24 | PASS | PASS | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | PASS | PASS |
| C-26 | PASS | PASS | PASS | PASS | PASS |
| C-27 | PASS | PASS | PASS | PASS | PASS |
| C-28 | PASS | PASS | PASS | PASS | PASS |
| C-29 | PASS | PASS | PASS | PASS | PASS |
| **Pass count** | **21/21** | **21/21** | **21/21** | **21/21** | **21/21** |

---

## Composite Scores

| Variation | Aspirational Pass | Formula | Score | Golden (>=9.6)? |
|-----------|-------------------|---------|-------|-----------------|
| V-01 (inertia-first) | 21/21 | 21/21 x 10 | **10.0** | **YES (100%)** |
| V-02 (Reviewer-first) | 21/21 | 21/21 x 10 | **10.0** | **YES (100%)** |
| V-03 (expanded Phase 0) | 21/21 | 21/21 x 10 | **10.0** | **YES (100%)** |
| V-04 (V-01 + V-03) | 21/21 | 21/21 x 10 | **10.0** | **YES (100%)** |
| V-05 (distillation) | 21/21 | 21/21 x 10 | **10.0** | **YES (100%)** |

**Ranking**: All five tied at 10.0/10.0. First round where every variation scores golden.

---

## Boundary Finding: V-02

The variation design document predicted V-02 at 19/21 (C-19 FAIL, C-21 FAIL). Actual: 21/21.

**Root cause of prediction error**: The prediction conflated physical role sequencing with the mechanism through which C-19 and C-21 are enforced.

- **C-19 mechanism**: Temporal separation is a property of the closure commitment contract -- each specialist seals their work with a first-person identity statement before the next reads it. In V-02, the Critic seals their evidence requirements before the Advocate reads them; the Advocate seals their best readings before the Chair reads them. The Logician names all downstream specialists and prohibits reclassification. All closure elements are present regardless of whether the Advocate ran before or after the Critic.

- **C-21 mechanism**: The Phase 0->Phase 3->Phase 4 Gen-ID provenance chain is a property of the two-field check fields (`Generalization assumed` + `Gen-ID anchor`) pointing back to Phase 0. Phase 0 Gen-IDs are pre-committed before all specialists run. Whether the Advocate sees the Critic's evidence requirements before writing their best readings does not affect whether the `Gen-ID anchor` field exists and traces back to Phase 0.

**Design implication**: Evidence-first ordering (Reviewer before Advocate) is a valid alternative skill architecture. C-19 and C-21 are not sequencing-dependent. Future skill designs can adopt this model where sharper evidence framing before the Advocate's commitment is preferable.

---

## Excellence Signals

All five variations scored 21/21. The differentiating patterns are structural improvements not currently captured by any criterion:

### Signal 1: `scope-column-gen-registry-accountability` (V-03, V-04)

V-03 and V-04 add a Scope column to the Gen-registry: the cell names what population, context, or mechanism the generalization must hold beyond the direct evidence. The Reviewer's UNSUPPORTED verdict and the Phase 4 UNSUPPORTED-GEN Gap field must address whether evidence covers the registered scope.

Current C-20 and C-21 require Gen-IDs and gap accounting but do not require the scope to be pre-registered or the Gap to address scope coverage. The Scope column makes UNSUPPORTED-GEN faults more precise: the evidential shortfall is not just "a generalization exists" but "evidence falls short of the registered scope." Candidate for C-30.

### Signal 2: `falsification-target-step3-close-loop` (V-01, V-04)

V-01 and V-04 close the inertia loop at Phase 4 Step 3 with an explicit reference to the Phase 0 falsification target outcome: "The Phase 0 falsification target [was met at / was not met; closest fault at] [F-ID, C-ID, class]." This creates a machine-readable close -- the analysis ends with an explicit verdict on whether the Phase 0 prediction was confirmed by the fault trace.

Current C-11 requires Phase 4 to return to Phase 0 pre-commitments; C-16 requires the binary H0 verdict. Neither requires Step 3 to name the closest matching fault by F-ID and class, creating a direct bridge from the Phase 0 prediction to the fault record. Candidate for C-30 or tightening of C-16.

### Signal 3: `numbered-protocol-labeled-substeps-phase4` (V-05)

V-05 renames the Phase 4 closing from running prose to a numbered five-step protocol with labeled sub-steps (Sub-step A / B / C). The unconditional Sub-step B flag is an explicit header. The CONFIRMED-ELSEWHERE Gen-ID rule is promoted to a numbered rule at the end of Step 4.

This is a usability improvement rather than a new criterion -- the rules enforced are identical to C-29. But the format change makes each criterion mechanically checkable without parsing running prose, which reduces execution variance. V-05 is the preferred canonical form for the skill update.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["scope-column-gen-registry-accountability", "falsification-target-step3-close-loop", "evidence-first-ordering-boundary-confirmed"]}
```
