Scorecard written. Here is the output:

---

## Round 7 Scoring -- simulate-derivation

### Results Summary

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 | **V-05** | 185/185 | Exemplary |
| 2 | **V-04** | 185/185 | Exemplary |
| 3 | **V-01** | 185/185 | Exemplary |
| 4 | **V-02** | 185/185 | Exemplary |
| 5 | **V-03** | 185/185 | Exemplary |

All five variations score 185/185 -- the v7 ceiling. Expected outcome: R6 V-05 already satisfied C-26 (two-gate architecture structurally present) and C-27 (named cross-evaluation block with >=2 demos). All R7 variations inherit both passes.

**The rubric cannot distinguish**:
- C-26: two-gate architecture as observed structural property vs. declared design commitment
- C-27: three cross-evaluation demonstrations vs. four including gate-architecture self-evaluation

Qualitative ranking within the tie is by v8-seeding strength: V-05 > V-04 (2 axes) > V-01 (gate-arch declaration) > V-02 (site map) > V-03 (bidirectional gates, phase-level additions).

---

### Excellence Signals from V-05

1. **Declared-gate-inventory pattern** -- gate-architecture principle names both gates and phase contexts before Phase 1 as a design commitment, not an observed property; LLM holds the full gate inventory holistically before generating any derivation step
2. **Cross-reference-saturation-declaration pattern** -- preamble table maps all four application sites to governing principles; saturation is declared and auditable in one pass, not inferred by reading all phases
3. **Bidirectional-gate-framing pattern** -- each gate adds a "Cleared state:" sentence naming specific compliance evidence alongside the prohibition; LLM has affirmative target, not only negative constraint
4. **Gate-architecture self-evaluation** -- 4th cross-eval demo applies gate-architecture principle to axis-label principle, confirming both gate labels ("EXACT BLOCKED", "SOUND BLOCKED") pass the distinguishing test

---

### Candidate v8 criteria (from R7 meta-finding)

| Candidate | What it detects |
|-----------|----------------|
| C-28 | Gate-architecture principle declared in preamble naming full gate inventory |
| C-29 | Each gate includes a named cleared-state condition (bidirectional) |
| C-30 | Cross-reference saturation declared in preamble table rather than practiced throughout |

Ceiling would rise to 200.

