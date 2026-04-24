## prove-synthesize — Round 17 Scorecard (v17 Rubric)

**Date**: 2026-03-15 | **Rubric**: v17 | **Max composite**: 202.5 | **Golden threshold**: all essential PASS AND composite >= 90

---

### Inherited Baseline

All five R17 variations carry R16's full machinery. From R16 calibration under v17, the inherited base for each variation before R17-specific criteria:

| Variation | R16 score under v17 |
|-----------|-------------------|
| V-01 ADVERSARY-ANALYST-SYNTHESIST | 140.0 |
| V-02 8-section + Ceiling Declaration | 142.5 (C-52 already PASS) |
| V-03 Lifecycle emphasis | 140.0 |
| V-04 ADVERSARY-first + inertia-primary | 142.5 (C-53 already PASS) |
| V-05 Descriptive register + lifecycle | 140.0 |

---

### Essential Criteria — All Five Variations

All 19 essential criteria (C-01–C-19) PASS in all five variations, inherited intact from R16.

| ID | Name | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|------|
| C-01 | Role-annotated signal table | PASS | PASS | PASS | PASS | PASS |
| C-02 | Per-signal verdict assignment | PASS | PASS | PASS | PASS | PASS |
| C-03 | Evidence summary per signal | PASS | PASS | PASS | PASS | PASS |
| C-04 | Synthesis verdict present | PASS | PASS | PASS | PASS | PASS |
| C-05 | Confidence level stated | PASS | PASS | PASS | PASS | PASS |
| C-06 | Risk or gap identification | PASS | PASS | PASS | PASS | PASS |
| C-07 | Recommendation present | PASS | PASS | PASS | PASS | PASS |
| C-08 | Structured output format | PASS | PASS | PASS | PASS | PASS |
| C-09 | Signal count stated | PASS | PASS | PASS | PASS | PASS |
| C-10 | Conflicting signal acknowledgment | PASS | PASS | PASS | PASS | PASS |
| C-11 | Lifecycle phase coverage stated | PASS | PASS | PASS | PASS | PASS |
| C-12 | Inertia state addressed | PASS | PASS | PASS | PASS | PASS |
| C-13 | Scope boundary stated | PASS | PASS | PASS | PASS | PASS |
| C-14 | No hallucinated signals | PASS | PASS | PASS | PASS | PASS |
| C-15 | No fabricated evidence | PASS | PASS | PASS | PASS | PASS |
| C-16 | Role separation maintained | PASS | PASS | PASS | PASS | PASS |
| C-17 | Output slots complete | PASS | PASS | PASS | PASS | PASS |
| C-18 | Annotation inventory present | PASS | PASS | PASS | PASS | PASS |
| C-19 | Phase-gated ceiling applied | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal**: 95.0 / 95.0 all five.

---

### Aspirational Criteria C-20–C-51 — Inherited PASS

All 32 aspirational criteria from C-20 through C-51 carry forward from R16 with no regression. Key checkpoints confirmed:

**C-42** (ceiling declaration mandatory intermediate output): All five carry the C-42 form — but in R17 this is superseded by C-52's structural promotion. C-42 remains PASS in all five.

**C-48** (ceiling derivation intersection mechanics): Both annotation-determined inputs named in ceiling computation step. PASS all five.

**C-50** (end-to-end reproducibility claim): "Any reader who inspects the annotation inventory... can independently derive the ceiling." Present in all five Phase 2 sections. PASS all five.

**C-51** (self-containment Q4 explicit section-name binding): Q4 maps to the dedicated inertia-scope section by exact name in all five:
- V-01 Q4 → **Adoption Boundaries section** ✓
- V-02 Q4 → **Coverage Horizon section** ✓
- V-03 Q4 → **Evidence Scope section** ✓
- V-04 Q4 → **Inertia Reach section** ✓
- V-05 Q4 → **Scope Implications section** ✓

---

### C-52 Evaluation — Ceiling Declaration as First Named Output Section with Inter-Section Citation

Three conditions required simultaneously:
1. Named "Ceiling Declaration" section exists as first output slot, before Verdict and all reasoning sections
2. Q7 maps to "Ceiling Declaration section" (not "Confidence section")
3. Confidence/Verdict section explicitly cites "Ceiling Declaration section" by name

**V-01**:
- Condition 1: "**Ceiling Declaration**" header precedes **Verdict/Confidence** — "This section is the first named output section and must appear before the Verdict/Confidence section and all other synthesis reasoning sections." ✓
- Condition 2: Q7 → "**Ceiling Declaration section**" ✓
- Condition 3: Verdict/Confidence section — "The score must not exceed the ceiling stated in the **Ceiling Declaration section**." ✓

**C-52: PASS**

