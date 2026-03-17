Done. Here's a summary of what changed:

---

## v4 adds three new aspirational criteria

**C-15 — Section-Boundary Gate as Structural Constraint**
Tests whether the inertia→compilation ordering is encoded as a *section-label rule* (`"ASSESSMENT must close before FINDINGS opens. No exceptions."`) rather than a role-number pipeline. Harder to accidentally violate than C-13 because reordering named sections is visible in the output structure.
- **Derived from**: V-05 (SITREP Briefing). **Passes**: V-05 only.

**C-16 — Quantified Inertia with Urgency Tiers**
Tests whether the inertia diagnosis assigns a numeric score (e.g., 0–5) with named tier labels (Healthy / Monitor / Alert / Critical), making action priority derivable from the score rather than from judgment.
- **Derived from**: V-02 (Signal Health Score). **Passes**: V-02 only.

**C-17 — Evidence-First Leaderboard Before Named Pattern**
Tests whether the leaderboard precedes the inertia diagnosis — so the reader sees contributor data before the pattern is named. The Lone Wolf claim is then *confirmed* by evidence already on the page rather than announced as an assertion.
- **Derived from**: V-04 and V-05. **Passes**: V-04, V-05.

---

**Scoring**: Aspirational tier is now 9 criteria at ~1.11 pts each. Total remains 100. The R3 universal tie at 100/100 is broken: V-05 (98.9) leads, V-02 and V-04 score 97.8, V-01 and V-03 score 96.7. No variation yet scores 100 against v4 — the ceiling is open.
score rather than from reviewer judgment, making the output machine-readable as well as human-readable.

**C-17 added** — Evidence-First Leaderboard Before Named Pattern. C-11 constrains inertia diagnosis to precede topic compilation. C-17 constrains the contributor leaderboard to precede the inertia diagnosis. V-04's "Role 1 = LEADERBOARD BUILDER" and V-05's "Section 1 SITUATION contains the contributor leaderboard" are the differentiating constructs. When the reader sees the contributor distribution before the pattern is named, the inertia claim is *confirmed* by data already on the page rather than *announced* as a new assertion. This produces a more credible diagnosis for the same pattern.

**Scoring updated** — Aspirational tier now contains 9 criteria at 10/9 pts each (~1.11). Total remains 100. V-05 scores 98.9 against v4 (C-16 FAIL — no numeric health score). V-02 and V-04 score 97.8 (each fail two of the three new criteria). V-01 and V-03 score 96.7 (fail all three new criteria).

---

## Essential Criteria (correctness baseline — 60% of score)

*Five criteria at 12 pts each. All five must pass to reach the golden threshold.*

### C-01 -- All Discovered Topics Listed with Named Gap Term

- **Weight**: essential
- **Category**: correctness
- **Text**: The output includes one row or entry for every topic discovered in the workspace scan. The instruction designates a specific named term for the condition where a topic appears in the scan but is absent from the output (e.g., "matrix gap", "compiler gap", "findings gap", or an equivalent label). The named gap makes the omission auditable: a reviewer scanning the output can identify exactly which topics were found but not compiled.
- **Pass condition**: Every topic from the scan appears in the output as a distinct row or block. If the workspace contains no topics, the output writes an explicit "no topics found" statement rather than an empty section. An output that silently drops topics without reporting the omission using the instruction's designated gap term fails. An instruction that defines the gap condition only in the pass condition (not in the instruction text itself) fails.

### C-02 -- Per-Topic Achievement Evaluation with Exact Names

- **Weight**: essential
- **Category**: correctness
- **Text**: For every discovered topic, the output presents both which achievements are earned and which are not yet earned. Achievement definitions applied must include at minimum: First Signal (>= 1 file), Signal Depth (>= 3 files), Full Sweep (signals span >= 3 namespaces), Solo Pioneer (exactly 1 contributor, >= 1 signal), and Team Topic (>= 2 contributors with >= 1 signal each).
- **Pass condition**: Every topic from the scan appears in an achievements section with at least one explicit earned or locked achievement listed. A topic row showing only `---` without checking any of the five defined achievements fails. Achievement names must match the defined set — paraphrasing ("Team Coverage" for "Team Topic") fails.

