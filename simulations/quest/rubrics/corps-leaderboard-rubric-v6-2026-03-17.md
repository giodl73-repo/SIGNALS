## Quest Rubric — corps-leaderboard v6

---

### What changed: v5 → v6

Two new aspirational criteria extracted from R5 scorecard excellence signals.

**C-20 — Three-Field Action Template with Breaks Condition**
Tests whether the next-actions section uses a three-field structured template — `-> Unlocks: {exact achievement or milestone name}` / `-> Breaks: {condition name from health score}` / `-> Priority: [tier]` — and whether the `Breaks` field is required to name the health condition it dissolves, or when that condition is already at score 0, to write a `prevents:` prevention rationale instead. C-05 requires that each action names a namespace+topic and an exact achievement or milestone name (the Unlocks field). C-14 requires a named Breaks field with an explicit N/A prohibition. C-20 tests a third constraint: when the health condition targeted by a Breaks entry is already resolved (score = 0), the field must shift register from "dissolves" to "prevents re-entry" by using a `prevents:` prefix with a rationale. This makes every action dual-annotated — carrot (what you earn) and release (what constraint dissolves or is blocked from returning) — and distinguishes passive naming from active condition management.
- **Derived from**: R5 excellence signal — all five variations (V-01 through V-05). **Passes**: V-01, V-02, V-03, V-04, V-05.

**C-21 — 1-Away Section Nearest-Miss Fallback**
Tests whether the 1-Away gap detection section (C-07), when no qualifying 1-away gaps are found, outputs a nearest-miss fallback that names the specific topic or milestone closest to qualifying and quantifies its remaining gap (e.g., "No 1-away gaps found. Closest: [topic] needs [n] more [unit]"). C-07 requires the null case to be stated explicitly; C-21 requires the null-case clause to additionally name the nearest qualifying candidate and measure its distance. A bare "no 1-away gaps found" statement satisfies C-07 but fails C-21. The nearest-miss pointer transforms a dead-end null into an actionable directive: a reader who finds nothing at the 1-away threshold is immediately shown the next most actionable target.
- **Derived from**: R5 excellence signal — V-01, V-02, V-03. **Passes**: V-01, V-02, V-03.

**Scoring updated** — Aspirational tier now contains 13 criteria at 10/13 pts each (~0.77). Total remains 100. All five R5 variations pass C-20 (all shared the three-field template). V-01, V-02, V-03 pass C-21; V-04 and V-05 fail C-21. Against v6: V-02 (fails C-19 only) scores ~99.2. V-03 (fails C-18 only) scores ~99.2. V-04 (fails C-21 only) scores ~99.2. V-05 (fails C-21 only) scores ~99.2. V-01 (fails C-18 and C-19) scores ~98.5. V-02, V-03, V-04, and V-05 are co-ceiling-setters at ~99.2. No variation yet scores 100 against v6 — the ceiling is open.

---

### What changed: v4 → v5

*(preserved verbatim — see full rubric at `simulations/quest/rubrics/corps-leaderboard-rubric-v6-2026-03-17.md`)*

---

## Essential Criteria (correctness baseline — 60% of score)

*Five criteria at 12 pts each. All five must pass to reach the golden threshold.*

### C-01 through C-05
*(unchanged — full text in file)*

---

## Recommended Criteria (improve output quality — 30% of score)

*Three criteria at 10 pts each: C-06, C-07, C-08 — unchanged.*

---

## Aspirational Criteria (ceiling-raising — 10% of score)

*Thirteen criteria at 10/13 pts each (~0.77).*

### C-09 through C-17
*[Inherited from R4. Text unchanged in v5 and v6. All R5 variations scored 100/100 against these criteria.]*

### C-18 -- Gate Markers as Literal Output Lines *(NEW v5)*
*(full text in file)*

### C-19 -- Synthesis Sentence with Concrete Numeric Claim *(NEW v5)*
*(full text in file)*

### C-20 -- Three-Field Action Template with Breaks Condition *(NEW v6)*

- **Weight**: aspirational | **Category**: behavior
- **Text**: The next-actions section uses a three-field structured template (`Unlocks / Breaks / Priority`) and the instruction requires the `Breaks` field to name the health condition the action dissolves. When the targeted condition is already at score 0, the instruction requires the field to use a `prevents:` prefix with a rationale rather than blank or N/A. C-14 requires a named Breaks field with N/A prohibition; C-20 requires the value itself to shift register when the condition is already resolved — from naming what dissolves to naming what is prevented from re-entering.
- **Pass condition**: Instruction defines the three-field template and states that zero-scored conditions require a `prevents:` prefix with rationale. A template without the zero-score `prevents:` requirement passes C-14 but fails C-20. If C-14 fails, this criterion automatically fails.
- **Derived from**: R5 — V-01, V-02, V-03, V-04, V-05. **Passes**: all five.

### C-21 -- 1-Away Section Nearest-Miss Fallback *(NEW v6)*