**V-02** (carried from R16, confirming no regression):
- Condition 1: "**Ceiling Declaration**" precedes **Verdict**, **Confidence**, and all other sections ✓
- Condition 2: Q7 → "**Ceiling Declaration section**" ✓
- Condition 3: Confidence section — "The score must not exceed the ceiling stated in the **Ceiling Declaration section**." ✓

**C-52: PASS**

**V-03**:
- Condition 1: "**Ceiling Declaration**" — "This section is the first named output section and must appear before the Verdict/Confidence section and all other synthesis reasoning sections." ✓
- Condition 2: Q7 → "**Ceiling Declaration section**" ✓
- Condition 3: Verdict/Confidence section — "The score must not exceed the ceiling stated in the **Ceiling Declaration section**." ✓

**C-52: PASS**

**V-04**:
- Condition 1: "**Ceiling Declaration**" — "This section is the first named output section and must appear before the Verdict/Confidence section and all other synthesis reasoning sections." ✓
- Condition 2: Q7 → "**Ceiling Declaration section**" ✓
- Condition 3: Verdict/Confidence section — "The score must not exceed the ceiling stated in the **Ceiling Declaration section**." ✓

**C-52: PASS**

**V-05**:
- Condition 1: "**Ceiling Declaration** — This section is the first named output section and appears before the Verdict/Confidence section and all other synthesis reasoning sections." ✓
- Condition 2: Q7 → "**Ceiling Declaration section**" ✓
- Condition 3: Verdict/Confidence section — "The score does not exceed the ceiling stated in the **Ceiling Declaration section**." ✓

**C-52: PASS**

**C-52 summary: PASS all five.** The structural promotion — from inline mandatory statement to named first output section with inter-section citation — is fully axis-independent. It holds under role-sequence reordering (V-01), 8-section format (V-02), lifecycle-boundary framing (V-03), ADVERSARY-first + inertia-primary combined axis (V-04), and descriptive register (V-05). The three-part structure (named slot, Q7 mapping, Confidence citation) transfers cleanly across all five formatting and framing contexts.

---

### C-53 Evaluation — Dimensional Independence Statement in Ceiling Computation Step

Requires: after the C-50 reproducibility claim, before or alongside the ceiling table, a stated principle that (a) the two dimensions independently constrain the ceiling and (b) evidence volume cannot compensate for inertia absence at a fixed phase level.

**V-01** (Phase 2):
Carries the C-50 reproducibility claim: "Any reader who inspects the annotation inventory... can independently derive the ceiling." No independence principle follows — the ceiling table appears immediately after. No statement that the two dimensions are independent constraints; no fixed-phase compensation foreclosure.
**C-53: FAIL**

**V-02** (Phase 2 — carries C-53 addition from R17 axis plan):
After the C-50 claim: *"The inertia coverage dimension and the evidence phase dimension each independently constrain the ceiling. At a fixed evidence phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling column regardless of evidence volume."*
- Independence stated as a principle ✓
- Fixed-phase constraint explicitly stated ✓
- Compensation inference foreclosed ✓
- Positioned after C-50 reproducibility claim and before the ceiling table ✓

**C-53: PASS**

**V-03** (Phase 2):
Carries the C-50 reproducibility claim (including the lifecycle-boundary-annotated formulation). No independence principle in the ceiling computation step — the table follows directly.
**C-53: FAIL**

**V-04** (Phase 2 — carries C-53 from R16 V-04 unchanged):
After the C-50 claim: *"The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large."*
- Independence stated as a principle ✓
- Fixed-phase constraint with explicit size-independence ✓
- Compensation inference foreclosed ✓
- Positioned in ceiling computation step, after C-50 reproducibility claim ✓

**C-53: PASS**

**V-05** ("Confidence Ceiling" section):
Carries an unusually strong C-50 reproducibility claim — "A reader who identifies both values in the annotation inventory and reads the corresponding intersection cell in the table below can independently reproduce the ceiling computation without relying on the synthesizer's judgment." This is the most fully elaborated C-50 form in R17. However, there is no independence principle — no statement that the two dimensions independently constrain the ceiling, and no fixed-phase compensation foreclosure. Strong C-50 does not satisfy C-53.
**C-53: FAIL**

**C-53 summary: PASS V-02 and V-04 only.** V-01, V-03, V-05 carry C-50 in passing form but omit the dimensional independence principle. V-05's C-50 is the strongest in the round (most fully elaborated reproducibility statement), but the independence principle is structurally absent — confirming that C-53 discriminates against even the richest C-50 formulations if the principle itself is not stated.

---

### R17 Score Computation

