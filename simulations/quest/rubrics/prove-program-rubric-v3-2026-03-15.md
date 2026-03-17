Done. Here is what was extracted and why each is structurally distinct:

---

**Three new aspirational criteria added as C-14, C-15, C-16:**

**C-14 — Plan-level output routing pre-commitment** (from V-02/V-04)
The plan table carries `Output label` and `Consumed by` columns *before any experiment runs*. This is the upstream anchor of the contract loop. C-11 (synthesis audit) closes it post-execution; C-15 closes it per-block. C-14 is the pre-commitment that makes both verifiable.

**C-15 — Per-experiment contract delivery boolean** (from V-02/V-04)
`Contract delivery: [output label] = "...", consumed by = "[step]" — delivered? Yes/No` — distinct from C-12 (COMPLETE marker, no plan reference, no boolean) by adding two things: explicit reference to the plan contract by label, and a Yes/No resolution. C-14 + C-15 together form a closed loop; neither alone satisfies both ends.

**C-16 — Gap-to-plan column threading** (from V-04)
V-04's unique contribution: a "Closes gap?" column in the plan table threads the inertia gap declaration (C-13 element 1) directly into the plan, making the gap-closing assignment visible before execution and preventing post-hoc reassignment in synthesis. Requires C-13 to PASS; neither C-13 nor C-14 alone captures this bridging step.

---

**Scoring changes:**
- Aspirational pool: 25 → 40 (8 criteria × 5 pts)
- Total pool: 115 → 130
- Baseline threshold unchanged at 100
ed hypothesis section (or equivalent) that
  appears before any experiment section, states a specific belief in positive form, and is not
  merely a restatement of the research question.

---

### C-02 -- Experiment plan with >=2 distinct types
- **Category**: coverage
- **Weight**: essential
- **Text**: The orchestrator produces an explicit experiment plan that selects at least two
  distinct experiment types (e.g., websearch, intelligence, analysis, interview, prototype, or
  custom) and explains the rationale for the chosen combination.
- **Pass condition**: A plan section lists >=2 experiment types by name, states why each was
  chosen for this research question, and the experiments actually execute in the body of the
  document.

---

### C-03 -- Feed-forward between experiments
- **Category**: behavior
- **Weight**: essential
- **Text**: Each experiment's outputs are consumed by subsequent steps. Later experiments or
  the synthesis explicitly reference findings from earlier experiments rather than treating
  each as independent.
- **Pass condition**: At least one instance of explicit forward-feeding: a later experiment or
  the synthesis section cites or incorporates a finding from an earlier experiment by name or
  content.

---

### C-04 -- Synthesis with "what we thought vs. what we actually learned"
- **Category**: correctness
- **Weight**: essential
- **Text**: The document contains a synthesis section that answers the original research
  question and contrasts the pre-investigation hypothesis against the post-investigation
  finding.
- **Pass condition**: Synthesis section present, contains both a restatement of the original
  hypothesis and a "what we actually learned" statement that either confirms, refines, or
  refutes it. May not simply repeat hypothesis verbatim as the finding.

---

### C-05 -- Qx.md format artifact at correct path
- **Category**: format
- **Weight**: essential
- **Text**: The output is written as a Qx.md-style research document (structured with labeled
  sections: hypothesis, experiments, findings, synthesis, principles) and saved at the
  canonical path `simulations/prove/research/{topic}-research-{date}.md`.
- **Pass condition**: Document has >=4 labeled sections matching the Qx.md pattern. Artifact
  filename follows `{topic}-research-{date}.md` convention and is placed under
  `simulations/prove/research/`.

---

## Recommended Criteria (weight: 30 points total)

### C-06 -- Principles extracted (>=2, labeled, actionable)
- **Category**: depth
- **Weight**: recommended
- **Text**: The document closes with a principles section that extracts at least two reusable,
  actionable principles from the investigation's findings -- not observations, but design rules
  or decision heuristics.
- **Pass condition**: Principles section present with >=2 entries. Each entry is labeled (e.g.,
  "P-01") and states a rule in imperative or conditional form ("When X, do Y" or "Always Z").
  Generic truisms ("do good research") do not pass.

---

### C-07 -- Confidence levels stated per major finding
- **Category**: depth
- **Weight**: recommended
- **Text**: Each major finding in the synthesis carries an explicit confidence level or evidence
  quality indicator (e.g., high/medium/low, or a brief qualifier such as "based on 3 sources"
  or "inconclusive").
