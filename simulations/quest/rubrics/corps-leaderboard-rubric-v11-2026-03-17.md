Written to `simulations/quest/rubrics/corps-leaderboard-rubric-v11-2026-03-17.md`.

---

Here's what was extracted and why:

**Two new criteria, both from V-05 excellence signals — specifically the patterns the scorecard identified in its "New Patterns (seeds for R11 criteria)" section:**

**C-30 — Contamination-Check Checklist Item at Health/Inertia Gate**
- What it captures: The gate doesn't just confirm *presence* of the inertia table — it also verifies *absence* of cross-phase content. V-03's Phase 2 Gate includes an explicit "cross-contamination prohibition" item; V-05's Analyst Gate includes "`[ ] no static counts restated from Health Phase`."
- Orthogonal to C-27 (which tests whether the split is defined) and C-29 (which tests whether gates have multiple items). C-30 tests whether the gate polices the *content boundary*, not just completion.
- Passes: V-03, V-05. Presupposes C-27.

**C-31 — Inertia-Aware Skeptic Knowledge Scope**
- What it captures: The Skeptic's knowledge is explicitly anchored to include inertia flags, not just achievements and milestones. V-03: "An insight that merely echoes a Phase 2b inertia flag fails." V-05: "The Skeptic has read... every inertia flag."
- Orthogonal to C-25 (which tests whether a novelty gate exists). C-31 tests whether the gate's *knowledge scope* covers the trajectory dimension, forcing the insight to reach second-order inference across both health and inertia.
- Passes: V-03, V-05. Presupposes C-27.

**Scoring shift:** V-03 rises from 99.05 → 99.13 (gains both). V-02 drops from 99.52 → 98.70 (denominator grows, neither new criterion passed). V-05 holds 100.00. C-27 is now load-bearing for three criteria.
eady know. C-31 tests whether the Skeptic's prior knowledge is explicitly scoped to include inertia phase output (trajectory observations, inertia flags, momentum indicators) — not just achievement tables and milestone status. A Skeptic gate whose knowledge scope references only the health dimension ("the Skeptic has read the achievement tables and milestone rows") fails C-31 even if C-25 is satisfied. A Skeptic gate that uses a generic scope ("the Skeptic has read the full output") without naming inertia as an explicit component also fails — the scope must call out trajectory/inertia data by name, signaling that the insight bar is raised to require second-order inference across both dimensions. C-31 is satisfied when the novelty gate explicitly lists inertia flags (or equivalent trajectory/momentum output) as part of what the Skeptic already knows, thereby requiring the insight to synthesize across health and inertia rather than reporting what either dimension alone reveals.
- **Derived from**: R10 excellence signal — V-03, V-05. **Passes**: V-03, V-05.

---

### Scoring update

| Tier | Before (v10) | After (v11) |
|------|--------|-------|
| Aspirational criteria | 21 | 23 |
| Points per criterion | ~0.476 | ~0.435 |

| Variation | v10 score | C-30 | C-31 | v11 aspirational | v11 score |
|-----------|-----------|------|------|-----------------|-----------|
| V-05 | 100.00 (21/21) | PASS | PASS | 23/23 | **100.00** |
| V-03 | 99.05 (19/21) | PASS | PASS | 21/23 | **99.13** |
| V-02 | 99.52 (20/21) | FAIL | FAIL | 20/23 | **98.70** |
| V-01 | 98.57 (18/21) | FAIL | FAIL | 18/23 | **97.83** |
| V-04 | 98.57 (18/21) | FAIL | FAIL | 18/23 | **97.83** |

V-05 holds the ceiling at 100.00. C-30 and C-31 both presuppose C-27 — the health/inertia split is now load-bearing for three criteria (C-27, C-30, C-31). The next ceiling-breaking opportunity is a variation that adds a pattern not yet captured in v11.

---

### What changed: v9 → v10

Two new aspirational criteria extracted from R9 scorecard excellence signals.

