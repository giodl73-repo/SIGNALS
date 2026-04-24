Here is the complete updated rubric:

---

## Quest Rubric — corps-leaderboard v5

### What changed: v4 → v5

Two new aspirational criteria extracted from R4 scorecard excellence signals.

**C-18 — Gate Markers as Literal Output Lines**
Tests whether section-transition announcements appear as machine-readable lines in the output artifact itself (e.g., `[GATE 2: SIGNAL HEALTH SCORE closed. ACHIEVEMENT COMPILATION opens now.]`), rather than only as ordering rules in the instruction text. C-15 tests whether the instruction contains a named section-boundary constraint; C-18 tests whether the transition is announced at the boundary as a printed line. When gate markers are output-layer artifacts, compliance is auditable by scanning the output for expected announcement lines — a reordered or skipped gate leaves a visible gap. The constraint distinguishes V-02 (Triple-Gate Pipeline) from all other R4 variations: V-02 is the only variation where section-transition gates produce detectable artifacts in the output.
- **Derived from**: V-02 (Triple-Gate Pipeline). **Passes**: V-02 only.

**C-19 — Synthesis Sentence with Concrete Numeric Claim**
Tests whether the team synthesis sentence (C-08) is required to include at least one concrete numeric value — a contributor count, signal count, namespace count, or topic count — alongside the cross-section observation. C-08 requires a synthesizing sentence that draws a conclusion not visible from any individual-topic view; C-19 requires that the observation be quantified. "3 of 4 contributors have signals in 2+ namespaces" is verifiable; "the team shows broad distribution" is not. The constraint is encoded in the instruction as a minimum requirement on the synthesis sentence. V-03 (Conversational Coach) is the only R4 variation that adds the numeric requirement to its C-08 synthesis clause.
- **Derived from**: V-03 (Conversational Coach). **Passes**: V-03 only.

**Scoring updated** — Aspirational tier now contains 11 criteria at 10/11 pts each (~0.91). Total remains 100. V-02 and V-03 become co-ceiling-setters at 99.1 against v5 (each fails one of the two new criteria). V-01 scores 98.2 (fails both new criteria). No variation yet scores 100 against v5 — the ceiling is open.

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

### C-08 -- Cross-Topic Team Synthesis

- **Weight**: recommended
- **Category**: depth
- **Text**: The output includes exactly one synthesizing sentence or short paragraph drawing a cross-topic or cross-contributor conclusion that is not visible from any single-topic view. The synthesis names topics or contributors and draws an implication that spans the full output.
- **Pass condition**: A team synthesis sentence appears that (1) references two or more topics or contributors in a single observation, (2) uses at least one specific name from the workspace, and (3) closes with a recommended implication for the team. A list of per-topic statistics does not satisfy this criterion — the synthesis must be a single sentence that emerges from comparing across rows, not restating them.

---

## Aspirational Criteria (ceiling-raising — 10% of score)

*Eleven criteria sharing 10 pts total (10/11 pts each, ~0.91). A perfect aspirational score requires all eleven.*

### C-09 -- Leaderboard Cited in Stagnation Evidence

- **Weight**: aspirational
- **Category**: depth
- **Text**: When the inertia diagnosis fires a pattern that is corroborated by contributor distribution data (e.g., "Lone Wolf" — single dominant contributor), the evidence for that pattern cites the contributor leaderboard explicitly by row or entry, rather than re-stating contributor counts independently. This creates a traceable chain from named pattern to visible leaderboard evidence already on the page.
- **Pass condition**: When a leaderboard-corroborated pattern is diagnosed (Lone Wolf, Stale Coverage, or equivalent), the evidence field or supporting note references the leaderboard by rank or contributor name (e.g., "Contributor X holds rank 1 with 100% of signals — see leaderboard row 1"). A diagnosis that names the pattern without cross-linking to the leaderboard row fails. If the workspace shows no stagnation pattern, or if the pattern is not leaderboard-corroborated (e.g., Empty Start), this criterion is passed by exception.

### C-10 -- Named Stagnation Pattern with Evidence

