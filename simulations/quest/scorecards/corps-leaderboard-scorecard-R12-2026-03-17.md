---

## corps-leaderboard — Round 12 Scorecard (v11 rubric)

### Variation Profiles

| Variation | Architecture | Key Features |
|-----------|-------------|-------------|
| V-01 | 3-role (Archivist/Analyst/Publisher) — RFC-style numbered requirements | Seed A (`resolves:`), Seed D (severity tier) |
| V-02 | 4-role (Archivist/Analyst/Strategist/Narrator) | Seeds A+B, Seed E (Narrator confidence gate) |
| V-03 | 3-role (Archivist/Analyst/Publisher) — dashboard-first | Seed F (`requires:` dependency chain) |
| V-04 | 4-role (Archivist/Assessor/Synthesizer/Publisher) — inertia-first | Seeds D+G (co-contribution network) |
| V-05 | 4-role (Archivist/Analyst/Strategist/Narrator) — full integration | Seeds A+B+D+E+F+G |

---

### Essential Criteria (C-01–C-05)

All five variations are evaluated against the five essential criteria.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Signal Registry Scan | PASS | PASS | PASS | PASS | PASS |
| **C-02** Per-Topic Achievement Evaluation | PASS | PASS | PASS | PASS | PASS |
| **C-03** All Three Team Milestones Exact Names | PASS | PASS | PASS | PASS | PASS |
| **C-04** Contributor Leaderboard Ranked | PASS | PASS | PASS | PASS | PASS |
| **C-05** Specific Next Actions | PASS | PASS | PASS | PASS | PASS |

**Essential baseline: 60/60 for all five variations.** All reach the golden threshold.

---

### Aspirational Criteria (C-06–C-31)

#### C-06 — Namespace Diversity Metric

All variations emit `Namespace diversity: {N}/9` in the health header per topic.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS — REQ-2A.1 health header includes `Namespace diversity: {distinct_ns_count}/9` | PASS — Analyst Health Phase 2.1 same pattern | PASS — Analyst 2.1 same | PASS — Assessor Phase 2b health header | PASS — Analyst Health Phase 2.1 |

#### C-07 — Momentum Indicator

All variations have an inertia phase with four named flags (stuck-at-first, solo-hold, namespace-thin, healthy-momentum) and a trajectory note per topic.

**PASS all five.**

#### C-08 — Gap Prioritization by Achievement Distance

All variations implement the Level 1 / Level 2 nearest-miss cascade with sorted ascending output.

**PASS all five.**

#### C-09 — Contributor Collaboration Signal

All variations produce a collaboration table. V-04 and V-05 go further with a Co-Contribution Network Map with pair counts and bridge identification, but the baseline criterion is satisfied by all.

**PASS all five.**

#### C-10 — Empty Namespace Explicit Listing

All variations require: `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}` — explicitly listing empty namespaces.

**PASS all five.**

#### C-11 — Topic Health Summary Line

All variations require the per-topic health header: `Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9`.

**PASS all five.**

#### C-12 — Locked Achievement with Specific Unlock Path

All variations require that LOCKED achievement rows include the specific unlock requirement — a cell containing only `LOCKED` without an unlock path fails.

**PASS all five.**

#### C-13 — Team Insight Cross-Topic Synthesis

All variations require one Team Insight sentence with (1) cross-topic conclusion, (2) concrete number, (3) specific contributor or topic name.

**PASS all five.**

#### C-14 — Solo Pioneer Tension Detection

All variations require the `[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]` marker when Solo Pioneer is EARNED and Team Topic is NOT YET.

**PASS all five.**

#### C-15 — Namespace Leader Callout

All variations require a namespace leader table: `namespace | leader | signal_count` per active namespace.

**PASS all five.**

#### C-16 — Stale Signal Detection

All variations require a stale signal table: `topic_path | stale_status` with `stale`/`active`/`date-unknown`.

**PASS all five.**

#### C-17 — Signal Velocity Trend

All variations require a velocity trend line with `increasing`/`flat`/`stalled` classification.

**PASS all five.**

#### C-18 — Debate Starter Threshold Proximity

