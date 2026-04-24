## corps-achievements — R7 Scorecard

**Rubric version**: v6 (23 criteria)
**Variations evaluated**: V-01 through V-05

---

### Scoring Legend

- **PASS** — criterion fully satisfied
- **PARTIAL** — partially satisfied, notable gap
- **FAIL** — not present or incorrect

---

### V-01 — Formal/Technical Imperative

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | SCAN GATE [C-01/C-15]; glob instruction explicit; no inferred paths |
| C-02 | PASS | COMPUTE GATE [C-02/C-15]; topic count match enforced |
| C-03 | PASS | MILESTONES GATE [C-03/C-15]; exact name enforcement with fail-message naming row |
| C-04 | PASS | STEP 4 leaderboard section present |
| C-05 | PASS | ACTIONS GATE condition (2): "names the exact achievement or milestone it unlocks" |
| C-06 | PASS | Earned Achievements / Locked Achievements explicitly labeled |
| C-07 | PASS | Two named categories: Earned / Locked |
| C-08 | PASS | `{{date}}` in all section headers |
| C-09 | PASS | STEP 5 — dedicated section with 4-column table |
| C-10 | PASS | STEP 7 insight gate condition (2): "Names specific topics, contributors, or numeric values — not only pattern labels" |
| C-11 | PASS | Pre-write gates at Step 2 and Step 4 |
| C-12 | PASS | `[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]` format enforced |
| C-13 | PASS | `**TEAM INSIGHT — [descriptive name]:**` format in template |
| C-14 | PASS | `[PATTERN_LABEL from registry]` label syntax in action rows |
| C-15 | PASS | All fail messages name specific instance: "file '[path]'", "topic '[path]'", "row '[written name]'" |
| C-16 | PASS | `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)` explicit formula |
| C-17 | PASS | SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, SHALLOW_POOL, ORPHAN_TOPIC — semantic names |
| C-18 | PASS | 4-column table: Topic/Milestone, Achievement to Unlock, Gap, Exact Action Needed |
| C-19 | PASS | FORMULA CORRECTION GATE condition (1): worked example for Rank 1 |
| C-20 | PASS | All gate labels carry criterion IDs; ACTIONS GATE condition (5) self-validates the label |
| C-21 | PASS | Condition (3): "If {total} does not equal the Score column entry, correct the Score column to {total} before proceeding" |
| C-22 | PASS | Step B in STEP 7: "Can this insight be reached from [topic path] data alone, without any other topic?" |
| C-23 | PASS | Every gate enumerates conditions as `(1)…(2)…(3)…` sub-steps |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 15/15
**Score**: (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = **100**

---

### V-02 — Conversational/Narrative Team Report

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "scan check [C-01/C-15]" with numbered sub-steps; workspace-empty fallback stated |
| C-02 | PASS | "Completeness check [C-02/C-15]" sub-step (1) counts topics; fail names "[path]" |
| C-03 | PASS | "Milestone check [C-03/C-15]" — exact names enforced in sub-steps |
| C-04 | PASS | Section 3 "Who's Leading" leaderboard |
| C-05 | PASS | "Actions check [C-05/C-12/C-14/C-20]" condition (2) checks exact achievement name |
| C-06 | PASS | Earned Achievements / Locked Achievements |
| C-07 | PASS | Two named categories |
| C-08 | PASS | `{{date}}` in headers |
| C-09 | PASS | Section 4 "One Step Away" with 4-column table |
| C-10 | PASS | Section 6 insight gate condition (2) requires specific names/numbers |
| C-11 | PASS | Pre-write gates before Section 1 and Section 3 |
| C-12 | PASS | `→ Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]` format |
| C-13 | PASS | `**TEAM INSIGHT — [descriptive name]:**` template |
| C-14 | PASS | `[PATTERN_LABEL from registry]` label syntax |
| C-15 | PASS | "Completeness check [C-02]: topic '[path]' got left out" — specific failure framing |
| C-16 | PASS | Formula stated inline |
| C-17 | PASS | Semantic labels |
| C-18 | PASS | 4-column table |
| C-19 | PASS | "Score verification check [C-19/C-21]" condition (1): worked example |
| C-20 | PASS | All gate labels carry criterion IDs; "Actions check [C-05/C-12/C-14/C-20]" |
| C-21 | PASS | Condition (3): "fix the Score column to show {total} and note: 'Score corrected'" |
| C-22 | PASS | "Could someone reach this conclusion from [topic path] data alone, without any other topic?" |
| C-23 | PASS | All checks enumerate numbered sub-steps |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 15/15
**Score**: **100**

---

### V-03 — Lifecycle Ordering: Milestone-First

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | SCAN GATE [C-01/C-15] with numbered sub-steps |
| C-02 | PASS | COMPUTE GATE [C-02/C-15] |
| C-03 | PASS | MILESTONES GATE [C-03/C-15]; Phase 2 runs before Phase 3 |
| C-04 | PASS | PHASE 4 leaderboard |
| C-05 | PASS | ACTIONS GATE [C-05/C-12/C-14/C-20] |
| C-06 | PASS | Earned / Locked separation |
| C-07 | PASS | Two named categories |
| C-08 | PASS | `{{date}}` framing; `ordering: milestone-first` in frontmatter |
| C-09 | PASS | PHASE 5 — 1-AWAY GAPS, 4-column table; Phase 2 milestone gaps fed into condition (3) |
| C-10 | PASS | PHASE 7 derivability protocol with topic-by-topic test |
| C-11 | PASS | Pre-write gates at PHASE 3 and PHASE 4; PHASE 3 gate explicitly asks whether milestone gaps from Phase 2 surface topics not yet in scan |
| C-12 | PASS | Action format with unlock + break pattern |
| C-13 | PASS | `**TEAM INSIGHT — [descriptive name]:**` format |
| C-14 | PASS | Registry label syntax enforced |
| C-15 | PASS | Fail messages name specific topic, file, or row |
| C-16 | PASS | Formula explicit |
| C-17 | PASS | Semantic labels |
| C-18 | PASS | 4-column table |
| C-19 | PASS | FORMULA CORRECTION GATE worked example |
| C-20 | PASS | All gate labels carry criterion IDs |
| C-21 | PASS | FORMULA CORRECTION GATE condition (3): correction instruction explicit |
| C-22 | PASS | PHASE 7 Step B: "Can this insight be reached from [topic path] alone, without any other topic?" |
| C-23 | PASS | All gates enumerate numbered sub-steps |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 15/15
**Score**: **100**

---

### V-04 — Combined: Formal + Milestone-First

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | SCAN GATE [C-01/C-15] formal command language |
| C-02 | PASS | COMPUTE GATE [C-02/C-15] |
| C-03 | PASS | MILESTONES GATE [C-03/C-15]; Phase 2 precedes Phase 3 |
| C-04 | PASS | PHASE 4 leaderboard |
| C-05 | PASS | ACTIONS GATE [C-05/C-12/C-14/C-20] condition (2) |
| C-06 | PASS | Earned / Locked separation |
| C-07 | PASS | Two named categories |
| C-08 | PASS | `{{date}}`; `ordering: milestone-first` + `register: formal` in frontmatter |
| C-09 | PASS | PHASE 5; milestone gaps from Phase 2 fed into 1-away check condition (3) |
| C-10 | PASS | PHASE 7 derivability protocol |
| C-11 | PASS | PHASE 4 pre-write gate explicitly cross-references milestone evidence from Phase 2: "Have I checked which contributors provided evidence toward the milestones earned in Phase 2?" |
| C-12 | PASS | Action format |
| C-13 | PASS | TEAM INSIGHT format |
| C-14 | PASS | Registry label syntax |
| C-15 | PASS | Specific failure instances named |
| C-16 | PASS | Formula explicit |
| C-17 | PASS | Semantic labels |
| C-18 | PASS | 4-column table |
| C-19 | PASS | Worked example in FORMULA CORRECTION GATE |
| C-20 | PASS | All gate labels carry criterion IDs; ACTIONS GATE condition (5) self-validates: "The gate label includes criterion IDs: [C-05/C-12/C-14/C-20]" |
| C-21 | PASS | Correction instruction in FORMULA CORRECTION GATE condition (3) |
| C-22 | PASS | Derivability elimination protocol in PHASE 7 |
| C-23 | PASS | All gates enumerate numbered sub-steps |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 15/15
**Score**: **100**

---

### V-05 — Combined: Conversational + Prominent Inertia Framing

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "Scan check [C-01/C-15]" with numbered sub-steps |
| C-02 | PASS | "Completeness check [C-02/C-15]" |
| C-03 | PASS | "Milestone check [C-03/C-15]" exact name enforcement |
| C-04 | PASS | Section 3 "Who's Leading" leaderboard |
| C-05 | PASS | "Actions check [C-05/C-12/C-14/C-20]" condition (2) checks exact achievement name |
| C-06 | PASS | Earned / Locked separation |
| C-07 | PASS | Two named categories |
| C-08 | PASS | `{{date}}` in headers |
| C-09 | PASS | Section 4 "One Step Away" with 4-column table |
| C-10 | PASS | Section 6 "The Pattern Only the Team Can See" — derivability test + gate condition (2) requires specific names |
| C-11 | PASS | Pre-write gates before Sections 1 and 3 |
| C-12 | PASS | `→ Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]` format |
| C-13 | PASS | `**TEAM INSIGHT — [descriptive name]:**` format |
| C-14 | PASS | Registry label syntax enforced |
| C-15 | PASS | "1-away check [C-09]: row '[topic]' missing '[column]'" — specific failure framing |
| C-16 | PASS | Formula stated inline |
| C-17 | PASS | Semantic labels |
| C-18 | PASS | 4-column table |
| C-19 | PASS | "Score check [C-19/C-21]" condition (1): worked example |
| C-20 | PASS | Gate labels carry criterion IDs; "Actions check [C-05/C-12/C-14/C-20]" |
| C-21 | PASS | Score check condition (3): "fix the Score column to {total}" |
| C-22 | PASS | "Could someone reach this conclusion from [topic path] data alone?" per-topic test |
| C-23 | PASS | All checks enumerate numbered sub-steps |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 15/15
**Score**: **100**

---

### Ranking

| Rank | Variation | Score |
|------|-----------|-------|
| 1 (tied) | V-01 Formal | 100 |
| 1 (tied) | V-02 Conversational | 100 |
| 1 (tied) | V-03 Milestone-First | 100 |
| 1 (tied) | V-04 Formal + Milestone-First | 100 |
| 1 (tied) | V-05 Conversational + Inertia-Throughout | 100 |

All variations score 100. This confirms that R7's variation axes (register, ordering, inertia prominence) are orthogonal to criterion coverage — register and ordering differences don't create criterion gaps. The structural floor established by R6 (C-21/C-22/C-23) is robust enough that all five register and ordering combinations satisfy every criterion.

---

### Excellence Signals

Two patterns appear in R7 that go beyond the current rubric floor:

**Pattern 1 — Cross-phase milestone carry-forward in pre-write gates** (V-03, V-04)

When milestone-first ordering is used, the pre-write gates in later phases don't just check completeness — they explicitly ask whether milestone data from the earlier phase changes the per-topic or contributor analysis. V-03 Phase 3: *"Milestone context from Phase 2 is now established — does any milestone gap point to a specific topic or achievement that should be highlighted in this section?"* V-04 Phase 4: *"Have I checked which contributors provided evidence toward the milestones earned in Phase 2?"* This creates inter-phase audit linkage, not just intra-section self-checks. The current C-11 requires a pre-write gate but does not require it to carry forward findings from earlier phases.

**Pattern 2 — Section-level inertia cost framing, not only in Next Actions** (V-05)

V-05 adds *Inertia notes* after every major output section: after Locked Achievements ("Would have earned this with one more [action] last sprint"), after Milestones ("this milestone has been sitting here"), after the Leaderboard ("Rank 2 is [n] points behind — one more topic contribution would change the top"), after 1-Away ("These are not hypotheticals"). The current C-12 requires anti-inertia framing only in the Next Actions action rows. V-05's section-level cost annotations make inertia visible at the point of each gap, not only at the action-planning stage — a structural change in where the urgency signal appears.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["cross-phase milestone carry-forward: pre-write gates in later phases explicitly audit whether milestone findings from earlier phases change per-topic or contributor analysis, creating structured inter-phase information flow beyond intra-section completeness checks", "section-level inertia cost framing: cost-of-inertia commentary surfaced at each output section through parenthetical annotations, making inertia visible at the point of each gap rather than only in Next Actions"]}
```