### C-03 -- All Three Team Milestones Present with Exact Names

- **Weight**: essential
- **Category**: correctness
- **Text**: The output reports all three team milestones using their exact names: "first team signal", "shared coverage", and "debate starter". Each milestone includes a status (EARNED or NOT YET) and supporting evidence (file path, contributor count, or namespace list).
- **Pass condition**: All three milestone names appear verbatim. A milestone labeled "first signal posted" instead of "first team signal", or "cross-contributor coverage" instead of "shared coverage", fails. Each milestone has a non-empty evidence field — "---" without explanation counts as a gap. A missing milestone section fails this criterion entirely.

### C-04 -- Contributor Leaderboard Present and Ranked

- **Weight**: essential
- **Category**: coverage
- **Text**: A contributor leaderboard section is present, ranked in descending order by signal count (or equivalent primary metric). Each entry includes at minimum: rank, contributor identity, total signal count, and topics covered. If contributor metadata is not extractable from the workspace, the leaderboard states this explicitly rather than being omitted.
- **Pass condition**: A leaderboard section exists with at least one entry. If no contributor attribution is detectable (no frontmatter `author:` / `contributor:` fields, no parseable filename prefixes), the output writes one explicit row stating "no contributor metadata found" — this passes. A missing leaderboard section fails regardless of workspace state. An unranked list fails.

### C-05 -- Specific Next Actions Naming Namespace and Achievement

- **Weight**: essential
- **Category**: behavior
- **Text**: The output includes at least 3 recommended next actions. Each action must name (1) a specific namespace and topic (not just a category), and (2) the exact achievement or milestone name it unlocks. Generic advice such as "add more signals" or "increase namespace coverage" without naming a target fails.
- **Pass condition**: At least 3 actions are present. Each action names a namespace (e.g., `scout`, `flow`, `trace`) and a topic path (e.g., `scout/competitors`), and references an achievement or milestone by its exact name from the defined set. An action that names a topic without naming the unlocked achievement fails. An action that names an achievement without a specific namespace+topic fails.

---

## Recommended Criteria (improve output quality — 30% of score)

*Three criteria at 10 pts each.*

### C-06 -- Earned / Available Achievement Separation

- **Weight**: recommended
- **Category**: format
- **Text**: The output visually or structurally separates earned achievements from locked/available achievements for each topic. A reader scanning the output can immediately distinguish what the team has already unlocked from what remains.
- **Pass condition**: The achievements section uses a consistent structural indicator to separate earned from locked (e.g., distinct subsections, table columns, badge markers like checkmark vs circle, or equivalent). A flat list of achievements without any earned/locked distinction fails. Topics with only earned or only locked achievements need only show one group — but must not mix the two without differentiation.

### C-07 -- 1-Away Gap Detection

- **Weight**: recommended
- **Category**: depth
- **Text**: The output identifies achievements or milestones that are exactly one step away from being unlocked, with the gap quantified precisely (e.g., "needs 1 more signal", "needs 1 more contributor", "needs 1 more namespace").
- **Pass condition**: A dedicated "close to unlock" or "almost there" section exists. Each entry names the topic or milestone, states the exact numeric gap (not "a few more"), and names the target achievement. If no gaps are within 1 step, the section states this explicitly rather than being omitted. A generic "keep adding signals" note without per-achievement gap counts fails.

### C-08 -- Empty Workspace Graceful Handling

- **Weight**: recommended
- **Category**: behavior
- **Text**: When `simulations/` is empty or absent, the output explicitly acknowledges this state and still produces all required sections (achievements, milestones, leaderboard, next actions) with empty or "NOT YET" values. The skill does not silently omit sections or produce a one-line error and stop.
- **Pass condition**: If evaluated on an empty workspace, all required sections appear with appropriate empty-state values. All three team milestones show "NOT YET". The leaderboard section states "no signals found". Next actions are still written (even if they all point to bootstrapping the first signal). If evaluated on a non-empty workspace, this criterion passes automatically — it is only falsifiable on the empty case.

---

## Aspirational Criteria (ceiling-raising — 10% of score)

