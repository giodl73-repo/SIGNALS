**v5 written.** Three new criteria extracted from R4:

| # | Name | Source signal | Why distinct from existing |
|---|------|--------------|----------------------------|
| C-20 | Gate-enforced hypothesis + falsification pre-check | V-02 GATE-beta | C-18 requires gates exist; C-09 requires falsification stated. C-20 requires a single gate that enforces both as an atomic conjunction at the Phase 1 -> plan boundary. Neither C-18+C-09 separately nor together implies C-20. |
| C-21 | Gate-enforced confidence calibration | V-02 GATE-epsilon | C-07 requires confidence levels present; C-18 requires gates exist. C-21 requires a gate that specifically enforces non-uniformity of the confidence column — presence is insufficient, differentiation is required. |
| C-22 | Per-consumer-block embedded citation contract | V-02 C-03 evidence ("E-02 input says cite...not a pointer") | C-17 tests the result (verbatim text in output); C-19 tests global FAIL conditions. C-22 tests that the anti-pointer prohibition is embedded locally inside each consumer block's INPUT section, not delegated to a distant global rule. |

Pool changes: aspirational 55 → 70 (14 × 5), total 145 → 160.
ositive form, and differs from the research question in specificity or framing.

---

### C-02 -- Experiment plan with >=2 distinct types
- **Category**: coverage
- **Weight**: essential
- **Text**: The orchestrator produces an explicit experiment plan that selects at least two distinct experiment types (e.g., websearch, intelligence, analysis, interview, prototype, or custom) and explains the rationale for the chosen combination.
- **Pass condition**: A plan section lists >=2 experiment types by name, states why each was chosen for this research question, and the experiments actually execute in the body of the document.

---

### C-03 -- Feed-forward between experiments
- **Category**: behavior
- **Weight**: essential
- **Text**: Each experiment's outputs are consumed by subsequent steps. Later experiments or the synthesis explicitly reference findings from earlier experiments rather than treating each as independent.
- **Pass condition**: At least one instance of explicit forward-feeding: a later experiment or the synthesis section cites or incorporates a finding from an earlier experiment by name or content.

---

### C-04 -- Synthesis with "what we thought vs. what we actually learned"
- **Category**: correctness
- **Weight**: essential
- **Text**: The document contains a synthesis section that answers the original research question and contrasts the pre-investigation hypothesis against the post-investigation finding.
- **Pass condition**: Synthesis section present, contains both a restatement of the original hypothesis and a "what we actually learned" statement that either confirms, refines, or refutes it. May not simply repeat hypothesis verbatim as the finding.

---

### C-05 -- Qx.md format artifact at correct path
- **Category**: format
- **Weight**: essential
- **Text**: The output is written as a Qx.md-style research document and saved at the canonical path `simulations/prove/research/{topic}-research-{date}.md`.
- **Pass condition**: Document has >=4 labeled sections matching the Qx.md pattern. Artifact filename follows `{topic}-research-{date}.md` convention and is placed under `simulations/prove/research/`.

---

## Recommended Criteria (weight: 30 points total)

### C-06 -- Principles extracted (>=2, labeled, actionable)
- **Category**: depth / **Weight**: recommended

### C-07 -- Confidence levels stated per major finding
- **Category**: depth / **Weight**: recommended

### C-08 -- Flexibility demonstrated beyond prove-topic
- **Category**: coverage / **Weight**: recommended

---

## Aspirational Criteria (weight: 70 points total)

*C-09 through C-16 unchanged from v3.*

### C-09 -- Falsification criterion stated
- **Category**: rigor / **Weight**: aspirational

### C-10 -- Cross-namespace note
- **Category**: coverage / **Weight**: aspirational

### C-11 -- Feed-forward audit ledger
- **Category**: traceability / **Weight**: aspirational

### C-12 -- Per-experiment COMPLETE markers with consumed-by routing
- **Category**: traceability
- **Weight**: aspirational
- **Derived from**: V-03 Round 1 excellence signal -- per-experiment COMPLETE + consumed-by
  routing is the most granular feed-forward enforcement.
- **Text**: Each experiment block terminates with an explicit COMPLETE record that states (a)
  what output the experiment produced and (b) which downstream step receives that output.
- **Pass condition**: >=2 experiment blocks each contain a COMPLETE record with both an output
  statement and an explicit "Consumed by: [step name or synthesis]" routing. The routings
  must be specific (not "see synthesis") and must match the actual flow of the document.

---

### C-13 -- Inertia gap bookending
- **Category**: program-level framing
- **Weight**: aspirational
- **Derived from**: V-05 Round 1 excellence signal -- gap declared before execution, experiment
  marked as gap-closing, synthesis closure verdict delivered.
- **Text**: The research program explicitly names the inertia gap before any experiment runs,
  marks the experiment designed to close it, and delivers an explicit closure verdict in the
  synthesis.
- **Pass condition**: Three elements all present: (1) gap declaration before the first
  experiment naming the limitation of single-topic prove; (2) an experiment marked as the
  gap-closing step with rationale; (3) a synthesis-level closure verdict stating whether the
  gap was closed and on what evidence.

