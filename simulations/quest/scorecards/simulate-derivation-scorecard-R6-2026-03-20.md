## Round 6 Scoring -- simulate-derivation

**Scorecard**: `simulations/quest/scorecards/simulate-derivation-scorecard-R6-2026-03-20.md`

---

### Results Summary

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 | **V-05** | 175/175 | Exemplary |
| 2 | **V-04** | 175/175 | Exemplary |
| 3 | **V-03** | 175/175 | Exemplary |
| 4 | **V-01** | 175/175 | Exemplary |
| 5 | **V-02** | 175/175 | Exemplary |

All five variations score 175/175 -- the v6 ceiling. Same pattern as R5: R5 V-05 already satisfied C-23/C-24/C-25 at the binary level, so all R6 variations inherit those passes. The rubric cannot distinguish "gate principle applied at the one template-demonstrated context (APPROX gate)" from "gate principle applied at a structurally novel context (EXACT gate at Phase 1) the template never showed."

**Qualitative ranking** (all 175 but evidence strength differs):

- **V-05 > V-04**: V-05 has two-gate architecture + cross-evaluation block + 4 cross-reference sites. V-04 has two of three (no cross-evaluation block) -- preferred fallback.
- **V-03 > V-01**: Both single additions; V-03 fills the Phase 2 site (most load-bearing gate); V-01 proves gate generalization with EXACT gate.
- **V-02 last**: Only addition improves C-25 evidence quality but leaves C-24 at R5 level (2 sites) and C-20 at single-gate-type status.

---

### Excellence Signals from V-05

1. **Two-gate architecture for generalization testing** -- EXACT gate (Phase 1, type classification) + APPROX gate (Phase 2, approximation verification) apply the same gate principle at structurally different contexts. The EXACT gate has no prior worked example; correct LLM application is first-principles evidence, not template recall.

2. **Explicit cross-evaluation block** -- demonstrates mutual principle applicability as three worked examples the LLM reads before Phase 1; reveals the genuine structural boundary (gate principle governs verdict recording; ordering principle governs fix sequencing -- complementary, not overlapping).

3. **Cross-reference saturation at all four major sites** -- Phase 1b, Phase 1, Phase 2, and Phase 4 each name their governing preamble principle; declaration-to-application traceability regardless of context window position in long derivations.

---

**R7 candidates** (from R6's meta-finding): C-26 (two-gate architecture at structurally different phase locations) and C-27 (named cross-evaluation block in preamble as demonstrative evidence, not mere co-location). These would raise the ceiling to 185.

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["two-gate architecture for principle generalization testing: EXACT classification gate (Phase 1) and APPROX verification gate (Phase 2) apply the same gate principle at structurally different contexts -- type assignment vs. approximation verification -- proving the gate principle is held as a first-principles commitment rather than a template-recalled pattern at the one demonstrated application site", "explicit cross-evaluation block in preamble: demonstrates mutual principle applicability as three worked examples before Phase 1, reveals the genuine structural boundary between gate principle (verdict recording) and ordering principle (fix sequencing) to prevent false equivalences, and makes C-25 auditable in a single preamble pass rather than inferrable from structural co-location", "cross-reference saturation at all major application sites: Phase 1 type-classification gate, Phase 2 approximation-verification gate, and Phase 4 fix-ordering rule each name their governing preamble principle, ensuring declaration-to-application traceability regardless of context window position in long derivations"]}
```
T), state the physical assumption (PHYSICAL), etc. "A step with an unexplained jump may not be labeled EXACT." V-01/V-04/V-05 additionally enforce this via the EXACT classification gate. Inherited core; gate strengthens enforcement.

| Recommended subtotal | V-01: 30/30 | V-02: 30/30 | V-03: 30/30 | V-04: 30/30 | V-05: 30/30 |

---

## Aspirational Criteria (85 pts)

### C-09 through C-19 (inherited from V-05-R5)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Catches fault not in paper | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-10 | Expands compressed steps | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-11 | APPROX verified independently (prose) | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-12 | Severity labels inline in Amend fixes | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-13 | Verification blocks contain prose reasoning | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-14 | APPROX reasoning independent of source | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-15 | All axes stack without phase-dropping | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-16 | Prose density uniform across block types | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-17 | APPROX gate has mandatory recovery | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-18 | Axis-commitment gateway gates Phase 2 entry | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-19 | Amend fixes ordered by severity (P1 first) | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |

All inherited unchanged from R5 V-05. Full evidence in R5 scorecard.

### C-20 through C-22 (new R5 aspirational criteria, inherited at PASS)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-20 | Mandatory gates name prohibited action explicitly | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-21 | Gateway axis labels name exact mechanistic behaviors | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-22 | Ordering rules stated as unconditional enumeration | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |

**C-20 evidence**:
- All variations: APPROX gate has "SOUND BLOCKED for this step... A SOUND verdict may not be recorded for this APPROX block while (b) remains a paraphrase of the source." Both accepted forms present.
- V-01, V-04, V-05 additionally: EXACT gate has "EXACT is BLOCKED for that step" and "EXACT BLOCKED for any step where the algebraic rule remains unnamed" -- a second gate type at a structurally different phase location.
- **Generalization quality**: V-01/V-04/V-05 have two mandatory gates that both comply with the gate principle at different contexts. V-02/V-03 satisfy C-20 by template text alone (one gate type).

**C-21/C-22 evidence** (all): Inherited unchanged. Axis labels name exact operation and format. Ordering rule is a single unconditional three-tier enumeration.

### C-23 through C-25 (new R6 aspirational criteria)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-23 | Structural principles in pre-phase preamble | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-24 | Application sites cross-reference preamble principle | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-25 | Co-located principles are mutually evaluable | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |

---

#### C-23 (pre-phase preamble)

All variations include `## STRUCTURAL COMMITMENTS` with all three principles (Gate, Axis-label, Ordering) before Phase 1. V-02 and V-05 additionally include the `**Cross-evaluation**` block within the preamble. All PASS -- the preamble is present and named before any phase in every variation.