*Nine criteria sharing 10 pts total (~1.11 pts each). A perfect aspirational score requires all nine.*

### C-09 -- Cross-Topic Team Insight

- **Weight**: aspirational
- **Category**: depth
- **Text**: The output includes exactly one synthesizing sentence or short paragraph drawing a cross-topic or cross-contributor conclusion that is not visible from any single-topic view. The insight is stated as a named finding (e.g., "Alice spans 4 topics — highest breadth on the team") using specific numbers and topic or contributor names.
- **Pass condition**: A team insight statement appears that (1) references two or more topics or contributors in a single observation, (2) uses at least one specific number or name, and (3) closes with a recommended implication for the team. A list of per-topic statistics does not satisfy this criterion — the insight must be a synthesizing sentence that emerges from comparing across rows, not restating them.

### C-10 -- Inertia Pattern Identification and Anti-Inertia Actions

- **Weight**: aspirational
- **Category**: depth
- **Text**: The output names the team's current stagnation pattern (e.g., "Lone Wolf" — single contributor dominates; "Namespace Tunnel" — all signals in one namespace; "Empty Start" — no signals yet; "Stale Coverage" — signals exist but no recent activity; "Shallow Spread" — many topics with only 1 signal each) and ties at least one recommended next action back to breaking that named pattern.
- **Pass condition**: A stagnation pattern is named (either from the listed examples or an equivalently specific label). The pattern is supported by evidence from the scan (e.g., "single contributor accounts for 100% of signals"). At least one next action explicitly references breaking this pattern by name. A generic observation ("the team should diversify") without naming the pattern fails. If the workspace shows no stagnation pattern, the output states this and this criterion is considered passed by exception.
- **Change from v1**: Added "Shallow Spread" (many topics each with only 1 signal) to the named pattern vocabulary.

### C-11 -- Pre-Compilation Inertia Diagnosis

- **Weight**: aspirational
- **Category**: depth
- **Text**: The stagnation pattern diagnosis (C-10) appears before the topic-by-topic achievement compilation, not as a closing appendix. By naming the inertia pattern upfront, the pattern frames how the team reads the entire achievement grid — every locked achievement is visible as a consequence of the named pattern rather than an isolated gap.
- **Pass condition**: The inertia diagnosis section (or equivalent named diagnostic step) is positioned before the per-topic achievement section in the output. If C-10 fails (no pattern named), this criterion automatically fails. A closing "team insight" note that diagnoses stagnation only after the full topic compilation fails — the diagnosis must precede the compilation, not follow it.
- **Derived from**: V-04 (Role Sequence + Inertia Framing) — the Inertia Diagnostician role fired before the Compiler role, forcing the pattern to frame the output.

### C-12 -- Full Action-Pattern Cohesion

- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every recommended next action (not just one) explicitly ties back to breaking the named stagnation pattern, referencing the pattern by name. This elevates the actions section from a list of independent recommendations into a coordinated response to a diagnosed team condition.
- **Pass condition**: Every action in the next-actions section names the stagnation pattern it addresses (or explicitly states it breaks a different component of the same pattern). An action that unlocks an achievement without referencing the pattern fails. If fewer than all actions name the pattern, this criterion fails — partial coverage (e.g., only the first action names the pattern) is not sufficient. If C-10 fails, this criterion automatically fails.
- **Derived from**: V-04 (Role Sequence + Inertia Framing) — "Anti-Inertia Next Actions" required each action to tie back to breaking the named pattern, distinguishing it from variates that named the pattern but then decoupled actions from it.

### C-13 -- Named Completion Gate in Role Sequence

