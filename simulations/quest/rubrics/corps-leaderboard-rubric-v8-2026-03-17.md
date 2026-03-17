Good — I have the variate file confirming the round context. Now writing the complete v8 rubric.

---

## Quest Rubric — corps-leaderboard v8

---

### What changed: v7 → v8

Two new aspirational criteria extracted from R7 scorecard excellence signals.

**C-24 — Gate-Level Prevents: Prefix Count Self-Audit**
Tests whether the output's ACTIONS GATE line (or equivalent gate construct) requires the model to count and explicitly report how many actions applied the `prevents:` prefix for zero-score conditions. C-20 tests whether the `prevents:` rule is stated somewhere in the instruction; C-22 tests whether it appears at two structurally independent locations; C-24 tests a third, distinct dimension: whether the model must perform a count audit at gate time — emitting a line of the form "prevents: prefix used for N zero-score conditions" or equivalent. The count report is a structural enforcement mechanism that operates after the action-writing phase closes. A model that wrote zero `prevents:` prefixes when zero-score conditions exist will surface a mismatch between the required count statement and its actual output, making the failure detectable at gate review rather than buried in the action rows. A gate line that confirms the number of actions written but does not separately require a `prevents:` prefix count fails C-24, even if C-20 and C-22 are satisfied.
- **Derived from**: R7 excellence signal — V-02 only. **Passes**: V-02.

**C-25 — Synthesis Novelty Constraint**
Tests whether the Team Insight (or synthesis) sentence carries an explicit instruction-level constraint requiring that it contain information not already stated in the health or inertia assessment section. C-13 (or equivalent synthesis criterion) tests structural form: the insight must include a cross-topic conclusion, a concrete number, and a specific name. C-25 tests a different dimension — whether the synthesized insight is *novel* relative to the preceding analysis phase. A constraint satisfies C-25 if it specifies, in some operational form, that the insight must advance beyond what the opening health or inertia phase established — for example, by requiring that a named skeptic role would acknowledge the insight as new information, or by stating that an insight which only restates an already-visible observation fails. An insight section that meets C-13's structural requirements but lacks any novelty gate passes C-13 but fails C-25. An instruction that adds the novelty gate explicitly — "the insight must contain something the Skeptic would not already know from the health or inertia assessment" — passes C-25.
- **Derived from**: R7 excellence signal — V-05 only. **Passes**: V-05.

**Scoring updated** — Aspirational tier now contains 17 criteria at 10/17 pts each (~0.588). Total remains 100. All five R7 variations pass C-01–C-23 (100/100 against v7). V-02 passes C-24, fails C-25; V-05 passes C-25, fails C-24; V-01, V-03, V-04 fail both. Against v8: V-02 and V-05 score ~99.41 (16/17 aspirational). V-01, V-03, V-04 score ~98.82 (15/17 aspirational). Two co-ceiling-setters at ~99.41. No variation yet scores 100 against v8 — the ceiling is open.

---

### What changed: v6 → v7

Two new aspirational criteria extracted from R6 scorecard excellence signals.

**C-22 — Dual-Statement Prevents-Rule Redundancy** — `prevents:` zero-score rule required at two structurally independent locations: once inside the template definition and once inside a pre-write check construct placed before the template.
- **Derived from**: R6 excellence signal — V-05 only. **Passes**: V-05.

**C-23 — Two-Level Nearest-Miss Cascade** — When no 1-away gaps exist, the output requires Level 1 (closest to 1-away, name + numeric gap) and Level 2 (closest to 2-away, name + numeric gap). Single-level nearest-miss satisfies C-21 but fails C-23.
- **Derived from**: R6 excellence signal — V-02, V-04.

### What changed: v5 → v6

*(preserved — see changelog)*

### What changed: v4 → v5

*(preserved — see changelog)*

---

## Essential Criteria (correctness baseline — 60% of score)

*Five criteria at 12 pts each. All five must pass to reach the golden threshold.*

### C-01 — Signal Registry Scan

- **Weight**: essential | **Category**: correctness
- **Text**: The skill scans the workspace by globbing `simulations/**/*.md` (or equivalent pattern) and builds a structured registry of all discovered signal files. For each entry the registry records at minimum: topic path, namespace, contributor identity, and file count. The scan phase must handle the empty-workspace case explicitly — when no signal files are found, the output records this state rather than silently proceeding to downstream phases.
- **Pass condition**: A scan phase is present and produces a registry with named fields: topic path, namespace, contributor set, and file count. An implementation that extracts only filenames without structured field assignment fails. A scan that omits the empty-workspace path (no explicit handling when zero files are found) fails.

### C-02 — Per-Topic Achievement Evaluation with Exact Names

