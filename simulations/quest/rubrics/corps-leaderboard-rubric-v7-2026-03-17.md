Now I have the full picture. The R6 scorecard has 4 excellence signals in the "new patterns" section. Two are criteria-grade — the others (zero-score register shift and hard requirement language) are refinements already captured in C-20/C-21. The genuinely new, testable patterns are:

- **Pre-write check table with dual-statement** (V-05 only) — `prevents:` rule stated twice: in template definition AND in a separate pre-write lookup table
- **Two-level nearest-miss cascade** (V-02, V-04) — Level 1 (1-away) + Level 2 (2-away) fallback, not just single nearest-miss

Those become C-22 and C-23. Here is the complete v7 rubric:

---

## Quest Rubric — corps-leaderboard v7

---

### What changed: v6 → v7

Two new aspirational criteria extracted from R6 scorecard excellence signals.

**C-22 — Dual-Statement Prevents-Rule Redundancy**
Tests whether the `prevents:` zero-score rule for the Breaks field appears in two structurally distinct locations within the instruction — once inside the action template definition and once inside a separate pre-write check construct (lookup table, decision matrix, or checklist) placed immediately before the template. C-20 tests whether the zero-score `prevents:` requirement exists somewhere in the instruction; C-22 tests whether it appears at two independent positions such that if the model skips one trigger surface, the other still fires. Redundant enforcement surfaces are structurally stronger than a single statement, however prominent: the pre-write check table operates as a generation friction point — it forces the model to look up each condition's score before filling the Breaks field, catching the zero-score case at decision time rather than relying solely on the template definition to carry the rule. A single statement of the rule, even in expanded form, satisfies C-20 but fails C-22.
- **Derived from**: R6 excellence signal — V-05 only. **Passes**: V-05.

**C-23 — Two-Level Nearest-Miss Cascade**
Tests whether the 1-Away section's if-none clause, when no qualifying 1-away gaps exist, outputs two cascade levels: Level 1 names the closest topic or milestone to the 1-away threshold with its numeric gap, and Level 2 names the closest topic or milestone to the 2-away threshold with its numeric gap. C-21 requires a single named nearest-miss pointer when the 1-away list is empty; C-23 requires two-level depth. A single-level nearest-miss (Level 1 only) satisfies C-21 but fails C-23. Both levels must carry a specific topic or milestone name and a numeric step count. The two-level cascade converts a terminal null state into a two-sprint trajectory: the reader who finds nothing at threshold 1 is shown the next most actionable target at threshold 1 and the one after that at threshold 2, enabling sprint planning without re-running the skill.
- **Derived from**: R6 excellence signal — V-02, V-04. **Passes**: V-02, V-04.

**Scoring updated** — Aspirational tier now contains 15 criteria at 10/15 pts each (~0.67). Total remains 100. All five R6 variations pass C-01–C-21 (100/100 against v6). V-05 passes C-22, fails C-23; V-02 and V-04 pass C-23, fail C-22; V-01 and V-03 fail both. Against v7: V-02, V-04, V-05 score ~99.33 (14/15 aspirational). V-01 and V-03 score ~98.67 (13/15 aspirational). Three co-ceiling-setters at ~99.33. No variation yet scores 100 against v7 — the ceiling is open.

---

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

- **Weight**: recommended | **Category**: format
- **Text**: The output visually or structurally separates earned achievements from locked/available achievements for each topic. A reader scanning the output can immediately distinguish what the team has already unlocked from what remains.
- **Pass condition**: The achievements section uses a consistent structural indicator to separate earned from locked (e.g., distinct subsections, table columns, badge markers like checkmark vs circle, or equivalent). A flat list of achievements without any earned/locked distinction fails. Topics with only earned or only locked achievements need only show one group — but must not mix the two without differentiation.

### C-07 — 1-Away Gap Detection

- **Weight**: recommended | **Category**: depth
- **Text**: The output identifies achievements or milestones that are exactly one step away from being unlocked, with the gap quantified precisely (e.g., "needs 1 more signal", "needs 1 more contributor", "needs 1 more namespace").
- **Pass condition**: A dedicated "close to unlock" or "almost there" section exists. Each entry names the topic or milestone, states the exact numeric gap (not "a few more"), and names the target achievement. If no gaps are within 1 step, the section states this explicitly rather than being omitted. A generic "keep adding signals" note without per-achievement gap counts fails.

### C-08 — Team Synthesis Sentence