- **Weight**: aspirational | **Category**: depth
- **Text**: The 1-Away section's if-none clause, when no qualifying 1-away gaps exist, names the specific topic or milestone closest to qualifying and states its numeric gap (e.g., "No 1-away gaps found. Closest: [topic] needs [n] more [unit]"). C-07 requires the null case to be stated explicitly; C-21 requires it to carry a named nearest-miss pointer with a numeric step count. A terminal absence declaration ("nothing is one step away") passes C-07 but fails C-21.
- **Pass condition**: Instruction's if-none clause requires naming the closest item and its numeric gap. Output if-none clause contains a specific topic or milestone name and a step count. If C-07 fails, this criterion automatically fails.
- **Derived from**: R5 — V-01, V-02, V-03. **Passes**: V-01, V-02, V-03.

---

## Scoring Reference

| Tier | Criteria | Count | Max pts |
|------|----------|-------|---------|
| Essential | C-01 – C-05 | 5 | 60 |
| Recommended | C-06 – C-08 | 3 | 30 |
| Aspirational | C-09 – C-21 | 13 | 10 |

**R5 variation scores against v6:**

| Variation | Fails | Score |
|-----------|-------|-------|
| V-01 All-Tables Scorecard | C-18, C-19 | **98.5** |
| V-02 Triple-Gate Pipeline | C-19 | **99.2** |
| V-03 Conversational Coach | C-18 | **99.2** |
| V-04 SITREP + Decision Risk | C-21 | **99.2** |
| V-05 Cascading Contracts | C-21 | **99.2** |

*Four co-ceiling-setters at ~99.2. Ceiling open at 100.*

---

The full rubric is written to `simulations/quest/rubrics/corps-leaderboard-rubric-v6-2026-03-17.md`.

Two structural distinctions worth noting:

- **C-20 vs C-14**: C-14 enforces Breaks field presence + N/A prohibition. C-20 enforces that the field's *value* changes meaning when the condition is already resolved — `prevents:` turns a zero-case from decorative into actionable.
- **C-21 vs C-07**: C-07 enforces that the 1-away null case is stated. C-21 enforces that the null-case output *directs* — it names where to look next rather than issuing a terminal empty-state declaration.
designated gap term fails. An instruction that defines the gap condition only in the pass condition (not in the instruction text itself) fails.

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

### C-08 -- Team Synthesis Sentence

- **Weight**: recommended
- **Category**: insight
- **Text**: The output includes one synthesis sentence whose observation requires seeing multiple topics or multiple contributors together — a conclusion that is invisible from any individual-topic view. The sentence must cross at least two topics or two contributors.
- **Pass condition**: A synthesis sentence exists and states a multi-topic or multi-contributor observation (e.g., "Contributors A and B overlap in scout and flow, while C is isolated in trace"). A sentence that describes one topic's state without referencing others fails. A generic statement such as "the team is making progress" without a specific cross-referencing claim fails.

---

## Aspirational Criteria (ceiling-raising — 10% of score)

*Thirteen criteria sharing 10 pts total (10/13 pts each, ~0.77). A perfect aspirational score requires all thirteen.*

*[C-09 through C-17 — aspirational criteria inherited from R4. Text unchanged in v5 and v6. All R5 variations scored 100/100 against these criteria.]*

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

### C-20 -- Three-Field Action Template with Breaks Condition *(NEW v6)*

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The next-actions section uses a three-field structured template — `-> Unlocks: {exact achievement or milestone name}` / `-> Breaks: {condition name from health score}` / `-> Priority: [tier]` — and the instruction requires the `Breaks` field to name the health condition the action dissolves. When the targeted health condition is already at score 0, the instruction requires the field to shift to a `prevents:` rationale (e.g., `prevents: {re-entry condition}`) rather than leaving the field blank or writing N/A. C-05 requires namespace+topic+achievement naming (the Unlocks field). C-14 requires a named Breaks field with N/A prohibition. C-20 tests a third constraint: the per-entry Breaks value must either name an active health condition (carrot + release pairing) or carry a `prevents:` prefix when that condition is already resolved. Every action is thereby dual-annotated — what you earn and what constraint dissolves or is blocked from returning. The pattern is verifiable by checking that each Breaks field entry either matches a named condition from the health score section or begins with `prevents:`.
- **Pass condition**: The instruction text defines a three-field action template that names all three fields (Unlocks, Breaks, Priority). The instruction states that the Breaks field must name a health condition and that when the condition is at score 0 the field must use a `prevents:` prefix with a rationale. A template that names the Breaks field without the zero-score `prevents:` requirement passes C-14 but fails C-20. An action list that uses the template in output without the instruction requirement fails. If C-14 fails, this criterion automatically fails.
- **Derived from**: R5 excellence signal — all five variations (V-01 through V-05). **Passes**: V-01, V-02, V-03, V-04, V-05.

### C-21 -- 1-Away Section Nearest-Miss Fallback *(NEW v6)*

