## Round 4 Scoring Complete

**Scorecard written**: `simulations/quest/scorecards/simulate-derivation-scorecard-R4-2026-03-20.md`

---

### Results Summary

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 | **V-05** | 145/145 | Exemplary |
| 2 | **V-04** | 135/145 | Exemplary |
| 3 | **V-01** | 130/145 | Exemplary |
| 4 | **V-02** | 132/145 | Proficient |
| 4 | **V-03** | 132/145 | Proficient |

**V-05 hits 145/145** — all four gaps closed: C-08 (+3), C-17 (+5), C-18 (+5), C-19 (+5).

**The surprising result**: V-02 and V-03 each score 132 pts (higher than V-01's 130) but land **Proficient** while V-01 lands **Exemplary**. C-08 PARTIAL (7/10) blocks the "all recommended pass" Exemplary gate — so band value and raw points diverge here. V-01's C-08 fix is worth more band-value per point than either C-17 or C-19 alone.

**Three new patterns from V-05:**

1. **Consequence-naming as the hard gate** — "SOUND BLOCKED" names the prohibited action, not just the required correction. An LLM can make a cosmetically different but still-paraphrase replacement and proceed; naming the prohibition prevents that.

2. **Commitment label alignment** — the gateway axis must name the exact behavior ("NEW-tagged fault detection"), not the general category ("source acknowledgment"). The LLM re-reads the label when filling the register.

3. **Unconditional three-tier ordering beats conditional two-tier** — "P1 first, then P2, then P3" in one sentence closes the P2-before-P3 gap that the conditional form ("if P1 exists... if P2 exists...") left invisible.

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["consequence-naming as hard gate: label the prohibited action ('SOUND BLOCKED') not just the required correction, so the LLM cannot pass around it with a cosmetic replacement", "commitment label alignment: the gateway axis label must name the exact behavior being committed to ('NEW-tagged fault detection'), not the general category ('source acknowledgment') -- the LLM re-reads the label when filling the register", "unconditional three-tier ordering beats conditional two-tier: 'P1 first, then P2, then P3' in one sentence closes P2-before-P3 implicitly; the conditional form ('if P1 exists... if P2 exists...') leaves the P2/P3 ordering gap invisible"]}
```
 | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Soundness verdict explicit | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-07 | Amend maps to faults, ordered | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-08 | Step types correctly classified | **PASS 10** | PARTIAL 7 | PARTIAL 7 | **PASS 10** | **PASS 10** |

**C-06 evidence**: All variations include the global verdict table (SOUND/CONDITIONALLY SOUND/BROKEN) with a narrative sentence requirement in Phase 4 — not buried in a step block.

**C-07 evidence**: The conditional priority rule ("if P1 faults exist, first fix must address P1; highest-severity issue leads") is an ordering rule. The behavior produces P1-first. Full pass in base carries through all variations. V-03/V-04/V-05 add the explicit statement which also satisfies C-07 more strongly (10/10 either way).

**C-08 PARTIAL (7/10) in V-02, V-03**: Type definitions read "exact algebraic identity" and "physical assumption encoded algebraically" — correct labels, but no instruction to name which identity or assumption in the Justification cell. The LLM can write "algebra holds" or "physical law applies" without citing the product rule or the equilibrium condition. Spot-check fails on vague justifications.

**C-08 PASS (10/10) in V-01, V-04, V-05**: Type definitions expanded with explicit naming requirements:
- EXACT: "the Justification cell must name the algebraic rule, identity, or substitution that makes this step exact (e.g., 'product rule,' 'distributivity,' 'substitution of Eq. 3'). A step with an unexplained jump may not be labeled EXACT."
- PHYSICAL: "the Justification cell must state the physical assumption being encoded (e.g., 'at equilibrium, dR/dt = 0,' 'incompressible flow,' 'quasi-static process')"
— spot-checkable justifications required by construction.

| Recommended subtotal | V-01: 30/30 | V-02: 27/30 | V-03: 27/30 | V-04: 30/30 | V-05: 30/30 |

---

### Aspirational Criteria (55 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Catches fault not in paper | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-10 | Expands compressed steps | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-11 | APPROX verified independently | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-12 | Severity labels inline in Amend | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-13 | Verification blocks prose reasoning | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-14 | APPROX reasoning source-independent | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-15 | All axes stack without phase-dropping | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-16 | Prose density uniform across block types | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-17 | APPROX gate: mandatory recovery instruction | **FAIL 0** | **PASS 5** | **FAIL 0** | **FAIL 0** | **PASS 5** |
| C-18 | Axis-commitment gateway gates Phase 2 | **FAIL 0** | **FAIL 0** | **FAIL 0** | **FAIL 0** | **PASS 5** |
| C-19 | Amend fixes ordered by severity P1-first | **FAIL 0** | **FAIL 0** | **PASS 5** | **PASS 5** | **PASS 5** |

**C-09 evidence** (all): Phase 2 source acknowledgment block ("If NO: this fault is a NEW finding") + Phase 3 NEW tagging instruction — the pipeline from verdict to register is complete.

**C-10 evidence** (all): Phase 1b expansion pass with S-NNa/S-NNb sub-step pattern and "(interpolated)" label is required; auto-pass note if none found.

**C-11 evidence** (all): APPROX check requires tracer to state (a) "in the tracer's own words — do not merely quote the paper" and (b) "name the domain regime, physical principle, or first-principles argument... Do not paraphrase the source sentence."

**C-12 evidence** (all): Amend template uses "[F-ID] [P1/P2/P3]: [specific fix]" format — severity label is inline at the point of recommended action.

**C-13 evidence** (all): Reasoning rule in Phase 2 — "Every verdict token must be followed by a dash and at least one sentence of reasoning. 'YES — [sentence]' or 'NO — [sentence]'. A block containing only YES or NO tokens for any check fails the minimum standard."

**C-14 evidence** (all): Source-removal test is present ("if the source sentence... were removed entirely, could you support your validity condition from domain knowledge alone?"). Domain-principle grounding required ("e.g., 'small-angle regime,' 'quasi-static assumption,' 'low Reynolds number'").

**C-15 evidence** (all): Gateway table commits to all three axes before Phase 2. Every interpolated sub-step must have a Phase 2 block (no holes), every NEW-tagged fault must have a complete register entry, prose rule applies throughout — no silent degradation path.

**C-16 evidence** (all): Density uniformity rule stated in Phase 2 — "Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks... Mixed density within a single step block fails this rule."

**C-17 evidence**:
- V-01/V-03/V-04 (FAIL): "If NO: replace (b) with a domain-principle-grounded statement before recording your verdict." This is imperative but does NOT name the consequence — no explicit prohibition on recording SOUND while (b) remains paraphrase. An LLM can replace (b) with a still-paraphrase-adjacent statement and continue.
- V-02/V-05 (PASS): "If NO: SOUND BLOCKED for this step. You must replace (b)... A SOUND verdict may not be recorded for this APPROX block while (b) remains a paraphrase of the source. Correct (b) now, then continue to the step verdict line." Consequence explicitly named; prohibition unambiguous.

**C-18 evidence**:
- V-01/V-02/V-03/V-04 (FAIL): Gateway axis C labeled "Source acknowledgment gate" with requirement text "Source acknowledgment gate will execute for every WEAK or BROKEN step verdict." Gate says "All three must show ACTIVE." Rubric requires axis C to be "NEW-tagged fault detection" — label mismatch fails C-18.
- V-05 (PASS): Gateway axis C relabeled "NEW-tagged fault detection" with requirement text "Every WEAK or BROKEN verdict where the source paper does not acknowledge the issue will receive a 'NEW: not acknowledged by paper' tag in the fault register." Gate says "All present axes must show ACTIVE." Exact match with rubric C-18 pass condition.

**C-19 evidence**:
- V-01/V-02 (FAIL): "Priority rule: if P1 faults exist in the register, your first fix must address a P1 fault. If no P1 faults exist but P2 faults exist, at least one fix must address a P2 fault. Highest-severity issue leads the Amend section." This ensures P1-first but does not state P2-before-P3 as an ordering rule. An Amend with P2 and P3 where a P3 fix precedes a P2 fix satisfies the old rule (since "at least one fix must address P2" doesn't require ordering between P2 and P3).
- V-03/V-04/V-05 (PASS): "Severity ordering rule: order all three fixes by severity — P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list." Explicit three-tier statement — satisfies C-19 pass condition verbatim.

| Aspirational subtotal | V-01: 40/55 | V-02: 40/55 | V-03: 40/55 | V-04: 45/55 | V-05: 55/55 |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 60/60 | 30/30 | 40/55 | **130/145** | Exemplary |
| V-02 | 60/60 | 27/30 | 40/55 | **127/145** | Proficient |
| V-03 | 60/60 | 27/30 | 40/55 | **127/145** | Proficient |
| V-04 | 60/60 | 30/30 | 45/55 | **135/145** | Exemplary |
| V-05 | 60/60 | 30/30 | 55/55 | **145/145** | Exemplary |

**Note on V-02 and V-03**: Both score 127/145 — same points as the base. V-02 recovers C-17 (+5) but loses no base points; V-03 recovers C-19 (+5) but loses no base points. The net gain is correct (+5 each), but C-08 PARTIAL (7/10 instead of 10/10) accounts for the gap from Exemplary: with C-08 PARTIAL, the "all recommended pass" condition for Exemplary is not met, landing both in Proficient band despite the score being 127/145.

**Wait — correction**: V-02 and V-03 score 127+5=132, not 127. Recomputing:
- V-02: 60 + 27 + 45 = 132? No. C-17 PASS = +5 vs base's C-17 FAIL = 0. So V-02 aspirational = 40 (base) + 5 (C-17) = 45. Total = 60+27+45 = 132. Correcting the table:

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 60/60 | 30/30 | 40/55 | **130/145** | Exemplary |
| V-02 | 60/60 | 27/30 | 45/55 | **132/145** | Proficient |
| V-03 | 60/60 | 27/30 | 45/55 | **132/145** | Proficient |
| V-04 | 60/60 | 30/30 | 45/55 | **135/145** | Exemplary |
| V-05 | 60/60 | 30/30 | 55/55 | **145/145** | Exemplary |

V-02 and V-03 each recover +5 from the base (132 vs 127 base), but C-08 PARTIAL (7/10 vs 10/10) means recommended is 27/30, which blocks the Exemplary band. Score range 132 ≥ 118 satisfies the numeric threshold, but rubric note confirms 127/145 = Proficient, implying the Exemplary qualifier "all recommended pass" is a hard gate. C-08 PARTIAL = recommended not all passing = Proficient.

---

## Rankings

| Rank | Variation | Score | Band | Key advantage |
|------|-----------|-------|------|---------------|
| 1 | **V-05** | 145/145 | Exemplary | All four gaps closed; ceiling hit |
| 2 | **V-04** | 135/145 | Exemplary | C-08 + C-19; safe fallback without APPROX gate risk |
| 3 | **V-01** | 130/145 | Exemplary | C-08 fix alone; all recommended pass |
| 4 | **V-02** | 132/145 | Proficient | Higher points than V-01 but C-08 partial blocks Exemplary |
| 4 | **V-03** | 132/145 | Proficient | Same as V-02; C-19 gains offset by C-08 partial |

**Decisive insight**: V-02 and V-03 score 2 pts higher than V-01 (132 vs 130) but land in a lower band (Proficient vs Exemplary) because C-08 PARTIAL blocks the "all recommended pass" Exemplary gate. V-01 is the better single-change bet if only one change can be made: C-08 delivers more band value per point than C-17 or C-19 alone.

---

## Excellence Signals from V-05

**1. Consequence-naming as the stop signal**
"SOUND BLOCKED for this step... A SOUND verdict may not be recorded for this APPROX block while (b) remains a paraphrase." Naming the consequence ("SOUND may not be recorded") creates a hard gate that the LLM cannot pass around by making a cosmetically different but still-paraphrase replacement. The label "SOUND BLOCKED" mirrors verdict vocabulary, making the block structurally visible.

**2. Axis label alignment at the commitment point**
Axis C relabeled from "Source acknowledgment gate" to "NEW-tagged fault detection" — the commitment table now names the exact behavior (tagging unacknowledged faults), not a general category (source acknowledgment). When the LLM fills the gateway table, it is committing to a specific named behavior rather than a vague intention. This closes C-18 because the rubric's pass condition requires the label to be "NEW-tagged fault detection."

**3. "All present axes" vs "all three" in the gate statement**
The gate wording "Do NOT proceed to Phase 2 until all present axes show ACTIVE" is future-proof — it works even if axes are added or removed without rewriting the gate. It also prevents a failure mode where the LLM marks an axis ABSENT and proceeds anyway under the old "all three" phrasing (which doesn't specify what to do when axes are absent).

**4. Unconditional three-tier severity ordering**
"P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix." The old conditional form ("if P1 exists...") created a gap: it required P1-first but didn't state P2-before-P3 as an ordering rule. The unconditional form closes all three tiers simultaneously.

**5. Justification requirement placed at the point of use**
Adding the naming requirement inside the type definitions — exactly where the LLM reads the constraint while filling the derivation map table — is more effective than a separate Phase 2 instruction. The LLM sees "must name the algebraic rule, identity, or substitution" at the moment it assigns the type label, which is the moment it writes the Justification cell.

---

## Recommendation

**Ship V-05 as the R4 skill.** It closes all four gaps and hits the ceiling.

**Fallback**: If V-02's SOUND BLOCKED gate produces over-cautious APPROX blocks that expand Phase 2 length and cause step truncation (the documented runtime risk), use **V-04** (135/145, Exemplary) which recovers C-08 and C-19 without touching the APPROX template.

**Do not ship V-02 or V-03 alone.** Both score 132/145 in points but land Proficient because C-08 PARTIAL blocks Exemplary. V-01 (130/145, Exemplary) is the better single-change option if band matters more than raw points.

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["consequence-naming as hard gate: label the prohibited action ('SOUND BLOCKED') not just the required correction, so the LLM cannot pass around it with a cosmetic replacement", "commitment label alignment: the gateway axis label must name the exact behavior being committed to ('NEW-tagged fault detection'), not the general category ('source acknowledgment') -- the LLM re-reads the label when filling the register", "unconditional three-tier ordering beats conditional two-tier: 'P1 first, then P2, then P3' in one sentence closes P2-before-P3 implicitly; the conditional form ('if P1 exists... if P2 exists...') leaves the P2/P3 ordering gap invisible"]}
```