- **Weight**: recommended | **Category**: insight
- **Text**: The output includes one synthesis sentence whose observation requires seeing multiple topics or multiple contributors together — a conclusion that is invisible from any individual-topic view. The sentence must cross at least two topics or two contributors.
- **Pass condition**: A synthesis sentence exists and states a multi-topic or multi-contributor observation (e.g., "Contributors A and B overlap in scout and flow, while C is isolated in trace"). A sentence that describes one topic's state without referencing others fails. A generic statement such as "the team is making progress" without a specific cross-referencing claim fails.

---

## Aspirational Criteria (ceiling-raising — 10% of score)

*Fifteen criteria sharing 10 pts total (10/15 pts each, ~0.67). A perfect aspirational score requires all fifteen.*

### C-09 — Five Named Stagnation Conditions

- **Weight**: aspirational | **Category**: correctness
- **Text**: The health score section evaluates exactly five named stagnation conditions: Empty Start, Lone Wolf, Namespace Tunnel, Stale Coverage, and Shallow Spread. Each condition is scored on the 0–3 scale and must appear by its exact name.
- **Pass condition**: All five condition names appear verbatim in the health score output. A renamed or paraphrased condition (e.g., "No Signals" for "Empty Start") fails. Fewer than five conditions evaluated fails.

### C-10 — Urgency Tiers 0=Low 1=Medium 2–3=High

- **Weight**: aspirational | **Category**: format
- **Text**: The health score section maps each stagnation condition score to an urgency tier using the exact mapping: 0 = LOW, 1 = MEDIUM, 2–3 = HIGH. The tier labels are present in the output alongside the numeric score.
- **Pass condition**: The three-tier mapping is defined in the instruction and appears in the output. An implementation that uses only numeric scores without tier labels fails. A mapping that deviates from the 0/1/2–3 breakpoints fails.

### C-11 — Health Score Precedes Achievement Compilation

- **Weight**: aspirational | **Category**: structure
- **Text**: The signal health score section is computed and output before the achievement compilation section. The ordering is enforced by the instruction — it is not left to the model's discretion.
- **Pass condition**: The instruction explicitly states that the health score phase must complete before the achievement phase begins. An instruction that lists health and achievements as peer sections without ordering enforcement fails. If C-09 or C-10 fails, this criterion automatically fails.

### C-12 — Empty-Workspace Path Explicit

- **Weight**: aspirational | **Category**: robustness
- **Text**: The instruction explicitly defines the output path for an empty workspace — when the scan phase finds zero signal files. The empty-workspace output is a named, distinct output state rather than a degenerate case of the normal output.
- **Pass condition**: The instruction contains an explicit empty-workspace clause naming what the output produces when the file count is zero (e.g., "output a registry with one row: `empty workspace — no signals found`"). An instruction that handles only the non-empty case fails.

### C-13 — Named Gate on Health-to-Achievement Transition

- **Weight**: aspirational | **Category**: structure
- **Text**: The transition from the health score phase to the achievement compilation phase is announced by a named gate in the instruction. The gate name is fixed and must appear in the output at the transition point.
- **Pass condition**: The instruction names the gate at the health-to-achievement boundary (e.g., `[HEALTH GATE closed. ACHIEVEMENT COMPILATION opens.]`) and requires it as a literal output line. A transition marked only by section headers without a named gate line fails. If C-11 fails, this criterion automatically fails.

### C-14 — Per-Action Field Template with Explicit N/A Prohibition

- **Weight**: aspirational | **Category**: behavior
- **Text**: The next-actions section requires each action to follow a named field template (at minimum: Unlocks, Breaks, Priority). The instruction explicitly prohibits writing "N/A" in any field — every field must carry a substantive value. The N/A prohibition must appear in the instruction text, not only in an example.
- **Pass condition**: The instruction defines a multi-field action template by name, lists each field, and states that N/A is not a valid field value. An instruction that shows an example with no N/A without explicitly prohibiting it fails. An action list without a named template structure fails.

### C-15 — Section-Boundary Gate as Structural Constraint

- **Weight**: aspirational | **Category**: structure
- **Text**: Each major section boundary is enforced by a gate that appears as a named structural constraint in the instruction — not merely as a suggested ordering. The gate names the section that closes and the section that opens, and its presence in the output is required.
- **Pass condition**: At least two section-boundary gates are defined in the instruction as required output lines with fixed names. An instruction that uses section headers to imply ordering without printing gate announcement lines fails. If C-13 fails, this criterion automatically fails.

