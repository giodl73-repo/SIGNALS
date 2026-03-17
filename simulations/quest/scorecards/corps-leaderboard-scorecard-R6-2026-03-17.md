I now have what I need. Let me score all five R6 variations against rubric v6.

---

# Quest Scorecard — corps-leaderboard R6

**Rubric version**: v6 | **Scoring date**: 2026-03-17
**Variations file**: `simulations/quest/variations/corps-leaderboard-variations-R6-2026-03-17.md`

---

## Scoring Context

**R5 baseline against v6** (from rubric):

| R5 Variation | Fails | Score |
|---|---|---|
| V-01 All-Tables Scorecard | C-18, C-19 | 98.5 |
| V-02 Triple-Gate Pipeline | C-19 | 99.2 |
| V-03 Conversational Coach | C-18 | 99.2 |
| V-04 SITREP + Decision Risk | C-21 | 99.2 |
| V-05 Cascading Contracts | C-21 | 99.2 |

**R6 design intent**: close C-20 and C-21 simultaneously in all five variations while carrying C-01–C-19 coverage forward.

---

## Criterion-by-Criterion Evaluation

### Essential Criteria — C-01 through C-05 (12 pts each, 60 pts total)

**C-01 — Scan phase builds registry** (glob, topic paths, namespaces, contributors, file counts)

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Phase 1 globs `simulations/**/*.md`, builds REGISTRY with topic path, namespace, contributor_set, file_count. Empty-workspace case recorded. |
| V-02 | **PASS** | Phase 1 "SCAN" does same. GATE 1 confirms count. |
| V-03 | **PASS** | Requirement 1 MUST clause enumerates all registry fields. |
| V-04 | **PASS** | Role 1 (Signal Archaeologist) builds Signal Inventory with same fields. |
| V-05 | **PASS** | Section 1 builds REGISTRY. [OPEN/CLOSE: SCAN] gates it. |

**C-02 — Contributor leaderboard with ranked table**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Phase 2 produces `Rank \| Contributor \| Total Signals \| Topics Covered \| Namespaces Active`. Descending rank, ties broken by topics. |
| V-02 | **PASS** | Phase 2 same table. Adds leaderboard observation sentence. |
| V-03 | **PASS** | Requirement 2 MUST produce ranked table with specified columns. |
| V-04 | **PASS** | Role 2 Part A has the table. Observation sentence required. |
| V-05 | **PASS** | Section 2 LEADERBOARD has same table. Observation sentence required. |

**C-03 — Signal Health Score with 5 named stagnation conditions**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Phase 3 scores Empty Start \| Lone Wolf \| Namespace Tunnel \| Stale Coverage \| Shallow Spread, 0–3, with urgency tiers and dominant condition. |
| V-02 | **PASS** | Phase 3 same table. GATE 3 names dominant condition. |
| V-03 | **PASS** | Requirement 3 MUST evaluate exactly 5 conditions. Exact names listed. Urgency tiers defined. |
| V-04 | **PASS** | Role 2 Part B scores all 5. HEALTH GATE output names dominant. |
| V-05 | **PASS** | Section 3 HEALTH SCORE same table. Urgency column expanded (0=LOW 1=MED 2–3=HIGH). |

**C-04 — Achievement evaluation per topic with 5 named achievements**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Phase 4 matrix table: First Signal \| Signal Depth \| Full Sweep \| Solo Pioneer \| Team Topic per topic. `✓` / `○+n` cell notation. Exact definitions listed. |
| V-02 | **PASS** | Phase 4 Earned/Locked list format. Exact achievement names, exact conditions. Table gap termed "pipeline gap." All 5 achievements defined verbatim. |
| V-03 | **PASS** | Requirement 4 MUST evaluate all 5. Names fixed. Earned/locked separated. Topic absent from output = spec gap. |
| V-04 | **PASS** | Role 3 Earned/Locked list. Exact definitions. "Findings gap" noted for missing topics. |
| V-05 | **PASS** | Section 4 ACHIEVEMENTS Earned/Locked list. "Stamp gap" term for missing topics. |

