## /quest:score — topic-story Round 2 (Rubric v2)

---

### Scoring Notes

Trace artifact is `placeholder`. Scoring evaluates prompt reliability — how confidently each variation elicits each criterion when run. C-01 (BLUF) is treated as dependent on audience-pressure framing: V-04/V-05 inherit R1 V-04's mechanism (100/100) and score PASS; V-01/V-02/V-03 have softer editorial framing and score PARTIAL.

---

### Per-Criterion Evaluation

#### C-01 — Bottom Line Up Front (essential / correctness)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PARTIAL | "Team lead who has 10 minutes" framing present, but 5-beat structure puts recommendation at Beat 5 with no explicit BLUF instruction. |
| V-02 | PARTIAL | "Give them a view" at end of prompt; no BLUF instruction. Story structure buries recommendation in Pass 2 Beat 5. |
| V-03 | PARTIAL | "Editorial, not neutral" tone instruction; no audience-pressure framing that pushes recommendation forward. |
| V-04 | PASS | Inherits R1 V-04 audience pressure verbatim: "A team lead has 10 minutes and must decide." Strong enough that R1 V-04 scored 100/100. |
| V-05 | PASS | "The reader: A principal engineer or team lead who has 10 minutes and is accountable for the call." Same R1 mechanism, named reader role added. |

---

#### C-02 — Labeled sections (essential / format)

All five variations: **PASS**. Each specifies 5 named beats (What we set out to understand / What the signals revealed / What the signals say together / What remains uncertain / The recommendation). No variation omits any beat.

---

#### C-03 — Cross-signal synthesis (essential / correctness)

All five variations: **PASS**. Every variation requires the pattern statement to reference what two or more signals show together that no single signal shows alone. V-02 additionally requires artifact name citation in Output 1.2.

---

#### C-04 — Pattern-not-summary (essential / depth)

All five variations: **PASS**. All explicitly distinguish synthesis from summary:
- V-01: "If this sentence could be derived from any single artifact, it is wrong."
- V-02: "If the sentence could be derived by reading any single artifact, it does not pass."
- V-03: Full "Synthesis, not summary" section with contrast framing.
- V-04: "If this sentence could come from reading one artifact, find the real pattern."
- V-05: Rule 1 explicit before/after example showing the distinction.

---

#### C-05 — Signal coverage is grounded (recommended / coverage)

All five variations: **PASS**. All instruct `Glob simulations/**/{topic}-*` and read every artifact. The "key finding per signal" steps in Beats 2/3 naturally surface multiple namespaces.

---

#### C-06 — Uncertainty is specific (recommended / depth)

All five variations: **PASS**:
- V-01: Uncertainty table requires naming the specific open question.
- V-02: Output 1.3 minimum one entry, generic hedges rejected.
- V-03: Conditional register + "An uncertainty that does not affect the recommendation is not worth naming — omit it."
- V-04: Output C table, minimum one row, generic hedges rejected.
- V-05: Rule 3 requires naming precisely, with directional consequence.

---

#### C-07 — Recommendation proportionality (recommended / correctness)

All five variations: **PASS**. The pattern-to-verb connection requirement (all variations) makes disproportionate recommendations structurally inconsistent — the verb must follow from the pattern, not individual findings.

---

#### C-08 — Narrative arc (aspirational / behavior)

All five variations: **PASS**. The 5-beat structure provides intent → evidence → pattern → uncertainty → recommendation arc in all variations. V-02's two-pass structure makes the arc most explicit.

---

#### C-09 — Delta surfacing (aspirational / depth)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | FAIL | No "expected X, found Y" instruction. Template slots do not prompt for contrastive framing. |
| V-02 | FAIL | Two-pass structure focused on analysis and composition; no delta instruction anywhere. |
| V-03 | PARTIAL | Rule example: "a gap neither signal named but both expose" models implicit discovery language, nudging contrastive register as side effect. Not explicit instruction. |
| V-04 | FAIL | Inherits V-01/V-02 mechanisms; neither produces delta instruction. |
| V-05 | PARTIAL | Rule 1 example: "a gap neither signal named but both expose" models the same discovery framing. Repeated exposure to this register makes contrastive statements more probable. |

---

#### C-10 — Pre-composition pattern artifact (aspirational / depth)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Step 1 explicitly titled "Pre-composition pattern block." Template must be completed before prose begins. |
| V-02 | PASS | Output 1.2 is a separate named deliverable before Pass 2 starts. Process gate enforces sequencing. |
| V-03 | PASS | "Before composing the narrative, write this labeled claim." Behavioral but explicit. |
| V-04 | PASS | Template slot (V-01) + process gate (V-02) combined. Strongest mechanism — both structural independence and sequencing enforced. |
| V-05 | PASS | Rule 2: "Before composing the narrative, write this labeled claim." Same behavioral mechanism as V-03. |

---

