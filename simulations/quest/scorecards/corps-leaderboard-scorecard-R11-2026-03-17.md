## Round 11 Scorecard — corps-leaderboard

### Scoring Reference

**Formula**: `90 + (aspirational_passed / 23) × 10`

**Essential** (C-01–C-05): 5 criteria × 12 pts = 60 pts. All five must pass.
**Aspirational** (C-06–C-31): 23 criteria × ~0.435 pts = 40 pts.

**Baseline pass set** (C-06–C-21, 13 active criteria): All five variations carry the baseline forward from prior rounds — no regressions detected.

---

### Per-Criterion Evaluation

#### Essential Criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Signal Registry Scan | PASS | PASS | PASS | PASS | PASS |
| **C-02** Per-Topic Achievement Evaluation | PASS | PASS | PASS | PASS | PASS |
| **C-03** All Three Team Milestones | PASS | PASS | PASS | PASS | PASS |
| **C-04** Contributor Leaderboard Ranked | PASS | PASS | PASS | PASS | PASS |
| **C-05** Next Actions w/ Namespace + Achievement | PASS | PASS | PASS | PASS | PASS |

All five essential criteria pass in all five variations. ✓

#### Aspirational Criteria C-06–C-21 (baseline, 13 active)

All five variations inherit these passes from prior rounds. No changes in R11 affect them.

**V-01 through V-05**: 13/13 PASS on baseline. Evidence: structural requirements for registry, achievements, milestones, leaderboard, nearest-miss, and actions have not been weakened.

#### Aspirational Criteria C-22–C-31 (new axes, added v7–v11)

---

**C-22 — Dual-Statement Prevents-Rule Redundancy**

| | Evidence | Result |
|--|---------|--------|
| V-01 | Sec 4: "The `prevents:` prefix rule MUST be applied inside the action template below AND enforced in the pre-write check above. These are two structurally independent enforcement points." | **PASS** |
| V-02 | Publisher 3.4: "prevents: prefix rule — stated here for the Pre-Write Check AND embedded inside each relevant action row below" — two distinct structural blocks. | **PASS** |
| V-03 | Phase 4b: "The `prevents:` prefix rule applies at two structurally independent points: (1) here in the Pre-Write Check... and (2) inside each action row" | **PASS** |
| V-04 | Strategist 3.2: "prevents: prefix rule — stated here for the Pre-Write Check AND embedded inside each relevant action row in the template below" | **PASS** |
| V-05 | Publisher 3.4: same dual-statement structure as V-02, structurally independent. | **PASS** |

---

**C-23 — Two-Level Nearest-Miss Cascade**

| | Evidence | Result |
|--|---------|--------|
| V-01 | Sec 4: Level 1 (1 unit away), Level 2 (only when no Level 1 exists, explicit "Level 1 empty" statement required). | **PASS** |
| V-02 | Analyst 2.3: Level 1 / Level 2 with explicit "Level 1: no topics are 1 unit away" gate. | **PASS** |
| V-03 | Phase 4a: Level 1 / Level 2 with explicit "Level 1: no topics are 1 unit away" before writing Level 2. | **PASS** |
| V-04 | Assessor 2.3: Level 1 / Level 2 with "Level 1 empty" gate. | **PASS** |
| V-05 | Analyst 2.3: same as V-02. | **PASS** |

---

**C-24 — Gate-Level Prevents: Prefix Count Self-Audit**

| | Evidence | Result |
|--|---------|--------|
| V-01 | Section 4 Gate + ACTIONS GATE line: `prevents: prefix used for {N} zero-score conditions` — N is a substitutable count. | **PASS** |
| V-02 | Publisher 3.4 + ACTIONS GATE line with {N} substitutable. | **PASS** |
| V-03 | Phase 4c + ACTIONS GATE: `prevents: prefix used for {N} zero-score conditions`. | **PASS** |
| V-04 | Strategist 3.2 + ACTIONS GATE with {N}. | **PASS** |
| V-05 | Publisher 3.4 + ACTIONS GATE with {N}. | **PASS** |

---

**C-25 — Synthesis Novelty Constraint**

