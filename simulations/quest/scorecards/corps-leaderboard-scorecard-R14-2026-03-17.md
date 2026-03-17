## Quest:Score — corps-leaderboard Round 14 (Rubric v11)

---

### Essential Criteria (C-01–C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Signal Registry Scan | PASS | PASS | PASS | PASS | PASS |
| C-02 Per-Topic Achievement Evaluation | PASS | PASS | PASS | PASS | PASS |
| C-03 All Three Team Milestones Exact | PASS | PASS | PASS | PASS | PASS |
| C-04 Contributor Leaderboard Ranked | PASS | PASS | PASS | PASS | PASS |
| C-05 Next Actions Namespace+Achievement | PASS | PASS | PASS | PASS | PASS |

All five essential criteria pass in all five variations. `all_essential_pass: true`.

---

### Aspirational Criteria — Per-Variation Evaluation

#### C-06 through C-21 (Prior-version text, inferred from structure)

All five variations carry the universal R13 seed set (A+B+H) and the full role pipeline with health/inertia split, so the pre-v7 aspirational criteria (C-06–C-21) pass uniformly. Key checks:

- **C-06 Namespace Diversity Metric** — All variations print `Namespace diversity: {N}/9` in every topic header. **PASS all.**
- **C-07 Momentum Indicator** — Velocity summary line (`Trend: increasing/flat/stalled`) present in all. **PASS all.**
- **C-08 Gap Prioritization by Achievement Distance** — Nearest-miss sections with ascending sort present in all. **PASS all.**
- **C-09 Contributor Collaboration Signal** — Collaboration signal/map table present in all. **PASS all.**
- **C-10 Empty Namespace Explicit Listing** — `Empty: {list}` in namespace coverage line in all. **PASS all.**
- **C-11 Topic Health Summary Line** — All variations produce per-topic health header with file/namespace/contributor counts. **PASS all.**
- **C-12 Locked Achievement with Specific Unlock Path** — All require LOCKED rows to state exact unlock requirement inline. **PASS all.**
- **C-13 Team Insight Cross-Topic Synthesis** — One-sentence insight with cross-topic conclusion + number + name in all. **PASS all.**
- **C-14 Solo Pioneer Tension Detection** — `[TENSION: solo hold ...]` marker when Solo Pioneer EARNED and Team Topic NOT YET, in all. **PASS all.**
- **C-15 Namespace Leader Callout** — `namespace | leader | signal_count` table present in all. **PASS all.**
- **C-16 Stale Signal Detection** — Stale signal table (`stale/active/date-unknown`) present in all. **PASS all.**
- **C-17 Signal Velocity Trend** — Velocity summary with trend classification present in all. **PASS all.**
- **C-18 Debate Starter Threshold Proximity** — `Debate starter: nearest topic is {name} with {N}/3 contributors...` present in all. **PASS all.**
- **C-19 Multi-Phase Execution Order** — Inertia Phase explicitly ordered before Health Phase in all. **PASS all.**
- **C-20 Prevents: Prefix Rule Statement** — Pre-Write Check section states the rule in all. **PASS all.**
- **C-21 Nearest-Miss Achievement Gap** — Level 1 nearest-miss with topic + achievement + gap present in all. **PASS all.**

#### C-22 through C-31 — Detailed Evaluation

**C-22 — Dual-Statement Prevents-Rule Redundancy**

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | First statement in §3.6 Pre-Write Check ("stated here as the first of two structurally independent enforcement points"); second embedded in §3.7 action template row comment ("second structurally independent enforcement point") | PASS |
| V-02 | Same dual-location structure: §3.6 and §3.7 template | PASS |
| V-03 | §3.2 Pre-Write Check (first) and §3.3 action template (second) | PASS |
| V-04 | §3.2 Pre-Write Check (first) and §3.3 tiered action template (second) | PASS |
| V-05 | §4.2 Pre-Write Check (first) and §4.3 tiered action template (second) | PASS |

**C-23 — Two-Level Nearest-Miss Cascade**