### C-16 — Dominant Condition Named in Gate Output

- **Weight**: aspirational | **Category**: depth
- **Text**: The health score gate output names the dominant stagnation condition — the condition with the highest score, or the first by priority if tied. The dominant condition name is required in the gate line, not merely present in the table above it.
- **Pass condition**: The health gate output line includes the dominant condition name (e.g., `[HEALTH GATE closed. Dominant condition: Lone Wolf (score 3, HIGH).]`). A gate line that announces the transition without naming the dominant condition fails. If C-13 fails, this criterion automatically fails.

### C-17 — Evidence-First Leaderboard Before Named Pattern

- **Weight**: aspirational | **Category**: structure
- **Text**: The leaderboard section presents ranked evidence (contributor table with signal counts) before labeling any named pattern or diagnosis about the contributor distribution. The evidence output precedes the interpretation.
- **Pass condition**: The contributor table appears before any named pattern label (e.g., "Lone Wolf pattern detected") in the leaderboard section. An instruction that outputs a pattern label before presenting the supporting table fails. If C-04 fails, this criterion automatically fails.

### C-18 — Gate Markers as Literal Output Lines *(NEW v5)*

- **Weight**: aspirational | **Category**: structure
- **Text**: The section-transition gates are announced as machine-readable lines in the output artifact itself — not only encoded as ordering rules in the instruction text. A gate marker appears at the section boundary as a printed line (e.g., `[GATE 2: SIGNAL HEALTH SCORE closed. ACHIEVEMENT COMPILATION opens now.]`). When gate markers are output-layer artifacts, compliance is auditable by scanning the output for expected announcement lines; a reordered or skipped gate leaves a visible gap. This is structurally stronger than C-15: C-15 tests whether the instruction has a named section-boundary rule; C-18 tests whether the transition produces a detectable artifact in the output.
- **Pass condition**: At least one section-transition boundary is announced by a literal printed line in the output at the exact transition point. The instruction specifies the gate marker format and which section transitions must produce a gate announcement line. An instruction that enforces ordering through section labels alone (C-15) without printing gate announcement lines fails. The gate marker must appear in the output (not just in the instruction text). If C-15 fails, this criterion automatically fails.
- **Derived from**: R4 excellence signal — V-02 (Triple-Gate Pipeline). **Passes**: V-02 only (R4). All five R6 variations pass.

### C-19 — Synthesis Sentence with Concrete Numeric Claim *(NEW v5)*

- **Weight**: aspirational | **Category**: depth
- **Text**: The team synthesis sentence (C-08) is required by the instruction to include at least one concrete numeric value — a contributor count, signal count, namespace count, or topic count — alongside the cross-section observation. C-08 requires a synthesizing sentence that draws a conclusion across topics or contributors; C-19 requires that the observation be anchored to a specific number, making the claim verifiable against workspace data. "3 of 4 contributors have signals in 2+ namespaces" is verifiable; "the team shows broad distribution" is not.
- **Pass condition**: The instruction text for the synthesis sentence includes an explicit numeric requirement (e.g., "include a specific number", "reference exact counts", "must name >= 2 topics or contributors and include a specific number"). The output synthesis sentence contains a numeric value that is extractable and checkable against workspace data. A synthesizing sentence that names topics or contributors without a concrete number fails. If C-08 fails, this criterion automatically fails.
- **Derived from**: R4 excellence signal — V-03 (Conversational Coach). **Passes**: V-03 only (R4). All five R6 variations pass.

### C-20 — Three-Field Action Template with Breaks Condition *(NEW v6)*

- **Weight**: aspirational | **Category**: behavior
- **Text**: The next-actions section uses a three-field structured template — `-> Unlocks: {exact achievement or milestone name}` / `-> Breaks: {condition name from health score}` / `-> Priority: [tier]` — and the instruction requires the `Breaks` field to name the health condition the action dissolves. When the targeted health condition is already at score 0, the instruction requires the field to shift to a `prevents:` rationale (e.g., `prevents: {re-entry condition} — {rationale}`) rather than leaving the field blank or writing N/A. C-05 requires namespace+topic+achievement naming (the Unlocks field). C-14 requires a named Breaks field with N/A prohibition. C-20 tests a third constraint: the per-entry Breaks value must either name an active health condition (carrot + release pairing) or carry a `prevents:` prefix when that condition is already resolved. Every action is thereby dual-annotated — what you earn and what constraint dissolves or is blocked from returning. The pattern is verifiable by checking that each Breaks field entry either matches a named condition from the health score section or begins with `prevents:`.
- **Pass condition**: The instruction text defines a three-field action template that names all three fields (Unlocks, Breaks, Priority). The instruction states that the Breaks field must name a health condition and that when the condition is at score 0 the field must use a `prevents:` prefix with a rationale. A template that names the Breaks field without the zero-score `prevents:` requirement passes C-14 but fails C-20. An action list that uses the template in output without the instruction requirement fails. If C-14 fails, this criterion automatically fails.
- **Derived from**: R5 excellence signal — all five variations (V-01 through V-05). **Passes**: all five.