| | Evidence | Result |
|--|---------|--------|
| V-01 | Sec 3 Skeptic Gate: "A skeptic has read Sections 2a and 2b in full… The insight MUST contain information the skeptic would not already know." Operational exclusion: restating visible data fails. | **PASS** |
| V-02 | Publisher 3.3: explicit Skeptic gate with knowledge scope, exclusion rules ("An insight that echoes an inertia flag… fails"). | **PASS** |
| V-03 | Phase 3b: "The insight must contain something that reader would not already know. An insight that merely restates a Phase 2a inertia flag or a Phase 2b achievement count fails." | **PASS** |
| V-04 | Strategist 3.1: "An insight that restates a milestone status or a tally… fails. An insight that merely echoes an inertia flag… also fails." Explicit exclusion novelty gate. | **PASS** |
| V-05 | Publisher 3.3: Skeptic gate with explicit exclusion of inertia-flag echoes and reconciliation-pairing restatements. | **PASS** |

---

**C-26 — Named Role-Sequence Architecture**

| | Evidence | Result |
|--|---------|--------|
| V-01 | No named roles. Sections 1–4 are phases only. No scope-boundary language per role. | **FAIL** |
| V-02 | Archivist (data collection only — does NOT evaluate achievements or assess trajectory) → Analyst (evaluation only — does NOT make recommendations) → Publisher (synthesis and actions only). Scope exclusions explicit. Handoff points named. | **PASS** |
| V-03 | No named roles. Phases 1–4 only. No role identities or scope constraints. | **FAIL** |
| V-04 | Surveyor (team-level data only — does NOT evaluate per-topic achievements, NOT assess trajectory) → Assessor (per-topic analysis only — does NOT make recommendations) → Strategist (synthesis and actions only). Three named roles with scope boundaries and handoff points. | **PASS** |
| V-05 | Same Archivist/Analyst/Publisher structure as V-02, with explicit scope exclusions. | **PASS** |

---

**C-27 — Health / Inertia Structural Separation**

| | Evidence | Result |
|--|---------|--------|
| V-01 | Section 2a (Health Phase) and 2b (Inertia Phase) are distinct labeled blocks. 2a: "SHALL NOT report trajectory, momentum, direction of change." 2b: "SHALL NOT restate file counts or achievement statuses already visible in Section 2a." | **PASS** |
| V-02 | Analyst 2.1 Health Phase + 2.2 Inertia Phase. 2.1: "does NOT report trajectory, momentum, direction of change." 2.2: "does NOT restate file counts or achievement statuses already reported in the Health Phase." | **PASS** |
| V-03 | Phase 2a (Inertia Phase, inverted order) + Phase 2b (Health Phase). 2a: "does NOT report file counts, achievement statuses, or coverage totals." 2b: "does NOT restate inertia flags or trajectory claims already visible in Phase 2a." | **PASS** |
| V-04 | Assessor 2.1 Health Phase + 2.2 Inertia Phase. Explicit exclusions: "does NOT report trajectory, momentum, direction of change or stall indicators" in Health; "does NOT restate file counts or achievement statuses" in Inertia. | **PASS** |
| V-05 | Analyst 2.1 Health Phase + 2.2 Inertia Phase, same boundary language as V-02. | **PASS** |

---

**C-28 — Named Artifact Set at Role Handoff**

| | Evidence | Result |
|--|---------|--------|
| V-01 | No role sequence. No handoffs. | **FAIL** |
| V-02 | Archivist Handoff: artifact list {1. Registry table, 2. Contributor index table}. Analyst Handoff: {1. Per-topic Health Phase achievement tables, 2. Team milestone table, 3. Inertia Phase table, 4. Nearest-miss assessment table}. Two handoffs, both with enumerated artifact inventories. | **PASS** |
| V-03 | No role sequence. Phases have no inter-phase artifact handoff declarations. | **FAIL** |
| V-04 | Surveyor Handoff: {1. Registry table, 2. Team milestone table, 3. Contributor leaderboard table}. Assessor Handoff: {1. Per-topic Health Phase achievement tables, 2. Inertia Phase table, 3. Nearest-miss assessment table}. Two handoffs with named artifact inventories. | **PASS** |
| V-05 | Archivist Handoff: {1. Registry table, 2. Contributor index table}. Analyst Handoff: {1. Per-topic Health Phase achievement tables, 2. Team milestone table, 3. Inertia Phase table, 4. Nearest-miss assessment table}. Same as V-02. | **PASS** |