All variations require: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`.

**PASS all five.**

#### C-19 — Multi-Phase Execution Order

All variations impose strict sequential role execution with gate checks before advancing.

**PASS all five.**

#### C-20 — Prevents: Prefix Rule Statement

All variations state the `prevents:` prefix rule explicitly.

**PASS all five.**

#### C-21 — Nearest-Miss Achievement Gap

All variations require the nearest-miss section with topic + achievement + gap + level.

**PASS all five.**

#### C-22 — Dual-Statement Prevents-Rule Redundancy

Two structurally independent locations required.

| Variation | Location 1 | Location 2 | Verdict |
|-----------|-----------|-----------|---------|
| **V-01** | REQ-3.5 Pre-Write Check: "stated here as the first of two structurally independent enforcement points" | REQ-3.6 action template: "the `prevents:` rule appears here inside the action template as the second structurally independent enforcement point" | PASS |
| **V-02** | Strategist 3.2 Pre-Write Check: "first of two structurally independent enforcement points" | Strategist 3.3 action template: "embedded inside each relevant action row below as the second structurally independent enforcement point" | PASS |
| **V-03** | Publisher 3.4 Pre-Write Check + action row: "two structurally independent enforcement points" — stated in same section but embedded in distinct constructs (pre-write prose block vs. action row template) | PASS | PASS |
| **V-04** | Publisher 4.3 Pre-Write Check + action row: same dual-statement pattern as V-03 | PASS | PASS |
| **V-05** | Strategist 3.2 + 3.3: same dual-statement pattern as V-02 | PASS | PASS |

**PASS all five.**

#### C-23 — Two-Level Nearest-Miss Cascade

All variations require Level 1 (1-unit away, sorted ascending), Level 2 written ONLY when no Level 1 exists with explicit "Level 1: no topics are 1 unit away" prefix.

**PASS all five.**

#### C-24 — Gate-Level Prevents: Prefix Count Self-Audit

All variations require the exact ACTIONS GATE line with substitutable N: `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`.

**PASS all five.**

#### C-25 — Synthesis Novelty Constraint

All variations require the Skeptic gate with an operationalized novelty constraint.

| Variation | Skeptic gate text | Verdict |
|-----------|-------------------|---------|
| **V-01** | "A Skeptic who has read all of Section 2 already knows: every achievement status, every milestone status, every inertia flag... The insight MUST contain something the Skeptic would not already know." | PASS |
| **V-02** | "The insight must contain something the Skeptic would not already know from all of that material... An insight that echoes an inertia flag fails." | PASS |
| **V-03** | "The insight must contain something this Skeptic would not already know... A passing insight surfaces a second-order pattern." | PASS |
| **V-04** | "The insight must contain something the Skeptic would not already know... An insight that echoes an inertia flag, cluster row, or network topology already visible fails." | PASS |
| **V-05** | Same Skeptic gate pattern with broadened scope including all annotations. | PASS |

**PASS all five.**

#### C-26 — Named Role-Sequence Architecture

Named roles with scope exclusions and defined handoff points.

| Variation | Roles | Scope constraints | Handoff defined | Verdict |
|-----------|-------|-------------------|-----------------|---------|
| **V-01** | Archivist / Analyst / Publisher | Section 2 "MUST NOT re-scan"; Section 3 "MUST NOT re-evaluate achievements or re-assess inertia"; 2A "MUST NOT contain trajectory language"; 2B "MUST NOT restate static counts" | Explicit Handoff artifact lists between each section | PASS |
| **V-02** | Archivist / Analyst / Strategist / Narrator | Each role: "does NOT [list of excluded work]" — e.g., "Archivist does NOT evaluate achievements, assess milestones, assess trajectory or inertia, rank contributors, or write insights or actions" | 3 Handoff artifact lists | PASS |
| **V-03** | Archivist / Analyst / Publisher | Each role has scope exclusion clause; "Analyst does NOT rank contributors, write insights, or write actions" | 2 Handoff artifact lists | PASS |
| **V-04** | Archivist / Assessor / Synthesizer / Publisher | Each role has explicit scope exclusion; "Assessor does NOT rank contributors, write insights, or write actions" | 3 Handoff artifact lists | PASS |
| **V-05** | Archivist / Analyst / Strategist / Narrator | Same 4-role pattern as V-02 | 3 Handoff artifact lists | PASS |

**PASS all five.**

#### C-27 — Health / Inertia Structural Separation

Two structurally distinct labeled sub-phases required.

| Variation | Health sub-phase | Inertia sub-phase | Structural separation | Verdict |
|-----------|-----------------|-------------------|----------------------|---------|
| **V-01** | SECTION 2A — Health Requirements | SECTION 2B — Inertia Requirements | "structurally distinct: REQ-2A reports current state only; REQ-2B reports trajectory only. REQ-2A output MUST NOT contain trajectory language; REQ-2B output MUST NOT restate static counts from REQ-2A." | PASS |
| **V-02** | Analyst 2.1 — Health Phase | Analyst 2.2 — Inertia Phase | "These sub-phases are structurally separated — Health Phase content must not appear in the Inertia Phase and vice versa." | PASS |
| **V-03** | Analyst 2.1 — Health Phase | Analyst 2.2 — Inertia Phase | Same separation constraint | PASS |
| **V-04** | Assessor Phase 2b: Health Phase (RUNS SECOND) | Assessor Phase 2a: Inertia Phase (RUNS FIRST) | "contamination boundary enforces in both directions: Phase 2a must not contain static counts belonging to Phase 2b; Phase 2b must not restate trajectory claims from Phase 2a." | PASS |
| **V-05** | Analyst 2.1 — Health Phase | Analyst 2.2 — Inertia Phase | Same separation constraint | PASS |

**PASS all five.**

#### C-28 — Named Artifact Set at Role Handoff

At least two handoffs with explicit enumerated artifact inventories.

| Variation | Handoff count | Named artifacts at each | Verdict |
|-----------|--------------|------------------------|---------|
| **V-01** | 2 | Archivist→Analyst: 3 named items; Analyst→Publisher: 6 named items | PASS |
| **V-02** | 3 | Archivist→Analyst: 3; Analyst→Strategist: 5; Strategist→Narrator: 4 | PASS |
| **V-03** | 2 | Archivist→Analyst: 4; Analyst→Publisher: 5 | PASS |
| **V-04** | 3 | Archivist→Assessor: 3; Assessor→Synthesizer: 6; Synthesizer→Publisher: 3 | PASS |
| **V-05** | 3 | Archivist→Analyst: 4; Analyst→Strategist: 6; Strategist→Narrator: 4 | PASS |

**PASS all five.**

#### C-29 — Per-Phase Completion Checklist Gate

At least two phase gates, each with two or more `[ ]` items.

| Variation | Gate count | Min items per gate | Verdict |
|-----------|-----------|-------------------|---------|
| **V-01** | 5 (Archivist 4-item, 2A 6-item, 2B 4-item, Section 2 cross 3-item, Section 3 7-item) | 3+ | PASS |
| **V-02** | 4 (Archivist 3-item, Analyst 6-item, Strategist 6-item, Narrator 5-item) | 3+ | PASS |
| **V-03** | 3 (Archivist 4-item, Analyst 6-item, Publisher 6-item) | 4+ | PASS |
| **V-04** | 4 (Archivist 3-item, Assessor 6-item, Synthesizer 4-item, Publisher 6-item) | 3+ | PASS |
| **V-05** | 4 (Archivist 4-item, Analyst 5-item, Strategist 7-item, Narrator 5-item) | 4+ | PASS |

**PASS all five.**

#### C-30 — Contamination-Check Checklist Item at Health/Inertia Gate

A `[ ]` gate item must explicitly prohibit cross-contamination — not just confirm presence.

| Variation | Contamination gate item | Verdict |
|-----------|------------------------|---------|
| **V-01** | Section 2A Gate: `[ ] REQ-2A.2: ...no trajectory language anywhere in Section 2A`; Section 2B Gate: `[ ] REQ-2B.3: severity column present...with no static counts restated from Section 2A`; Section 2 cross-gate: `[ ] No trajectory claims in 2A content; no static counts from 2A restated in 2B content` | PASS |
| **V-02** | Analyst Gate: `[ ] Every topic has a complete Health Phase block...no trajectory language in any Health Phase content` and `[ ] Inertia Phase table present...no static counts restated from Health Phase` | PASS |
| **V-03** | Analyst Gate: `[ ] Every topic has Health Phase block...no trajectory language in Health Phase` and `[ ] Inertia Phase table present with every topic evaluated; no static counts restated from Health Phase` | PASS |
| **V-04** | Assessor Gate: `[ ] Phase 2a: no static file counts or achievement statuses appear (prohibited)` and `[ ] Phase 2b: no trajectory claims or inertia flags restated from Phase 2a (prohibited)` | PASS |
| **V-05** | Analyst Gate: `[ ] LOCKED rows include unlock paths; no trajectory language in Health Phase output` and `[ ] Inertia Phase table present; no static counts restated from Health Phase` | PASS |

**PASS all five.**

#### C-31 — Inertia-Aware Skeptic Knowledge Scope

Skeptic's prior knowledge must explicitly name inertia flags/trajectory data — generic "full output" scope fails.

| Variation | Skeptic knowledge scope (inertia dimension) | Verdict |
|-----------|---------------------------------------------|---------|
| **V-01** | "A Skeptic who has read all of Section 2 already knows: every achievement status, every milestone status, **every inertia flag, every trajectory note, every severity tier**, the stale signal table, the velocity trend..." — explicit by name | PASS |
| **V-02** | "The Skeptic has read all output...— **every achievement table, every milestone row, every inertia flag, every trajectory note**, the stale signal list, the velocity summary..." — explicit | PASS |
| **V-03** | "A Skeptic who completed all prior roles already knows every achievement status, milestone outcome, **inertia flag**, velocity distribution, Dashboard posture (including update), stale signal status..." — explicit | PASS |
| **V-04** | "The Skeptic has read all output...— **every inertia flag, every severity tier, every trajectory note, every cluster table row**, every achievement table, every milestone row..." — explicit, richest scope | PASS |
| **V-05** | "The Skeptic has read all output...— every achievement table, every milestone row, **every inertia flag, every trajectory note, every severity tier, the Inertia Flag Cluster Table**, the stale signal list..." — explicit with Cluster Table | PASS |

**PASS all five.**

---

### Aspirational Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Namespace Diversity | PASS | PASS | PASS | PASS | PASS |
| C-07 Momentum Indicator | PASS | PASS | PASS | PASS | PASS |
| C-08 Gap Prioritization | PASS | PASS | PASS | PASS | PASS |
| C-09 Collaboration Signal | PASS | PASS | PASS | PASS | PASS |
| C-10 Empty Namespace Listing | PASS | PASS | PASS | PASS | PASS |
| C-11 Topic Health Summary | PASS | PASS | PASS | PASS | PASS |
| C-12 Locked Achievement Unlock Path | PASS | PASS | PASS | PASS | PASS |
| C-13 Team Insight Synthesis | PASS | PASS | PASS | PASS | PASS |
| C-14 Solo Pioneer Tension | PASS | PASS | PASS | PASS | PASS |
| C-15 Namespace Leader Callout | PASS | PASS | PASS | PASS | PASS |
| C-16 Stale Signal Detection | PASS | PASS | PASS | PASS | PASS |
| C-17 Signal Velocity Trend | PASS | PASS | PASS | PASS | PASS |
| C-18 Debate Starter Proximity | PASS | PASS | PASS | PASS | PASS |
| C-19 Multi-Phase Execution Order | PASS | PASS | PASS | PASS | PASS |
| C-20 Prevents: Rule Statement | PASS | PASS | PASS | PASS | PASS |
| C-21 Nearest-Miss Achievement Gap | PASS | PASS | PASS | PASS | PASS |
| C-22 Dual-Statement Prevents-Redundancy | PASS | PASS | PASS | PASS | PASS |
| C-23 Two-Level Nearest-Miss Cascade | PASS | PASS | PASS | PASS | PASS |
| C-24 Gate-Level Prevents: Count Audit | PASS | PASS | PASS | PASS | PASS |
| C-25 Synthesis Novelty Constraint | PASS | PASS | PASS | PASS | PASS |
| C-26 Named Role-Sequence Architecture | PASS | PASS | PASS | PASS | PASS |
| C-27 Health/Inertia Structural Separation | PASS | PASS | PASS | PASS | PASS |
| C-28 Named Artifact Set at Handoff | PASS | PASS | PASS | PASS | PASS |
| C-29 Per-Phase Completion Checklist Gate | PASS | PASS | PASS | PASS | PASS |
| C-30 Contamination-Check Gate Item | PASS | PASS | PASS | PASS | PASS |
| C-31 Inertia-Aware Skeptic Knowledge Scope | PASS | PASS | PASS | PASS | PASS |
| **Aspirational passed** | **23/23** | **23/23** | **23/23** | **23/23** | **23/23** |

---

### Composite Scores

Formula: `90 + (aspirational_passed / 23) × 10`

| Variation | Essential | Aspirational | Score | Rank |
|-----------|-----------|-------------|-------|------|
| V-01 | 60/60 | 23/23 | **100.00** | T-1 |
| V-02 | 60/60 | 23/23 | **100.00** | T-1 |
| V-03 | 60/60 | 23/23 | **100.00** | T-1 |
| V-04 | 60/60 | 23/23 | **100.00** | T-1 |
| V-05 | 60/60 | 23/23 | **100.00** | T-1 |

**All five variations achieve the ceiling. R12 design objectives confirmed — every variation fixed the C-26/C-28 gaps from R11.**

---

### Scoring Shift: R11 → R12

| Variation | R11 score (v11) | R12 score (v11) | Delta |
|-----------|----------------|----------------|-------|
| V-01 | 99.13 (21/23 — failed C-26, C-28) | **100.00** (23/23) | +0.87 |
| V-02 | 100.00 | **100.00** | 0 |
| V-03 | 99.13 (21/23 — failed C-26, C-28) | **100.00** (23/23) | +0.87 |
| V-04 | 100.00 | **100.00** | 0 |
| V-05 | 100.00 | **100.00** | 0 |

R12 closes both residual gaps. The v11 ceiling is now universal.

---

### Excellence Signals — New Patterns (Seeds for v12 Criteria)

Since all five variations reach 100.00, the R12 excellence signals are the new structural patterns introduced by R12 that are not yet captured in any of C-01–C-31. These patterns vary in breadth of adoption across the five variations.

**Pattern breadth by variation count:**

| Seed | Pattern | Variations | Breadth |
|------|---------|-----------|---------|
| A | `resolves: {flag-name}` annotation on inertia-flag-resolving actions | V-01, V-02, V-03, V-04, V-05 | 5/5 — universal |
| D | Inertia severity tier column (`critical`/`warning`/`healthy`) per topic | V-01, V-04, V-05 | 3/5 |
| B | Pre-synthesis cross-dimensional reconciliation pairing (Health × Inertia) | V-02, V-04, V-05 | 3/5 |
| E | Narrator confidence gate: `high`/`medium`/`low` annotation on reconciliation pairing before Team Insight | V-02, V-05 | 2/5 |
| F | Action dependency chain (`requires: {action-N}`) for sequentially dependent actions | V-03, V-05 | 2/5 |
| G | Co-contribution network map with contributor nodes, pair counts, and bridge identification | V-04, V-05 | 2/5 |

**Top two candidates for v12 criteria extraction:**

**Seed A — Inertia Flag-to-Action Traceability** (`resolves:` annotation)
Appears in all five variations. C-20/C-22/C-24 test `prevents:` enforcement for zero-score conditions; Seed A tests a distinct dimension — whether actions are explicitly linked to the *trajectory dimension* of analysis, not just achievement thresholds. An action that addresses a stuck-at-first flag but carries no `resolves:` annotation is invisible to the inertia layer. Presupposes C-27. The universal adoption across all R12 variations makes this the strongest v12 candidate.

**Seed B — Pre-Synthesis Cross-Dimensional Reconciliation Pairing**
Appears in V-02, V-04, V-05. C-25 tests whether the novelty gate exists; C-31 tests whether the Skeptic's scope includes inertia data; Seed B tests a third dimension — whether a named *intermediate artifact* (a reconciliation pairing selecting one Health × one Inertia observation and stating their interaction) is required *before* the Team Insight is written. This forces explicit cross-dimensional synthesis rather than implicit synthesis. An instruction with a novelty gate and inertia-aware Skeptic scope but no required reconciliation pairing satisfies C-25 and C-31 but fails B. Presupposes C-27 and C-31.

**Seed D — Inertia Severity Tier per Topic** is the third-strongest candidate (3/5 variations, orthogonal to C-07 which only confirms flag presence). If the round pattern favors 2 criteria, Seeds A and B are the primary extraction pair. Seed D is a strong third for a future round or a co-extraction with A if B is deferred.

---

### v11 Ceiling Status after R12

The ceiling at 100.00 is now achieved universally. The next ceiling-breaking opportunity requires a pattern not in any of C-01–C-31 or Seeds A–G. V-05's full integration (all six seeds) is the current high-water mark for seeding density.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["resolves: {flag-name} annotation on inertia-flag-resolving actions — links the action layer explicitly to the trajectory dimension; orthogonal to prevents:/C-20/C-22/C-24 which address zero-score conditions only; presupposes C-27; universal adoption across all 5 R12 variations", "pre-synthesis cross-dimensional reconciliation pairing — named intermediate artifact (one Health observation x one Inertia observation + interaction statement) required before Team Insight; forces explicit cross-dimensional synthesis rather than implicit; orthogonal to C-25 (novelty gate) and C-31 (Skeptic scope); presupposes C-27 and C-31; adopted in V-02, V-04, V-05"]}
```