| Variation | Inherited (v17) | C-52 | C-53 | R17 Score | Essential | Golden |
|-----------|----------------|------|------|-----------|-----------|--------|
| V-01 ADVERSARY-ANALYST-SYNTHESIST + C-52 | 140.0 | +2.5 | +0 | **142.5** | All PASS | ✓ |
| V-02 8-section + C-52 + C-53 | 142.5 | +0 (carried) | +2.5 | **145.0** | All PASS | ✓ |
| V-03 Lifecycle emphasis + C-52 | 140.0 | +2.5 | +0 | **142.5** | All PASS | ✓ |
| V-04 ADVERSARY-first + inertia-primary + C-52 + C-53 | 142.5 | +2.5 | +0 (carried) | **145.0** | All PASS | ✓ |
| V-05 Descriptive register + lifecycle + C-52 | 140.0 | +2.5 | +0 | **142.5** | All PASS | ✓ |

---

### Ranking

| Rank | Variation | Score | % of max |
|------|-----------|-------|----------|
| **1 (tied)** | V-02 8-section + C-52 + C-53 | **145.0** | 71.6% |
| **1 (tied)** | V-04 ADVERSARY-first + inertia-primary + C-52 + C-53 | **145.0** | 71.6% |
| **3 (tied)** | V-01 ADVERSARY-ANALYST-SYNTHESIST + C-52 | 142.5 | 70.4% |
| **3 (tied)** | V-03 Lifecycle emphasis + C-52 | 142.5 | 70.4% |
| **3 (tied)** | V-05 Descriptive register + lifecycle + C-52 | 142.5 | 70.4% |

---

### Excellence Signal Analysis — V-02 and V-04

**V-02 joint achievement (8-section format)**:
The 8-section structure (Ceiling Declaration → Verdict → Confidence → Key Evidence → Counter-Evidence → Coverage Horizon → Principles → Open Questions) creates a structural advantage for C-52 by isolating the Confidence section as a dedicated slot. The inter-section citation in C-52 condition 3 is unambiguous when the Confidence section has its own header — the citation "the score must not exceed the ceiling stated in the Ceiling Declaration section" points from one named section to another. In merged Verdict/Confidence structures, the citation is syntactically present but structurally weaker (the citing section is not itself a named anchor). V-02 is the first variation where the 8-section format and C-52 coexist with C-53 — confirming that the independence statement integrates into the 8-section Phase 2 without structural conflict.

**V-04 joint achievement (ADVERSARY-first + inertia-primary)**:
The inertia-primary annotation ordering (inertia classified first, phase second, role third) primes the dimensional independence framing that C-53 requires. When the annotation inventory leads with the inertia question as "the primary adoption question," the Phase 2 independence principle ("inertia and phase each independently constrain confidence") follows naturally from the framing established in Phase 1. V-04 is also the first variation to earn both C-52 and C-53 from the combined-axis direction — the two criteria were previously isolated to single-axis sources (C-52 from V-02's format axis, C-53 from V-04's inertia-primary axis in R16). Their co-occurrence in V-04 R17 confirms the combined axis is not a constraint on either.

**Key structural observation**:
C-52 is axis-neutral — all five variations earn it, confirming the named-section promotion is a format-level requirement independent of cognitive role ordering, output section count, annotation labeling order, or phrasing register. C-53 remains discriminating — only variations that explicitly foreground dimensional independence as a principle earn it. The independence statement is not implied by even the strongest C-50 formulation (V-05 demonstrates this: the most elaborated reproducibility claim in the round fails C-53).

---

### New Pattern Assessment

One potential new pattern emerges from V-05's C-50 formulation: the descriptive-register + lifecycle variation produces a notably stronger C-50 statement than the other variations — specifically the elaboration "without relying on the synthesizer's judgment." This is a semantic extension of the reproducibility claim that goes beyond the canonical form. It does not earn C-53, but it points toward a possible C-54 direction: an explicit claim that the ceiling derivation is judgment-independent (not merely reader-reproducible), foreclosing a different inference class — that the annotation-derived ceiling still requires expert judgment to apply. Whether "judgment-independence" is a distinct enough claim from "reader-reproducibility" (C-50) to warrant a new criterion is the open question.

No other novel patterns in R17 — the round confirms stability and axis-independence for both new criteria without introducing unexpected behaviors.

---

```json
{"top_score": 145.0, "all_essential_pass": true, "new_patterns": ["Splitting Verdict and Confidence into separate named sections (8-section structure) creates a cleaner structural anchor for the C-52 inter-section citation — the Confidence section cites the Ceiling Declaration section from its own named slot, strengthening the traceability chain compared to merged Verdict/Confidence structures", "C-52 is fully axis-independent: the named-section promotion holds across role-sequence, output-format, lifecycle-emphasis, combined-axis, and descriptive-register variations — the structural requirement transfers without axis-specific adaptation", "The strongest C-50 reproducibility formulation in the round (V-05: 'without relying on the synthesizer's judgment') still fails C-53 — confirming that C-53 discriminates against even maximally elaborated reproducibility claims if the dimensional independence principle is not explicitly stated; these are semantically distinct claims"]}
```