All variations define Level 1 (1-unit away) and Level 2 (2-unit away, **only** when Level 1 empty, with explicit "Level 1: no topics are 1 unit away" statement). **PASS all.**

**C-24 — Gate-Level Prevents: Prefix Count Self-Audit**

All variations include: `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` with substitutable N. **PASS all.**

**C-25 — Synthesis Novelty Constraint**

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Publisher §3.5: "A Skeptic who has read all Archivist and Analyst output already knows... The insight MUST contain something the Skeptic would not already know from all of that material" with explicit failure condition for restating field-report achievement status | PASS |
| V-02 | Same Skeptic gate; "including from the progress bar values" extension | PASS |
| V-03 | Publisher §4.3: Skeptic gate with "including from the leaderboard velocity column" | PASS |
| V-04 | Narrator §4.4: Skeptic gate with milestone proximity ladders in known scope | PASS |
| V-05 | Narrator §5.4: Full Skeptic gate including discrepancy table, echo table, tiered actions | PASS |

**C-26 — Named Role-Sequence Architecture**

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Archivist ("does NOT evaluate achievements, assess trajectory, rank contributors, or write insights or actions"), Analyst ("does NOT rank contributors, write insights, or write actions"), Publisher — explicit scope boundaries and handoff points | PASS |
| V-02 | Same 3-role structure with explicit scope exclusions | PASS |
| V-03 | 4-role: Archivist → Analyst (adds leaderboard) → Strategist ("Actions only... Does NOT produce...reconciliation pairing, or Team Insight") → Publisher. Each has named scope exclusions. | PASS |
| V-04 | 4-role: Archivist → Analyst → Strategist → Narrator. Each with explicit scope boundaries. | PASS |
| V-05 | 5-role: Archivist → Assessor ("trajectory assessment only... Does NOT evaluate achievements") → Inspector ("current-state assessment only... Does NOT restate inertia flags") → Strategist ("Actions only") → Narrator ("Synthesis only"). Clear scope exclusions. | PASS |

**C-27 — Health / Inertia Structural Separation**

All variations explicitly label `### 2.1 — Inertia Phase (RUNS FIRST)` and `### 2.2 — Health Phase (RUNS SECOND)` (or equivalent role-boundary separation in V-05: Assessor=inertia / Inspector=health) with each sub-phase restricted to its own data type. **PASS all.**

**C-28 — Named Artifact Set at Role Handoff**

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Archivist Handoff enumerates artifacts 1–3 by name; Analyst Handoff enumerates artifacts 1–6 by name | PASS |
| V-02 | Same: Archivist Handoff (3 named), Analyst Handoff (6 named) | PASS |
| V-03 | Archivist Handoff (3 named), Analyst Handoff (7 named including Leaderboard with Velocity), Strategist Handoff (4 named) | PASS |
| V-04 | Archivist Handoff (3 named), Analyst Handoff (6 named with proximity ladders), Strategist Handoff (4 named) | PASS |
| V-05 | Archivist Handoff (3 named), Assessor Handoff (3 named), Inspector Handoff (5 named), Strategist Handoff (4 named) | PASS |

**C-29 — Per-Phase Completion Checklist Gate**

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Section 2.1 Gate (3 `[ ]` items) + Section 2.2 Gate (7 `[ ]` items) + Publisher Gate (8 `[ ]` items). At least two phase gates each with 2+ distinct items. | PASS |
| V-02 | Section 2.1 Gate (3 items) + Section 2.2 Gate (7 items) + Publisher Gate (8 items) | PASS |
| V-03 | Section 2.1 Gate (3 items) + Section 2.2 Gate (5 items, covers 2.2–2.4) + Strategist Gate (4 items) + Publisher Gate (3 items) | PASS |
| V-04 | Section 2.1 Gate (2 items) + Section 2.2 Gate (5 items) + Strategist Gate (4 items) + Narrator Gate (4 items) | PASS |
| V-05 | Archivist Gate (3 items) + Assessor Gate (4 items) + Inspector Gate (5 items) + Strategist Gate (4 items) + Narrator Gate (4 items) | PASS |

**C-30 — Contamination-Check Checklist Item at Health/Inertia Gate**

