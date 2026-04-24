**R16 scoring complete.** Scorecard written to `simulations/quest/scorecards/corps-leaderboard-scorecard-R16-2026-03-17.md`. Rubric v13 reconstructed and written to `simulations/quest/rubrics/corps-leaderboard-rubric-v13-2026-03-17.md`.

---

**Summary:**

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | V-05 | **100.00** (28/28) |
| 2 | V-01 | 98.93 (25/28) |
| 2 | V-02 | 98.93 (25/28) |
| 2 | V-03 | 98.93 (25/28) |
| 2 | V-04 | 98.93 (25/28) |

**What held the ceiling**: V-05 exclusively passes the three new v13 criteria — C-34 (Seed X falsifiability contract), C-35 (5-role Inspector discrepancy check), C-36 (Seeds K+V combined for 2D Round×Tier action matrix). V-02 has V but not K; V-04 has K but not V — neither achieves the 2D matrix.

**5 new patterns for v14** (C-37 through C-41): namespace gap debt (Seed AA), achievement co-occurrence matrix (Seed Z), flag lifecycle annotation (Seed Y), milestone regression risk (Seed AB), contributor onboarding path (Seed AC).

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["namespace gap debt column: per-contributor gap_debt = 9 minus distinct_namespaces; top-ranked contributor with gap_debt=7 signals breadth concentration risk invisible to signal count alone (Seed AA, V-01+V-05)", "achievement co-occurrence matrix: 5x5 symmetric count table revealing which achievement pairs always co-occur vs. appear independently (Seed Z, V-02+V-05)", "flag lifecycle annotation: each inertia flag tagged new/persistent/resolved against baseline file; persistent flags prioritized in action writing (Seed Y, V-03+V-05)", "milestone regression risk: per earned milestone stable/fragile:{contributor} by single-contributor removal test (Seed AB, V-04+V-05)", "contributor onboarding path: per Solo Pioneer EARNED + Team Topic NOT YET, one-line prompt naming fastest namespace+signal unlock (Seed AC, V-05 only)"]}
```
scending by gap in all 5 |
| C-09 Contributor Collaboration Signal | PASS | PASS | PASS | PASS | PASS | Collaboration-type table (pair/ensemble) in all 5 |
| C-10 Empty Namespace Explicit Listing | PASS | PASS | PASS | PASS | PASS | `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}` in all 5 |
| C-11 Topic Health Summary Line | PASS | PASS | PASS | PASS | PASS | Per-topic header with Files/Namespaces/Contributors/Diversity in all 5 |
| C-12 Locked Achievement Unlock Path | PASS | PASS | PASS | PASS | PASS | LOCKED rows include inline numeric unlock requirements in all 5 |
| C-13 Team Insight Cross-Topic Synthesis | PASS | PASS | PASS | PASS | PASS | One sentence with (1) cross-topic conclusion (2) concrete number (3) specific name in all 5 |
| C-14 Solo Pioneer Tension Detection | PASS | PASS | PASS | PASS | PASS | `[TENSION: solo hold — 1 additional contributor...]` in all 5 |
| C-15 Namespace Leader Callout | PASS | PASS | PASS | PASS | PASS | `namespace | leader | signal_count` table in all 5 |
| C-16 Stale Signal Detection | PASS | PASS | PASS | PASS | PASS | `topic_path | stale_status` (stale/active/date-unknown) in all 5 |
| C-17 Signal Velocity Trend | PASS | PASS | PASS | PASS | PASS | Velocity summary with Trend: increasing/flat/stalled in all 5 |
| C-18 Debate Starter Threshold Proximity | PASS | PASS | PASS | PASS | PASS | `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)` in all 5 |
| C-19 Multi-Phase Execution Order | PASS | PASS | PASS | PASS | PASS | Sequential named-role pipelines (3-role V-01/V-02; 4-role V-03/V-04; 5-role V-05) in all 5 |
| C-20 Prevents: Prefix Rule Statement | PASS | PASS | PASS | PASS | PASS | `prevents:` rule in Pre-Write Check in all 5 |
| C-21 Nearest-Miss Achievement Gap | PASS | PASS | PASS | PASS | PASS | Nearest-miss table with topic/achievement/gap/level in all 5 |
| C-22 Dual-Statement Prevents-Rule Redundancy | PASS | PASS | PASS | PASS | PASS | Two structurally independent enforcement points (Pre-Write Check + action template) in all 5 |
| C-23 Two-Level Nearest-Miss Cascade | PASS | PASS | PASS | PASS | PASS | Level 1 / Level 2 with conditional gate ("Level 1: none" before Level 2) in all 5 |
| C-24 Gate-Level Prevents: Prefix Count Audit | PASS | PASS | PASS | PASS | PASS | `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` substitutable N in all 5 |
| C-25 Synthesis Novelty Constraint | PASS | PASS | PASS | PASS | PASS | Named Skeptic gate with exclusion rule in all 5 |
| C-26 Named Role-Sequence Architecture | PASS | PASS | PASS | PASS | PASS | All pipelines have named roles with scope boundaries (explicit "does NOT" exclusions) and handoff points |
| C-27 Health / Inertia Structural Separation | PASS | PASS | PASS | PASS | PASS | Inertia Phase and Health Phase are structurally distinct labeled blocks in all 5; lifecycle note enforces Inertia before Health |
| C-28 Named Artifact Set at Role Handoff | PASS | PASS | PASS | PASS | PASS | Every handoff enumerates specific named artifacts (tables, columns) not category labels in all 5 |
| C-29 Per-Phase Completion Checklist Gate | PASS | PASS | PASS | PASS | PASS | Multi-item `[ ]` gates at Archivist, Inertia Phase, Health Phase, terminal action gate in all 5 |
| C-30 Contamination-Check Gate Item | PASS | PASS | PASS | PASS | PASS | Gate item explicitly prohibiting cross-phase content (no trajectory in Health; no static counts in Inertia) in all 5 |
| C-31 Inertia-Aware Skeptic Knowledge Scope | PASS | PASS | PASS | PASS | PASS | Skeptic scope names inertia flags, severity tiers, velocity summary explicitly in all 5 |
| C-32 Milestone Proximity Ladder | PASS | PASS | PASS | PASS | PASS | **R15 universal** — per-precondition deficit breakdown for every NOT YET milestone; Skeptic scope includes ladder breakdowns in all 5 |
| C-33 Flag/Achievement Echo Detection | PASS | PASS | PASS | PASS | PASS | **R15 universal** — dedicated Echo Detection section with Rules A+B, echo table, retraction statements, Pre-Write Check exclusion on `resolves:` in all 5 |

---

### Aspirational Criteria — C-34 through C-36 (new in v13)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-34** Insight Falsifiability Contract | FAIL | FAIL | FAIL | FAIL | PASS | Requires Seed X (only V-05); `[holds if:] / [falsified by:]` contract lines absent in V-01/02/03/04 |
| **C-35** Cross-Role Discrepancy Check | FAIL | FAIL | FAIL | FAIL | PASS | Requires 5-role Inspector architecture (only V-05); no Discrepancy Table in V-01/02/03/04 |
| **C-36** 2D Action Matrix (Round x Tier) | FAIL | FAIL | FAIL | FAIL | PASS | Requires Seeds K+V simultaneously (only V-05); V-02 has V not K; V-04 has K not V |

---

### Detailed C-35 Verification — Distinguishing from C-33

C-33 (Echo Detection) tests **logical** coexistence constraints — impossibility rules between flag categories and achievement names that are structurally derivable without reference to Health Phase data (e.g., `healthy-momentum` + `Solo Pioneer` is logically impossible by definition). C-35 tests **empirical** consistency — a downstream role (Inspector) compares flag assignments against actual Health Phase evidence rows to catch flags that are logically permissible but data-incorrect (e.g., `stuck-at-first` was flagged but Health Phase §2.2 shows Signal Depth EARNED).

- **V-03** (4-role with Reconciler): The Reconciler performs pre-synthesis cross-dimensional reconciliation (Seed B) — this satisfies the pairing requirement at synthesis time, not the empirical flag-vs-data comparison at evaluation time. FAIL C-35.
- **V-04** (4-role with tiered actions): No Inspector equivalent. Seed W (coalition mapping) and Seed AB (regression risk) are forward-looking analyses, not backward flag-validity checks. FAIL C-35.
- **V-05** (5-role): Inspector role explicitly compares Assessor's inertia output against Health Phase evidence; produces Discrepancy Table; Strategist Pre-Write Check excludes discrepancy-retracted flags. PASS C-35.

### Detailed C-36 Verification — K-only and V-only partial cases

C-36 requires BOTH the temporal dimension (Round 1/2/3 = gap distance) AND the severity dimension (CRITICAL/WARNING/ADVANCING = inertia tier) simultaneously per action row.

- **V-02**: Carries Seed V (Round 1/2/3 multi-round sequencing) without Seed K. Action rows have round labels but no tier labels. Single axis. FAIL C-36.
- **V-04**: Carries Seed K ([CRITICAL]/[WARNING]/[ADVANCING] tier labels) without Seed V. Action rows have tier labels but no round labels. Single axis. FAIL C-36.
- **V-05**: Carries both K and V. Strategist §4.3 outputs actions indexed by Round × Tier simultaneously — "Round 1 | CRITICAL: {action}", "Round 2 | WARNING: {action}". Both axes defined. PASS C-36.

---

### Final Scores

| Variation | Essential | Aspirational | Formula | Score |
|-----------|-----------|--------------|---------|-------|
| V-01 | 5/5 | 25/28 | 90 + (25/28)×10 | **98.93** |
| V-02 | 5/5 | 25/28 | 90 + (25/28)×10 | **98.93** |
| V-03 | 5/5 | 25/28 | 90 + (25/28)×10 | **98.93** |
| V-04 | 5/5 | 25/28 | 90 + (25/28)×10 | **98.93** |
| V-05 | 5/5 | 28/28 | 90 + (28/28)×10 | **100.00** |

**Rank**: V-05 holds the ceiling at 100.00. V-01/V-02/V-03/V-04 are tied at 98.93. The three new v13 criteria (C-34, C-35, C-36) all fail in V-01 through V-04. V-05 passes all three because it carries Seed X (C-34), 5-role Inspector architecture (C-35), and Seeds K+V simultaneously (C-36).

---

### Excellence Signals

**R16 introduces 5 new structural patterns absent from v13 criteria — candidates for v14:**

**1. Seed AA — Namespace Gap Debt Column** (V-01, V-05)
`gap_debt = 9 − distinct_contributor_namespaces` added to contributor leaderboard. Changes interpretation: a top-ranked contributor with `gap_debt=7` signals concentration risk that raw signal count conceals. No current criterion tests per-contributor namespace breadth deficit. **Candidate: C-37**.

**2. Seed Z — Achievement Co-Occurrence Matrix** (V-02, V-05)
5×5 symmetric count table showing how often each achievement pair co-occurs on the same topic (diagonal = solo earns). Reveals structural coupling patterns — if `First Signal + Solo Pioneer` always co-occur, the team predominantly makes solo starts. No current criterion tests achievement-pair coupling. **Candidate: C-38**.

**3. Seed Y — Flag Lifecycle Annotation** (V-03, V-05)
Inertia flags tagged `new` / `persistent` / `resolved` against `simulations/.leaderboard-baseline.md`. `persistent` flags (resisted one cycle) receive priority over `new` flags in action writing. No current criterion tests lifecycle status relative to a prior-run baseline. **Candidate: C-39**.

**4. Seed AB — Milestone Regression Risk** (V-04, V-05)
Per-earned-milestone table: `milestone | earned | regression risk | at-risk contributor` — `stable` or `fragile: {contributor}`. Identifies earned milestones at fragility risk from contributor departure. No current criterion tests earned-milestone stability. **Candidate: C-40**.

**5. Seed AC — Contributor Onboarding Path** (V-05 only)
For every Solo Pioneer EARNED + Team Topic NOT YET topic: one-line onboarding prompt naming the topic, current sole contributor, and fastest namespace+signal-type to unlock Team Topic. Converts tension flag into concrete onboarding invite. No current criterion tests per-tension actionable onboarding path. **Candidate: C-41**.

---

### New Patterns (seeds for v14 criteria)

1. Namespace gap debt column — per-contributor `gap_debt = 9 − distinct_namespaces` in leaderboard; top-ranked contributor with high gap_debt signals breadth opportunity missed by signal count alone (Seed AA, V-01+V-05)
2. Achievement co-occurrence matrix — 5×5 symmetric count table revealing which achievement pairs always co-occur vs. appear independently, exposing structural team behavior patterns (Seed Z, V-02+V-05)
3. Flag lifecycle annotation — `new/persistent/resolved` per inertia flag relative to baseline file; `persistent` flags prioritized in action writing as they survived one full cycle (Seed Y, V-03+V-05)
4. Milestone regression risk table — per-earned milestone `stable/fragile: {contributor}` computed by single-contributor removal test (Seed AB, V-04+V-05)
5. Contributor onboarding path — per Solo Pioneer + Team Topic NOT YET: one-line prompt naming current sole contributor and fastest namespace unlock (Seed AC, V-05 only)

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["namespace gap debt column: per-contributor gap_debt = 9 minus distinct_namespaces added to leaderboard; top-ranked contributor with gap_debt=7 signals breadth concentration risk invisible to signal count alone (Seed AA, V-01+V-05)", "achievement co-occurrence matrix: 5x5 symmetric count table showing how often each achievement pair co-occurs on the same topic, diagonal = solo earns; reveals structural team behavior patterns such as persistent solo-start without follow-through (Seed Z, V-02+V-05)", "flag lifecycle annotation: each inertia flag tagged new/persistent/resolved against a leaderboard baseline file; persistent flags prioritized in action writing as they resisted one full cycle (Seed Y, V-03+V-05)", "milestone regression risk: per earned milestone a stable/fragile:{contributor} determination computed by single-contributor removal test, identifying earned milestones at risk from departure (Seed AB, V-04+V-05)", "contributor onboarding path: for every Solo Pioneer EARNED + Team Topic NOT YET topic, a one-line onboarding prompt naming current sole contributor and the fastest namespace+signal-type unlock for Team Topic (Seed AC, V-05 only)"]}
```
