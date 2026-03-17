Here is the complete updated rubric:

---

# prove-program Rubric -- v4

**Version**: v4
**Date**: 2026-03-15
**Changes from v3**: Added C-17, C-18, C-19 from R3 excellence signals. Aspirational pool 40 -> 55 (11 criteria x 5 pts). Total pool 130 -> 145.

---

## Scoring Schema

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01 - C-05 | 12 | 60 |
| Recommended | C-06 - C-08 | 10 | 30 |
| Aspirational | C-09 - C-19 | 5 | 55 |
| **Total** | | | **145** |

**Pass threshold**: 100. PASS/PARTIAL/FAIL -> full/half/zero credit.
All five essential criteria must PASS; a document that scores >=100 but fails any essential criterion is incomplete regardless of total score.

---

## Essential Criteria (weight: 60 points total)

### C-01 -- Hypothesis pre-commitment
- **Category**: rigor
- **Weight**: essential
- **Text**: The orchestrator produces a dedicated hypothesis section (or equivalent) that appears before any experiment section, states a specific belief in positive form, and is not merely a restatement of the research question.
- **Pass condition**: A named hypothesis section (or COMMIT block) exists before the first experiment block, contains a testable assertion in positive form, and differs from the research question in specificity or framing.

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

## Aspirational Criteria (weight: 55 points total)

*C-09 through C-16 unchanged from v3.*

### C-17 -- Verbatim feed-forward quotation
- **Category**: behavior
- **Weight**: aspirational
- **Derived from**: V-01 Round 3 excellence signal -- "Input: quote the specific output content from the previous block -- not 'see above.'"
- **Text**: Each experiment block's Input section reproduces the exact text of the upstream output it consumes -- not a paraphrase, summary, or pointer such as "see above" or "per E-01."
- **Pass condition**: >=2 experiment blocks contain an Input section with a directly quoted or blockquoted extract from a prior block. Paraphrase of the form "Based on E-01's finding that..." does not satisfy; pointer-only references ("see E-01") fail.

---

### C-18 -- Inter-phase GATE enforcement
- **Category**: lifecycle
- **Weight**: aspirational
- **Derived from**: V-01 Round 3 excellence signal -- explicit GATE tokens block each major phase transition beyond Phase 0. Distinct from C-13 (inertia gap gate only).
- **Text**: The skill template includes named GATE or equivalent checkpoint tokens at each major phase transition beyond Phase 0, blocking forward progress until stated conditions are cleared.
- **Pass condition**: >=2 phase transitions (e.g., Phase 1 -> 1B, Phase 1B -> 2, Phase 2 -> 3A) carry explicit named blockers. The Phase 0 inertia gap gate does not count. Gates must be positional and conditional.

---

### C-19 -- Per-criterion FAIL conditions in template
- **Category**: verifiability
- **Weight**: aspirational
- **Derived from**: V-03 Round 3 excellence signal -- every criterion carries an inline FAIL condition in the template text. Distinct from C-12 (post-execution COMPLETE marker): FAIL conditions gate entry; COMPLETE markers confirm exit.
- **Text**: The skill template declares an explicit FAIL condition for each criterion it enforces, embedded inline alongside the criterion it gates.
- **Pass condition**: >=3 FAIL conditions appear embedded in the template text (not in a separate appendix), each tied to a specific criterion or checkpoint. Conditions must be precise, not generic. A single global FAIL condition does not satisfy.

---

## New Scoring Notes (additions to v3)

- C-17 strengthens C-03: C-17 PASS automatically satisfies C-03. Award both independently.
- C-18 subsumes the Phase 0 gate mechanism of C-13 element 1 structurally but not in content. Both may PASS independently.
- C-19 and C-12 bracket each experiment block: C-19 gates entry, C-12 confirms exit. Award each independently.
- Feed-forward family now six layers (C-03, C-11, C-12, C-14, C-15, C-17): prose reference, per-block routing, per-block completion marker, plan pre-commitment, plan-referenced boolean, verbatim quotation. Any combination may be awarded; each layer is independent.

---

Written to `simulations/quest/rubrics/prove-program-rubric-v4-2026-03-15.md`.

**Three new criteria added:**

| # | Name | Source | Why distinct |
|---|------|---------|--------------|
| C-17 | Verbatim feed-forward quotation | V-01 R3 | C-03 allows paraphrase; C-17 requires exact text, prevents drift, makes C-11 auditable without re-reading prose |
| C-18 | Inter-phase GATE enforcement | V-01 R3 | C-13 captures Phase 0 gate only; C-18 requires >=2 additional phase-boundary gates converting lifecycle from advisory to enforcing |
| C-19 | Per-criterion FAIL conditions in template | V-03 R3 | C-12 is post-execution positive confirmation; C-19 is pre-execution negative gate — they bracket each block from opposite ends |
ompliance by reading the ledger alone without scanning the experiment
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

### C-17 -- Verbatim feed-forward quotation
- **Category**: behavior
- **Weight**: aspirational
- **Derived from**: V-01 Round 3 excellence signal -- "Input: quote the specific output
  content from the previous block -- not 'see above.'" Distinct from C-03 (which passes on
  reference by name or paraphrase): verbatim quotation anchors the feed-forward chain to exact
  evidence, prevents interpretive drift between blocks, and makes C-11 independently auditable
  without re-reading experiment prose.