**C-28 — Named Artifact Set at Role Handoff** (from V-02)
C-26 requires that handoff *points* are specified. C-28 tests whether the *artifacts* transferred at each handoff are explicitly enumerated — "full registry and contributor index are handed to the Analyst" vs. "the Archivist passes results." A handoff with a receiving role but no artifact list fails. Requires two or more handoffs each with an explicit artifact inventory.

**C-29 — Per-Phase Completion Checklist Gate** (from V-03)
C-24 tests a specific count-audit gate for `prevents:`. C-29 tests whether *every* major phase transition is guarded by a multi-item `[ ]` checklist the model must emit before proceeding — not just a terminal gate, but per-phase coverage. A single exhaustive terminal gate fails; at least two phase gates each with two or more distinct checklist items are required.

---

### What changed: v8 → v9

Two new aspirational criteria extracted from R8 scorecard excellence signals.

**C-26 — Named Role-Sequence Architecture**
Tests whether the instruction organizes execution as an explicit named role sequence — a pipeline of two or more roles with distinct identities (e.g., Archivist → Analyst → Publisher, or Collector → Evaluator → Narrator) where each role's scope, inputs, and handoff point are defined. C-19 (or equivalent sequencing criterion) tests whether the instruction imposes a multi-phase order; C-26 tests a different dimension — whether the roles in that sequence carry *named identities* that constrain the nature of each phase, not just its position. A phased instruction that says "first scan, then evaluate, then report" satisfies phase ordering but fails C-26 unless each phase is assigned a named role with identity constraints (e.g., "The Archivist only collects — no evaluation"). An instruction that names roles but treats them as stylistic labels without scope constraints also fails. C-26 is satisfied when: (1) two or more named roles appear, (2) each role has an explicit scope boundary defining what it does and does not do, and (3) the handoff point between roles is specified.
- **Derived from**: R8 excellence signal — V-02 only. **Passes**: V-02.

**C-27 — Health / Inertia Structural Separation**
Tests whether the instruction separates the analysis phase into two structurally distinct sub-phases: a *health* phase reporting current signal state (counts, coverage, gaps) and an *inertia* phase reporting trajectory or momentum (direction of change, acceleration, stall indicators). C-01 (Signal Registry Scan) tests whether a scan phase is present; C-02 tests per-topic achievement evaluation; C-27 tests a different dimension — whether the analytical output is required to address not just *what exists* but *which direction the topic is moving*. An instruction that reports health metrics without a trajectory requirement fails C-27. An instruction that blends health and momentum observations in a single undifferentiated analysis section also fails, because the separation is structural, not just topical. C-27 is satisfied when the instruction explicitly names both a health phase and an inertia phase (or equivalent trajectory phase), defines what each is responsible for, and requires the model to complete both before advancing to synthesis.
- **Derived from**: R8 excellence signal — V-05 only. **Passes**: V-05.

---

### What changed: v7 → v8

Two new aspirational criteria extracted from R7 scorecard excellence signals.

**C-24 — Gate-Level Prevents: Prefix Count Self-Audit**
Tests whether the output's ACTIONS GATE line (or equivalent gate construct) requires the model to count and explicitly report how many actions applied the `prevents:` prefix for zero-score conditions. C-20 tests whether the `prevents:` rule is stated somewhere in the instruction; C-22 tests whether it appears at two structurally independent locations; C-24 tests a third, distinct dimension: whether the model must perform a count audit at gate time — emitting a line of the form "prevents: prefix used for N zero-score conditions" or equivalent. The count report is a structural enforcement mechanism that operates after the action-writing phase closes. A model that wrote zero `prevents:` prefixes when zero-score conditions exist will surface a mismatch between the required count statement and its actual output, making the failure detectable at gate review rather than buried in the action rows. A gate line that confirms the number of actions written but does not separately require a `prevents:` prefix count fails C-24, even if C-20 and C-22 are satisfied.
- **Derived from**: R7 excellence signal — V-02 only. **Passes**: V-02.