---

### C-14 -- Plan-level output routing pre-commitment
- **Category**: verifiability
- **Weight**: aspirational
- **Derived from**: V-02/V-04 Round 2 excellence signal -- plan table with Output label and
  Consumed by columns pre-commits routing before execution begins.
- **Text**: The experiment plan table includes dedicated columns for the expected output label
  and downstream consumer for each planned experiment.
- **Pass condition**: The plan section uses a table or structured list with >=2 experiment
  rows, each specifying both an output label and a named consumer. Output labels must
  correspond to labels used in the experiment blocks and synthesis.

---

### C-15 -- Per-experiment contract delivery boolean
- **Category**: traceability
- **Weight**: aspirational
- **Derived from**: V-02/V-04 Round 2 excellence signal -- "Contract delivery: [output label],
  consumed by [step] -- delivered? Yes/No".
- **Text**: Each experiment block closes with a delivery verification statement that references
  the plan's contracted output by label, names the contracted consumer, and resolves with an
  explicit boolean (delivered? Yes / delivered? No).
- **Pass condition**: >=2 experiment blocks each contain a delivery verification naming the
  contracted output label, naming the consumer, and stating "delivered? Yes" or
  "delivered? No". Output labels must match those declared in the plan.

---

### C-16 -- Gap-to-plan column threading
- **Category**: program-level framing
- **Weight**: aspirational
- **Derived from**: V-04 Round 2 excellence signal -- "Closes inertia gap?" column in the plan
  table threads the gap declaration directly into the plan before execution.
- **Text**: The experiment plan table includes a dedicated column or per-row marker indicating
  which experiment is assigned to close the inertia gap declared under C-13.
- **Pass condition**: C-13 must also PASS. The plan table contains a column or per-row marker
  applied to the experiment designated as the gap-closing step. A gap-closing label added
  retroactively in synthesis without appearing in the plan does not satisfy.

---

### C-17 -- Verbatim feed-forward quotation
- **Category**: behavior
- **Weight**: aspirational
- **Derived from**: V-01 Round 3 excellence signal -- "Input: quote the specific output content
  from the previous block -- not 'see above.'"
- **Text**: Each experiment block's Input section reproduces the exact text of the upstream
  output it consumes -- not a paraphrase, summary, or pointer such as "see above" or "per E-01."
- **Pass condition**: >=2 experiment blocks contain an Input section with a directly quoted or
  blockquoted extract from a prior block. Paraphrase of the form "Based on E-01's finding
  that..." does not satisfy; pointer-only references ("see E-01", "per above") fail. If verbatim
  is impractical due to length, a clearly marked excerpt with ellipsis notation passes.

---

### C-18 -- Inter-phase GATE enforcement
- **Category**: lifecycle
- **Weight**: aspirational
- **Derived from**: V-01 Round 3 excellence signal -- named GATE tokens block each major phase
  transition, converting the lifecycle from advisory to enforcing.
- **Text**: The skill template includes named GATE or equivalent checkpoint tokens at each
  major phase transition beyond Phase 0, blocking forward progress until stated conditions
  are cleared.
- **Pass condition**: >=2 phase transitions carry explicit GATE, STOP, or equivalent named
  blockers. Each gate names the condition to clear before advancing. The Phase 0 inertia gap
  gate (C-13) does not count. Gates must be positional (before the phase they block) and
  conditional (state what must be true to proceed).

---

### C-19 -- Per-criterion FAIL conditions in template
- **Category**: verifiability
- **Weight**: aspirational
- **Derived from**: V-03 Round 3 excellence signal -- every enforced criterion carries an
  inline FAIL condition in the template text itself.
- **Text**: The skill template declares an explicit FAIL condition for each criterion or
  checkpoint it enforces, embedded inline alongside the criterion it gates.
- **Pass condition**: >=3 FAIL conditions appear embedded in the template text (not in a
  separate appendix), each tied to a specific criterion or phase checkpoint. Conditions must
  be precise, not generic. A single global FAIL condition does not satisfy.

---

### C-20 -- Gate-enforced hypothesis + falsification pre-check (NEW v5)
- **Category**: lifecycle
- **Weight**: aspirational
- **Derived from**: V-02 Round 4 excellence signal -- GATE-beta "explicitly blocks Phase 1B
  until hypothesis is positive-form AND falsification present." Distinct from C-18 (gates
  exist at phase transitions) and C-09 (falsification criterion stated): C-20 requires a
  single named gate that tests hypothesis polarity and falsification presence as an atomic
  conjunction at the Phase 1 -> plan boundary. C-18 PASS + C-09 PASS does not imply C-20;
  the enforcement must be unified at one gate.
- **Text**: A named gate positioned at the Phase 1 -> experiment-plan boundary explicitly
  enforces two conditions in conjunction: (a) the hypothesis is stated in positive form, and
  (b) a falsification criterion is present. The gate blocks plan construction until both are
  satisfied; failing either condition individually is sufficient to halt progress.
