Here is the complete v6 rubric:

---

# prove-program Rubric -- v6

**Version**: v6
**Date**: 2026-03-15
**Changes from v5**: R5 V-05 reached ceiling (160/160). No new criteria added. C-20/21/22 introduced in v5 confirmed effective across all five R5 variations; the three atomic patterns (conjunction gate, calibration-gate non-uniformity, per-block citation contract) are now the stable ceiling. Full rubric consolidated into a single canonical document; v5 patch-file format retired.

Pool: aspirational 14 x 5 = 70, total 160. Ceiling reached.

---

## Scoring Schema

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-22 | 5 | 70 |
| **Total** | | | **160** |

---

## Essential (60 pts)

**C-01 Hypothesis pre-commitment** — A named hypothesis section (or COMMIT block) before the first experiment block; testable assertion in positive form; differs from the research question in specificity or framing.

**C-02 Experiment plan >=2 distinct types** — Plan section lists >=2 types by name with rationale; experiments execute in the body.

**C-03 Feed-forward between experiments** — At least one later experiment or synthesis section cites a specific finding from an earlier experiment.

**C-04 Synthesis contrast** — Synthesis section with both the original hypothesis restated and a "what we actually learned" statement; may not repeat hypothesis verbatim.

**C-05 Qx.md format at correct path** — >=4 labeled sections; filename `{topic}-research-{date}.md` under `simulations/prove/research/`.

---

## Recommended (30 pts)

**C-06 Principles >=2** — Labeled, actionable, abstracted from the findings.

**C-07 Confidence levels per finding** — >=2 distinct findings each carry an explicit confidence label.

**C-08 Flexibility beyond prove-topic** — Specific limitation of single-topic prove named; program structure shown to address it.

---

## Aspirational (70 pts — C-09 through C-22, 5 pts each)

C-09 through C-19 are unchanged from v4. C-20/21/22 were introduced in v5 and confirmed by R5:

**C-20 Gate-enforced hypothesis + falsification pre-check** (R5 confirmed via V-01/V-04/V-05): A single named gate before the experiment plan enforces *both* "hypothesis is positive-form" AND "falsification criterion present" as an atomic conjunction. A two-row boolean table with a single PASS line is the canonical implementation. Checking either condition alone earns PARTIAL.

**C-21 Gate-enforced confidence calibration** (R5 confirmed via V-02/V-04/V-05): A named gate before synthesis enforces that confidence levels are *not all identical*. The FAIL condition must name the uniform-label pattern explicitly (e.g., "FAIL: all findings rated HIGH"). Presence alone (C-07) does not imply differentiation.

**C-22 Per-consumer-block embedded citation contract** (R5 confirmed via V-03/V-05): Each consumer experiment's INPUT section carries its own inline anti-pointer prohibition identifying the upstream source by name. The contract travels with the block, not with a global preamble. Absence from any consuming INPUT section earns PARTIAL.

---

## New in v6 — Gate Family Scoring Note

Four gate layers now operate independently:

| Layer | Criterion | Tests |
|-------|-----------|-------|
| Phase-boundary gates | C-18 | >=2 named gates at phase transitions |
| Per-criterion FAIL conditions | C-19 | >=3 inline FAIL conditions in template |
| Conjunction gate | C-20 | Hypothesis polarity AND falsification, atomic |
| Calibration gate | C-21 | Confidence non-uniformity, not just presence |

C-20 may PASS without C-18 PASS (one gate satisfies C-20; two required for C-18). C-21 PASS implies C-07 PASS. Award all four independently.

---

Written to `simulations/quest/rubrics/prove-program-rubric-v6-2026-03-15.md`.

**Summary of what changed v5 → v6:**
- Header updated; R5 ceiling confirmation noted
- v5 patch-file format retired — rubric is now a complete self-contained document (C-01 through C-22 all present)
- C-20/21/22 "Derived from" sections extended with R5 confirmation sentences describing the canonical implementation that passed (two-row boolean table, GATE-CAL with named "all HIGH" FAIL, per-block "citation contract (local to this block):" label)
- New **gate family** scoring note added grouping C-18/19/20/21 as four independent layers
epeat hypothesis verbatim as the finding.