This tests whether the phase gate at the health/inertia boundary contains a `[ ]` item explicitly prohibiting cross-contamination (absence of prohibited content, not just presence of required content). C-30 presupposes C-27.

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Section 2.2 Gate item 5: `[ ] Inertia Phase table present; no static counts from Health Phase restated in inertia content (cross-contamination check)` — explicitly verifies absence of prohibited content | PASS |
| V-02 | Section 2.2 Gate item 5: `[ ] Inertia Phase table present; no static counts from Health Phase restated in inertia content (cross-contamination check)` | PASS |
| V-03 | Section 2.2 Gate (covers 2.2–2.4) item 2: `[ ] Inertia Phase table present; no static counts from Health Phase restated in inertia content (cross-contamination check)` | PASS |
| V-04 | Section 2.2 Gate item 3: `[ ] Inertia Phase table present; no static counts from Health Phase restated in inertia content (cross-contamination check)` | PASS |
| V-05 | Inspector Gate item 5: `[ ] Inertia Phase table present; no static counts from Health Phase restated in inertia content (cross-contamination check)` | PASS |

**C-31 — Inertia-Aware Skeptic Knowledge Scope**

Tests whether the Skeptic's prior knowledge explicitly names inertia flags/trajectory output, not just health-phase data. C-31 presupposes C-27.

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Publisher §3.5 Skeptic gate: "every achievement status (from field reports), every milestone row, **every inertia flag, every severity tier, every trajectory note**, the stale signal table, the velocity summary..." — inertia flags named explicitly by category | PASS |
| V-02 | Publisher §3.5 Skeptic gate: "every achievement status (with progress bars), every milestone row, **every inertia flag, every severity tier, every trajectory note**, the stale signal table..." | PASS |
| V-03 | Publisher §4.3 Skeptic gate: "every achievement status, every milestone row, **every inertia flag, every severity tier, every trajectory note**, the stale signal table, the velocity summary, the nearest-miss assessment, the leaderboard (including the velocity column)..." | PASS |
| V-04 | Narrator §4.4 Skeptic gate: "every achievement table, every milestone row (including proximity ladders for all NOT YET milestones), **every inertia flag, every severity tier, every trajectory note**..." | PASS |
| V-05 | Narrator §5.4 Skeptic gate: "every achievement table (with tension markers), every milestone row (including proximity ladders), **every inertia flag, every severity tier, every trajectory note**, the discrepancy table, the echo detection table..." | PASS |

---

### Composite Scores

| Variation | Essential | Aspirational (of 23) | Score | Formula |
|-----------|-----------|----------------------|-------|---------|
| V-01 | 5/5 | 23/23 | **100.00** | 90 + (23/23)×10 |
| V-02 | 5/5 | 23/23 | **100.00** | 90 + (23/23)×10 |
| V-03 | 5/5 | 23/23 | **100.00** | 90 + (23/23)×10 |
| V-04 | 5/5 | 23/23 | **100.00** | 90 + (23/23)×10 |
| V-05 | 5/5 | 23/23 | **100.00** | 90 + (23/23)×10 |

**Universal ceiling: 100.00. All five variations fully saturate v11.**

---

### Ranking

All five variations tie at 100.00 — the rubric is fully saturated. Ranking by structural sophistication:

1. **V-05** (100.00) — 5-role pipeline; full integration of all R14 seeds (M+N+O+R+S); echo detection; confidence band + projection test on insight; non-retracted flag constraint on reconciliation
2. **V-04** (100.00) — 4-role; inertia-first + tiered actions + Seeds M+N; milestone proximity ladders in both Analyst and Narrator Skeptic scope
3. **V-03** (100.00) — 4-role; early leaderboard in Analyst with velocity column (Seed R); Strategist writes actions with leaderboard data available
4. **V-02** (100.00) — 3-role; progress bars + Seed M gap-binding on every action row
5. **V-01** (100.00) — 3-role; field-report prose health blocks + Seed O confidence band on insight

---

### Excellence Signals from V-05 (ceiling holder)