- **Weight**: aspirational
- **Category**: depth
- **Text**: The output names the team's current stagnation pattern using a specific label from the canonical set: "Empty Start" (no signals yet), "Lone Wolf" (single contributor dominates), "Namespace Tunnel" (all signals in one namespace), "Stale Coverage" (signals exist but no recent activity), "Shallow Spread" (many topics with only 1 signal each). The pattern is supported by evidence from the workspace scan, and at least one recommended next action ties back to breaking that named pattern.
- **Pass condition**: A stagnation pattern is named using one of the listed labels (or an equivalently specific label if the workspace exhibits a distinct condition). The pattern is supported by evidence (e.g., "single contributor accounts for 100% of signals"). At least one next action explicitly references breaking this pattern by name. A generic observation ("the team should diversify") without naming the pattern fails. If the workspace shows no stagnation pattern, the output states this and this criterion is considered passed by exception.

### C-11 -- Health Diagnosis Precedes Topic Compilation

- **Weight**: aspirational
- **Category**: structure
- **Text**: The stagnation pattern diagnosis (C-10) appears before the topic-by-topic achievement compilation in the output, not as a closing appendix. By naming the inertia pattern upfront, the pattern frames how the team reads the entire achievement grid — every locked achievement becomes visible as a consequence of the named pattern rather than an isolated gap.
- **Pass condition**: The inertia or health diagnosis section (or equivalent named diagnostic step) is positioned before the per-topic achievement section in the output. If C-10 fails (no pattern named), this criterion automatically fails. A closing "team insight" note that diagnoses stagnation only after the full topic compilation fails — the diagnosis must precede the compilation, not follow it.

### C-12 -- Workspace-Empty Path Handled

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The instruction explicitly defines what to output when the workspace contains no signals. All required sections still appear with empty-state values (achievements with no topics, milestones at NOT YET, leaderboard noting no contributors, next actions pointing to bootstrapping the first signal). The skill does not silently collapse to a one-line error or omit sections on an empty workspace.
- **Pass condition**: The instruction includes an explicit clause covering the empty-workspace case, stating what each section should contain when no topics or signals are found. A skill that produces correct empty-state output by convention (without explicit instruction) fails — the clause must appear in the instruction text. An instruction that handles non-empty workspaces only, leaving the empty case implicit, fails.

### C-13 -- Named Completion Gate in Role Sequence

- **Weight**: aspirational
- **Category**: structure
- **Text**: The skill defines a named role or phase sequence in which the inertia diagnosis role holds an explicit completion gate before any topic-compilation or achievement-grid role begins. The gate is structural: the instruction text assigns positions by name (e.g., "Role 1: Inertia Diagnostician fires before Role 3: Topic Compiler") such that reordering reads as a rule violation, not a style variation. Prose ordering ("diagnose stagnation, then compile topics") does not satisfy this criterion — the position must be named.
- **Pass condition**: (1) The inertia diagnosis role or phase is assigned an explicit position label (role number, "first", or equivalent) in the instruction text. (2) A dependency constraint is stated (e.g., "fires before", "must complete before", "completion gate") that makes the ordering structural rather than advisory. A skill that achieves correct ordering in output without naming the gate mechanism fails. If C-11 fails, this criterion automatically fails.

### C-14 -- Per-Action Breaks Field with N/A Prohibition

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The next-actions section uses a per-action structured field template that includes a named "Breaks" field, and the instruction text explicitly states that this field cannot be omitted and that "N/A" is not a valid value. The prohibition must appear in the instruction, not only in the pass condition. This enforces that every action declares what pattern or anti-pattern it breaks rather than leaving the connection implicit.
- **Pass condition**: (1) The action template names a Breaks field by label. (2) The instruction text includes an explicit prohibition statement that names the failure mode: omission is not permitted, and "N/A" (or an equivalent escape value) is explicitly stated as invalid. A skill that produces full Breaks field coverage without stating the prohibition in the instruction text fails — the prohibition must be present in the skill definition, not inferred from observed output.

### C-15 -- Section-Boundary Gate as Structural Constraint

- **Weight**: aspirational
- **Category**: structure
- **Text**: The inertia-before-compilation ordering (C-11) is encoded as a *section-boundary constraint* — a rule that names sections by label and states that one must close before another opens (e.g., "ASSESSMENT must close before FINDINGS opens. No exceptions."). This is structurally stronger than a role-number gate (C-13): violating a section-boundary constraint requires reordering named sections that are visible in the output structure, whereas skipping a step number in a procedural list can occur without leaving a trace. C-13 and C-15 are independent — a skill may satisfy either, both, or neither.
- **Pass condition**: The instruction text includes a section-boundary rule that (1) names both the closing section and the opening section by label (not by role number), and (2) uses language expressing that the transition is mandatory ("must close before", "must be complete before", "No exceptions", or equivalent). A gate expressed as "Role 1 fires before Role 2" satisfies C-13 but not C-15 — the gate must reference named sections, not role or step indices. If C-11 fails, this criterion automatically fails.
- **Derived from**: R3 excellence signal — V-05 (SITREP Briefing).