### C-21 — 1-Away Section Nearest-Miss Fallback *(NEW v6)*

- **Weight**: aspirational | **Category**: depth
- **Text**: The 1-Away gap detection section (C-07), when no qualifying 1-away gaps exist, outputs a nearest-miss fallback that names the specific topic or milestone closest to qualifying and quantifies its remaining gap (e.g., "No 1-away gaps found. Closest: [topic] needs [n] more [unit]"). C-07 requires that the null case be stated explicitly rather than omitting the section; C-21 requires that the null-case clause additionally name the nearest qualifying candidate and measure its distance. A bare "no 1-away gaps found" statement satisfies C-07 but fails C-21. The nearest-miss pointer transforms a dead-end null into an actionable directive: the reader who finds nothing at the 1-away threshold is immediately shown the next most actionable target. The constraint is verifiable: the if-none clause must contain a specific topic name and a numeric gap count, not just an absence declaration.
- **Pass condition**: The instruction text includes an if-none clause for the 1-Away section that requires, when no 1-away gaps are present, naming the closest qualifying item and stating its numeric gap. The output if-none clause contains a specific topic or milestone name and a numeric step count (e.g., "needs 2 more signals"). A null-case clause that states only "no 1-away gaps exist" or "nothing is one step away" without a named nearest-miss entry fails. An instruction that covers only the positive case (gaps exist) without addressing the null case fails C-07 and automatically fails C-21.
- **Derived from**: R5 excellence signal — V-01, V-02, V-03. **Passes**: V-01, V-02, V-03 (R5). All five R6 variations pass.

### C-22 — Dual-Statement Prevents-Rule Redundancy *(NEW v7)*

- **Weight**: aspirational | **Category**: structure
- **Text**: The `prevents:` zero-score rule for the Breaks field (C-20) appears in two structurally distinct locations within the instruction: (1) inside the action template definition section and (2) inside a separate pre-write check construct — lookup table, decision matrix, or checklist — placed immediately before the action template. C-20 tests whether the zero-score `prevents:` requirement exists somewhere in the instruction; C-22 tests whether it is stated at two independent positions such that if the model skips one trigger surface the other still fires. The pre-write check table operates as a generation friction point: it forces the model to look up each condition's score before filling the Breaks field, catching the zero-score case at decision time. A redundant enforcement surface is structurally stronger than a single statement, however prominent — the model must pass through both checkpoints to produce a compliant output. A single statement of the rule, even in expanded or emphasized form, satisfies C-20 but fails C-22.
- **Pass condition**: The instruction contains two distinct occurrences of the `prevents:` zero-score requirement: one inside the action template definition and one inside a separate pre-write check structure (table mapping condition score ranges to required field formats, checklist, or equivalent). The two occurrences must be in structurally different locations — a repeated sentence within the same paragraph does not satisfy this criterion. If C-20 fails, this criterion automatically fails.
- **Derived from**: R6 excellence signal — V-05. **Passes**: V-05.

### C-23 — Two-Level Nearest-Miss Cascade *(NEW v7)*