**C-25 — Synthesis Novelty Constraint**
Tests whether the Team Insight (or synthesis) sentence carries an explicit instruction-level constraint requiring that it contain information not already stated in the health or inertia assessment section. C-13 (or equivalent synthesis criterion) tests structural form: the insight must include a cross-topic conclusion, a concrete number, and a specific name. C-25 tests a different dimension — whether the synthesized insight is *novel* relative to the preceding analysis phase. A constraint satisfies C-25 if it specifies, in some operational form, that the insight must advance beyond what the opening health or inertia phase established — for example, by requiring that a named skeptic role would acknowledge the insight as new information, or by stating that an insight which only restates an already-visible observation fails. An insight section that meets C-13's structural requirements but lacks any novelty gate passes C-13 but fails C-25. An instruction that adds the novelty gate explicitly — "the insight must contain something the Skeptic would not already know from the health or inertia assessment" — passes C-25.
- **Derived from**: R7 excellence signal — V-05 only. **Passes**: V-05.

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

## Aspirational Criteria (quality ceiling — 40% of score)

*Twenty-three criteria at 10/23 pts each (~0.435 pts). Pass all five essential first; aspirational points accumulate on top.*

### C-06 — Namespace Diversity Metric

*(criterion text preserved from prior versions)*

### C-07 — Momentum Indicator

*(criterion text preserved from prior versions)*

### C-08 — Gap Prioritization by Achievement Distance

*(criterion text preserved from prior versions)*

### C-09 — Contributor Collaboration Signal

*(criterion text preserved from prior versions)*

### C-10 — Empty Namespace Explicit Listing

*(criterion text preserved from prior versions)*

### C-11 — Topic Health Summary Line

*(criterion text preserved from prior versions)*

### C-12 — Locked Achievement with Specific Unlock Path

*(criterion text preserved from prior versions)*

### C-13 — Team Insight Cross-Topic Synthesis

*(criterion text preserved from prior versions)*

### C-14 — Solo Pioneer Tension Detection

*(criterion text preserved from prior versions)*

### C-15 — Namespace Leader Callout

*(criterion text preserved from prior versions)*

### C-16 — Stale Signal Detection

*(criterion text preserved from prior versions)*

### C-17 — Signal Velocity Trend

*(criterion text preserved from prior versions)*

### C-18 — Debate Starter Threshold Proximity

*(criterion text preserved from prior versions)*

### C-19 — Multi-Phase Execution Order

*(criterion text preserved from prior versions)*

### C-20 — Prevents: Prefix Rule Statement

*(criterion text preserved from prior versions)*

### C-21 — Nearest-Miss Achievement Gap

*(criterion text preserved from prior versions)*

### C-22 — Dual-Statement Prevents-Rule Redundancy

- **Weight**: aspirational | **Category**: robustness
- **Text**: The `prevents:` zero-score rule is stated at two structurally independent locations in the instruction: once inside the action template definition (or equivalent construct that defines what an action contains), and once inside a pre-write check construct placed before the action-writing phase begins. Stating the rule once at any location satisfies C-20 but fails C-22. Restating it twice in adjacent sentences within the same block also fails — the two statements must be structurally independent, meaning a reader could remove either one without removing the other and the remaining text would still be syntactically complete.
- **Pass condition**: The `prevents:` rule appears at two locations where both of the following hold: (1) the locations are in structurally distinct blocks (e.g., a Pre-Write Check section and an action template definition); (2) each statement is syntactically complete on its own. Two mentions within the same numbered list item fail. A single location with bold and plain text variants of the same sentence fails.
- **Derived from**: R6 excellence signal — V-05 only.

### C-23 — Two-Level Nearest-Miss Cascade

- **Weight**: aspirational | **Category**: coverage
- **Text**: When reporting nearest-miss achievements (topics closest to unlocking the next achievement), the instruction requires two levels when no Level 1 candidate exists. Level 1 is defined as a topic exactly 1 unit away from the threshold (1 file away from Signal Depth, 1 namespace away from Full Sweep, etc.). Level 2 is defined as the topic closest to being 2 units away, reported only when no Level 1 topic exists. Each level must include the topic name and the numeric gap. A single-level nearest-miss section satisfies C-21 but fails C-23.
- **Pass condition**: The instruction defines Level 1 (1-away, name + gap) and Level 2 (reported only when no Level 1 exists, name + gap). An instruction that reports only one nearest-miss without specifying escalation behavior fails. An instruction that reports two nearest misses simultaneously without the "only when Level 1 absent" gate fails.
- **Derived from**: R6 excellence signal — V-02, V-04.