**Seed N — Milestone Proximity Ladder**: For every NOT YET milestone, a detailed breakdown of remaining preconditions appears inline after the milestone row — not just the aggregate gap but per-topic and per-contributor deficits. For `shared coverage`: lists how many more contributors each sub-threshold topic needs. For `debate starter`: names the nearest topic with exact N/3 count. The Skeptic gate explicitly includes "every milestone row (including proximity ladders for all NOT YET milestones)" — raising the novelty bar to require synthesis beyond the per-milestone proximity detail. Present in V-04 and V-05. **Not captured by C-21 or C-23** (which cover achievement-level nearest-miss only, not milestone-level precondition decomposition).

**Seed S — Echo Detection Check**: After completing the Health Phase, the Inspector runs a dedicated consistency scan checking for *logical mutual exclusions* between achievement claims and inertia flag assignments — distinct from the discrepancy check (which catches data-level contradictions). Examples: `healthy-momentum` raised + `Solo Pioneer` EARNED (impossible: healthy-momentum requires ≥2 contributors, Solo Pioneer requires exactly 1); `First Signal LOCKED` + any non-momentum flag raised (flags can't evaluate topics with 0 files). The echo table produces explicit retraction statements. The Strategist pre-write check excludes echo-corrected flags from `resolves:` targeting. Present in V-05 only. **Orthogonal to C-27** (which tests whether the health/inertia split exists) and **to C-30** (which tests whether the gate polices contamination). Echo detection tests whether the output layer enforces semantic consistency of flag/achievement coexistence rules.

**Seed M — Quantified Action-to-Gap Binding**: Every action row carries `[closes: {achievement} gap of {N} {unit} for {topic_path}]`, binding the action to a *specific threshold delta* rather than just an achievement name. Milestone-targeting actions state remaining preconditions from the proximity ladder. C-05 tests namespace + achievement name; Seed M tests a different dimension — whether the *measurable gap* closed by the action is declared at the action row. Present in V-02, V-04, V-05.

**Seed O — Insight Confidence Band**: The Team Insight sentence is followed by `[confidence: HIGH/MEDIUM/LOW] [supporting observations: {N}]`, where the band is calibrated to independent cross-dimensional observations (HIGH ≥3, MEDIUM =2, LOW =1). C-13 tests form; C-25 tests novelty. Neither captures *confidence calibration*. Present in V-01 and V-05.

**Seed R — Leaderboard Velocity Column**: Adds a `velocity` column (`rising/steady/stalled/unknown`) inferred by cross-referencing each contributor's files against the stale signal table. C-04 tests leaderboard presence; C-07 tests momentum indicators for topics. Seed R introduces contributor-dimension velocity — orthogonal to topic momentum. Present in V-03 and V-05.

---

### New Patterns (seeds for v12 criteria)

**Seed N** and **Seed S** are the strongest v12 criterion candidates:

- **Seed N (milestone proximity ladder)**: Orthogonal to C-21/C-23 (achievement nearest-miss). The new criterion would test whether NOT YET milestone rows include a per-precondition breakdown with individual action counts — extending the nearest-miss concept into the milestone dimension. Present in 2 variations; the variate explicitly identifies it as under-captured.

- **Seed S (echo detection)**: Orthogonal to C-27 (health/inertia split) and C-30 (contamination check). The new criterion would test whether a consistency check verifies the logical coexistence rules between flag assignments and achievement claims — not data contradictions but impossibility checks. Present in 1 variation (V-05); requires structural investment.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["milestone proximity ladder — for every NOT YET milestone, inline breakdown of per-topic and per-contributor precondition deficits with individual action counts (Seed N; V-04 and V-05); orthogonal to C-21/C-23 which cover achievement-level nearest-miss only", "echo detection check — post-health consistency scan for logical mutual exclusions between achievement claims and inertia flag assignments (healthy-momentum + Solo Pioneer, First Signal LOCKED + any flag, etc.) not caught by the discrepancy check; produces echo table with retraction statements; Strategist excludes echo-corrected flags from resolves: (Seed S; V-05 only); orthogonal to C-27 and C-30"]}
```
