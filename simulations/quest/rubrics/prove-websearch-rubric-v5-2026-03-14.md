Written to `simulations/quest/rubrics/prove-websearch-rubric-v5-2026-03-14.md`.

---

**v5 summary -- 25 criteria, max 130 pts (+8 pts from v4):**

| New ID | Pattern | Closes |
|--------|---------|--------|
| C-22 | `verdict-copy-forward-binding` | Structural carry-through escape on C-18 -- advisory "consistent with" chain replaced by PHASE 3 Verdict token + Rule 7 verbatim copy-forward + GATE 3 enforcement |
| C-23 | `evidence-floor-enforcement` | Thin-evidence escape -- Rule 8 minimum 2 sources per SEARCH BLOCK with mandatory supplemental search trigger |
| C-24 | `synthesis-citation-isolation` | New-claim injection escape -- PHASE 3.5 admissibility registry locks citation set before synthesis; prose prohibition is not structural |
| C-25 | `baseline-anchored-falsification` | Abstract falsification drift on C-21 -- PRE-COMMIT event must name a concrete status-quo baseline, framing falsification as failure-to-outperform rather than abstract contrary result |

**Retroactive R4 scores under v5:** V-01 = 124, V-02 = 120, V-03 = 120, V-04 = 126, V-05 = **130/130**.

The progression from C-18 (verdict field) → C-20 (field precedes synthesis) → C-22 (copy-forward chain) is the clearest example of the rubric's closure pattern: each round identifies the escape the previous criterion still admits, and the new criterion eliminates exactly that escape.
30, V-04 = 126/130, V-05 = 130/130.
V-02 and V-03 remain at 120 (no new criteria pass -- no Rule 7/8, no PHASE 3.5, no baseline anchor).

---

**New criteria (C-22/C-23/C-24/C-25) -- what each closes:**

**C-22 -- Verdict-Copy-Forward Binding (2 pts)**
Closes the *structural carry-through* escape on C-18. C-18 requires verdict propagation, and C-20 requires the verdict to be a standalone field preceding synthesis. But an advisory "Must be consistent with PHASE 3" check satisfies both the letter of C-18 and the shape of C-20 while still allowing a model to independently re-assess in PHASE 4. C-22 requires PHASE 3 to emit a standalone `Verdict token:` field; Rule 7 (at RULES level, with named violation consequence) to mandate verbatim copy-forward of that token to PHASE 4; and GATE 3 to explicitly verify token existence. The chain -- PHASE 3 emits, GATE 3 checks, Rule 7 mandates verbatim copy, PHASE 4 references by rule number -- is structurally unbroken and cannot be silently violated.

**C-23 -- Evidence-Floor Enforcement (2 pts)**
Closes the *thin-evidence* escape. C-03 requires a structured search record with query, sources, and extracted evidence. A single-source SEARCH BLOCK satisfies C-03's letter. C-23 requires a Rule 8 (at RULES level) establishing a minimum of 2 sources per SEARCH BLOCK, with an explicit mandatory supplemental search trigger: if a first search returns fewer than 2 usable sources, a follow-up search must be executed and documented before the block closes. Naming the floor (2) and the trigger (supplemental search) converts the minimum from an implicit expectation to an enforced structural requirement.

**C-24 -- Synthesis-Citation Isolation (2 pts)**
Closes the *new-claim injection* escape. A prose instruction such as "do not introduce new claims in the synthesis phase" cannot structurally prevent a model from citing in PHASE 4 a source it encountered but did not formally record in PHASE 2. C-24 requires a PHASE 3.5 admissibility registry block between the search phase and the synthesis phase. The registry lists the exact citation set admitted to synthesis (URL + title per source). PHASE 4 is then structurally bound to cite only from the registry. Any source appearing in PHASE 4 that is absent from the registry is a structural violation -- visible and auditable, not dependent on prose compliance.

