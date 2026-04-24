Written to `simulations/quest/rubrics/prove-websearch-rubric-v4-2026-03-14.md`.

---

**v4 summary — 21 criteria, max 122 pts:**

| New ID | Pattern | Closes | Pts |
|--------|---------|--------|-----|
| C-19 | `rules-block-violation-consequence` | Borderline-reading escape on C-17 — gate-embedded mandates admit a conditional reading; RULES-level placement + named violation consequence removes it | 2 |
| C-20 | `verdict-field-precedes-synthesis` | Embedded-verdict weakness on C-18 — a verdict clause in a Conclusion template can be prose-obscured; standalone field as first PHASE 4 entry forces binary rendering before convergence begins | 2 |
| C-21 | `pre-commit-gate-binding` | Priming window on C-16 — a GATE 1-only declaration can drift under Q1 framing; GATE 0 PRE-COMMIT isolation + GATE 1 copy-forward binding front-loads adversarial commitment before the query template is seen | 2 |

**Retroactive R3 scores under v4:** V-04 = 118/122, V-05 = 120/122. The remaining 2-pt gap (C-21 was not in V-04's design) frames the open question for R4.
al | 2 | R1 excellence signal |
| C-15 | Rule-first constraint ordering | aspirational | 2 | R1 excellence signal |
| C-16 | Null-attack target declaration | aspirational | 2 | R2 `null-attack-target-declaration` |
| C-17 | Unconditional refinement mandate | aspirational | 2 | R2 `unconditional-refinement-mandate` |
| C-18 | Null-attack verdict propagation | aspirational | 2 | R2 `null-attack-verdict-propagation` |
| **C-19** | **Rules-block violation consequence** | aspirational | 2 | R3 `rules-block-violation-consequence` |
| **C-20** | **Verdict field precedes synthesis** | aspirational | 2 | R3 `verdict-field-precedes-synthesis` |
| **C-21** | **Pre-commit gate binding** | aspirational | 2 | R3 `pre-commit-gate-binding` |

---

**New criteria (C-19/C-20/C-21) -- what each closes:**

**C-19 -- Rules-Block Violation Consequence (2 pts)**
Closes the *borderline-reading* escape on C-17. Gate-embedded unconditional language (e.g., "every query has a refinement entry") is near-passing but admits a reading that "entry" is conditional on refinement occurring. C-19 requires the mandate to appear in a RULES block (parsed before any phase template) with "no exceptions" and a named violation consequence. RULES-level placement + named consequence converts the instruction from guidance to enforcement, eliminating the conditional reading that causes PARTIAL scores.

**C-20 -- Verdict Field Precedes Synthesis (2 pts)**
Closes the *embedded-verdict* weakness on C-18. A null-attack verdict embedded as a clause in a Conclusion paragraph template satisfies the letter of C-18 but allows prose framing to obscure the binary result. C-20 requires the verdict to be a standalone labeled field (`Null-Attack Verdict: [YES / NO / INCONCLUSIVE]`) placed as the *first* field in PHASE 4, before Convergence and Conflict sub-fields are written. Structural precedence forces binary rendering before convergence analysis begins; the Conclusion then references rather than re-adjudicates the verdict.

**C-21 -- Pre-Commit Gate Binding (2 pts)**
Strengthens C-16 beyond single-gate enforcement. A GATE 1 target declaration (naming a falsifier before Q2 executes) can be generated independently at the moment Q2 is designed, which means pro-hypothesis framing from Q1 can still prime the falsifier choice. C-21 requires a GATE 0 PRE-COMMIT block before the query template is seen, where the falsification event is committed in isolation. GATE 1 then requires Q2's target declaration to match (copy-forward) the PRE-COMMIT event rather than be independently generated. Front-loading the adversarial commitment at the earliest structural point closes the priming window.

---

## Essential Criteria (weight: 60 pts total, 12 pts each)

### C-01 -- URL-Grounded Claims
- **Category**: correctness
- **Weight**: essential
- **Text**: Every factual claim in the output is grounded by a URL pointing to a live or
  archived web source. Claims without a URL are assertions, not evidence, and fail this
  criterion regardless of plausibility.
- **Pass condition**: Every factual claim has a corresponding URL. A single ungrounded
  claim fails this criterion for the entire output.

---

### C-02 -- Direct Quote with Attribution
- **Category**: correctness
- **Weight**: essential
- **Text**: For each source cited, the output includes at least one verbatim excerpt (direct
  quote) from that source, clearly marked as a quote and attributed to the source URL.
  Paraphrases or summaries without direct quotes do not satisfy this criterion.
- **Pass condition**: At least one direct quote per cited source. Sources cited without any
  verbatim excerpt fail this criterion.

---

### C-03 -- Structured Search Record
- **Category**: format
- **Weight**: essential
- **Text**: For each search performed, the output records: (a) the exact query string used,
  (b) the list of sources found, and (c) the evidence extracted from each source.
- **Pass condition**: Each search block contains all three fields -- query, sources, and
  extracted evidence. Missing any field in any search block fails this criterion.

---

### C-04 -- Hypothesis Relevance Stated
- **Category**: coverage
- **Weight**: essential
- **Text**: For each piece of evidence, the output explicitly states how the evidence
  relates to the hypothesis being investigated (supports, refutes, or is neutral/mixed).
- **Pass condition**: Every evidence item includes an explicit relevance label or sentence
  linking it to the hypothesis. Generic evidence with no stated connection fails.

---

### C-05 -- Evidence Strength Rated
- **Category**: correctness
- **Weight**: essential
- **Text**: Each source or evidence block is rated for strength using the prescribed
  vocabulary: strong / weak / mixed. The rating is justified with at least one sentence.
- **Pass condition**: Every source has a strength rating from {strong, weak, mixed} with
  a one-sentence justification. Missing or unjustified ratings fail this criterion.

---

## Recommended Criteria (weight: 30 pts total, 10 pts each)

### C-06 -- Multi-Query Coverage
- **Category**: depth
- **Weight**: recommended
- **Text**: The investigation uses more than one query to explore the hypothesis from
  different angles (e.g., pro framing, con framing, domain-specific terms). Single-query
  outputs are less thorough and may miss contrarian evidence.
- **Pass condition**: At least two distinct query strings are present in the output, with
  queries visibly different in framing or terminology.

---

### C-07 -- Balanced Evidence Set
- **Category**: coverage
- **Weight**: recommended
- **Text**: The output includes evidence on both sides of the hypothesis -- both supporting
  and refuting sources -- or explicitly documents that only one-sided evidence was found
  after attempting balanced queries.
- **Pass condition**: At least one supporting and one refuting (or mixed) evidence item
  is present, OR the output contains a documented note that refuting/supporting evidence
  could not be found despite targeted queries.

---

### C-08 -- Source Credibility Assessment
- **Category**: depth
- **Weight**: recommended
- **Text**: For each source, the output notes the credibility or authority of the source
  (e.g., peer-reviewed, industry report, news outlet, blog, forum). This helps the reader
  calibrate confidence in the evidence.
- **Pass condition**: At least half of cited sources have a credibility note (one phrase
  or label is sufficient). Outputs with zero credibility notes fail.

---

## Aspirational Criteria (weight: 32 pts total)

### C-09 -- Cross-Source Synthesis (5 pts)
- **Category**: depth
- **Weight**: aspirational
- **Text**: After presenting individual evidence items, the output provides a synthesis
  section that identifies where sources converge, where they conflict, and what the
  aggregate evidence says about the hypothesis. This is beyond per-source analysis.
- **Pass condition**: A synthesis paragraph or section is present that references at least
  two sources by name and draws a cross-source conclusion about the hypothesis.

---

### C-10 -- Query Refinement Trail (5 pts)
- **Category**: behavior
- **Weight**: aspirational
- **Text**: The output shows iterative search behavior -- initial queries, results that
  prompted refinement, and the refined queries that followed. This demonstrates active
  epistemic hygiene rather than a single-pass search.
- **Pass condition**: At least one instance of documented query refinement is present,
  showing the original query, what gap it revealed, and the follow-up query used.

---

### C-11 -- Phase-Gate Enforcement (2 pts)
- **Category**: structure
- **Weight**: aspirational
- **Derived from**: R1 pattern `phase-gate-vs-step`
- **Text**: Multi-query and balance requirements are enforced via explicit "GATE: do not
  proceed" checkpoints rather than numbered steps. Gates are structurally harder to skip
  under output pressure because they require a binary verdict before the next phase can
  begin. Numbered steps allow the model to proceed regardless of whether the step's
  condition was met.
- **Pass condition**: At least C-06 and C-07 requirements are enforced by named GATE
  blocks (not numbered steps) that contain an explicit "do not proceed" or equivalent
  stop condition.

---

### C-12 -- Live-Phase Trail Placement (2 pts)
- **Category**: behavior
- **Weight**: aspirational
- **Derived from**: R1 pattern `live-trail-placement`
- **Text**: The query refinement trail (C-10) is placed in the search/collection phase,
  not in the synthesis phase. Placement during the live search captures observed behavior
  at the moment of observation. Placement in the synthesis phase forces retrospective
  reconstruction from memory, which is less accurate and loses the causal link between
  gap-discovery and query adjustment.
- **Pass condition**: The query refinement trail field appears inside the search record
  (alongside query, sources, evidence) rather than in a post-synthesis section.

---

### C-13 -- Named-Target Gate Framing (2 pts)
- **Category**: correctness
- **Weight**: aspirational
- **Derived from**: R1 pattern `gate-framing-names-target`
- **Text**: The gate condition for multi-query coverage names the specific epistemic target
  of Q2 (e.g., "Q2 must explicitly target the refutation side"), not just "distinct framing
  or terminology." Naming the target closes the semantic loophole where two slightly
  different pro-hypothesis queries satisfy the letter of "2 distinct queries" while failing
  the spirit of adversarial coverage.
- **Pass condition**: The GATE or instruction for multi-query coverage explicitly identifies
  what Q2 must attack (refutation, null hypothesis, opposing mechanism). A gate that only
  requires "distinct framing" without naming the target does not pass.

---

### C-14 -- Structured Synthesis Sub-Fields (2 pts)
- **Category**: format
- **Weight**: aspirational
- **Derived from**: R1 excellence signal (pre-printed synthesis sub-fields > prose instruction)
- **Text**: The synthesis section uses pre-printed sub-fields (e.g., Convergence:,
  Conflict:, Conclusion:) rather than a prose instruction to "write a paragraph naming
  two sources." Pre-printed fields require the model to produce three distinct sub-answers.
  A prose instruction can be satisfied by a single paragraph that addresses only one
  dimension, making C-09 easier to nominally pass without genuine multi-dimensional
  synthesis.
- **Pass condition**: The synthesis section contains at least two named sub-fields
  (labels followed by a required fill-in). A single undivided synthesis paragraph does
  not pass, even if it references multiple sources.

---

### C-15 -- Rule-First Constraint Ordering (2 pts)
- **Category**: structure
- **Weight**: aspirational
- **Derived from**: R1 excellence signal (rules enumerated before content fields)
- **Text**: The skill prompt enumerates hard constraints (no training-data evidence,
  verbatim quotes only, URL required per claim) in a numbered rules block before the
  Topic and Hypothesis fields. Rule-first ordering ensures constraints are parsed before
  content is seen, reducing the probability that rules are treated as trailing caveats
  and glossed over during output generation.
- **Pass condition**: A numbered or labeled rules block appears before the first content
  input field (Topic, Hypothesis, or equivalent). Rules that appear only inline within
  later sections, or only as footnotes, do not pass.

---

### C-16 -- Null-Attack Target Declaration (2 pts)
- **Category**: correctness
- **Weight**: aspirational
- **Derived from**: R2 pattern `null-attack-target-declaration`
- **Text**: The refuting query (Q2) includes a pre-committed declaration of the specific
  falsifying result being sought -- not a general "refuting framing" instruction. Naming
  a concrete falsifier closes the semantic loophole where a query like "limitations of X"
  satisfies "refuting framing" while actually targeting qualifications or caveats rather
  than a genuine null hypothesis attack. The declaration must appear before the search
  executes, not as a post-hoc label applied to whatever was found.
- **Pass condition**: The Q2 instruction or gate contains a pre-committed target
  declaration naming a specific falsifying result (e.g., "evidence that X does NOT
  achieve Y under condition Z"). A gate that only requires "refuting framing" without a
  named falsifier does not pass.

---

### C-17 -- Unconditional Refinement Mandate (2 pts)
- **Category**: behavior
- **Weight**: aspirational
- **Derived from**: R2 pattern `unconditional-refinement-mandate`
- **Text**: The query refinement trail (C-10) is required for every search block
  unconditionally -- including when no refinement occurred. "Ran as planned" or "N/A" is
  a valid fill-in; the field cannot be omitted. A conditional mandate ("document
  refinement if it occurs") creates a silent escape: the model can skip the field when
  it chose not to refine, hiding the fact that it considered and rejected adjustment.
  Unconditional completion forces acknowledgement of the decision either way.
- **Pass condition**: The refinement trail instruction explicitly requires completion for
  every SEARCH block with no conditional or "if applicable" escape. An instruction that
  accepts "ran as planned" or "no refinement needed" as explicit fill-ins (confirming
  unconditional completion is expected) satisfies the pass condition. A conditional
  instruction ("if you refined your query, document it here") does not pass.

---

### C-18 -- Null-Attack Verdict Propagation (2 pts)
- **Category**: correctness
- **Weight**: aspirational
- **Derived from**: R2 pattern `null-attack-verdict-propagation`
- **Text**: The conclusion or synthesis phase requires an explicit YES/NO verdict on the
  null hypothesis attack: did the adversarial search find a genuine falsifier? Without
  this requirement, a failed null hypothesis attack (Q2 found only qualifications, not
  genuine falsifiers) can disappear after the search phase, leaving the final conclusion
  unaware that the adversarial test was inconclusive. Verdict propagation ensures the
  adversarial result is visible at the decision point, not buried in the search record.
- **Pass condition**: The synthesis or conclusion section contains a required field or
  instruction that forces an explicit null hypothesis verdict (YES falsified / NO not
  falsified / INCONCLUSIVE). A synthesis that only summarizes convergence and conflict
  without a dedicated null-hypothesis verdict field does not pass.

---

### C-19 -- Rules-Block Violation Consequence (2 pts)
- **Category**: structure
- **Weight**: aspirational
- **Derived from**: R3 pattern `rules-block-violation-consequence`
- **Text**: The unconditional refinement mandate (C-17) is placed in a RULES block that
  is parsed before any phase template, carries an explicit "no exceptions" qualifier, and
  names the consequence of omission (e.g., "omitting this field is a Rule N violation").
  Gate-embedded unconditional language is near-passing but admits a borderline reading
  that "entry" is conditional on refinement having occurred. RULES-level placement
  eliminates ambiguity of scope; naming the violation consequence converts the instruction
  from guidance to enforcement, removing the conditional reading entirely.
- **Pass condition**: The refinement mandate appears in a pre-phase RULES block (not
  embedded inside a gate or phase section) and includes both "no exceptions" and a named
  violation consequence. A mandate that meets C-17 but lacks RULES-level placement and
  violation consequence does not pass C-19.

---

### C-20 -- Verdict Field Precedes Synthesis (2 pts)
- **Category**: format
- **Weight**: aspirational
- **Derived from**: R3 pattern `verdict-field-precedes-synthesis`
- **Text**: The null-attack verdict (C-18) is rendered as a standalone labeled field
  (`Null-Attack Verdict: [YES / NO / INCONCLUSIVE]`) placed as the *first* field in the
  synthesis phase, before Convergence, Conflict, and Conclusion sub-fields are written.
  A verdict embedded as a clause in a Conclusion paragraph template satisfies the letter
  of C-18 but allows prose framing to obscure the binary result. Structural precedence
  forces binary rendering before convergence analysis begins. The Conclusion then
  references the verdict rather than re-adjudicating it, establishing the adversarial
  result as a standalone decision artifact at the synthesis level.
- **Pass condition**: A standalone `Null-Attack Verdict:` field (or equivalent labeled
  field requiring YES/NO/INCONCLUSIVE) appears as the first entry in the synthesis
  section, before any convergence or conflict sub-fields. A verdict embedded only in a
  Conclusion paragraph template or as a prose instruction does not pass.

---

### C-21 -- Pre-Commit Gate Binding (2 pts)
- **Category**: correctness
- **Weight**: aspirational
- **Derived from**: R3 pattern `pre-commit-gate-binding`
- **Text**: The falsification event commitment (C-16) is front-loaded to a GATE 0
  PRE-COMMIT block that executes before the query template is seen. GATE 1 then requires
  Q2's target declaration to match (copy-forward) the PRE-COMMIT event rather than be
  independently generated at query-design time. A GATE 1-only target declaration can
  still be primed by pro-hypothesis framing absorbed during Q1 design; PRE-COMMIT
  isolation closes the priming window by separating adversarial commitment from query
  construction. GATE 1 binding (copy-forward, not re-generation) ensures the committed
  falsifier is preserved rather than drifted during the template execution phase.
- **Pass condition**: A GATE 0 or equivalent PRE-COMMIT block appears before the query
  design template requiring the falsification event to be named in isolation. GATE 1 (or
  equivalent) explicitly requires Q2's target declaration to match or copy the PRE-COMMIT
  event rather than be independently produced. A single gate at query-design time (no
  pre-commit isolation) does not pass C-21, even if it satisfies C-16.

---

## Criterion Summary

| ID   | Text (short)                      | Weight       | Category    | Pts |
|------|-----------------------------------|--------------|-------------|-----|
| C-01 | URL-grounded claims               | essential    | correctness | 12  |
| C-02 | Direct quote with attribution     | essential    | correctness | 12  |
| C-03 | Structured search record          | essential    | format      | 12  |
| C-04 | Hypothesis relevance stated       | essential    | coverage    | 12  |
| C-05 | Evidence strength rated           | essential    | correctness | 12  |
| C-06 | Multi-query coverage              | recommended  | depth       | 10  |
| C-07 | Balanced evidence set             | recommended  | coverage    | 10  |
| C-08 | Source credibility assessment     | recommended  | depth       | 10  |
| C-09 | Cross-source synthesis            | aspirational | depth       |  5  |
| C-10 | Query refinement trail            | aspirational | behavior    |  5  |
| C-11 | Phase-gate enforcement            | aspirational | structure   |  2  |
| C-12 | Live-phase trail placement        | aspirational | behavior    |  2  |
| C-13 | Named-target gate framing         | aspirational | correctness |  2  |
| C-14 | Structured synthesis sub-fields   | aspirational | format      |  2  |
| C-15 | Rule-first constraint ordering    | aspirational | structure   |  2  |
| C-16 | Null-attack target declaration    | aspirational | correctness |  2  |
| C-17 | Unconditional refinement mandate  | aspirational | behavior    |  2  |
| C-18 | Null-attack verdict propagation   | aspirational | correctness |  2  |
| C-19 | Rules-block violation consequence | aspirational | structure   |  2  |
| C-20 | Verdict field precedes synthesis  | aspirational | format      |  2  |
| C-21 | Pre-commit gate binding           | aspirational | correctness |  2  |

**Total max: 122 pts.**

---

## Scoring Examples

All 5 essential pass, 2 of 3 recommended pass, 0 aspirational:

```
score = 60 + (2/3 * 30) + 0
      = 60 + 20 + 0
      = 80  --> meets golden threshold (all essential + composite >= 80)
```

All 5 essential pass, 1 of 3 recommended pass, 0 aspirational:

```
score = 60 + (1/3 * 30) + 0
      = 60 + 10 + 0
      = 70  --> fails golden threshold (composite < 80)
```

All 5 essential pass, 3 of 3 recommended pass, all 12 aspirational pass:

```
score = 60 + 30 + (5+5+2+2+2+2+2+2+2+2+2+2)
      = 60 + 30 + 32
      = 122  --> perfect score
```

R3 retroactive scores under v4:

```
V-01: 112 -- C-11 FAIL, C-18 FAIL, C-19 FAIL, C-20 FAIL, C-21 FAIL
V-02: 115 -- C-17 PARTIAL, C-19 FAIL, C-21 FAIL
V-03: 114 -- C-17 PARTIAL, C-18 PARTIAL, C-19 FAIL
V-04: 118 -- C-19 PASS, C-20 PASS, C-21 FAIL (no PRE-COMMIT block)
V-05: 120 -- C-19 PASS, C-20 PASS, C-21 PASS
```

V-05 (120/122) under v4: C-19 passes via Rule 6 RULES-block placement with violation
consequence. C-20 passes via standalone verdict field preceding synthesis sub-fields.
C-21 passes via GATE 0 PRE-COMMIT + GATE 1 copy-forward binding. Remaining 2-pt gap
requires identifying the next structural escape -- the subject of R4.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria, max 100 pts |
| v2 | 2026-03-14 | +5 aspirational criteria (C-11-C-15) from R1 excellence signals; max 110 pts |
| v3 | 2026-03-14 | +3 aspirational criteria (C-16-C-18) from R2 excellence signals; max 116 pts |
| v4 | 2026-03-14 | +3 aspirational criteria (C-19-C-21) from R3 excellence signals; max 122 pts |