- **Pass condition**: >=2 findings in the synthesis or findings section are annotated with
  confidence level or evidence-quality qualifier. Unlabeled or uniform confidence across all
  findings does not pass.

---

### C-08 -- Flexibility demonstrated beyond prove-topic
- **Category**: coverage
- **Weight**: recommended
- **Text**: The experiment sequence includes at least one experiment type or scope that would
  not be available in prove-topic (e.g., a cross-namespace lookup, a custom data analysis, a
  non-Signal research question, or a web search on an external domain).
- **Pass condition**: At least one experiment step either (a) queries data outside the current
  Signal topic context, (b) uses a custom experiment not in the standard prove skill set, or
  (c) spans multiple namespaces. The document or experiment log makes this flexibility visible.

---

## Aspirational Criteria (weight: 40 points total)

### C-09 -- Falsification criteria stated in hypothesis
- **Category**: rigor
- **Weight**: aspirational
- **Text**: The hypothesis section states explicit falsification criteria: what evidence would
  cause the researcher to reject the hypothesis. This frames the investigation as scientific
  rather than confirmatory.
- **Pass condition**: Hypothesis section contains a named "Falsification" field or equivalent
  statement of the form "This hypothesis would be refuted if [condition]." The condition must
  be specific and testable, not vacuous ("if all evidence contradicts it").

---

### C-10 -- Cross-namespace artifact integration
- **Category**: integration
- **Weight**: aspirational
- **Text**: The synthesis or principles section names at least one artifact from a different
  Signal namespace (e.g., a scout brief, a flow diagram, a trace contract) that the
  prove-program findings connect to or update, demonstrating the skill operating as connective
  tissue across the plugin.
- **Pass condition**: Synthesis or cross-namespace note explicitly names an artifact from a
  different namespace (by type or path), states what the connection is, and the reference is
  substantive (not a generic "see also").

---

### C-11 -- Feed-forward ledger table
- **Category**: verifiability
- **Weight**: aspirational
- **Derived from**: V-02 Round 1 excellence signal -- feed-forward ledger table audits
  plan-to-execution contract by inspection, scannable without reading prose.
- **Text**: The document includes a dedicated feed-forward ledger: a structured table that maps
  every experiment from the plan to its output label and names the downstream step that
  consumed that output. This makes the plan-to-execution contract verifiable by inspection
  without reading prose.
- **Pass condition**: A ledger section (or equivalent table) is present with one row per
  planned experiment, columns for output label and consumer, and all rows populated. A reader
  can confirm C-03 compliance by reading the ledger alone without scanning the experiment
  prose.

---

### C-12 -- Per-experiment COMPLETE markers with consumed-by routing
- **Category**: traceability
- **Weight**: aspirational
- **Derived from**: V-03 Round 1 excellence signal -- per-experiment COMPLETE + consumed-by
  routing is the most granular feed-forward enforcement.
- **Text**: Each experiment block terminates with an explicit COMPLETE record that states (a)
  what output the experiment produced and (b) which downstream step receives that output. This
  makes the feed-forward chain traceable at the block level rather than requiring whole-document
  comprehension.
- **Pass condition**: >=2 experiment blocks each contain a COMPLETE record with both an output
  statement and an explicit "Consumed by: [step name or synthesis]" routing. The routings
  must be specific (not "see synthesis") and must match the actual flow of the document.

---

### C-13 -- Inertia gap bookending
- **Category**: program-level framing
- **Weight**: aspirational
- **Derived from**: V-05 Round 1 excellence signal -- strongest C-08 enforcement: gap declared
  before execution, experiment marked as gap-closing, synthesis closure verdict delivered.
- **Text**: The research program explicitly names what a single-topic prove run could not
  address (the inertia gap) before any experiment runs, marks the experiment designed to close
  the gap, and delivers an explicit closure verdict in the synthesis. This elevates the
  document from a research record to a gap-closure proof.
- **Pass condition**: Three elements all present: (1) a gap declaration before the first
  experiment that names the limitation of single-topic prove for this question; (2) an
  experiment marked as the gap-closing step, with rationale; (3) a synthesis-level closure
  verdict that explicitly states whether the gap was closed and on what evidence. Frontmatter
  field `inertia_gap_closed: true/false` or equivalent structured marker satisfies element 3
  when accompanied by prose support.

---

### C-14 -- Plan-level output routing pre-commitment
- **Category**: verifiability
- **Weight**: aspirational
- **Derived from**: V-02/V-04 Round 2 excellence signal -- plan table with Output label and
  Consumed by columns pre-commits routing before execution begins, creating the upstream anchor
  that C-11 (post-execution ledger) and C-15 (boolean verification) verify against.