### C-16 -- Quantified Inertia with Urgency Tiers

- **Weight**: aspirational
- **Category**: depth
- **Text**: The inertia diagnosis section assigns a numeric severity score to the team's health (e.g., a 0–5 scale) and maps score ranges to named urgency tiers (e.g., Healthy / Monitor / Alert / Critical). The next-actions section references the urgency tier or score when ordering or framing recommendations, making action priority derivable from the score rather than from reviewer judgment.
- **Pass condition**: (1) The inertia/health section includes a numeric score (integer or float on a stated scale) representing overall pattern severity. (2) Named tier labels are defined at score boundaries (at least two tiers, e.g., "0–1: Healthy, 2–3: Monitor, 4–5: Alert/Critical"). (3) At least one next action references the urgency tier or score as the reason for its priority (e.g., "Priority: Critical — score 5/5"). A named pattern without a score fails. A score without tier labels fails. If C-10 fails, this criterion automatically fails.
- **Derived from**: R3 excellence signal — V-02 (Signal Health Score).

### C-17 -- Evidence-First Leaderboard Before Named Pattern

- **Weight**: aspirational
- **Category**: structure
- **Text**: The contributor leaderboard is computed and displayed as the first section or role in the output — before the inertia diagnosis, and therefore before the pattern is named. When the reader encounters the contributor distribution before the pattern label, the inertia claim is confirmed by data already visible on the page rather than announced as a new assertion. This produces a more credible diagnosis for the same pattern: a "Lone Wolf" finding is self-evident from the leaderboard rather than imposed by the instruction.
- **Pass condition**: The contributor leaderboard section appears earlier in the output than the inertia diagnosis section. The inertia diagnosis section references the leaderboard data explicitly when naming the pattern (e.g., "As shown above, contributor X accounts for Y% of signals"). An output where the leaderboard follows the inertia diagnosis fails, even if C-04 passes. If C-10 fails, this criterion automatically fails.
- **Derived from**: R3 excellence signal — V-04 (Leaderboard-First) and V-05 (SITREP Briefing).

### C-18 -- Gate Markers as Literal Output Lines *(NEW v5)*

- **Weight**: aspirational
- **Category**: structure
- **Text**: The section-transition gates are announced as machine-readable lines in the output artifact itself — not only encoded as ordering rules in the instruction text. A gate marker appears at the section boundary as a printed line (e.g., `[GATE 2: SIGNAL HEALTH SCORE closed. ACHIEVEMENT COMPILATION opens now.]`). When gate markers are output-layer artifacts, compliance is auditable by scanning the output for expected announcement lines; a reordered or skipped gate leaves a visible gap. This is structurally stronger than C-15: C-15 tests whether the instruction has a named section-boundary rule; C-18 tests whether the transition produces a detectable artifact in the output.
- **Pass condition**: At least one section-transition boundary is announced by a literal printed line in the output at the exact transition point. The instruction specifies the gate marker format and which section transitions must produce a gate announcement line. An instruction that enforces ordering through section labels alone (C-15) without printing gate announcement lines fails. The gate marker must appear in the output (not just in the instruction text). If C-15 fails, this criterion automatically fails.
- **Derived from**: R4 excellence signal — V-02 (Triple-Gate Pipeline). **Passes**: V-02 only.

### C-19 -- Synthesis Sentence with Concrete Numeric Claim *(NEW v5)*