---

**C-29 — Per-Phase Completion Checklist Gate**

| | Evidence | Result |
|--|---------|--------|
| V-01 | Section 1 Gate (2 items), Section 2 Gate (6 items), Section 3 Gate (3 items), Section 4 Gate (5 items). Four gates, each with ≥2 distinct checklist items. | **PASS** |
| V-02 | Archivist Gate (2 items), Analyst Gate (5 items), Publisher Gate (5 items). Three role gates, each ≥2 items. | **PASS** |
| V-03 | Phase 1 Gate (2 items), Phase 2 Gate (5 items), Phase 3 Gate (3 items), Phase 4 Gate (4 items). Four gates, each ≥2 distinct items. | **PASS** |
| V-04 | Surveyor Gate (3 items), Assessor Gate (4 items), Strategist Gate (5 items). Three gates, each ≥2 distinct items. | **PASS** |
| V-05 | Archivist Gate (2 items), Analyst Gate (5 items), Publisher Gate (6 items). Three gates, each ≥2 items. | **PASS** |

---

**C-30 — Contamination-Check Checklist Item at Health/Inertia Gate**

| | Evidence | Result |
|--|---------|--------|
| V-01 | Section 2 Gate includes: `[ ] No trajectory claims appear in Section 2a; no static counts from Section 2a restated in Section 2b`. Explicit dual-direction prohibition at gate. | **PASS** |
| V-02 | Analyst Gate includes: `[ ] Inertia Phase table present; no static counts restated from Health Phase`. Explicit content-boundary enforcer at the evaluation phase gate. | **PASS** |
| V-03 | Phase 2 Gate includes: `[ ] No static counts or achievement statuses appear in Phase 2a (Inertia only); no trajectory claims or inertia flags restated in Phase 2b (Health only)`. Inverted direction but explicit prohibition. | **PASS** |
| V-04 | Assessor Gate includes: `[ ] Inertia Phase table present; no static counts restated from Health Phase`. Content boundary enforced at gate level. | **PASS** |
| V-05 | Analyst Gate includes: `[ ] Inertia Phase table present; no static counts restated from Health Phase`. Same as V-02. | **PASS** |

---

**C-31 — Inertia-Aware Skeptic Knowledge Scope**

| | Evidence | Result |
|--|---------|--------|
| V-01 | Sec 3 Skeptic: "A skeptic has read Sections 2a and 2b in full and already knows every achievement status, every milestone status, **every inertia flag**, every trajectory note, and every contributor tally." Inertia flags named explicitly. | **PASS** |
| V-02 | Publisher 3.3: "The Skeptic has read the Analyst's full output — every achievement table, every milestone row, **every inertia flag**, every trajectory note, and the nearest-miss assessment." Inertia flags named by name. | **PASS** |
| V-03 | Phase 3b: "a reader who completed Phase 2 already knows **every inertia flag (Phase 2a)**, the full cluster distribution, every achievement status and milestone outcome (Phase 2b)." Inertia flags explicitly in knowledge scope. "An insight that merely restates a Phase 2a inertia flag… fails." | **PASS** |
| V-04 | Strategist 3.1: "An insight that merely **echoes an inertia flag** from the Assessor's output also fails." The Skeptic's knowledge is anchored to the Assessor's full output, explicitly including inertia flags. | **PASS** |
| V-05 | Publisher 3.3: "every inertia flag, every trajectory note" explicitly named in Skeptic knowledge scope. | **PASS** |

---

### Composite Aspirational Scores