**C-05 — Actions specify namespace+topic and exact achievement/milestone name (Unlocks field)**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Table row: `[namespace/topic + what to do] \| [exact achievement or milestone name] \| ...` — exact achievement or milestone name required in Unlocks. Generic actions without namespace+topic fail. |
| V-02 | **PASS** | "Each must follow this three-field template... Unlocks: {exact achievement or milestone name}." Generic advice fails. |
| V-03 | **PASS** | Requirement 7: "Each action MUST name a specific namespace and topic path. Generic advice without a specific target MUST NOT appear." |
| V-04 | **PASS** | Role 3 action template: `-> Unlocks: {exact achievement or milestone name}`. "Generic advice without a specific namespace and topic fails." |
| V-05 | **PASS** | Section 7 template: `-> Unlocks: {exact achievement or milestone name}`. "Generic advice without a specific namespace and topic fails." |

**Essential subtotal: 60/60 for all five.**

---

### Recommended Criteria — C-06 through C-08 (10 pts each, 30 pts total)

**C-06 — Gate lines at each phase**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Explicit "Gate line: [code block]" at end of each phase (Phases 1–6 + completion gate). |
| V-02 | **PASS** | [GATE 1–5] + [COMPLETION GATE] at each phase boundary. |
| V-03 | **PASS** | "The skill MUST output: [code block]" at end of each requirement. |
| V-04 | **PASS** | [ARCHAEOLOGY GATE], [HEALTH GATE], [COMPLETION GATE]. |
| V-05 | **PASS** | [OPEN/CLOSE] bidirectional stamps at both ends of all 9 sections. |

**C-07 — 1-away gap detection section**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Phase 6 "1-Away Gaps" table. Null case requires `(nearest miss)` row. |
| V-02 | **PASS** | Phase 5 "1-Away Gaps" list. Two-level cascading fallback when empty. |
| V-03 | **PASS** | Requirement 6: skill MUST identify every 1-unit gap. Nearest-miss pointer when none found. |
| V-04 | **PASS** | Role 3 "1-Away Gaps" list. Two-level cascade Level 1 + Level 2 when empty. |
| V-05 | **PASS** | Section 6 "1-AWAY GAPS" with hard if-none requirement clause. |

**C-08 — Team milestones with fixed verbatim names**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Phase 5 table: `first team signal \| shared coverage \| debate starter`. "Milestone names are fixed. Do not rename..." |
| V-02 | **PASS** | Phase 4 team milestones table with exact names. "Renaming or paraphrasing fails." |
| V-03 | **PASS** | Requirement 5: "Milestone names MUST NOT be renamed, abbreviated, or paraphrased." All 3 fixed names listed. |
| V-04 | **PASS** | Role 3 milestones table. "Names verbatim: `first team signal`, `shared coverage`, `debate starter`. Renaming fails." |
| V-05 | **PASS** | Section 5 MILESTONES table. "Milestone names are fixed verbatim... Any renaming, abbreviation, or paraphrase fails." |

**Recommended subtotal: 30/30 for all five.**

---

### Aspirational Criteria — C-09 through C-21 (10/13 pts ≈ 0.77 each, 10 pts total)

**C-09 through C-17** — All R5 and R6 variations pass (confirmed by rubric: "All R5 variations scored 100/100 against these criteria" and R6 carries same implementations forward):

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-09 (5 named conditions) | PASS | PASS | PASS | PASS | PASS |
| C-10 (urgency tiers 0=L 1=M 2–3=H) | PASS | PASS | PASS | PASS | PASS |
| C-11 (health precedes achievements) | PASS | PASS | PASS | PASS | PASS |
| C-12 (empty-workspace path explicit) | PASS | PASS | PASS | PASS | PASS |
| C-13 (named gate on health→achievement) | PASS | PASS | PASS | PASS | PASS |
| C-14 (N/A prohibition, Breaks field) | PASS | PASS | PASS | PASS | PASS |
| C-15 (gate line confirms health close) | PASS | PASS | PASS | PASS | PASS |
| C-16 (dominant condition named) | PASS | PASS | PASS | PASS | PASS |
| C-17 (evidence-first leaderboard before named pattern) | PASS | PASS | PASS | PASS | PASS |