- **Weight**: aspirational
- **Category**: depth
- **Text**: The team synthesis sentence (C-08) is required by the instruction to include at least one concrete numeric value — a contributor count, signal count, namespace count, or topic count — alongside the cross-section observation. C-08 requires a synthesizing sentence that draws a conclusion across topics or contributors; C-19 requires that the observation be anchored to a specific number, making the claim verifiable against workspace data. "3 of 4 contributors have signals in 2+ namespaces" is verifiable; "the team shows broad distribution" is not.
- **Pass condition**: The instruction text for the synthesis sentence includes an explicit numeric requirement (e.g., "include a specific number", "reference exact counts", "must name >= 2 topics or contributors and include a specific number"). The output synthesis sentence contains a numeric value that is extractable and checkable against workspace data. A synthesizing sentence that names topics or contributors without a concrete number fails. If C-08 fails, this criterion automatically fails.
- **Derived from**: R4 excellence signal — V-03 (Conversational Coach). **Passes**: V-03 only.

---

## Scoring Reference

| Tier | Criteria | Count | Max contribution |
|------|----------|-------|-----------------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 pts |
| Recommended | C-06, C-07, C-08 | 3 | 30 pts |
| Aspirational | C-09 through C-19 | 11 | 10 pts |

**Aspirational per-criterion weight**: 10/11 pts (~0.91). Scores are reported to one decimal place.

**Golden threshold**: All 5 essential pass + composite >= 80.

**R4 variation scores against v5**:

| Variation | C-18 | C-19 | Aspirational (11) | Total |
|-----------|------|------|-------------------|-------|
| V-01 All-Tables Scorecard | FAIL | FAIL | 9/11 * 10 = 8.18 | **98.2** |
| V-02 Triple-Gate Pipeline | PASS | FAIL | 10/11 * 10 = 9.09 | **99.1** |
| V-03 Conversational Coach | FAIL | PASS | 10/11 * 10 = 9.09 | **99.1** |

*V-02 and V-03 are co-ceiling-setters. No variation yet scores 100 against v5.*

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added "Shallow Spread" to C-10 pattern vocabulary; added C-11 (pre-compilation inertia diagnosis) and C-12 (full action-pattern cohesion) from V-04 R1 excellence signals |
| v3 | 2026-03-17 | Added C-13 (named completion gate in role sequence) and C-14 (per-action field template with explicit N/A prohibition) from R2 scorecard excellence signals; aspirational tier expands to 6 criteria at ~1.67 pts each; total remains 100 |
| v4 | 2026-03-17 | Added C-15 (section-boundary gate as structural constraint), C-16 (quantified inertia with urgency tiers), and C-17 (evidence-first leaderboard before named pattern) from R3 scorecard excellence signals; aspirational tier expands to 9 criteria at ~1.11 pts each; total remains 100; V-05 is new ceiling at 98.9 |
| v5 | 2026-03-17 | Added C-18 (gate markers as literal output lines) and C-19 (synthesis sentence with concrete numeric claim) from R4 scorecard excellence signals; aspirational tier expands to 11 criteria at ~0.91 pts each; total remains 100; V-02 and V-03 are co-ceiling-setters at 99.1; no variation yet scores 100 against v5 |

---

**Two patterns extracted, two criteria added.** The key structural distinction:

- **C-18** closes the gap between "ordering is a rule" and "ordering is observable in the artifact." C-15 enforces via instruction; C-18 enforces via output trace. V-02 is the only R4 variation where a skipped gate is detectable without re-reading the instruction.

- **C-19** closes the gap between "synthesis references" and "synthesis quantifies." C-08 requires a cross-section observation; C-19 requires that observation to carry a checkable number. V-03 is the only R4 variation that encodes the numeric requirement in the instruction rather than relying on model judgment.
ull action-pattern cohesion) from V-04 R1 excellence signals |
| v3 | 2026-03-17 | Added C-13 (named completion gate in role sequence) and C-14 (per-action field template with explicit N/A prohibition) from R2 scorecard excellence signals; aspirational tier expands to 6 criteria at ~1.67 pts each; total remains 100 |
| v4 | 2026-03-17 | Added C-15 (section-boundary gate as structural constraint), C-16 (quantified inertia with urgency tiers), and C-17 (evidence-first leaderboard before named pattern) from R3 scorecard excellence signals; aspirational tier expands to 9 criteria at ~1.11 pts each; total remains 100; V-05 is new ceiling at 98.9 |
| v5 | 2026-03-17 | Added C-18 (gate markers as literal output lines) and C-19 (synthesis sentence with concrete numeric claim) from R4 scorecard excellence signals; aspirational tier expands to 11 criteria at ~0.91 pts each; total remains 100; V-02 and V-03 are co-ceiling-setters at 99.1; no variation yet scores 100 against v5 |