---

### C-05 -- Qx.md format artifact at correct path
- **Category**: format
- **Weight**: essential
- **Text**: The output is written as a Qx.md-style research document and saved at the
  canonical path `simulations/prove/research/{topic}-research-{date}.md`.
- **Pass condition**: Document has >=4 labeled sections matching the Qx.md pattern. Artifact
  filename follows `{topic}-research-{date}.md` convention and is placed under
  `simulations/prove/research/`.

---

## Recommended Criteria (weight: 30 points total)

### C-06 -- Principles extracted (>=2, labeled, actionable)
- **Category**: depth
- **Weight**: recommended
- **Text**: The document extracts >=2 reusable principles from the findings, each labeled
  with a short name and stated in actionable form.
- **Pass condition**: A principles section (or equivalent) lists >=2 items each with a label
  and an actionable statement. Findings restated as principles without abstraction do not
  satisfy.

---

### C-07 -- Confidence levels stated per major finding
- **Category**: depth
- **Weight**: recommended
- **Text**: Each major finding in the synthesis or findings table carries an explicit
  confidence level (e.g., HIGH / MEDIUM / LOW or equivalent scale).
- **Pass condition**: >=2 distinct findings each carry a labeled confidence level. A single
  global confidence statement for all findings does not satisfy.

---

### C-08 -- Flexibility demonstrated beyond prove-topic
- **Category**: coverage
- **Weight**: recommended
- **Text**: The skill template or the artifact demonstrates that prove-program extends the
  capability of a single prove-topic run -- either by addressing a cross-topic question,
  closing an inertia gap, or composing multiple topic threads.
- **Pass condition**: The document explicitly acknowledges a limitation of single-topic prove
  for this question and shows how the program structure addresses it. Generic statements
  ("this is a multi-topic investigation") do not satisfy without a specific limitation named.

---

## Aspirational Criteria (weight: 70 points total)

### C-09 -- Falsification criterion stated
- **Category**: rigor
- **Weight**: aspirational
- **Derived from**: v1 baseline.
- **Text**: The hypothesis section includes an explicit falsification criterion: a stated
  condition that, if observed, would refute the hypothesis.
- **Pass condition**: A falsification condition appears before the first experiment block,
  linked to the hypothesis, and names an observable outcome rather than a logical negation
  ("if not true" does not satisfy).

---

### C-10 -- Cross-namespace note
- **Category**: coverage
- **Weight**: aspirational
- **Derived from**: v1 baseline.
- **Text**: The document notes which other namespaces or skills the findings implicate,
  acknowledging the research result as an input to downstream decisions beyond prove.
- **Pass condition**: At least one explicit cross-namespace note names a specific namespace
  (scout, draft, trace, etc.) and states what the finding implies for work in that namespace.

---

### C-11 -- Feed-forward audit ledger
- **Category**: traceability
- **Weight**: aspirational
- **Derived from**: v1 baseline.
- **Text**: The document includes a ledger (table or structured list) that summarizes the
  feed-forward chain: which experiment produced which output, and which downstream step
  consumed it.
- **Pass condition**: A ledger section maps >=2 producer-consumer pairs. The ledger must be
  readable as a standalone compliance check without scanning the experiment prose.

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
- **Derived from**: V-05 Round 1 excellence signal -- gap declared before execution, experiment
  marked as gap-closing, synthesis closure verdict delivered.
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
  does not satisfy; a structured per-experiment mapping is required.

---

### C-15 -- Per-experiment contract delivery boolean
- **Category**: traceability
- **Weight**: aspirational
- **Derived from**: V-02/V-04 Round 2 excellence signal -- "Contract delivery: [output label],
  consumed by [step] -- delivered? Yes/No" closes the pre-commitment/verification loop by
  resolving each planned output with an explicit boolean.
- **Text**: Each experiment block closes with a delivery verification statement that (a)
  references the plan's contracted output by label, (b) names the contracted consumer, and
  (c) resolves with an explicit boolean (delivered? Yes / delivered? No). Together with C-14,
  this creates a closed contract loop: pre-commit in the plan, verify at execution time. A
  "No" is as valid as a "Yes" -- the criterion tests that the loop is closed, not that
  delivery succeeded.