- **Text**: The experiment plan table includes dedicated columns for the expected output label
  and downstream consumer for each planned experiment. This pre-commits the routing contract
  before any experiment runs, making deviations between plan and execution immediately visible
  when compared against C-11 or C-15.
- **Pass condition**: The plan section uses a table or structured list with >=2 experiment
  rows, each specifying both an output label and a named consumer. Column names may vary
  ("Output label / Consumed by", "Produces / Used by", or equivalent). The output labels must
  correspond to labels used in the experiment blocks and synthesis. Prose description of intent
  does not satisfy this criterion; a structured per-experiment mapping is required.

---

### C-15 -- Per-experiment contract delivery boolean
- **Category**: traceability
- **Weight**: aspirational
- **Derived from**: V-02/V-04 Round 2 excellence signal -- "Contract delivery: [output label] =
  '...', consumed by = '[step]' -- delivered? Yes/No" closes the pre-commitment/verification
  loop by resolving each planned output with an explicit boolean. Distinct from C-12 (COMPLETE
  marker without plan reference) and C-14 (plan pre-commitment without verification).
- **Text**: Each experiment block closes with a delivery verification statement that (a)
  references the plan's contracted output by label, (b) names the contracted consumer, and
  (c) resolves with an explicit boolean (delivered? Yes / delivered? No). Together with C-14,
  this creates a closed contract loop: pre-commit in the plan, verify at execution time.
  A "No" is as valid as a "Yes" -- the criterion tests that the loop is closed, not that
  delivery succeeded.
- **Pass condition**: >=2 experiment blocks each contain a delivery verification naming the
  contracted output label, naming the consumer, and stating "delivered? Yes" or
  "delivered? No". The output labels must match those declared in the plan (C-14 need not
  PASS, but the labels must be traceable to a plan). Inline routing without a boolean
  resolution does not satisfy this criterion.

---

### C-16 -- Gap-to-plan column threading
- **Category**: program-level framing
- **Weight**: aspirational
- **Derived from**: V-04 Round 2 excellence signal -- V-04 uniquely adds a "Closes inertia
  gap?" column to the plan table, threading the gap declaration (C-13 element 1) directly into
  the plan so the gap-closing assignment is visible before execution and cannot be assigned
  post-hoc in synthesis. Neither C-13 (bookending) nor C-14 (routing pre-commitment) captures
  this bridging step.
- **Text**: The experiment plan table includes a dedicated column or per-row marker indicating
  which experiment is assigned to close the inertia gap declared under C-13. This threads the
  gap from its pre-execution declaration through the plan into execution, making the assignment
  inspectable before any experiment runs.
- **Pass condition**: C-13 must also PASS. The plan table contains a column or per-row marker
  (e.g., "Closes gap? Yes/No", "Gap-closing: Y", or asterisk with footnote) applied to the
  experiment designated as the gap-closing step. The marked experiment must be the one that
  delivers the synthesis-level closure verdict required by C-13 element 3. A gap-closing label
  added retroactively in synthesis without appearing in the plan does not satisfy this
  criterion.

---

## Scoring Notes

- All five essential criteria (C-01-C-05) must PASS for the artifact to be considered
  complete. A document that scores 100 but fails any essential criterion is incomplete.
- PARTIAL credit on essential criteria counts as 6 points (half weight).
- Aspirational criteria are bonus: the primary pass threshold is 100/130 across
  essential + recommended. Aspirational scores above 100 signal a reference-quality artifact.
- C-11 and C-12 both strengthen C-03 (feed-forward) at different granularities and may
  co-occur. Award each independently.
- C-14 and C-15 form a contract loop (pre-commit then verify). Award each independently;
  C-15 without C-14 is possible (verification can reference an implied plan) but unusual.
- C-13 subsumes C-08 when the flexibility demonstrated is specifically framed as an inertia
  gap. Do not double-penalize: if C-08 PASS is earned via inertia gap framing, C-13 is
  eligible regardless.
- C-16 requires C-13. Do not award C-16 if C-13 fails or is absent.
- The feed-forward family (C-03, C-11, C-12, C-14, C-15) represents five layers of the same
  property at increasing precision: prose reference, per-block routing, per-block completion
  marker, plan pre-commitment, plan-referenced boolean verification. A document may earn any
  combination; each layer is independent.