**C-18 — Gate Markers as Literal Output Lines**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "Gate line: [code block]" at each phase — explicit output directive with exact text. All 7 phases gated. C-19 repair also included (concrete number in synthesis). |
| V-02 | **PASS** | `[GATE N: ...]` code blocks as direct output instructions at each gate. "[COMPLETION GATE: ...]" closes. |
| V-03 | **PASS** | "The skill MUST output: [code block]" — MUST directive makes gate text a formal requirement at each requirement boundary. |
| V-04 | **PASS** | `[ARCHAEOLOGY GATE: ...]`, `[HEALTH GATE: ...]`, `[COMPLETION GATE: ...]` as code block directives. |
| V-05 | **PASS** (strongest) | `[OPEN: {section}]` and `[CLOSE: {section} \| {next} opens next]` appear as literal instruction lines at two positions per section — any skip is detectable at two output points. |

**C-19 — Synthesis Sentence with Concrete Numeric Claim**

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "Include at least one concrete number from: contributor count, signal count, namespace count, or topic count." Explicit requirement. |
| V-02 | **PASS** | "Include at least one number from: **contributor count**, **signal count**, **namespace count**, or **topic count**." |
| V-03 | **PASS** | Requirement 8: "Includes at least one concrete number of type: **contributor count**, **signal count**, **namespace count**, or **topic count**." MUST language. |
| V-04 | **PASS** | "Include at least one number from: **contributor count**, **signal count**, **namespace count**, or **topic count**." |
| V-05 | **PASS** (most explicit) | Three enumerated requirements: spans 2+ topics/contributors; includes concrete number; ends with recommended implication. |

**C-20 — Three-Field Action Template with Breaks Condition (NEW v6)**

Tests: three-field template present AND zero-scored conditions require `prevents:` prefix with rationale.

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Table columns: Action \| Unlocks \| Breaks \| Priority. Breaks column rule: "score = 0 (resolved): write `prevents: {condition name} — {re-entry rationale}`." Worked example inline. `prevents:` prefix mandatory when score = 0. |
| V-02 | **PASS** | Three-field bullet template `-> Unlocks / -> Breaks / -> Priority`. "Condition score = 0 (resolved): write `prevents: {condition name} — {re-entry rationale}`." |
| V-03 | **PASS** | "WHEN the action targets a health condition with score = 0: the Breaks field MUST begin with `prevents:` followed by a re-entry rationale." MUST-keyword makes zero-score rule independently auditable. |
| V-04 | **PASS** | Three-field template in Role 3. Paired worked examples side-by-side: one active (score >= 1), one resolved (score = 0 → `prevents:` prefix). "The `prevents:` prefix is required when the condition score = 0." |
| V-05 | **PASS** (strongest) | Pre-write check table: `score >= 1 → condition name`, `score = 0 → prevents: {condition name} — {re-entry rationale}`. Rule stated twice: in template definition AND in pre-write check table. Two worked examples. |

**C-21 — 1-Away Section Nearest-Miss Fallback (NEW v6)**