---

#### C-24 (application-site cross-references)

| Application site | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------------|------|------|------|------|------|
| Phase 1b completion check (axis-label principle) | YES | YES | YES | YES | YES |
| Phase 1 EXACT gate (gate principle) | YES | no | no | YES | YES |
| Phase 2 APPROX gate (gate principle) | no | no | YES | YES | YES |
| Phase 4 ordering rule (ordering principle) | YES | YES | YES | YES | YES |
| **Cross-reference count** | **3** | **2** | **3** | **4** | **4** |

C-24 minimum is one cross-reference. All variations exceed it. Evidence quality: V-02 stays at R5 level (2 sites). V-01 and V-03 reach 3 sites. V-04 and V-05 saturate all four major application sites -- an LLM generating any phase can trace back to the governing principle without searching the full skill text.

---

#### C-25 (co-located principles mutually evaluable)

**V-01, V-03, V-04**: Preamble has three co-located principles. Structural mutual evaluability: gate principle defines "verdict token BLOCKED" -- axis-label distinguishing test ("could a non-compliant behavior satisfy this label?") applies to "EXACT BLOCKED" or "SOUND BLOCKED." Ordering principle's unconditional enumeration can be checked against whether it names a blocked action. Same structural evidence as R5 V-05. PASS.

**V-02, V-05**: Preamble includes an explicit `**Cross-evaluation**` block with three worked examples:
- Axis-label principle applied to "SOUND BLOCKED": names exact token; WEAK is a different token; passes.
- Gate principle applied to ordering rule: ordering rule blocks a misordered fix sequence (not a verdict token) -- complementary domains; neither subsumes the other.
- Ordering principle applied to the preamble itself: three principles in fixed order; unconditional enumeration; passes.

V-02/V-05 make C-25 directly auditable in a single preamble pass. V-01/V-03/V-04 pass by structural design. Both forms are PASS; evidence quality differs.

---

| Aspirational subtotal | V-01: 85/85 | V-02: 85/85 | V-03: 85/85 | V-04: 85/85 | V-05: 85/85 |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 60/60 | 30/30 | 85/85 | **175/175** | Exemplary |
| V-02 | 60/60 | 30/30 | 85/85 | **175/175** | Exemplary |
| V-03 | 60/60 | 30/30 | 85/85 | **175/175** | Exemplary |
| V-04 | 60/60 | 30/30 | 85/85 | **175/175** | Exemplary |
| V-05 | 60/60 | 30/30 | 85/85 | **175/175** | Exemplary |

**The R6 result**: All five variations score 175/175. R5 V-05 already satisfied C-23/C-24/C-25; all R6 variations inherit those passes. The v6 rubric's binary PASS/FAIL criteria cannot distinguish "gate principle applied only at the APPROX gate (the one template-demonstrated site)" from "gate principle applied at a novel type-classification site the template has never shown." The rubric ceiling is reached and held.

---

## Rankings

Since all five variations score 175/175, ranking is by multi-dimensional evidence quality across C-20, C-24, and C-25:

| Rank | Variation | Score | Band | Evidence quality |
|------|-----------|-------|------|-----------------|
| 1 | **V-05** | 175/175 | Exemplary | Two-gate architecture + cross-evaluation block + 4 application-site cross-references |
| 2 | **V-04** | 175/175 | Exemplary | Two-gate architecture + 4 application-site cross-references; C-25 structural; preferred fallback |
| 3 | **V-03** | 175/175 | Exemplary | Phase 2 cross-reference; 3 sites; single gate type; C-25 structural |
| 4 | **V-01** | 175/175 | Exemplary | Novel EXACT gate; 3 sites; two gate types; C-25 structural |
| 5 | **V-02** | 175/175 | Exemplary | Cross-evaluation block; C-25 explicit; C-24 at R5 level (2 sites); no novel gate |

