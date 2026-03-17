Looking at the scorecard, I'll extract the three distinct excellence patterns before adding them:

1. **V-02**: Feed-forward ledger table — a dedicated audit section mapping each planned experiment's output to its consumer, making the plan-to-execution contract verifiable by inspection rather than prose reading.

2. **V-03**: Per-experiment COMPLETE markers with explicit `→ Consumed by:` routing — the most granular feed-forward enforcement, making the chain traceable at the block level.

3. **V-05**: Inertia gap bookending — a full bookended contract: declare the gap before execution, mark the experiment that closes it, deliver a closure verdict in synthesis. Elevates the document from a research record to a gap-closure proof.

These are structurally distinct from each other and from C-09/C-10. Adding as C-11, C-12, C-13.

---

```markdown
# prove-program Rubric — v2
_Updated: 2026-03-15_
_Changelog: v1→v2 — Added C-11, C-12, C-13 from V-02/V-03/V-05 excellence signals._

## Overview

Rubric for the `prove-program` skill. Scores a Qx.md-style multi-experiment research document
produced by an orchestrated prove program. The rubric tests whether the artifact demonstrates
the four behaviors that distinguish prove-program from simpler prove skills: hypothesis-first
framing, multi-experiment orchestration, feed-forward between experiments, and synthesis that
contrasts pre- and post-investigation belief.

## Scoring Summary

| Tier | Criteria | Points each | Pool |
|------|----------|-------------|------|
| Essential | C-01 – C-05 | 12 | 60 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-13 | 5 | 25 |
| **Total** | | | **115** |

Baseline threshold: **100**. Aspirational criteria (C-09–C-13) represent the stretch ceiling
above 100; a document scoring ≥100 passes. All essential criteria must PASS for a document to
be considered complete regardless of total score.

---

## Essential Criteria (weight: 60 points total)

### C-01 — Hypothesis stated before any experiment
- **Category**: behavior
- **Weight**: essential
- **Text**: The document opens with a hypothesis — a clear claim about what the researcher
  believes is true — before any experiment is described or run.
- **Pass condition**: The document contains a named hypothesis section (or equivalent) that
  appears before any experiment section, states a specific belief in positive form, and is not
  merely a restatement of the research question.

---

### C-02 — Experiment plan with ≥2 distinct types
- **Category**: coverage
- **Weight**: essential
- **Text**: The orchestrator produces an explicit experiment plan that selects at least two
  distinct experiment types (e.g., websearch, intelligence, analysis, interview, prototype, or
  custom) and explains the rationale for the chosen combination.
- **Pass condition**: A plan section lists ≥2 experiment types by name, states why each was
  chosen for this research question, and the experiments actually execute in the body of the
  document.

---

### C-03 — Feed-forward between experiments
- **Category**: behavior
- **Weight**: essential
- **Text**: Each experiment's outputs are consumed by subsequent steps. Later experiments or
  the synthesis explicitly reference findings from earlier experiments rather than treating
  each as independent.
- **Pass condition**: At least one instance of explicit forward-feeding: a later experiment or
  the synthesis section cites or incorporates a finding from an earlier experiment by name or
  content.

---

### C-04 — Synthesis with "what we thought vs. what we actually learned"
- **Category**: correctness
- **Weight**: essential
- **Text**: The document contains a synthesis section that answers the original research
  question and contrasts the pre-investigation hypothesis against the post-investigation
  finding.
- **Pass condition**: Synthesis section present, contains both a restatement of the original
  hypothesis and a "what we actually learned" statement that either confirms, refines, or
  refutes it. May not simply repeat hypothesis verbatim as the finding.

---

### C-05 — Qx.md format artifact at correct path
- **Category**: format
- **Weight**: essential
- **Text**: The output is written as a Qx.md-style research document (structured with labeled
  sections: hypothesis, experiments, findings, synthesis, principles) and saved at the
  canonical path `simulations/prove/research/{topic}-research-{date}.md`.
- **Pass condition**: Document has ≥4 labeled sections matching the Qx.md pattern. Artifact
  filename follows `{topic}-research-{date}.md` convention and is placed under
  `simulations/prove/research/`.

---

## Recommended Criteria (weight: 30 points total)

### C-06 — Principles extracted (≥2, labeled, actionable)
- **Category**: depth
- **Weight**: recommended
- **Text**: The document closes with a principles section that extracts at least two reusable,
  actionable principles from the investigation's findings — not observations, but design rules
  or decision heuristics.
- **Pass condition**: Principles section present with ≥2 entries. Each entry is labeled (e.g.,
  "P-01") and states a rule in imperative or conditional form ("When X, do Y" or "Always Z").
  Generic truisms ("do good research") do not pass.

---

### C-07 — Confidence levels stated per major finding
- **Category**: depth
- **Weight**: recommended
- **Text**: Each major finding in the synthesis carries an explicit confidence level or evidence
  quality indicator (e.g., high/medium/low, or a brief qualifier such as "based on 3 sources"
  or "inconclusive").
- **Pass condition**: ≥2 findings in the synthesis or findings section are annotated with
  confidence level or evidence-quality qualifier. Unlabeled or uniform confidence across all
  findings does not pass.

---

### C-08 — Flexibility demonstrated beyond prove-topic
- **Category**: coverage
- **Weight**: recommended
- **Text**: The experiment sequence includes at least one experiment type or scope that would
  not be available in prove-topic (e.g., a cross-namespace lookup, a custom data analysis, a
  non-Signal research question, or a web search on an external domain).
- **Pass condition**: At least one experiment step either (a) queries data outside the current
  Signal topic context, (b) uses a custom experiment not in the standard prove skill set, or
  (c) spans multiple namespaces. The document or experiment log makes this flexibility visible.

---

## Aspirational Criteria (weight: 25 points total)

### C-09 — Falsification criteria stated in hypothesis
- **Category**: rigor
- **Weight**: aspirational
- **Text**: The hypothesis section states explicit falsification criteria: what evidence would
  cause the researcher to reject the hypothesis. This frames the investigation as scientific
  rather than confirmatory.
- **Pass condition**: Hypothesis section contains a named "Falsification" field or equivalent
  statement of the form "This hypothesis would be refuted if [condition]." The condition must
  be specific and testable, not vacuous ("if all evidence contradicts it").

---

### C-10 — Cross-namespace artifact integration
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

### C-11 — Feed-forward ledger table
- **Category**: verifiability
- **Weight**: aspirational
- **Derived from**: V-02 excellence signal — "Feed-forward ledger table audits plan-to-execution
  contract by inspection — unique structural addition."
- **Text**: The document includes a dedicated feed-forward ledger: a structured table that maps
  every experiment from the plan to its output label and names the downstream step that
  consumed that output. This makes the plan-to-execution contract verifiable by inspection
  without reading prose.
- **Pass condition**: A ledger section (or equivalent table) is present with one row per
  planned experiment, columns for output label and consumer, and all rows populated. A reader
  can confirm C-03 compliance by reading the ledger alone without scanning the experiment
  prose.

---

### C-12 — Per-experiment COMPLETE markers with consumed-by routing
- **Category**: traceability
- **Weight**: aspirational
- **Derived from**: V-03 excellence signal — "Per-experiment COMPLETE + Consumed-by routing is
  the most granular feed-forward enforcement."
- **Text**: Each experiment block terminates with an explicit COMPLETE record that states (a)
  what output the experiment produced and (b) which downstream step receives that output. This
  makes the feed-forward chain traceable at the block level rather than requiring whole-document
  comprehension.
- **Pass condition**: ≥2 experiment blocks each contain a COMPLETE record with both an output
  statement and an explicit "→ Consumed by: [step name or synthesis]" routing. The routings
  must be specific (not "see synthesis") and must match the actual flow of the document.

---

### C-13 — Inertia gap bookending
- **Category**: program-level framing
- **Weight**: aspirational
- **Derived from**: V-05 excellence signal — "Strongest C-08 enforcement of all variants: (a)
  inertia gap declared before execution, (b) experiment marked as addressing the gap, (c)
  'Inertia gap closure' verdict in synthesis confirms the gap was actually closed."
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

## Scoring Notes

- All five essential criteria (C-01–C-05) must PASS for the artifact to be considered
  complete. A document that scores 100 but fails any essential criterion is incomplete.
- PARTIAL credit on essential criteria counts as 6 points (half weight).
- Aspirational criteria are bonus: the primary pass threshold is 100/100 across
  essential + recommended. Aspirational scores above 100 signal a reference-quality artifact.
- C-11 and C-12 both strengthen C-03 (feed-forward) at different granularities and may
  co-occur. Award each independently.
- C-13 subsumes C-08 when the flexibility demonstrated is specifically framed as an inertia
  gap. Do not double-penalize: if C-08 PASS is earned via inertia gap framing, C-13 is
  eligible regardless.
```

---

Three new aspirational criteria added:

- **C-11** (feed-forward ledger) — from V-02: makes C-03 compliance scannable via a single audit table
- **C-12** (per-experiment COMPLETE + consumed-by) — from V-03: most granular feed-forward traceability, auditable at block level
- **C-13** (inertia gap bookending) — from V-05: full three-part contract (declare → mark → close) that turns the document into a gap-closure proof

Total bumped from 100 to 115, with 100 as the primary pass threshold and the 25-point aspirational pool as stretch ceiling. The scoring notes clarify C-13/C-08 interaction to prevent double-scoring.