Tests: when no 1-away gaps exist, if-none clause names specific topic/milestone and states numeric gap.

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "(nearest miss)" row appended to 1-away table when empty: `\| (nearest miss) \| [topic] needs [n] more [unit] \| **[Achievement]** — closest to 1-away threshold \|` — specific topic + numeric gap required. "`No 1-away gaps` alone without this row fails." |
| V-02 | **PASS** (deepest) | Two-level cascading fallback required when list empty: Level 1 (closest 1-away candidate + numeric gap) and Level 2 (closest 2-away candidate + numeric gap). Both required. Converts null into two-sprint plan. |
| V-03 | **PASS** | Requirement 6: "WHEN no 1-away gaps exist, the skill MUST output a nearest-miss pointer: `No 1-away gaps found. Closest: {topic} needs {n} more {unit} to unlock **{Achievement}**.`" MUST clause + exact format required. |
| V-04 | **PASS** | Role 3 two-level cascade: Level 1 + Level 2, both with specific topic and numeric gap. Both required when list empty. |
| V-05 | **PASS** | Section 6 if-none clause stated as hard requirement: "This clause is required. It must name a specific topic or milestone and include a specific numeric gap count. `No 1-away gaps found` alone does not satisfy this requirement." |

**Aspirational subtotal: 10/10 (all 13 criteria pass) for all five.**

---

## Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | **Total** |
|---|---|---|---|---|
| V-01 All-Tables Scorecard | 60 | 30 | 10 | **100** |
| V-02 Cascading Nearest-Miss | 60 | 30 | 10 | **100** |
| V-03 Declarative Spec | 60 | 30 | 10 | **100** |
| V-04 3-Role + Worked Examples | 60 | 30 | 10 | **100** |
| V-05 Bidirectional Stamps + Full | 60 | 30 | 10 | **100** |

**All five R6 variations reach 100. Ceiling closed at v6.**

---

## Rank (structural strength, all tied at 100)

1. **V-05** — Strongest overall: bidirectional stamps (C-18 double-position detection) + C-20 rule stated twice (template + pre-write check table) + C-21 stated as hard structural requirement. Highest combined audit resistance.
2. **V-03** — Strongest on constraint auditability: MUST/SHALL/WHEN language makes each of the 21 criteria independently findable by keyword scan. Lowest ambiguity between requirement and suggestion.
3. **V-04** — Strongest on C-20 guidance: paired worked examples (active vs. resolved case) at point of writing eliminate register confusion via priming rather than instruction.
4. **V-02** — Strongest on C-21 depth: two-level cascade converts null gap detection into a two-sprint plan at thresholds 1 and 2.
5. **V-01** — Strongest on machine-readability: table-column layout makes C-20 and C-21 auditable by cell content rather than prose parsing.

---

## Excellence Signals

**New patterns from R6 top variations (not present in R5):**

1. **Zero-score register shift** (C-20 core): when a health condition scores 0, the Breaks field stops naming what dissolves and starts naming what is prevented from re-entering — `prevents: {condition} — {rationale}`. This converts a static label into an active anti-regression contract.

2. **Pre-write check table as generation friction point** (V-05): a lookup table placed immediately before the action template forces the model to look up each condition's score before writing the Breaks value — catching the zero-score case at decision time rather than instruction time.

3. **Dual-statement of zero-score rule** (V-05): stating the `prevents:` requirement once in the template definition and again in the pre-write check table creates two redundant surfaces — if one is skipped by the model, the other still triggers.

4. **Two-level nearest-miss cascade** (V-02, V-04): Level 1 (closest to threshold 1) + Level 2 (closest to threshold 2) — when no 1-away gaps exist, the output provides not just the next target but a two-sprint trajectory. The null state becomes a sprint plan.

5. **Hard structural requirement language for if-none clause** (V-05): "This clause is required. A statement of absence without a named nearest-miss pointer and numeric gap fails this section." Stating the if-none clause as a structural requirement (not a suggestion) closes the gap between C-07 (null stated) and C-21 (null directed).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["zero-score register shift in Breaks field from condition-name to prevents: prefix with re-entry rationale", "pre-write check table as decision-gate before writing Breaks field catches zero-score case at generation time", "two-level nearest-miss cascade (threshold-1 plus threshold-2) converts null gap detection into a two-sprint plan", "dual-statement of prevents: rule across template definition and pre-write check creates redundant enforcement surface"]}
```