- **Weight**: aspirational | **Category**: depth
- **Text**: When no qualifying 1-away gaps exist, the if-none clause outputs two cascade levels: Level 1 names the topic or milestone closest to the 1-away threshold with its numeric gap, and Level 2 names the topic or milestone closest to the 2-away threshold with its numeric gap. C-21 requires a single named nearest-miss pointer; C-23 requires two-level depth, converting the null state into a two-sprint trajectory. A single-level nearest-miss (Level 1 only) satisfies C-21 but fails C-23. Both levels must carry a specific topic or milestone name and a numeric step count. The two-sprint structure means a reader who finds nothing at threshold 1 is shown not only the next most actionable target but the one after that, enabling forward planning without re-running the skill.
- **Pass condition**: The instruction's if-none clause for the 1-Away section requires two named levels when no 1-away gaps exist: Level 1 (closest to 1-away threshold, with specific topic name and numeric gap) and Level 2 (closest to 2-away threshold, with specific topic name and numeric gap). An instruction that requires only one fallback level passes C-21 but fails C-23. Both levels must be explicitly required — an instruction that shows a two-level example without requiring both levels fails. If C-21 fails, this criterion automatically fails.
- **Derived from**: R6 excellence signal — V-02 (Cascading Nearest-Miss), V-04 (3-Role + Worked Examples). **Passes**: V-02, V-04.

---

## Scoring Reference

| Tier | Criteria | Count | Max contribution |
|------|----------|-------|-----------------|
| Essential | C-01 – C-05 | 5 | 60 pts |
| Recommended | C-06 – C-08 | 3 | 30 pts |
| Aspirational | C-09 – C-23 | 15 | 10 pts |

**Aspirational per-criterion weight**: 10/15 pts (~0.67). Scores are reported to one decimal place.

**Golden threshold**: All 5 essential pass + composite >= 80.

**R6 variation scores against v7**:

| Variation | C-22 | C-23 | Aspirational (15) | Total |
|-----------|------|------|-------------------|-------|
| V-01 All-Tables Scorecard | FAIL | FAIL | 13/15 × 10 = 8.67 | **98.7** |
| V-02 Cascading Nearest-Miss | FAIL | PASS | 14/15 × 10 = 9.33 | **99.3** |
| V-03 Declarative Spec | FAIL | FAIL | 13/15 × 10 = 8.67 | **98.7** |
| V-04 3-Role + Worked Examples | FAIL | PASS | 14/15 × 10 = 9.33 | **99.3** |
| V-05 Bidirectional Stamps | PASS | FAIL | 14/15 × 10 = 9.33 | **99.3** |

*V-02, V-04, and V-05 are co-ceiling-setters at ~99.3 against v7. No variation yet scores 100 against v7.*

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added C-11 (pre-compilation inertia diagnosis) and C-12 (full action-pattern cohesion) from V-04 R1 excellence signals; aspirational expands to 4 criteria |
| v3 | 2026-03-17 | Added C-13 (named completion gate in role sequence) and C-14 (per-action field template with explicit N/A prohibition) from R2 excellence signals; aspirational expands to 6 criteria at ~1.67 pts each |
| v4 | 2026-03-17 | Added C-15 (section-boundary gate as structural constraint), C-16 (quantified inertia with urgency tiers), and C-17 (evidence-first leaderboard before named pattern) from R3 excellence signals; aspirational expands to 9 criteria at ~1.11 pts each |
| v5 | 2026-03-17 | Added C-18 (gate markers as literal output lines) and C-19 (synthesis sentence with concrete numeric claim) from R4 excellence signals; aspirational expands to 11 criteria at ~0.91 pts each; total remains 100 |
| v6 | 2026-03-17 | Added C-20 (three-field action template with Breaks condition) and C-21 (1-away section nearest-miss fallback) from R5 excellence signals; aspirational expands to 13 criteria at ~0.77 pts each; V-02, V-03, V-04, V-05 co-ceiling at ~99.2 |
| v7 | 2026-03-17 | Added C-22 (dual-statement prevents-rule redundancy) and C-23 (two-level nearest-miss cascade) from R6 excellence signals; aspirational expands to 15 criteria at ~0.67 pts each; total remains 100; V-02, V-04, V-05 co-ceiling at ~99.3; ceiling open |

---

**Two patterns extracted, two criteria added.** The key structural distinctions:

- **C-22 vs C-20**: C-20 enforces that the `prevents:` zero-score rule exists in the instruction. C-22 enforces that it exists *twice* — in the template definition and in a separate pre-write check table. The pre-write table is a generation friction point that forces a score lookup at write time; the dual-statement creates a redundant trigger so that skipping one surface does not eliminate enforcement.

- **C-23 vs C-21**: C-21 enforces that the null case directs — it names a nearest-miss with a numeric gap. C-23 enforces that it directs *two steps forward* — Level 1 (closest to threshold 1) and Level 2 (closest to threshold 2). A single-level nearest-miss answers "what's next." A two-level cascade answers "what's next and what's after that," converting a null state into a two-sprint plan.