#### C-11 — Pattern-to-recommendation traceability (aspirational / correctness)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Template slot: "This pattern produces a [verb] recommendation because: [one sentence]." Fills during Step 1, before prose. |
| V-02 | PASS | Beat 5 requires explicit citation: "The pattern — [restate] — produces this call because [logical connection]." |
| V-03 | PASS | Beat 5: "Connect it explicitly to the pattern: 'The pattern — [restate] — points to [verb] because [one sentence].'" |
| V-04 | PASS | Dual enforcement: template slot (Output B second line) + Beat 5 explicit format. |
| V-05 | PASS | Rule 4 + revision pressure: "If you cannot write this sentence, your pattern and recommendation are not actually connected — revise one of them." Strongest behavioral mechanism. |

---

#### C-12 — Decision-cost annotated uncertainty (aspirational / depth)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Table with explicit direction columns: "If resolved [direction A] / If resolved [direction B]." Column headers enforce directional form. |
| V-02 | PASS | Output 1.3 requires: "if resolved [direction A], recommendation shifts to [verb]." |
| V-03 | PASS | Conditional register + example + "An uncertainty that affects the recommendation but does not state the directional consequence is incomplete — add it." |
| V-04 | PASS | Table columns (V-01) + register instruction (V-02). Strongest structural enforcement. |
| V-05 | PASS | Rule 3 + example ("If the API rate-limit constraint is lifted, this moves from pause to proceed") + "Do not name an uncertainty without stating its directional consequence — it is incomplete." |

---

### Composite Scores

| Var | Essential (×60) | Recommended (×30) | Aspirational (×10) | Composite |
|-----|-----------------|-------------------|--------------------|-----------|
| V-01 | 3.5/4 = **52.5** | 3/3 = **30** | 4/5 = **8** | **90.5** |
| V-02 | 3.5/4 = **52.5** | 3/3 = **30** | 4/5 = **8** | **90.5** |
| V-03 | 3.5/4 = **52.5** | 3/3 = **30** | 4.5/5 = **9** | **91.5** |
| V-04 | 4/4 = **60** | 3/3 = **30** | 4/5 = **8** | **98** |
| V-05 | 4/4 = **60** | 3/3 = **30** | 4.5/5 = **9** | **99** |

**Golden threshold**: all essential pass AND composite >= 80.

| Var | All Essential Pass | Golden? | Band |
|-----|-------------------|---------|------|
| V-01 | No (C-01 PARTIAL) | No | Partial — useful with caveats |
| V-02 | No (C-01 PARTIAL) | No | Partial — useful with caveats |
| V-03 | No (C-01 PARTIAL) | No | Partial — useful with caveats |
| V-04 | Yes | Yes | Golden |
| V-05 | Yes | Yes | Golden — highest composite |

---

### Rankings

1. **V-05** — 99 (Golden). Audience pressure drives C-01. Rule 4 revision pressure is strongest C-11 mechanism. Rule 1 example produces partial C-09 delta. Rule 3 conditional form fully covers C-12.
2. **V-04** — 98 (Golden). Strongest C-10 (template + gate) and C-12 (table columns). Misses C-09 entirely. Slightly weaker C-11 than V-05 (slot present, no revision pressure).
3. **V-03** — 91.5 (Partial). C-09 partial from discovery example. Loses essential points on C-01 (no audience pressure). Best single-axis behavioral variation.
4. **V-01 / V-02** — 90.5 (Partial). C-01 partial. Template (V-01) and gate (V-02) are the structural substrates that V-04 combines — neither achieves Golden alone without audience pressure.

---

### Excellence Signals (from V-05)

**E-01 — Revision pressure creates self-verification for C-11.**
Rule 4's "if you cannot write this sentence, your pattern and recommendation are not actually connected — revise one of them" is qualitatively different from a template slot. The slot can be filled weakly; the revision instruction forces the model to check whether the derivation is real before proceeding. This is the C-11 mechanism that V-04's template lacks.

**E-02 — Synthesis examples with gap language generate partial C-09 compliance as a side effect.**
Rule 1's anti-summary example ("a gap neither signal named but both expose") models the discovery/contrastive register implicitly. The model doesn't receive explicit C-09 instruction, but the example primes the contrastive framing. This is a zero-instruction-cost partial lift — any variation that models the synthesis register with this language gets partial C-09 at no added verbosity.

**E-03 — Named reader with stated accountability maximizes C-01 reliability.**
"The reader: A principal engineer or team lead who has 10 minutes and is accountable for the proceed/pause/pivot/abandon call" combines role, time constraint, and accountability. This is the specific audience formulation from R1 V-04 that drove 100/100. Variations without it (V-01/V-02/V-03) drop to PARTIAL on C-01 even when everything else is correct.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Revision pressure on derivation ('if you cannot write this sentence, revise one of them') operationalizes C-11 as self-verification without template slots", "Synthesis examples with implicit discovery language ('a gap neither signal named but both expose') produce partial C-09 delta surfacing as a side effect of the anti-summary instruction at zero additional verbosity cost"]}
```