- **Text**: Each experiment block's Input section reproduces the exact text of the upstream
  output it consumes -- not a paraphrase, summary, or pointer such as "see above" or "per
  E-01." The quoted text must be the actual output content, not a description of what E-01
  produced.
- **Pass condition**: >=2 experiment blocks contain an Input section with a directly quoted or
  blockquoted extract from a prior block. The extract must be recognizable as text from that
  block (not a rewrite). Paraphrase of the form "Based on E-01's finding that..." does not
  satisfy; pointer-only references ("see E-01", "per above") fail. If verbatim is impractical
  due to length, a clearly marked excerpt with ellipsis notation passes.

---

### C-18 -- Inter-phase GATE enforcement
- **Category**: lifecycle
- **Weight**: aspirational
- **Derived from**: V-01 Round 3 excellence signal -- explicit GATE tokens block phase
  progression at each major transition (Phase 1 -> 1B, Phase 1B -> 2, Phase 2 -> 3),
  converting the lifecycle from advisory to enforcing. Distinct from C-13 (which captures only
  the Phase 0 inertia gap gate): C-18 covers the full set of phase boundaries beyond Phase 0.
- **Text**: The skill template includes named GATE or equivalent checkpoint tokens at each
  major phase transition beyond Phase 0, blocking forward progress until stated conditions
  are cleared. This makes the lifecycle enforcing rather than advisory: the orchestrator
  cannot proceed to the next phase without explicitly satisfying the gate condition.
- **Pass condition**: >=2 phase transitions (e.g., Phase 1 -> 1B, Phase 1B -> 2, Phase 2 ->
  Phase 3A) carry explicit GATE, STOP, or equivalent named blockers. Each gate names the
  condition to clear before advancing. The Phase 0 inertia gap gate (C-13) does not count
  toward this total. Gates must be positional (appearing before the phase they block) and
  conditional (state what must be true to proceed, not just announce a phase boundary).

---

### C-19 -- Per-criterion FAIL conditions in template
- **Category**: verifiability
- **Weight**: aspirational
- **Derived from**: V-03 Round 3 excellence signal -- every enforced criterion carries an
  inline FAIL condition in the template text itself, making the rubric self-enforcing.
  Distinct from C-12 (COMPLETE marker per block, post-execution positive confirmation):
  FAIL conditions are pre-emptive negative gates naming the failure mode before the
  orchestrator acts. Together C-12 and C-19 bracket each experiment block: C-19 gates entry,
  C-12 confirms exit.
- **Text**: The skill template declares an explicit FAIL condition for each criterion or
  checkpoint it enforces, embedded inline alongside the criterion it gates. The orchestrator
  is given the failure mode -- not just the success mode -- so it can self-check at each step
  without consulting an external rubric.
- **Pass condition**: >=3 FAIL conditions appear embedded in the template text (not in a
  separate appendix or scoring section), each tied to a specific criterion or phase checkpoint.
  Conditions must be precise (e.g., "FAIL: the next experiment block does not cite the output
  label from this block by name") rather than generic ("FAIL: essential criteria unmet").
  A single global FAIL condition does not satisfy this criterion.

---

## Scoring Notes

- All five essential criteria (C-01--C-05) must PASS for the artifact to be considered
  complete. A document that scores >=100 but fails any essential criterion is incomplete.
- PARTIAL credit on essential criteria counts as 6 points (half weight).
- Aspirational criteria are bonus: the primary pass threshold is 100/145 across
  essential + recommended. Aspirational scores above 100 signal a reference-quality artifact.
- C-11 and C-12 both strengthen C-03 (feed-forward) at different granularities and may
  co-occur. Award each independently.
- C-14 and C-15 form a contract loop (pre-commit then verify). Award each independently;
  C-15 without C-14 is possible (verification can reference an implied plan) but unusual.
- C-13 subsumes C-08 when the flexibility demonstrated is specifically framed as an inertia
  gap. Do not double-penalize: if C-08 PASS is earned via inertia gap framing, C-13 is
  eligible regardless.
- C-16 requires C-13. Do not award C-16 if C-13 fails or is absent.
- C-17 strengthens C-03: a document with C-17 PASS automatically satisfies C-03. Award
  both independently.
- C-18 subsumes the Phase 0 gate mechanism of C-13 element 1 in terms of structure (GATE
  token) but not content (inertia gap declaration). Both may PASS independently; C-18 does
  not require C-13 to PASS.
- C-19 and C-12 bracket each experiment block: C-19 gates entry (FAIL conditions before
  execution), C-12 confirms exit (COMPLETE marker after execution). Award each independently.
- Feed-forward family (C-03, C-11, C-12, C-14, C-15, C-17): six layers of the same property
  at increasing precision -- prose reference, per-block routing, per-block completion marker,
  plan pre-commitment, plan-referenced boolean, verbatim quotation. Any combination may be
  awarded; each layer is independent.