- **Pass condition**: A single named gate appears before the experiment plan section and lists
  both "hypothesis is positive-form" and "falsification criterion present" as required
  conditions. The conjunction is explicit: both must be true. A gate that checks only
  hypothesis positivity without falsification, or vice versa, earns PARTIAL (2.5 pts).

---

### C-21 -- Gate-enforced confidence calibration (NEW v5)
- **Category**: depth
- **Weight**: aspirational
- **Derived from**: V-02 Round 4 excellence signal -- GATE-epsilon "enforces distinct
  confidence levels -- must not all be identical." Distinct from C-07 (confidence levels
  stated per major finding) and C-18 (inter-phase gates exist): C-21 requires a gate that
  specifically tests non-uniformity of the confidence column, providing structural enforcement
  against lazy uniform confidence assignment. C-07 PASS + C-18 PASS does not imply C-21.
- **Text**: A named gate enforces that confidence levels across the findings table are not all
  identical. The gate checks the confidence column and blocks advancement if every finding
  carries the same confidence rating, converting C-07 from a presence check to a calibration
  check.
- **Pass condition**: A named gate explicitly states that confidence levels must not all be
  identical, or that >=2 distinct confidence ratings must appear across the finding set. The
  gate must reference the confidence column or field by name or description. A FAIL condition
  stating "all confidence ratings are identical" embedded at the appropriate gate satisfies
  this criterion.

---

### C-22 -- Per-consumer-block embedded citation contract (NEW v5)
- **Category**: behavior
- **Weight**: aspirational
- **Derived from**: V-02 Round 4 excellence signal -- C-03 evidence shows "E-02 input says
  'cite the specific finding content from E-01, not a pointer such as see above or per E-01.'"
  The anti-pointer prohibition is embedded inside the consumer experiment's INPUT section
  template, making the citation rule local to each consumption point. Distinct from C-17
  (result: verbatim text present in the output) and C-19 (global FAIL conditions distributed
  across template): C-22 requires the citation contract to be local to each consumer block's
  INPUT section, not delegated to a distant global rule.
- **Text**: Each experiment block's INPUT section template includes its own inline citation
  contract: it identifies the specific upstream experiment it consumes and explicitly prohibits
  pointer references ("see above", "per E-01", "as noted earlier"). The prohibition is local
  to the block. This makes every consumer self-enforcing without requiring the orchestrator
  to recall a distant global rule.
- **Pass condition**: >=2 experiment blocks contain an INPUT section that (a) identifies the
  upstream experiment by name or label, and (b) includes an inline prohibition against pointer
  references. The prohibition must appear within the INPUT section itself, not in a global
  FAIL block or appendix. A shared boilerplate instruction that names the upstream source
  relative to each block (e.g., "cite the output of the preceding experiment, not 'see
  above'") satisfies. Absence of the prohibition from any individual INPUT section that
  performs feed-forward consumption earns PARTIAL.

---

## Scoring Notes

- All five essential criteria (C-01--C-05) must PASS for the artifact to be considered
  complete. A document that scores >=100 but fails any essential criterion is incomplete.
- PARTIAL credit on essential criteria counts as 6 points (half weight).
- Aspirational criteria are bonus: the primary pass threshold is 100/160 across
  essential + recommended. Aspirational scores above 100 signal a reference-quality artifact.
- C-11 and C-12 both strengthen C-03 (feed-forward) at different granularities. Award each
  independently.
- C-14 and C-15 form a contract loop (pre-commit then verify). Award each independently.
- C-13 subsumes C-08 when the flexibility demonstrated is specifically framed as an inertia
  gap. Do not double-penalize.
- C-16 requires C-13. Do not award C-16 if C-13 fails or is absent.
- C-17 strengthens C-03: C-17 PASS automatically satisfies C-03. Award both independently.
- C-18 subsumes the Phase 0 gate mechanism of C-13 structurally but not in content. Both
  may PASS independently.
- C-19 and C-12 bracket each experiment block: C-19 gates entry, C-12 confirms exit. Award
  each independently.
- C-20 requires C-18 context (gates exist) but is not implied by it. C-20 may PASS
  independently of C-18; a single gate covering the hypothesis+falsification conjunction
  counts for C-20 but does not satisfy C-18's >=2-gate requirement.
- C-21 requires C-07 context (confidence levels present) but is not implied by it. In
  practice, C-21 PASS implies C-07 PASS because the gate enforces presence as well as
  non-uniformity.
- C-22 strengthens C-17 from the consumer side: C-17 tests the result (exact text present),
  C-22 tests the template instruction (local prohibition embedded). Both may PASS
  independently. C-22 PASS without C-17 PASS indicates the contract is declared but not
  followed.
- Feed-forward family now seven layers (C-03, C-11, C-12, C-14, C-15, C-17, C-22): prose
  reference, per-block routing, per-block completion marker, plan pre-commitment,
  plan-referenced boolean, verbatim quotation, per-consumer citation contract. Any combination
  may be awarded; each layer is independent.