- **Weight**: aspirational
- **Category**: structure
- **Text**: The skill defines a named role sequence in which the inertia diagnosis role holds an explicit completion gate before any topic-compilation or achievement-grid role begins. The gate is structural: the instruction text assigns positions by name (e.g., "Role 1: Inertia Diagnostician fires before Role 3: Topic Compiler") such that reordering reads as a rule violation, not a style variation. Prose ordering ("diagnose stagnation, then compile topics") does not satisfy this criterion — the position must be named.
- **Pass condition**: (1) The inertia diagnosis role or phase is assigned an explicit position label (role number, "first", or equivalent) in the instruction text. (2) A dependency constraint is stated (e.g., "fires before", "must complete before", "completion gate") that makes the ordering structural rather than advisory. A skill that achieves correct ordering in output without naming the gate mechanism fails. If C-11 fails, this criterion automatically fails.
- **Derived from**: R2 excellence signal — V-01 ("Role 1 = Inertia Diagnostician with completion gate before Role 3") and V-04 ("Inertia Diagnostician fires before Compiler") both named the gate; V-03 (coach voice) and V-05 (lifecycle phases) produced correct ordering by convention but provided no structural gate, making them vulnerable to generation reordering.

### C-14 -- Per-Action Field Template with Explicit Failure-Mode Prohibition

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The next-actions section uses a per-action structured field template that includes a named pattern-reference field, and the instruction text explicitly states that omitting that field is not permitted — naming the prohibited escape hatch (e.g., "No action may omit field 3. `N/A` is not valid."). The prohibition must appear in the instruction, not only in the pass condition. This distinguishes C-14 from C-12: C-12 tests whether all actions name the pattern; C-14 tests whether the instruction text itself forecloses the omission path.
- **Pass condition**: (1) The action template names a pattern-reference field by position number or label. (2) The instruction text includes an explicit prohibition statement that names the failure mode (omission or a specific invalid value such as "N/A"). A skill that produces full C-12 compliance without stating the prohibition in the instruction text fails C-14 — the prohibition must be present in the skill definition, not inferred from observed output. If C-12 fails, this criterion automatically fails.
- **Derived from**: R2 excellence signal — V-01's "No action may omit field 3. `N/A` is not valid." is the distinguishing construct; V-04 achieves C-12 through structural section design ("Anti-Inertia Next Actions") but omits the explicit N/A prohibition, making it the critical differentiator between the two 100-point variates under v2 scoring.

### C-15 -- Section-Boundary Gate as Structural Constraint

- **Weight**: aspirational
- **Category**: structure
- **Text**: The inertia-before-compilation ordering (C-11) is encoded as a *section-boundary constraint* — a rule that names sections by label and states that one must close before another opens (e.g., "ASSESSMENT must close before FINDINGS opens. No exceptions."). This is structurally stronger than a role-number gate (C-13): violating a section-boundary constraint requires reordering named sections that are visible in the output structure, whereas skipping a step number in a procedural list can occur without leaving a trace. C-13 and C-15 are independent — a skill may satisfy either, both, or neither.
- **Pass condition**: The instruction text includes a section-boundary rule that (1) names both the closing section and the opening section by label (not by role number), and (2) uses language expressing that the transition is mandatory ("must close before", "must be complete before", "No exceptions", or equivalent). A gate expressed as "Role 1 fires before Role 2" satisfies C-13 but not C-15 — the gate must reference named sections, not role or step indices. If C-11 fails, this criterion automatically fails.
- **Derived from**: R3 excellence signal — V-05 (SITREP Briefing): `"ASSESSMENT must close before FINDINGS opens. No exceptions."` is a template-level constraint rather than a procedural pipeline instruction, making the ordering enforceable at the format level.

### C-16 -- Quantified Inertia with Urgency Tiers

- **Weight**: aspirational
- **Category**: depth
- **Text**: The inertia diagnosis section assigns a numeric severity score to the team's health (e.g., a 0–5 scale) and maps score ranges to named urgency tiers (e.g., Healthy / Monitor / Alert / Critical). The next-actions section references the urgency tier or score when ordering or framing recommendations, making action priority derivable from the score rather than from reviewer judgment.
- **Pass condition**: (1) The inertia/health section includes a numeric score (integer or float on a stated scale) representing overall pattern severity. (2) Named tier labels are defined at score boundaries (at least two tiers, e.g., "0–1: Healthy, 2–3: Monitor, 4–5: Alert/Critical"). (3) At least one next action references the urgency tier or score as the reason for its priority (e.g., "Priority: Critical — score 5/5"). A named pattern without a score fails. A score without tier labels fails. If C-10 fails, this criterion automatically fails.
- **Derived from**: R3 excellence signal — V-02 (Signal Health Score): the 0–5 scoring system with tier labels converted the inertia diagnosis from a qualitative judgment into a scored severity signal, making action priority computable rather than evaluated.