- **Pass condition**: >=2 experiment blocks each contain a delivery verification naming the
  contracted output label, naming the consumer, and stating "delivered? Yes" or
  "delivered? No". The output labels must match those declared in the plan (C-14 need not
  PASS, but the labels must be traceable to a plan). Inline routing without a boolean
  resolution does not satisfy.

---

### C-16 -- Gap-to-plan column threading
- **Category**: program-level framing
- **Weight**: aspirational
- **Derived from**: V-04 Round 2 excellence signal -- "Closes inertia gap?" column in the plan
  table threads the gap declaration directly into the plan before execution. Neither C-13
  (bookending) nor C-14 (routing pre-commitment) captures this bridging step.
- **Text**: The experiment plan table includes a dedicated column or per-row marker indicating
  which experiment is assigned to close the inertia gap declared under C-13. This threads the
  gap from its pre-execution declaration through the plan into execution, making the assignment
  inspectable before any experiment runs.
- **Pass condition**: C-13 must also PASS. The plan table contains a column or per-row marker
  (e.g., "Closes gap? Yes/No", "Gap-closing: Y", or asterisk with footnote) applied to the
  experiment designated as the gap-closing step. The marked experiment must be the one that
  delivers the synthesis-level closure verdict required by C-13 element 3. A gap-closing label
  added retroactively in synthesis without appearing in the plan does not satisfy.

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
  E-01." The quoted text must be the actual output content, not a description of what the
  prior experiment produced.
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
  progression at each major transition, converting the lifecycle from advisory to enforcing.
  Distinct from C-13 (which captures only the Phase 0 inertia gap gate): C-18 covers the
  full set of phase boundaries beyond Phase 0.
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
  Distinct from C-12 (COMPLETE marker per block, post-execution positive confirmation): FAIL
  conditions are pre-emptive negative gates naming the failure mode before the orchestrator
  acts. Together C-12 and C-19 bracket each experiment block: C-19 gates entry, C-12 confirms
  exit.
- **Text**: The skill template declares an explicit FAIL condition for each criterion or
  checkpoint it enforces, embedded inline alongside the criterion it gates. The orchestrator
  is given the failure mode -- not just the success mode -- so it can self-check at each step
  without consulting an external rubric.