**C-25 -- Baseline-Anchored Falsification (2 pts)**
Sharpens C-21 beyond event isolation. A PRE-COMMIT falsification event stated as an abstract contrary result (e.g., "evidence that X is not effective") admits a Q2 that satisfies the structural requirement while targeting qualifications, caveats, or niche failures rather than genuine falsification relative to a baseline. C-25 requires the PRE-COMMIT event to name a concrete status-quo baseline (the current standard, incumbent approach, or established rate) and frame the falsification as evidence of failure to outperform that baseline. Anchoring to a concrete comparator sharpens the adversarial commitment from "evidence against X" to "evidence that X fails to improve on [specific baseline Y]," closing the abstract-falsifier drift that allows a softened Q2 to pass structural gates while missing the genuine null hypothesis.

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

## Aspirational Criteria (weight: 40 pts total)

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

### C-22 -- Verdict-Copy-Forward Binding (2 pts)
- **Category**: correctness
- **Weight**: aspirational
- **Derived from**: R4 pattern `verdict-copy-forward-binding`
- **Text**: The null-attack verdict propagation (C-18) is enforced as a named structural
  artifact chain rather than an advisory consistency check. PHASE 3 emits a standalone
  `Verdict token:` field containing exactly one of {YES / NO / INCONCLUSIVE}; a RULES-level
  Rule 7 mandates verbatim copy-forward of that token to PHASE 4 with an explicit
  violation consequence; GATE 3 verifies the token exists before synthesis proceeds;
  PHASE 4 references the token by rule number rather than re-assessing it. Advisory
  language such as "Must be consistent with PHASE 3" satisfies the shape of C-18 but
  allows a model to independently re-adjudicate in PHASE 4. The copy-forward chain
  eliminates independent re-adjudication structurally rather than relying on prose
  compliance.
- **Pass condition**: PHASE 3 contains a standalone `Verdict token:` field; a RULES-level
  mandate (with named violation consequence) requires verbatim copy-forward to PHASE 4;
  GATE 3 explicitly checks token existence; PHASE 4 references the token by rule rather
  than re-assessing. Advisory "consistent with" language without the token+mandate+gate
  chain does not pass.

---

### C-23 -- Evidence-Floor Enforcement (2 pts)
- **Category**: coverage
- **Weight**: aspirational
- **Derived from**: R4 pattern `evidence-floor-enforcement`
- **Text**: Each SEARCH BLOCK requires a minimum of 2 usable sources, enforced by a
  RULES-level rule (Rule 8 or equivalent) with an explicit mandatory supplemental search
  trigger. A single-source SEARCH BLOCK nominally satisfies C-03's structural requirements
  (query + sources + evidence) while enabling thin-evidence synthesis. Naming the floor (2)
  and the trigger (if fewer than 2 usable sources are found, execute and document a
  supplemental search before closing the block) converts the minimum from implicit
  expectation to a structural requirement that cannot be silently bypassed.