- **Weight**: essential | **Category**: correctness
- **Text**: For every discovered topic, the output presents both which achievements are earned and which are not yet earned. Achievement definitions applied must include at minimum: First Signal (>= 1 file), Signal Depth (>= 3 files), Full Sweep (signals span >= 3 namespaces), Solo Pioneer (exactly 1 contributor, >= 1 signal), and Team Topic (>= 2 contributors with >= 1 signal each).
- **Pass condition**: Every topic from the scan appears in an achievements section with at least one explicit earned or locked achievement listed. A topic row showing only `---` without checking any of the five defined achievements fails. Achievement names must match the defined set — paraphrasing ("Team Coverage" for "Team Topic") fails.

### C-03 — All Three Team Milestones Present with Exact Names

- **Weight**: essential | **Category**: correctness
- **Text**: The output reports all three team milestones using their exact names: "first team signal", "shared coverage", and "debate starter". Each milestone includes a status (EARNED or NOT YET) and supporting evidence (file path, contributor count, or namespace list).
- **Pass condition**: All three milestone names appear verbatim. A milestone labeled "first signal posted" instead of "first team signal", or "cross-contributor coverage" instead of "shared coverage", fails. Each milestone has a non-empty evidence field — "---" without explanation counts as a gap. A missing milestone section fails this criterion entirely.

### C-04 — Contributor Leaderboard Present and Ranked

- **Weight**: essential | **Category**: coverage
- **Text**: A contributor leaderboard section is present, ranked in descending order by signal count (or equivalent primary metric). Each entry includes at minimum: rank, contributor identity, total signal count, and topics covered. If contributor metadata is not extractable from the workspace, the leaderboard states this explicitly rather than being omitted.
- **Pass condition**: A leaderboard section exists with at least one entry. If no contributor attribution is detectable (no frontmatter `author:` / `contributor:` fields, no parseable filename prefixes), the output writes one explicit row stating "no contributor metadata found" — this passes. A missing leaderboard section fails regardless of workspace state. An unranked list fails.

### C-05 — Specific Next Actions Naming Namespace and Achievement

- **Weight**: essential | **Category**: behavior
- **Text**: The output includes at least 3 recommended next actions. Each action must name (1) a specific namespace and topic (not just a category), and (2) the exact achievement or milestone name it unlocks. Generic advice such as "add more signals" or "increase namespace coverage" without naming a target fails.
- **Pass condition**: At least 3 actions are present. Each action names a namespace (e.g., `scout`, `flow`, `trace`) and a topic path (e.g., `scout/competitors`), and references an achievement or milestone by its exact name from the defined set. An action that names a topic without naming the unlocked achievement fails. An action that names an achievement without a specific namespace+topic fails.

---

## Recommended Criteria (improve output quality — 30% of score)

*Three criteria at 10 pts each.*

### C-06 — Earned / Available Achievement Separation

*(preserved from v7)*

### C-07 — *(preserved from v7)*

### C-08 — *(preserved from v7)*

---

## Aspirational Criteria (excellence ceiling — 10% of score)

*Seventeen criteria at 10/17 pts each (~0.588). All five R7 variations pass C-09–C-21 (forward-carried from v6). C-22 and C-23 forward-carried from v7. C-24 and C-25 new in v8.*

### C-09 through C-21 — *(preserved from v7)*

---

### C-22 — Dual-Statement Prevents-Rule Redundancy

- **Weight**: aspirational | **Category**: structural enforcement
- **Text**: The `prevents:` zero-score rule for the Breaks field appears in two structurally distinct locations within the instruction — once inside the action template definition and once inside a separate pre-write check construct (lookup table, decision matrix, or checklist) placed immediately before the template. C-20 tests whether the zero-score `prevents:` requirement exists somewhere in the instruction; C-22 tests whether it appears at two independent positions such that if the model skips one trigger surface, the other still fires. The pre-write check table operates as a generation friction point — it forces the model to look up each condition's score before filling the Breaks field, catching the zero-score case at decision time rather than relying solely on the template definition to carry the rule. A single statement of the rule, even in expanded form, satisfies C-20 but fails C-22.
- **Pass condition**: A pre-write check construct (named and placed before the template) contains the `prevents:` rule for the score = 0 case AND the template's Breaks field definition also states or restates the same rule. Both locations must be structurally independent — the pre-write check must not be embedded inside the template definition itself.
- **Derived from**: R6 excellence signal — V-05 only. R7: all five pass.

### C-23 — Two-Level Nearest-Miss Cascade

- **Weight**: aspirational | **Category**: structural enforcement
- **Text**: The 1-Away section's if-none clause, when no qualifying 1-away gaps exist, outputs two cascade levels: Level 1 names the closest topic or milestone to the 1-away threshold with its numeric gap, and Level 2 names the closest topic or milestone to the 2-away threshold with its numeric gap. C-21 requires a single named nearest-miss pointer when the 1-away list is empty; C-23 requires two-level depth. A single-level nearest-miss (Level 1 only) satisfies C-21 but fails C-23. Both levels must carry a specific topic or milestone name and a numeric step count. The two-level cascade converts a terminal null state into a two-sprint trajectory: the reader who finds nothing at threshold 1 is shown the next most actionable target at threshold 1 and the one after that at threshold 2, enabling sprint planning without re-running the skill.
- **Pass condition**: When the 1-away list is empty, the output requires both a Level 1 row (closest to 1-away, specific name, numeric gap) and a Level 2 row (closest to 2-away, specific name, numeric gap). An absence statement without both levels fails. A level entry with a vague name ("a topic", "some topic") or without a numeric gap fails.
- **Derived from**: R6 excellence signal — V-02, V-04. R7: all five pass.