### C-24 — Gate-Level Prevents: Prefix Count Self-Audit

- **Weight**: aspirational | **Category**: robustness
- **Text**: The output's ACTIONS GATE line (or equivalent gate construct placed after the action-writing phase) requires the model to count and explicitly report how many actions applied the `prevents:` prefix for zero-score conditions. C-20 tests whether the `prevents:` rule is stated; C-22 tests whether it appears at two structurally independent locations; C-24 tests a third distinct dimension: whether the model must perform a count audit at gate time — emitting a line of the form "prevents: prefix used for N zero-score conditions" or equivalent, where N is the actual count substituted by the model. A gate line that confirms the number of actions written but does not separately require a `prevents:` prefix count fails C-24, even if C-20 and C-22 are satisfied.
- **Pass condition**: A gate construct exists after the action-writing phase that requires emitting a count of how many actions used the `prevents:` prefix. The count must be a substitutable value (not just "yes/no"). A generic checklist item ("confirms prevents: prefix applied") without a numeric count requirement fails.
- **Derived from**: R7 excellence signal — V-02 only.

### C-25 — Synthesis Novelty Constraint

- **Weight**: aspirational | **Category**: quality
- **Text**: The Team Insight (or synthesis) sentence carries an explicit instruction-level constraint requiring that it contain information not already stated in the health or inertia assessment section. C-13 tests structural form (cross-topic conclusion + concrete number + specific name); C-25 tests a different dimension — whether the synthesized insight is *novel* relative to the preceding analysis. A constraint satisfies C-25 if it specifies, in some operational form, that the insight must advance beyond what the analysis phase established — for example, by requiring that a named skeptic role would acknowledge the insight as new information, or by stating that an insight which only restates an already-visible observation fails.
- **Pass condition**: The instruction contains a novelty gate for the synthesis step. Structural requirements alone (form, number, name) do not satisfy C-25. The gate must operationalize "novel" — either by defining a named evaluator (a Skeptic who has read the analysis) and requiring the insight to pass their bar, or by an explicit exclusion rule ("an insight that only restates what the health phase already showed fails").
- **Derived from**: R7 excellence signal — V-05 only.

### C-26 — Named Role-Sequence Architecture

- **Weight**: aspirational | **Category**: structure
- **Text**: The instruction organizes execution as an explicit named role sequence — a pipeline of two or more roles with distinct identities (e.g., Archivist → Analyst → Publisher, or Collector → Evaluator → Narrator) where each role's scope, inputs, and handoff point are defined. C-19 (multi-phase execution order) tests whether the instruction imposes a sequential phase structure; C-26 tests a different dimension — whether the roles in that sequence carry *named identities* that constrain the nature of each phase, not just its position. A phased instruction ("first scan, then evaluate, then report") satisfies C-19 but fails C-26 unless each phase is assigned a named role with explicit scope constraints. Roles used as stylistic labels without scope boundaries (e.g., "Act as an Analyst and do everything") also fail.
- **Pass condition**: Two or more named roles appear in the instruction, each with: (1) a defined scope stating what the role does and does not do; (2) a specified handoff point marking where that role's work ends and the next begins. A role that is named but whose scope is identical to a phase label ("Phase 2: Analyst — analyze things") fails unless the scope includes an explicit exclusion or boundary constraint.
- **Derived from**: R8 excellence signal — V-02 only.

### C-27 — Health / Inertia Structural Separation