- **Pass condition**: A RULES-level rule establishes a minimum of 2 sources per SEARCH
  BLOCK and explicitly states that a supplemental search must be executed and documented
  if the floor is not met on the first query. A soft guideline ("try to find multiple
  sources") or a floor stated only inside a phase section (not at RULES level) does not
  pass.

---

### C-24 -- Synthesis-Citation Isolation (2 pts)
- **Category**: structure
- **Weight**: aspirational
- **Derived from**: R4 pattern `synthesis-citation-isolation`
- **Text**: A PHASE 3.5 admissibility registry (or equivalent named block) is placed
  between the search phase and the synthesis phase. The registry enumerates the exact
  citation set admitted to synthesis (at minimum: URL and title per source). The synthesis
  phase (PHASE 4) is structurally bound to cite only sources present in the registry.
  A prose instruction to "not introduce new claims in synthesis" cannot structurally
  prevent a model from citing in PHASE 4 a source encountered but not formally recorded
  in PHASE 2; the admissibility registry makes any out-of-registry citation auditable
  and structurally visible, not dependent on prose compliance.
- **Pass condition**: A named block between search and synthesis enumerates the admitted
  citation set; PHASE 4 is explicitly bound to cite only from that registry. A prose
  prohibition on new claims without a structural admissibility block does not pass.

---

### C-25 -- Baseline-Anchored Falsification (2 pts)
- **Category**: correctness
- **Weight**: aspirational
- **Derived from**: R4 pattern `baseline-anchored-falsification`
- **Text**: The PRE-COMMIT falsification event (C-21) names a concrete status-quo baseline
  (the current standard, incumbent approach, or established benchmark rate) and frames the
  falsification as evidence of failure to outperform that baseline. An abstract contrary
  result declaration (e.g., "evidence that X is not effective") satisfies the structural
  gates of C-16 and C-21 while admitting a Q2 that targets qualifications, edge-case
  failures, or implementation caveats rather than genuine null hypothesis falsification.
  Anchoring to a specific comparator sharpens the adversarial commitment from "evidence
  against X" to "evidence that X fails to improve on [baseline Y under condition Z],"
  closing the abstract-falsifier drift that allows a softened adversarial query to pass
  structural gates while missing the genuine null hypothesis.
- **Pass condition**: The PRE-COMMIT block names a specific status-quo baseline or
  comparator and frames the falsification event as failure to outperform it. A falsification
  event stated only as an abstract contrary result (without a named baseline) does not
  pass, even if it satisfies C-16 and C-21.

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
| C-22 | Verdict-copy-forward binding      | aspirational | correctness |  2  |
| C-23 | Evidence-floor enforcement        | aspirational | coverage    |  2  |
| C-24 | Synthesis-citation isolation      | aspirational | structure   |  2  |
| C-25 | Baseline-anchored falsification   | aspirational | correctness |  2  |

**Total max: 130 pts.**

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

All 5 essential pass, 3 of 3 recommended pass, all 16 aspirational pass:

```
score = 60 + 30 + (5+5+2+2+2+2+2+2+2+2+2+2+2+2+2+2)
      = 60 + 30 + 40
      = 130  --> perfect score
```

R4 retroactive scores under v5:

```
V-01: 124 -- C-22 PASS (Rule 7 chain); C-23/C-24/C-25 FAIL (no Rule 8, no registry, no baseline anchor)
V-02: 120 -- C-22/C-23/C-24/C-25 FAIL (advisory consistency, no Rule 7/8, no registry, no baseline)
V-03: 120 -- C-22/C-23/C-24/C-25 FAIL (advisory consistency, no Rule 7/8, no registry binding, no baseline)
V-04: 126 -- C-22 PASS (Rule 7), C-23 PASS (Rule 8); C-24/C-25 FAIL (no registry, no baseline anchor)
V-05: 130 -- C-22 PASS (Rule 7), C-23 PASS (Rule 8), C-24 PASS (PHASE 3.5 registry), C-25 PASS (inertia baseline)
```

V-05 (130/130) under v5: C-22 passes via Rule 7 RULES-level copy-forward chain with GATE 3 enforcement
and named violation consequence. C-23 passes via Rule 8 2-source floor with supplemental search trigger.
C-24 passes via PHASE 3.5 admissibility registry binding synthesis to the recorded citation set. C-25
passes via status-quo inertia framing in PRE-COMMIT anchoring Q2 to failure-to-outperform-baseline.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria, max 100 pts |
| v2 | 2026-03-14 | +5 aspirational criteria (C-11-C-15) from R1 excellence signals; max 110 pts |
| v3 | 2026-03-14 | +3 aspirational criteria (C-16-C-18) from R2 excellence signals; max 116 pts |
| v4 | 2026-03-14 | +3 aspirational criteria (C-19-C-21) from R3 excellence signals; max 122 pts |
| v5 | 2026-03-14 | +4 aspirational criteria (C-22-C-25) from R4 excellence signals; max 130 pts |