### C-17 -- Evidence-First Leaderboard Before Named Pattern

- **Weight**: aspirational
- **Category**: structure
- **Text**: The contributor leaderboard is computed and displayed as the first section or role in the output — before the inertia diagnosis, and therefore before the pattern is named. When the reader encounters the contributor distribution before the pattern label, the inertia claim is confirmed by data already visible on the page rather than announced as a new assertion. This produces a more credible diagnosis for the same pattern: a "Lone Wolf" finding is self-evident from the leaderboard rather than imposed by the instruction.
- **Pass condition**: The contributor leaderboard section appears earlier in the output than the inertia diagnosis section. The inertia diagnosis section references the leaderboard data explicitly when naming the pattern (e.g., "As shown above, contributor X accounts for Y% of signals"). An output where the leaderboard follows the inertia diagnosis fails, even if C-04 passes (C-04 tests presence and ranking; C-17 tests position relative to the diagnosis). If C-10 fails, this criterion automatically fails.
- **Derived from**: R3 excellence signal — V-04 (Leaderboard-First): "Role 1 is LEADERBOARD BUILDER (runs first)"; V-05 (SITREP Briefing): "Section 1 SITUATION has contributor leaderboard table" preceding "Section 2 ASSESSMENT". Both place contributor data before pattern interpretation, distinguishing them from V-01, V-02, and V-03 where the inertia diagnosis precedes or runs independently of the leaderboard.

---

## Scoring Reference

| Tier | Criteria | Count | Max contribution |
|------|----------|-------|-----------------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 pts |
| Recommended | C-06, C-07, C-08 | 3 | 30 pts |
| Aspirational | C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17 | 9 | 10 pts |

**Aspirational per-criterion weight**: 10/9 pts (~1.11). Scores are reported to one decimal place.

**Golden threshold**: All 5 essential pass + composite >= 80.

**Minimum passing composite** (all essential, no recommended, no aspirational):
`5/5 * 60 + 0/3 * 30 + 0/9 * 10 = 60` — below golden threshold.

**Typical floor for golden** (all essential + 2/3 recommended):
`60 + 20 + 0 = 80` — exactly at golden threshold.

**R3 variation scores against v4 rubric**:

| Variation | C-15 | C-16 | C-17 | Aspirational (9) | Total |
|-----------|------|------|------|-----------------|-------|
| V-01 Achievement Matrix | FAIL | FAIL | FAIL | 6/9 * 10 = 6.7 | **96.7** |
| V-02 Signal Health Score | FAIL | PASS | FAIL | 7/9 * 10 = 7.8 | **97.8** |
| V-03 CLI Terminal Dashboard | FAIL | FAIL | FAIL | 6/9 * 10 = 6.7 | **96.7** |
| V-04 Leaderboard-First | FAIL | FAIL | PASS | 7/9 * 10 = 7.8 | **97.8** |
| V-05 SITREP Briefing | PASS | FAIL | PASS | 8/9 * 10 = 8.9 | **98.9** |

*All 5 pass C-09 through C-14 (inherited from R3 universal 100/100). New criteria create differentiation: V-05 is the new ceiling-setter at 98.9. No variation yet scores 100 against v4.*

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added "Shallow Spread" to C-10 pattern vocabulary; added C-11 (pre-compilation inertia diagnosis) and C-12 (full action-pattern cohesion) from V-04 R1 excellence signals |
| v3 | 2026-03-17 | Added C-13 (named completion gate in role sequence) and C-14 (per-action field template with explicit N/A prohibition) from R2 scorecard excellence signals; aspirational tier expands to 6 criteria at ~1.67 pts each; total remains 100 |
| v4 | 2026-03-17 | Added C-15 (section-boundary gate as structural constraint), C-16 (quantified inertia with urgency tiers), and C-17 (evidence-first leaderboard before named pattern) from R3 scorecard excellence signals; aspirational tier expands to 9 criteria at ~1.11 pts each; total remains 100; V-05 is new ceiling at 98.9 |