---

### C-24 — Gate-Level Prevents: Prefix Count Self-Audit

- **Weight**: aspirational | **Category**: output verification
- **Text**: The output's ACTIONS GATE line (or equivalent gate construct placed after the action-writing phase) requires the model to count and explicitly report how many actions applied the `prevents:` prefix for zero-score conditions. C-20 tests whether the `prevents:` rule is stated; C-22 tests whether it appears at two structurally independent locations; C-24 tests a third, distinct dimension: whether the model performs a count audit at gate time — emitting a statement of the form "prevents: prefix used for N zero-score conditions" or equivalent. The count report is a structural enforcement mechanism that operates after the action-writing phase closes. A model that wrote zero `prevents:` prefixes when zero-score conditions exist will surface a mismatch between the required count statement and its actual output, making the failure detectable at gate review rather than buried in the action rows. A gate line that confirms the number of actions written but does not separately require a `prevents:` prefix count fails C-24, even if C-20 and C-22 are satisfied.
- **Pass condition**: The ACTIONS GATE (or equivalent named gate construct) includes a required count field specifically tracking `prevents:` prefix usage across all written actions. The field must distinguish between "N zero-score conditions triggered prevents:" and a generic action count. A gate that omits this count entirely fails. A gate that reports only total action count fails.
- **Derived from**: R7 excellence signal — V-02 only. **Passes**: V-02.

### C-25 — Synthesis Novelty Constraint

- **Weight**: aspirational | **Category**: insight quality
- **Text**: The Team Insight (or synthesis) sentence carries an explicit instruction-level constraint requiring that it contain information not already stated in the health or inertia assessment section. C-13 (or equivalent synthesis criterion) tests structural form — the insight must include a cross-topic conclusion, a concrete number, and a specific name. C-25 tests a different dimension: whether the synthesized insight is *novel* relative to the preceding analysis phase. A constraint satisfies C-25 if it specifies, in some operational form, that the insight must advance beyond what the opening health or inertia phase established — for example, by requiring that a named skeptic role would acknowledge the insight as new information, or by explicitly stating that an insight which only restates an already-visible observation fails. An insight section that meets C-13's structural requirements but contains no novelty gate passes C-13 but fails C-25. The novelty gate operates as a content filter on the synthesis phase: the model must not recycle observations the health/inertia section already establishes; it must add a new cross-dimension conclusion visible only from the combined view.
- **Pass condition**: The instruction contains an explicit novelty constraint on the Team Insight sentence, specifying (in some form) that the insight must not be a restatement of the health or inertia assessment and must contain a conclusion the analysis phase did not already state. The constraint must be operationally testable — "the insight should be interesting" is not sufficient. A novelty gate tied to a named role (e.g., "the Skeptic would acknowledge this as new") or to a structural exclusion ("must not appear in the inertia section") passes.
- **Derived from**: R7 excellence signal — V-05 only. **Passes**: V-05.

---

## Scoring Summary

| Tier | Criteria | Pts Each | Total |
|------|----------|----------|-------|
| Essential | C-01–C-05 (5) | 12.00 | 60 |
| Recommended | C-06–C-08 (3) | 10.00 | 30 |
| Aspirational | C-09–C-25 (17) | ~0.588 | 10 |
| **Total** | | | **100** |

### v8 Scores — R7 Variations

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total |
|-----------|---------------|-----------------|-------------------|-------|
| V-01 | 60/60 | 30/30 | 8.82 (15/17) | **98.82** |
| V-02 | 60/60 | 30/30 | 9.41 (16/17) | **99.41** |
| V-03 | 60/60 | 30/30 | 8.82 (15/17) | **98.82** |
| V-04 | 60/60 | 30/30 | 8.82 (15/17) | **98.82** |
| V-05 | 60/60 | 30/30 | 9.41 (16/17) | **99.41** |

V-02 passes C-24, fails C-25. V-05 passes C-25, fails C-24. V-01, V-03, V-04 fail both. Two co-ceiling-setters at **99.41**. The v8 ceiling is open — no variation yet scores 100.

---

```json
{
  "rubric_version": 8,
  "top_score": 99.41,
  "ceiling_open": true,
  "ceiling_holders": ["V-02", "V-05"],
  "new_criteria": ["C-24", "C-25"],
  "aspirational_count": 17,
  "pts_per_aspirational": 0.588,
  "open_gaps": {
    "C-24": ["V-01", "V-03", "V-04", "V-05"],
    "C-25": ["V-01", "V-02", "V-03", "V-04"]
  }
}
```
