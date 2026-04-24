Rubric written to `simulations/quest/rubrics/prove-program-rubric-2026-03-15.md`.

**Design decisions:**

**Essential (5)** — the four things that make prove-program distinct from a basic document:
- C-01: Hypothesis before experiments (enforces the investigate-don't-explore pattern)
- C-02: Multi-experiment plan with rationale (the "program" in prove-program)
- C-03: Feed-forward between experiments (what separates orchestration from parallel execution)
- C-04: "What we thought vs. learned" synthesis (the core insight delivery)
- C-05: Qx.md format at canonical path (artifact hygiene)

**Recommended (3)** — depth signals:
- C-06: Labeled, actionable principles (not just observations)
- C-07: Confidence levels per finding (epistemic honesty)
- C-08: Flexibility demonstrated — at least one experiment scope that prove-topic couldn't do (validates the skill's differentiation claim)

**Aspirational (2)** — raise the bar:
- C-09: Falsification criteria (proper scientific framing)
- C-10: Cross-namespace artifact integration (prove-program operating as a connective tissue skill)
sis — a clear claim about what the researcher believes is true — before any experiment is described or run.
- **Pass condition**: The document contains a named hypothesis section (or equivalent) that appears before any experiment section, states a specific belief in positive form, and is not merely a restatement of the research question.

---

### C-02 — Experiment plan with ≥2 distinct types
- **Category**: coverage
- **Weight**: essential
- **Text**: The orchestrator produces an explicit experiment plan that selects at least two distinct experiment types (e.g., websearch, intelligence, analysis, interview, prototype, or custom) and explains the rationale for the chosen combination.
- **Pass condition**: A plan section lists ≥2 experiment types by name, states why each was chosen for this research question, and the experiments actually execute in the body of the document.

---

### C-03 — Feed-forward between experiments
- **Category**: behavior
- **Weight**: essential
- **Text**: Each experiment's outputs are consumed by subsequent steps. Later experiments or the synthesis explicitly reference findings from earlier experiments rather than treating each as independent.
- **Pass condition**: At least one instance of explicit forward-feeding: a later experiment or the synthesis section cites or incorporates a finding from an earlier experiment by name or content.

---

### C-04 — Synthesis with "what we thought vs. what we actually learned"
- **Category**: correctness
- **Weight**: essential
- **Text**: The document contains a synthesis section that answers the original research question and contrasts the pre-investigation hypothesis against the post-investigation finding.
- **Pass condition**: Synthesis section present, contains both a restatement of the original hypothesis and a "what we actually learned" statement that either confirms, refines, or refutes it. May not simply repeat hypothesis verbatim as the finding.

---

### C-05 — Qx.md format artifact at correct path
- **Category**: format
- **Weight**: essential
- **Text**: The output is written as a Qx.md-style research document (structured with labeled sections: hypothesis, experiments, findings, synthesis, principles) and saved at the canonical path `simulations/prove/research/{topic}-research-{date}.md`.
- **Pass condition**: Document has ≥4 labeled sections matching the Qx.md pattern. Artifact filename follows `{topic}-research-{date}.md` convention and is placed under `simulations/prove/research/`.

---

## Recommended Criteria (weight: 30 points total)

### C-06 — Principles extracted (≥2, labeled, actionable)
- **Category**: depth
- **Weight**: recommended
- **Text**: The document closes with a principles section that extracts at least two reusable, actionable principles from the investigation's findings — not observations, but design rules or decision heuristics.
- **Pass condition**: Principles section present with ≥2 entries. Each entry is labeled (e.g., "P-01") and states a rule in imperative or conditional form ("When X, do Y" or "Always Z"). Generic truisms ("do good research") do not pass.

---

### C-07 — Confidence levels stated per major finding
- **Category**: depth
- **Weight**: recommended
- **Text**: Each major finding in the synthesis carries an explicit confidence level or evidence quality indicator (e.g., high/medium/low, or a brief qualifier such as "based on 3 sources" or "inconclusive").
- **Pass condition**: ≥2 findings in the synthesis or findings section are annotated with confidence level or evidence-quality qualifier. Unlabeled or uniform confidence across all findings does not pass.

---

### C-08 — Flexibility demonstrated beyond prove-topic
- **Category**: coverage
- **Weight**: recommended
- **Text**: The experiment sequence includes at least one experiment type or scope that would not be available in prove-topic (e.g., a cross-namespace lookup, a custom data analysis, a non-Signal research question, or a web search on an external domain).
- **Pass condition**: At least one experiment step either (a) queries data outside the current Signal topic context, (b) uses a custom experiment not in the standard prove skill set, or (c) spans multiple namespaces. The document or experiment log makes this flexibility visible.

---

## Aspirational Criteria (weight: 10 points total)

### C-09 — Falsification criteria in hypothesis
- **Category**: depth
- **Weight**: aspirational
- **Text**: The hypothesis section explicitly states what evidence would falsify the claim — "what would change my mind." This transforms the hypothesis from a belief into a testable scientific statement.
- **Pass condition**: Hypothesis section contains a named falsification condition or counter-evidence statement ("This hypothesis would be false if..." or equivalent). Absence of any falsification language fails.

---

### C-10 — Cross-namespace artifact integration
- **Category**: coverage
- **Weight**: aspirational
- **Text**: The research document references or produces artifacts that connect to other Signal namespaces — either consuming scout/draft/review signals as inputs or producing findings that feed into draft/listen/topic artifacts.
- **Pass condition**: At least one explicit cross-namespace reference: either (a) a scout, draft, review, or trace artifact is cited as input evidence, or (b) the synthesis explicitly notes that findings should flow into a named downstream artifact (e.g., "these findings should update the draft spec at...").

---

## Scoring Summary

| ID   | Criterion                              | Weight        | Category    |
|------|----------------------------------------|---------------|-------------|
| C-01 | Hypothesis-first framing               | essential     | correctness |
| C-02 | Experiment plan with ≥2 distinct types | essential     | coverage    |
| C-03 | Feed-forward between experiments       | essential     | behavior    |
| C-04 | Synthesis: thought vs. learned         | essential     | correctness |
| C-05 | Qx.md format at correct path           | essential     | format      |
| C-06 | Principles extracted (≥2, labeled)     | recommended   | depth       |
| C-07 | Confidence levels per finding          | recommended   | depth       |
| C-08 | Flexibility beyond prove-topic         | recommended   | coverage    |
| C-09 | Falsification criteria in hypothesis   | aspirational  | depth       |
| C-10 | Cross-namespace artifact integration   | aspirational  | coverage    |

**Golden threshold**: All 5 essential pass AND composite ≥ 80.