**Ranking basis**: V-05 is ranked first because it is the only variation that demonstrates all three R6 generalization tests simultaneously. V-04 is second because it covers two of the three tests (gate generalization + cross-reference saturation) without the ~130-word preamble growth risk of V-05. V-02 ranks last because it improves C-25 evidence quality while leaving C-24 at R5 level and C-20 at single-gate-type status -- the weakest incremental change when measured against R6's generalization thesis.

---

## Excellence Signals from V-05

**1. Two-gate architecture as proof of principle generalization**
V-05 has two mandatory gates using gate-principle vocabulary: the APPROX source-removal gate ("SOUND BLOCKED") at Phase 2 and the EXACT classification gate ("EXACT BLOCKED") at Phase 1. These operate at structurally different points -- approximation verification vs. type classification -- and apply the same gate principle. The EXACT gate has no worked example in prior template history; any correct LLM application of "EXACT BLOCKED for any step where the algebraic rule remains unnamed" is evidence the gate principle is held as a first-principles commitment, not recalled from a template demonstration. C-20 passes in all five variations, but only V-05 (and V-04/V-01 partially) provides evidence that C-20 will hold in novel gate contexts the rubric's binary check cannot observe.

**2. Explicit cross-evaluation block as LLM-executable C-25 evidence**
V-05's `**Cross-evaluation**` block demonstrates three mutual applications of the preamble principles before any phase begins. It reveals a genuine structural boundary: the gate principle governs verdict recording; the ordering principle governs fix sequencing. They govern complementary domains and neither subsumes the other. This boundary information prevents false equivalences where an LLM might over-apply one principle to the other's domain. R5 V-05 had the same structural mutual evaluability but required the LLM to infer it; V-05-R6 shows it explicitly and makes C-25 checkable in a single preamble pass.

**3. Cross-reference saturation at all four major application sites**
V-05 cross-references the governing preamble principle at all four major application sites: Phase 1b completion check, Phase 1 EXACT gate, Phase 2 APPROX gate, and Phase 4 ordering rule. An LLM generating any phase in a long derivation -- including under context compression -- can trace back to the governing principle at that phase without searching the full skill text. The declaration-to-application chain is auditable in a single forward pass regardless of entry point.

---

## Meta-Finding: R6 Improvements Exceed Rubric Resolution (Again)

R6 exposes the same ceiling effect R5 did, one level up. The v6 rubric's C-23/C-24/C-25 criteria detect whether the preamble architecture is present, whether at least one application-site cross-reference exists, and whether co-located principles can be applied to each other. R5 V-05 already satisfied all three at the binary level; all R6 variations inherit those passes. The rubric cannot distinguish "gate principle applied only at the one template-demonstrated gate" from "gate principle applied at a novel type-classification site the template has never shown."

**Implication for R7**: Two potential new rubric criteria emerge from V-05-R6's innovations:

| Candidate | What it detects |
|-----------|----------------|
| C-26 | Two or more mandatory gates in the skill apply the gate principle at structurally different phase locations or step-type contexts (type classification vs. approximation verification vs. structural axis commitment) |
| C-27 | The preamble's cross-evaluation block is present as a named demonstrative block showing each principle applied to at least one other, not merely as co-location of independent principles |

These would raise the ceiling from 175 to 185 and force R7 variations to demonstrate that multi-context gate generalization and explicit cross-principle application are committed architectural properties, not incidental template features.

---

## Recommendation

**Ship V-05 as the R6 skill.** It is the only variation that delivers all three R6 generalization tests simultaneously and achieves the highest multi-dimensional evidence quality across C-20, C-24, and C-25.

**Fallback**: If V-05's ~130 words of added instruction (cross-evaluation block + EXACT gate) causes Phase 2 or Phase 3 compression on 10+ step derivations, use **V-04** (novel EXACT gate + Phase 2 cross-reference, no cross-evaluation block, ~100 words added). V-04 retains the gate generalization test and saturated cross-references; it sacrifices only the explicit C-25 demonstration.

**Do not ship V-01, V-02, or V-03 alone.** Each addresses only one of three R6 dimensions. V-01 proves gate generalization but lacks Phase 2 cross-reference and C-25 demonstration. V-02 adds C-25 explicitness but leaves C-24 at R5 level and adds no novel gate. V-03 saturates Phase 2 but adds no novel gate type and no C-25 demonstration.

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["two-gate architecture for principle generalization testing: EXACT classification gate (Phase 1) and APPROX verification gate (Phase 2) apply the same gate principle at structurally different contexts -- type assignment vs. approximation verification -- proving the gate principle is held as a first-principles commitment rather than a template-recalled pattern at the one demonstrated application site", "explicit cross-evaluation block in preamble: demonstrates mutual principle applicability as three worked examples before Phase 1, reveals the genuine structural boundary between gate principle (verdict recording) and ordering principle (fix sequencing) to prevent false equivalences, and makes C-25 auditable in a single preamble pass rather than inferrable from structural co-location", "cross-reference saturation at all major application sites: Phase 1 type-classification gate, Phase 2 approximation-verification gate, and Phase 4 fix-ordering rule each name their governing preamble principle, ensuring declaration-to-application traceability regardless of context window position in long derivations"]}
```