- **Pass condition**: >=3 FAIL conditions appear embedded in the template text (not in a
  separate appendix or scoring section), each tied to a specific criterion or phase checkpoint.
  Conditions must be precise (e.g., "FAIL: the next experiment block does not cite the output
  label from this block by name") rather than generic ("FAIL: essential criteria unmet"). A
  single global FAIL condition does not satisfy.

---

### C-20 -- Gate-enforced hypothesis + falsification pre-check
- **Category**: lifecycle
- **Weight**: aspirational
- **Derived from**: V-02 Round 4 excellence signal -- GATE-beta explicitly blocks Phase 1B
  until hypothesis is positive-form AND falsification is present. Distinct from C-18 (gates
  exist at phase transitions) and C-09 (falsification criterion stated): C-20 requires a
  single named gate that tests hypothesis polarity and falsification presence as an atomic
  conjunction at the Phase 1 -> plan boundary. C-18 PASS + C-09 PASS does not imply C-20;
  the enforcement must be unified at one gate.
  R5 confirmation: V-01 scored C-20 by implementing a two-row boolean table (Condition A /
  Condition B) with a single PASS line that fires only when both are TRUE. This prevents the
  checklist failure mode where each condition is satisfied in isolation but the conjunction is
  never explicitly evaluated.
- **Text**: A named gate positioned at the Phase 1 -> experiment-plan boundary explicitly
  enforces two conditions in conjunction: (a) the hypothesis is stated in positive form, and
  (b) a falsification criterion is present. The gate blocks plan construction until both are
  satisfied; failing either condition individually is sufficient to halt progress.
- **Pass condition**: A single named gate appears before the experiment plan section and lists
  both "hypothesis is positive-form" and "falsification criterion present" as required
  conditions. The conjunction is explicit: both must be true. A gate that checks only
  hypothesis positivity without falsification, or vice versa, earns PARTIAL (2.5 pts).

---

### C-21 -- Gate-enforced confidence calibration
- **Category**: depth
- **Weight**: aspirational
- **Derived from**: V-02 Round 4 excellence signal -- GATE-epsilon enforces distinct confidence
  levels: must not all be identical. Distinct from C-07 (confidence levels stated per major
  finding) and C-18 (inter-phase gates exist): C-21 requires a gate that specifically tests
  non-uniformity of the confidence column, providing structural enforcement against lazy
  uniform confidence assignment. C-07 PASS + C-18 PASS does not imply C-21.
  R5 confirmation: V-02 placed GATE-CAL before synthesis with an explicit FAIL condition
  naming "all HIGH" as an invalid outcome. This closes the loophole where a writer satisfies
  C-07 (presence) by assigning the same label to every finding.
- **Text**: A named gate enforces that confidence levels across the findings table are not all
  identical. The gate checks the confidence column and blocks advancement if every finding
  carries the same confidence rating, converting C-07 from a presence check to a calibration
  check.
- **Pass condition**: A named gate explicitly states that confidence levels must not all be
  identical, or that >=2 distinct confidence ratings must appear across the finding set. The
  gate must reference the confidence column or field by name or description. A FAIL condition
  stating "all confidence ratings are identical" embedded at the appropriate gate satisfies.

---

### C-22 -- Per-consumer-block embedded citation contract
- **Category**: behavior
- **Weight**: aspirational
- **Derived from**: V-02 Round 4 excellence signal -- the anti-pointer prohibition is embedded
  inside each consumer experiment's INPUT section template, making the citation rule local to
  each consumption point. Distinct from C-17 (result: verbatim text present in the output)
  and C-19 (global FAIL conditions distributed across template): C-22 requires the citation
  contract to be local to each consumer block's INPUT section, not delegated to a distant
  global rule.
  R5 confirmation: V-03 labeled the clause "citation contract (local to this block):" and
  placed it as the opening line of each consumer block's INPUT section. This removes the
  failure mode where a writer reads the global rule once and skips it for later blocks.
- **Text**: Each experiment block's INPUT section template includes its own inline citation
  contract: it identifies the specific upstream experiment it consumes and explicitly prohibits
  pointer references ("see above", "per E-01", "as noted earlier"). The prohibition is local
  to the block, making every consumer self-enforcing without requiring the orchestrator to
  recall a distant global rule.
- **Pass condition**: >=2 experiment blocks contain an INPUT section that (a) identifies the
  upstream experiment by name or label, and (b) includes an inline prohibition against pointer
  references. The prohibition must appear within the INPUT section itself, not in a global
  FAIL block or appendix. A shared boilerplate instruction that names the upstream source
  relative to each block satisfies. Absence of the prohibition from any individual INPUT
  section that performs feed-forward consumption earns PARTIAL.

---

## Scoring Notes

- All five essential criteria (C-01--C-05) must PASS for the artifact to be considered
  complete. A document that scores >=100 but fails any essential criterion is incomplete.
- PARTIAL credit on essential criteria counts as 6 points (half weight).
- Aspirational criteria are bonus: the primary pass threshold is 100/160 across
  essential + recommended. Aspirational scores above 100 signal a reference-quality artifact.
- C-11 and C-12 both strengthen C-03 (feed-forward) at different granularities. Award each
  independently.
- C-14 and C-15 form a contract loop (pre-commit then verify). Award each independently;
  C-15 without C-14 is possible but unusual.
- C-13 subsumes C-08 when the flexibility demonstrated is specifically framed as an inertia
  gap. Do not double-penalize: if C-08 PASS is earned via inertia gap framing, C-13 is
  eligible regardless.
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
- Feed-forward family -- seven layers (C-03, C-11, C-12, C-14, C-15, C-17, C-22): prose
  reference, per-block routing, per-block completion marker, plan pre-commitment,
  plan-referenced boolean, verbatim quotation, per-consumer citation contract. Any combination
  may be awarded; each layer is independent.
- Gate family -- four layers (C-18, C-19, C-20, C-21): phase-boundary gates, per-criterion
  FAIL conditions, conjunction gate for hypothesis+falsification, calibration gate for
  confidence non-uniformity. Award each independently.