- **Weight**: aspirational
- **Category**: depth
- **Text**: The 1-Away gap detection section (C-07), when no qualifying 1-away gaps exist, outputs a nearest-miss fallback that names the specific topic or milestone closest to qualifying and quantifies its remaining gap (e.g., "No 1-away gaps found. Closest: [topic] needs [n] more [unit]"). C-07 requires that the null case be stated explicitly rather than omitting the section; C-21 requires that the null-case clause additionally name the nearest qualifying candidate and measure its distance. A bare "no 1-away gaps found" statement satisfies C-07 but fails C-21. The nearest-miss pointer transforms a dead-end null into an actionable directive: the reader who finds nothing at the 1-away threshold is immediately shown the next most actionable target. The constraint is verifiable: the if-none clause must contain a specific topic name and a numeric gap count, not just an absence declaration.
- **Pass condition**: The instruction text includes an if-none clause for the 1-Away section that requires, when no 1-away gaps are present, naming the closest qualifying item and stating its numeric gap. The output if-none clause contains a specific topic or milestone name and a numeric step count (e.g., "needs 2 more signals"). A null-case clause that states only "no 1-away gaps exist" or "nothing is one step away" without a named nearest-miss entry fails. An instruction that covers only the positive case (gaps exist) without addressing the null case fails C-07 and automatically fails C-21.
- **Derived from**: R5 excellence signal — V-01, V-02, V-03. **Passes**: V-01, V-02, V-03.

---

## Scoring Reference

| Tier | Criteria | Count | Max contribution |
|------|----------|-------|-----------------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 pts |
| Recommended | C-06, C-07, C-08 | 3 | 30 pts |
| Aspirational | C-09 through C-21 | 13 | 10 pts |

**Aspirational per-criterion weight**: 10/13 pts (~0.77). Scores are reported to one decimal place.

**Golden threshold**: All 5 essential pass + composite >= 80.

**R5 variation scores against v6**:

| Variation | C-18 | C-19 | C-20 | C-21 | Aspirational (13) | Total |
|-----------|------|------|------|------|-------------------|-------|
| V-01 All-Tables Scorecard | FAIL | FAIL | PASS | PASS | 11/13 * 10 = 8.46 | **98.5** |
| V-02 Triple-Gate Pipeline | PASS | FAIL | PASS | PASS | 12/13 * 10 = 9.23 | **99.2** |
| V-03 Conversational Coach | FAIL | PASS | PASS | PASS | 12/13 * 10 = 9.23 | **99.2** |
| V-04 SITREP + Decision Risk | PASS | PASS | PASS | FAIL | 12/13 * 10 = 9.23 | **99.2** |
| V-05 Cascading Contracts | PASS | PASS | PASS | FAIL | 12/13 * 10 = 9.23 | **99.2** |

*V-02, V-03, V-04, and V-05 are co-ceiling-setters at ~99.2 against v6. No variation yet scores 100 against v6.*

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | Added "Shallow Spread" to C-10 pattern vocabulary; added C-11 (pre-compilation inertia diagnosis) and C-12 (full action-pattern cohesion) from V-04 R1 excellence signals |
| v3 | 2026-03-17 | Added C-13 (named completion gate in role sequence) and C-14 (per-action field template with explicit N/A prohibition) from R2 scorecard excellence signals; aspirational tier expands to 6 criteria at ~1.67 pts each; total remains 100 |
| v4 | 2026-03-17 | Added C-15 (section-boundary gate as structural constraint), C-16 (quantified inertia with urgency tiers), and C-17 (evidence-first leaderboard before named pattern) from R3 scorecard excellence signals; aspirational tier expands to 9 criteria at ~1.11 pts each; total remains 100; V-05 is new ceiling at 98.9 |
| v5 | 2026-03-17 | Added C-18 (gate markers as literal output lines) and C-19 (synthesis sentence with concrete numeric claim) from R4 scorecard excellence signals; aspirational tier expands to 11 criteria at ~0.91 pts each; total remains 100; V-02 and V-03 are co-ceiling-setters at 99.1; no variation yet scores 100 against v5 |
| v6 | 2026-03-17 | Added C-20 (three-field action template with Breaks condition) and C-21 (1-away section nearest-miss fallback) from R5 scorecard excellence signals; aspirational tier expands to 13 criteria at ~0.77 pts each; total remains 100; V-02, V-03, V-04, and V-05 are co-ceiling-setters at ~99.2; no variation yet scores 100 against v6 |

---

**Two patterns extracted, two criteria added.** The key structural distinctions:

- **C-20** closes the gap between "Breaks field names a condition" (C-14) and "Breaks field manages condition state." C-14 enforces presence and N/A prohibition; C-20 enforces that the field's value shifts register when the condition is already resolved — from naming what dissolves to naming what is prevented from re-entering. The `prevents:` prefix makes the zero-case actionable rather than decorative.

- **C-21** closes the gap between "null case is stated" (C-07) and "null case directs." C-07 enforces that the section does not silently disappear when no 1-away gaps exist; C-21 enforces that the null-case output carries a named nearest-miss pointer with a numeric gap. A reader who finds no 1-away targets is told where to look next rather than receiving a terminal empty-state declaration.