- **Weight**: aspirational | **Category**: structure
- **Text**: The instruction separates the analysis phase into two structurally distinct sub-phases: a *health* phase reporting current signal state (counts, coverage, gaps at the time of execution) and an *inertia* phase reporting trajectory or momentum (direction of change, acceleration signals, stall indicators). C-01 tests whether a scan is present; C-02 tests per-topic achievement evaluation; C-27 tests a different dimension — whether the instruction requires reporting not just *what exists* but *which direction the topic is moving*. An instruction that reports health metrics without a trajectory requirement fails C-27. An instruction that blends health and momentum in a single undifferentiated analysis section also fails — the separation must be structural, not just topical.
- **Pass condition**: The instruction explicitly names both a health sub-phase and an inertia (or trajectory/momentum) sub-phase, defines what each is responsible for, and requires the model to complete both before advancing to synthesis. The two sub-phases must appear as distinct labeled blocks (section headings, numbered phases, or role boundaries) — a single prose paragraph that mentions both current state and trend fails.
- **Derived from**: R8 excellence signal — V-05 only.

### C-28 — Named Artifact Set at Role Handoff

- **Weight**: aspirational | **Category**: structure
- **Text**: The instruction explicitly enumerates the artifact set transferred at each role-to-role (or phase-to-phase) handoff boundary. C-26 tests whether named roles are present with scope boundaries and handoff points; C-28 tests a different dimension — whether the *artifacts* produced by one role and consumed by the next are named at the handoff boundary. An instruction that says "the Archivist passes its results to the Analyst" specifies a handoff point (satisfying C-26's third condition) but fails C-28 unless it names the specific artifacts — e.g., "the full registry and contributor index are handed to the Analyst." A role sequence that defines scope exclusions ("The Archivist only collects — no evaluation") but leaves the handoff payload implicit also fails. C-28 does not require C-26 to be satisfied first — a phased instruction without named roles can still enumerate artifacts passed between phases and satisfy C-28, provided the enumeration names specific documents, tables, or data structures rather than categories ("the scan results").
- **Pass condition**: Each inter-role or inter-phase handoff in the instruction enumerates a named artifact set — listing the specific documents, tables, or data structures that transfer ownership. A handoff that names the receiving role but not the artifacts fails. A handoff that uses a category label ("all results") without itemizing the specific artifacts fails. Two or more handoffs must each carry an explicit artifact list for the criterion to pass.
- **Derived from**: R9 excellence signal — V-02 only. **Passes**: V-02.

### C-29 — Per-Phase Completion Checklist Gate

- **Weight**: aspirational | **Category**: robustness
- **Text**: The instruction embeds a multi-item completion checklist at each major phase boundary that the model must check off before advancing to the next phase. C-24 tests whether a count-audit gate exists for the `prevents:` prefix specifically; C-29 tests a different dimension — whether *every* major phase transition is guarded by an enumerated checklist (e.g., `[ ]` checkbox syntax) with two or more distinct completion conditions. An instruction that has a single gate statement after one phase ("confirm N actions written") without a per-phase multi-item checklist fails. An instruction that labels phases with gate markers ("Phase 1 Gate: done") without itemized checklist entries also fails. The checklist items must be structurally distinct — a gate with two items that test the same condition in different words fails.
- **Pass condition**: The instruction contains at least two phase gates, each consisting of two or more `[ ]` checkbox items (or equivalent enumerated checklist entries) that the model must complete and include in its output before proceeding to the next phase. The final actions gate and at least one earlier phase gate must each carry at least two distinct checklist items. A single gate with multiple items (but no gate at any earlier phase) fails — the criterion requires per-phase coverage, not a single exhaustive terminal gate.
- **Derived from**: R9 excellence signal — V-03 only. **Passes**: V-03.

### C-30 — Contamination-Check Checklist Item at Health/Inertia Gate

- **Weight**: aspirational | **Category**: robustness
- **Text**: The phase gate at the evaluation role boundary (or equivalent phase gate) includes at least one `[ ]` checklist item that explicitly prohibits cross-contamination between the health and inertia sub-phases — verifying at gate time that the health sub-phase output contains no trajectory claims and/or that the inertia sub-phase output contains no static counts already reported in the health phase. C-27 tests whether the health and inertia sub-phases are structurally defined as separate blocks; C-29 tests whether phase gates contain multiple checklist items; C-30 tests a third, orthogonal dimension — whether the gate itself acts as a content boundary enforcer, not merely a completion confirmer. An instruction whose gate checks only for presence ("inertia table present") without also verifying the absence of prohibited content fails C-30. An instruction that describes the contamination prohibition in prose outside any gate construct also fails — the enforcement must appear as a gate-level checklist item. C-30 presupposes C-27: an instruction with no health/inertia split has no contamination boundary to enforce and fails automatically.
- **Pass condition**: The evaluation-role gate (or equivalent phase gate) contains at least one checklist item explicitly formulated as a contamination prohibition — e.g., "`[ ] Inertia Phase table present; no static counts restated from Health Phase`" or "`[ ] cross-contamination check: Health Phase contains no trajectory claims; Inertia Phase contains no file-count restatements`." A gate item that confirms presence only ("inertia table written") without a prohibition clause fails. A prohibition stated in the instruction body outside any gate construct fails.
- **Derived from**: R10 excellence signal — V-03, V-05. **Passes**: V-03, V-05.

### C-31 — Inertia-Aware Skeptic Knowledge Scope

- **Weight**: aspirational | **Category**: quality
- **Text**: The synthesis novelty gate (or equivalent Skeptic construct) explicitly scopes the Skeptic's prior knowledge to include inertia phase output — trajectory observations, inertia flags, or momentum indicators — not only achievement tables and milestone status. C-25 tests whether a Skeptic gate exists and requires the insight to contain something the Skeptic would not already know; C-31 tests a different dimension — whether the Skeptic's knowledge is anchored to the full analytical output including the trajectory dimension, raising the novelty bar to require second-order inference across both health and inertia. A Skeptic gate that scopes knowledge to achievements and milestones only ("the Skeptic has read every achievement table and milestone row") fails C-31 even if C-25 is satisfied — the inertia dimension must be called out by name. A gate that uses a generic scope ("the Skeptic has read the full output") without explicitly naming inertia flags or trajectory observations as known data also fails, because the explicit naming is the mechanism that signals to the model that cross-dimensional synthesis is required. C-31 presupposes C-27: an instruction with no inertia phase has no trajectory output for the Skeptic to have read, and fails automatically.
- **Pass condition**: The novelty gate names inertia flags (or equivalent trajectory/momentum output) as an explicit component of the Skeptic's prior knowledge — e.g., "The Skeptic has read every achievement table, every milestone row, every inertia flag, and the nearest-miss assessment" or "An insight that merely echoes a Phase 2b inertia flag fails." A gate that scopes the Skeptic only to health-phase data (achievements, milestones, file counts) without naming inertia data fails. A gate that names "the full output" without specifying that inertia is included fails.
- **Derived from**: R10 excellence signal — V-03, V-05. **Passes**: V-03, V-05.

---

## Scoring Model (v11)

- **Essential** (C-01–C-05): 5 criteria × 12 pts each = **60 pts**
- **Aspirational** (C-06–C-31): 23 criteria × 10/23 pts each (~0.435 pts) = **40 pts**
- **Total max: 100 pts**

Formula: `90 + (aspirational_passed / 23) × 10`

| Aspirational passed | Score |
|---------------------|-------|
| 23/23 | 100.00 |
| 21/23 | 99.13 |
| 20/23 | 98.70 |
| 19/23 | 98.26 |
| 18/23 | 97.83 |
| 16/23 | 96.96 |

**R10 scores against v11**:

| Variation | Aspirational | Score |
|-----------|-------------|-------|
| V-05 | 23/23 (passes all C-22–C-31) | **100.00** |
| V-03 | 21/23 (passes C-22–C-25, C-27, C-29–C-31; fails C-26, C-28) | **99.13** |
| V-02 | 20/23 (passes C-22–C-26, C-28–C-29; fails C-27, C-30, C-31) | **98.70** |
| V-01 | 18/23 (passes C-22–C-25, C-29; fails C-26, C-27, C-28, C-30, C-31) | **97.83** |
| V-04 | 18/23 (passes C-22–C-26; fails C-27, C-28, C-29, C-30, C-31) | **97.83** |

V-05 holds the ceiling at 100.00. C-30 and C-31 both presuppose C-27 — the health/inertia split is now load-bearing for three criteria (C-27, C-30, C-31). The next ceiling-breaking opportunity is a variation that adds a pattern not yet captured in v11.