| Variation | Baseline (C-06–C-21) | C-22 | C-23 | C-24 | C-25 | C-26 | C-27 | C-28 | C-29 | C-30 | C-31 | Total Asp. |
|-----------|---------------------|------|------|------|------|------|------|------|------|------|------|------------|
| V-01 | 13 | P | P | P | P | F | P | F | P | P | P | **21/23** |
| V-02 | 13 | P | P | P | P | P | P | P | P | P | P | **23/23** |
| V-03 | 13 | P | P | P | P | F | P | F | P | P | P | **21/23** |
| V-04 | 13 | P | P | P | P | P | P | P | P | P | P | **23/23** |
| V-05 | 13 | P | P | P | P | P | P | P | P | P | P | **23/23** |

---

### Final Scores

| Rank | Variation | Essential | Aspirational | Score |
|------|-----------|-----------|--------------|-------|
| 1 (tie) | **V-02** | 5/5 | 23/23 | **100.00** |
| 1 (tie) | **V-04** | 5/5 | 23/23 | **100.00** |
| 1 (tie) | **V-05** | 5/5 | 23/23 | **100.00** |
| 4 (tie) | **V-01** | 5/5 | 21/23 | **99.13** |
| 4 (tie) | **V-03** | 5/5 | 21/23 | **99.13** |

Three variations reach the ceiling. V-01 and V-03 both fail C-26 (no named role sequence) and C-28 (no artifact handoffs). C-27 remains load-bearing for three criteria: C-27 itself, C-30, and C-31 — all five variations now pass it.

---

### Excellence Signals

**Top-scoring variations**: V-02, V-04, V-05. All three pass the same 23 criteria. What distinguishes V-05 from V-02 and V-04 is the explicit introduction of two structural patterns not yet tested by v11:

---

**Seed A — Inertia Flag-to-Action Traceability** (V-01, V-05)

Actions whose primary purpose resolves an inertia flag declare `resolves: {flag-name}` in the action row, traced back to a specific observation from the Inertia Phase. This is orthogonal to the `prevents:` machinery (zero-score conditions) and the achievement-name requirement (C-05). It creates a visible link from the action layer to the trajectory dimension. Appears in V-01 (as the sole seed) and V-05 (integrated with Seed B). Neither v11 criterion tests for this — it lives between C-20/C-24 (prevents: prefix) and C-27 (inertia phase exists), covering the gap of whether trajectory observations actually route into actions.

**Seed B — Pre-Synthesis Cross-Dimensional Reconciliation** (V-02, V-05)

Before the Publisher writes the Team Insight, it emits an explicit reconciliation pairing: one Health Phase observation and one Inertia Phase observation, with a stated interaction. The Skeptic gate then requires the Team Insight to advance beyond this pairing — an insight that merely restates the reconciliation row fails. This forces a provable structured synthesis step at the instruction level, not just at knowledge-scope level. Orthogonal to C-25 (novelty relative to analysis phase) and C-31 (Skeptic knowledge includes inertia flags) — C-33 would test whether the instruction mandates a concrete named H+I pairing as an intermediate output. Appears in V-02 and V-05.

**Seed C — Inertia Flag Cluster Table** (V-03)

After per-topic inertia evaluation, V-03 requires a cluster table grouping topics by shared flag pattern (`stuck-at-first: [topic-a, topic-c]`). This enables second-order trajectory pattern recognition — seeing which topics share the same stall condition — not available from individual inertia rows. Appears only in V-03 (the inertia-first lifecycle variation). Not present in V-05. Presupposes C-27.

The ceiling-breaking opportunity for v12: a variation passing both C-32 (Seed A) and C-33 (Seed B) while holding all 23 v11 criteria would score 25/25 under a v12 rubric.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Inertia Flag-to-Action Traceability: actions resolving an inertia flag declare resolves:{flag-name} in the action row, linking the action layer directly to a specific Inertia Phase observation — orthogonal to prevents: (zero-score conditions) and C-05 (achievement naming)", "Pre-Synthesis Cross-Dimensional Reconciliation: Publisher emits an explicit named pairing of one Health Phase observation and one Inertia Phase observation with an interaction statement before writing the Team Insight; Skeptic gate requires the insight to advance beyond the reconciliation pairing, not merely restate it"]}
```