---

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["declared-gate-inventory pattern: gate-architecture principle in preamble names both gate instances (EXACT classification at Phase 1, APPROX verification at Phase 2) and their phase contexts as a first-class design commitment before any phase begins -- makes two-gate architecture a holistic pre-phase commitment rather than an observed property inferred from sequential gate encounters", "cross-reference-saturation-declaration pattern: preamble table mapping all four application sites to their governing principles makes C-24 saturation auditable in a single preamble pass without reading any phase -- declaration of saturation intent rather than practice of saturation throughout phases", "bidirectional-gate-framing pattern: each gate adds a Cleared state sentence naming the specific compliance evidence required alongside the verdict-blocking condition -- gives the LLM an affirmative compliance threshold rather than only a negative constraint, enabling precision targeting not just error avoidance"]}
```
ning | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-14 | APPROX reasoning independent of source | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-15 | All axes stack without phase-dropping | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-16 | Prose density uniform across block types | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-17 | APPROX gate has mandatory recovery | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-18 | Axis-commitment gateway gates Phase 2 entry | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-19 | Amend fixes ordered by severity (P1 first) | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-20 | Mandatory gates name prohibited action explicitly | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-21 | Gateway axis labels name exact mechanistic behaviors | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-22 | Ordering rules stated as unconditional enumeration | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-23 | Structural principles in pre-phase preamble | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-24 | Application sites cross-reference preamble principle | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-25 | Co-located principles are mutually evaluable | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |

All four application sites carry cross-references in all R7 variations (inherited from R6 V-05 which saturated all four). Cross-evaluation block present in all variations (>=3 demos each). Named STRUCTURAL COMMITMENTS preamble before Phase 1 in all.

---

#### C-26 | Two-gate architecture at structurally different phases (new v7)

| Variation | EXACT gate (Phase 1) | APPROX gate (Phase 2) | Different contexts | Gate-arch declared | Verdict |
|-----------|---------------------|----------------------|--------------------|--------------------|---------|
| V-01 | YES -- "EXACT BLOCKED for any step where the algebraic rule remains unnamed" | YES -- "SOUND BLOCKED...while (b) remains a paraphrase" | YES -- type assignment vs. soundness recording | YES -- 4th preamble principle | **PASS 5** |
| V-02 | YES -- same gate text | YES -- same gate text | YES | NO -- 3 principles only | **PASS 5** |
| V-03 | YES -- same + cleared state | YES -- same + cleared state | YES | NO -- 3 principles only | **PASS 5** |
| V-04 | YES -- same as V-01 | YES -- same as V-01 | YES | YES -- 4th preamble principle | **PASS 5** |
| V-05 | YES -- same + cleared state | YES -- same + cleared state | YES | YES -- 4th preamble principle | **PASS 5** |

C-26's binary pass condition requires structural presence of both gates satisfying C-20 at different phases. All satisfy. Quality distinction: V-01/V-04/V-05 declare the gate inventory in the preamble as a design commitment; V-02/V-03 have both gates structurally without the declaration. This is a v8 distinction, not a v7 one.

---

#### C-27 | Explicit cross-evaluation block in preamble as demonstrative evidence (new v7)

| Variation | Named block | Demo count | All 3 elements per demo | Before Phase 1 | Verdict |
|-----------|-------------|-----------|-------------------------|----------------|---------|
| V-01 | YES -- `**Cross-evaluation**` | 4 | YES | YES | **PASS 5** |
| V-02 | YES -- `**Cross-evaluation**` | 3 | YES | YES | **PASS 5** |
| V-03 | YES -- `**Cross-evaluation**` | 3 | YES | YES | **PASS 5** |
| V-04 | YES -- `**Cross-evaluation**` | 4 | YES | YES | **PASS 5** |
| V-05 | YES -- `**Cross-evaluation**` | 4 | YES | YES | **PASS 5** |

V-02/V-03 demos: (1) axis-label applied to "SOUND BLOCKED"; (2) gate applied to ordering rule; (3) ordering applied to preamble (3 principles in fixed order). V-01/V-04/V-05 add a 4th: gate-architecture applied to axis-label -- tests whether "EXACT BLOCKED" and "SOUND BLOCKED" satisfy the distinguishing test. C-27 requires >=2 demos; all pass.

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 60/60 | 30/30 | 95/95 | **185/185** | Exemplary |
| V-02 | 60/60 | 30/30 | 95/95 | **185/185** | Exemplary |
| V-03 | 60/60 | 30/30 | 95/95 | **185/185** | Exemplary |
| V-04 | 60/60 | 30/30 | 95/95 | **185/185** | Exemplary |
| V-05 | 60/60 | 30/30 | 95/95 | **185/185** | Exemplary |

---

### Rankings

| Rank | Variation | Score | Band | v8 seeding strength |
|------|-----------|-------|------|---------------------|
| 1 | **V-05** | 185/185 | Exemplary | All 3 axes: gate-architecture declaration + cross-reference site map + bidirectional gates + 4 cross-eval demos |
| 2 | **V-04** | 185/185 | Exemplary | 2 axes: gate-architecture + site map + 4 demos; preferred fallback (preamble-only additions) |
| 3 | **V-01** | 185/185 | Exemplary | 1 axis: gate-architecture declaration + 4 demos; strongest v8 C-28 evidence |
| 4 | **V-02** | 185/185 | Exemplary | 1 axis: cross-reference site map + 3 demos; declared saturation without gate-arch declaration |
| 5 | **V-03** | 185/185 | Exemplary | 1 axis: bidirectional gates + 3 demos; phase-level additions; weakest structural evidence |

---

### Excellence Signals from V-05

**1. Declared-gate-inventory pattern**
V-05's gate-architecture principle names both gates and their phase contexts before Phase 1: "The gate-architecture is a design commitment, not an observed property: both gates are active before any derivation step is classified or any verification block is written." Prior behavior: an LLM encountered Gate 1 at Phase 1 and Gate 2 at Phase 2 and inferred the two-gate architecture from context. V-05 declares the full gate inventory holistically before any phase begins. Positions v8 C-28 (hypothetical: gate architecture declared as first-class principle with full gate inventory named in preamble).

**2. Cross-reference-saturation-declaration pattern**
V-05's cross-reference map table makes saturation auditable in a single preamble pass: the 4-row table maps every application site to its governing principle. Prior behavior: V-05-R6 had cross-references at all four sites throughout the phases but no preamble location confirmed this intention -- an evaluator had to read all phases to verify saturation. V-05 eliminates that search. Positions v8 C-28 (declared vs. practiced saturation).

**3. Bidirectional-gate-framing pattern**
V-05 adds "Cleared state:" sentences to both gates naming the specific compliance evidence required: "Cleared state: EXACT may be assigned when the Justification cell names a specific algebraic rule... specific enough that an independent reader could verify the step using only that name" and "Cleared state: SOUND may be recorded when (b) names a domain regime... that would remain fully supportable if the source sentence were removed." Gates become bidirectional: they name what is blocked AND what compliance looks like. Positions v8 C-29 (hypothetical: each gate includes a named cleared-state condition).

**4. Gate-architecture self-evaluation as 4th cross-eval demonstration**
V-05's 4th demo: "Gate-architecture principle applied to the axis-label principle: Do 'EXACT BLOCKED' and 'SOUND BLOCKED' satisfy the axis-label distinguishing test?" Self-referential consistency check -- the gate-architecture commitment evaluates its own gate labels against the distinguishing test. Both labels pass. Gate-architecture confirmed internally.

---

### Meta-Finding: R7 Improvements Exceed Rubric Resolution (Third Consecutive Round)

The rubric cannot distinguish:
- Two-gate architecture as observed structural property vs. declared design commitment
- Three cross-evaluation demonstrations vs. four including gate-architecture self-evaluation
- Cross-references practiced throughout phases vs. saturation declared in preamble table
- Inhibitory gates vs. bidirectional gates with cleared-state examples

**Candidate v8 criteria**:

| Candidate | What it detects | Pts |
|-----------|----------------|-----|
| C-28 | Gate-architecture principle declared in preamble naming both gate instances and phase contexts as a first-class design commitment -- not merely implied by two gate instructions existing in the skill | 5 |
| C-29 | Each mandatory gate includes a named cleared-state condition showing what compliance evidence looks like, alongside the verdict-blocking condition | 5 |
| C-30 | Cross-reference saturation at all application sites explicitly declared in a preamble table rather than practiced through individual cross-references throughout the phases | 5 |

Adding C-28/C-29/C-30 raises the ceiling to 200. R8 variations need to demonstrate declared-gate-inventory, bidirectional-gate-framing, and saturation-declaration as committed architectural properties verifiable in the preamble without reading any phase.

---

### Recommendation

**Ship V-05 as the R7 skill.** Only variation activating all three R7 structural innovations simultaneously. **Fallback**: V-04 (drops bidirectional gates only -- preamble-only additions, no phase density risk on long derivations).

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["declared-gate-inventory pattern: gate-architecture principle in preamble names both gate instances (EXACT classification at Phase 1, APPROX verification at Phase 2) and their phase contexts as a first-class design commitment before any phase begins -- makes two-gate architecture a holistic pre-phase commitment rather than an observed property inferred from sequential gate encounters", "cross-reference-saturation-declaration pattern: preamble table mapping all four application sites to their governing principles makes C-24 saturation auditable in a single preamble pass without reading any phase -- declaration of saturation intent rather than practice of saturation throughout phases", "bidirectional-gate-framing pattern: each gate adds a Cleared state sentence naming the specific compliance evidence required alongside the verdict-blocking condition -- gives the LLM an affirmative compliance threshold rather than only a negative constraint, enabling precision targeting not just error avoidance"]}
```
