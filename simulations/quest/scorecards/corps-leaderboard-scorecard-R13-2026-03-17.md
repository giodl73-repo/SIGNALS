## R13 Scorecard — corps-leaderboard (v11 rubric)

---

### Essential Criteria — All Variations (C-01 through C-05)

All five R13 variations are evaluated against the same baseline. Each variation carries the complete Archivist role with full registry scan, all five achievement evaluations (exact names), all three team milestones (exact names), contributor leaderboard, and at least 3 namespace-specific next actions.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Signal Registry Scan | PASS | PASS | PASS | PASS | PASS |
| C-02 Per-Topic Achievement (Exact Names) | PASS | PASS | PASS | PASS | PASS |
| C-03 All Three Milestones (Exact Names) | PASS | PASS | PASS | PASS | PASS |
| C-04 Contributor Leaderboard | PASS | PASS | PASS | PASS | PASS |
| C-05 Next Actions (Namespace + Achievement) | PASS | PASS | PASS | PASS | PASS |

**Essential: 5/5 all variations.**

---

### Aspirational Criteria — Detailed Evaluation

#### C-06 through C-21 (preserved criterion text)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-06 Namespace Diversity Metric | PASS | PASS | PASS | PASS | PASS | All: `Namespace diversity: {N}/9` per topic + coverage line |
| C-07 Momentum Indicator | PASS | PASS | PASS | PASS | PASS | All: velocity summary with `Trend: increasing/flat/stalled` |
| C-08 Gap Prioritization by Achievement Distance | PASS | PASS | PASS | PASS | PASS | All: nearest-miss sorted ascending by gap |
| C-09 Contributor Collaboration Signal | PASS | PASS | PASS | PASS | PASS | All: collaboration map/signal section |
| C-10 Empty Namespace Explicit Listing | PASS | PASS | PASS | PASS | PASS | All: `Empty: {list}` in coverage line |
| C-11 Topic Health Summary Line | PASS | PASS | PASS | PASS | PASS | All: `Health — Files: {N} \| Namespaces: ... \| Namespace diversity: {N}/9` |
| C-12 Locked Achievement with Specific Unlock Path | PASS | PASS | PASS | PASS | PASS | All: "LOCKED rows include specific unlock paths" enforced |
| C-13 Team Insight Cross-Topic Synthesis | PASS | PASS | PASS | PASS | PASS | All: one sentence with cross-topic conclusion + number + name |
| C-14 Solo Pioneer Tension Detection | PASS | PASS | PASS | PASS | PASS | All: `[TENSION: solo hold — unlock requires 1 additional contributor...]` |
| C-15 Namespace Leader Callout | PASS | PASS | PASS | PASS | PASS | All: namespace leader table per active namespace |
| C-16 Stale Signal Detection | PASS | PASS | PASS | PASS | PASS | All: stale signal table (`stale`/`active`/`date-unknown`) |
| C-17 Signal Velocity Trend | PASS | PASS | PASS | PASS | PASS | All: velocity summary with `{N_signals}/{N_topics}` + Trend |
| C-18 Debate Starter Threshold Proximity | PASS | PASS | PASS | PASS | PASS | All: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)` |
| C-19 Multi-Phase Execution Order | PASS | PASS | PASS | PASS | PASS | All: explicit multi-role/multi-phase sequential architecture |
| C-20 Prevents: Prefix Rule Statement | PASS | PASS | PASS | PASS | PASS | All: stated in Pre-Write Check section |
| C-21 Nearest-Miss Achievement Gap | PASS | PASS | PASS | PASS | PASS | All: Level 1 (1-away) and Level 2 (2-away when no Level 1) |

---

#### C-22 — Dual-Statement Prevents-Rule Redundancy

**Evidence pattern (all variations):** `prevents:` stated as "first of two structurally independent enforcement points" in Pre-Write Check section, and "second structurally independent enforcement point" embedded in the action row template. The two locations are in distinct labeled blocks (Pre-Write Check vs. action format definition). Both statements are syntactically complete independently.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS (§3.6 + §3.7) | PASS (§4.2 + §4.3) | PASS (§3.6 + §3.7) | PASS (§3.2 + §3.3) | PASS (§4.2 + §4.3) |

---

#### C-23 — Two-Level Nearest-Miss Cascade

**Evidence:** All variations define Level 1 (exactly 1 unit away) and Level 2 (closest to 2 units away, emitted ONLY when no Level 1 exists, with explicit "Level 1: no topics are 1 unit away" prefix). All: PASS.

---

#### C-24 — Gate-Level Prevents: Prefix Count Self-Audit

**Evidence:** All variations include exactly `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` after the action-writing phase closes. `{N}` is a substitutable count, not a yes/no. All: PASS.

---

#### C-25 — Synthesis Novelty Constraint

All variations include an explicit Skeptic gate requiring the insight to contain something the Skeptic would not already know, with operational failure conditions ("an insight that restates... fails"). All: PASS.

---

#### C-26 — Named Role-Sequence Architecture

| Variation | Roles | Scope Exclusions | Handoff Points |
|-----------|-------|-----------------|----------------|
| V-01 | Archivist → Analyst → Publisher | Each role lists explicit "does NOT" constraints | Gate + Handoff before each role transition |
| V-02 | Archivist → Assessor → Inspector → Strategist → Narrator | Assessor: "does NOT evaluate achievements"; Inspector: "does NOT restate inertia flags" | 4 named handoffs |
| V-03 | Archivist → Analyst → Publisher | Same pattern | 2 handoffs |
| V-04 | Archivist → Analyst → Strategist → Narrator | Same pattern | 3 handoffs |
| V-05 | Archivist → Assessor → Inspector → Strategist → Narrator | Full scope exclusion per role | 4 named handoffs |

All: PASS.

---

#### C-27 — Health / Inertia Structural Separation

| Variation | Structure | Separation Evidence |
|-----------|-----------|---------------------|
| V-01 | §2.1 Inertia Phase (RUNS FIRST) / §2.2 Health Phase (RUNS SECOND) | "Inertia Phase content must not appear in the Health Phase and vice versa" |
| V-02 | Role 2: Assessor (trajectory only) / Role 3: Inspector (current state only) | Dedicated single-purpose roles enforcing separation at architecture level |
| V-03 | §2.1 Health Phase / §2.2 Inertia Phase | "Does NOT report trajectory, momentum, or stall indicators" / "Does NOT restate file counts..." |
| V-04 | §2.1 Inertia Phase (RUNS FIRST) / §2.2 Health Phase (RUNS SECOND) | Same as V-01 |
| V-05 | Assessor role (trajectory) / Inspector role (health) | Same as V-02 + severity-ordered topic reporting driven by Assessor output |

All: PASS.

---

#### C-28 — Named Artifact Set at Role Handoff

All variations enumerate specific artifacts (named tables, columns, data structures) at each handoff boundary. Evidence sample:

- **V-01 Analyst Handoff**: Lists 6 artifacts by name — Inertia Phase table (columns named), Stale signal table, per-topic Health Phase achievement blocks, Team milestone table, Debate starter proximity + namespace leader, Nearest-miss table.
- **V-02**: 4 inter-role handoffs, each enumerating specific artifacts with column names.

A handoff phrased generically as "passes results" would fail; all R13 handoffs enumerate specific documents. All: PASS.

---

#### C-29 — Per-Phase Completion Checklist Gate

| Variation | Phase Gates | Items per Gate |
|-----------|-------------|----------------|
| V-01 | §2.1 Gate (3 items), §2.2 Gate (7 items), Publisher Gate (8 items) | All ≥ 2 distinct items |
| V-02 | Assessor Gate (3), Inspector Gate (5), Strategist Gate (4), Narrator Gate (4) | All ≥ 2 |
| V-03 | Analyst Gate (5), Publisher Gate (8) | Both ≥ 2 |
| V-04 | §2.1 Gate (2), §2.2 Gate (4), Strategist Gate (5), Narrator Gate (4) | All ≥ 2 |
| V-05 | Assessor Gate (4), Inspector Gate (4), Strategist Gate (5), Narrator Gate (6) | All ≥ 2 |

At least two phase gates per variation, each with ≥ 2 distinct items. All: PASS.

---

#### C-30 — Contamination-Check Checklist Item at Health/Inertia Gate

C-30 requires at least one gate-level checklist item explicitly prohibiting cross-phase content (verifying *absence* of contamination, not just *presence* of output).

| Variation | Gate Contamination Item(s) |
|-----------|---------------------------|
| V-01 | §2.1 Gate: `[ ] No static file counts, achievement statuses, or coverage totals in Inertia Phase content`; §2.2 Gate: `[ ] No trajectory language, momentum claims, or inertia flag restatements in Health Phase` |
| V-02 | Assessor Gate: `[ ] Inertia table present; ... no file counts or achievement statuses in Assessor output (prohibited — current-state data)`; Inspector Gate: `[ ] No trajectory language or inertia flag restatements in any Health Phase content` |
| V-03 | Analyst Gate: `[ ] Inertia table conforms to stub pattern; no static counts from Health Phase restated` |
| V-04 | §2.1 Gate: `[ ] no file counts or achievement statuses (prohibited — current-state data)`; §2.2 Gate: `[ ] no trajectory language in Health Phase` |
| V-05 | Assessor Gate: `[ ] No static file counts, achievement statuses, or coverage totals in Assessor output`; Inspector Gate: `[ ] no trajectory language in Health Phase` |

All include gate-level prohibition items verifying absence of cross-phase content. All: PASS.

---

#### C-31 — Inertia-Aware Skeptic Knowledge Scope

C-31 requires the Skeptic's knowledge to explicitly name inertia flags/trajectory data, not just health-phase data.

| Variation | Skeptic Scope Evidence |
|-----------|----------------------|
| V-01 | "every inertia flag, every severity tier, every trajectory note, the stale signal table, the velocity summary" — named explicitly |
| V-02 | "every inertia flag, every trajectory note, the discrepancy table with retracted flags, the stale signal table, the velocity summary" |
| V-03 | "every inertia flag, every trajectory note, the stale signal table, the velocity summary" |
| V-04 | "every inertia flag, every severity tier, every trajectory note, the stale signal table, the velocity summary, the nearest-miss assessment, the tiered action list" |
| V-05 | "every inertia flag, every severity tier, every trajectory note, the discrepancy table, the stale signal table, the velocity summary" plus "confidence annotation" |

All: PASS. Every variation calls out inertia flags and trajectory notes by name in the Skeptic scope definition.

---

### Composite Scores

| Variation | Essential | Aspirational | Score |
|-----------|-----------|--------------|-------|
| V-01 | 5/5 | 23/23 | **100.00** |
| V-02 | 5/5 | 23/23 | **100.00** |
| V-03 | 5/5 | 23/23 | **100.00** |
| V-04 | 5/5 | 23/23 | **100.00** |
| V-05 | 5/5 | 23/23 | **100.00** |

**Universal ceiling: 100.00. The v11 rubric remains non-discriminating across R13.** All variations were designed to pass 23/23 and do so. The next ceiling-breaking opportunity is a variation that introduces patterns not yet captured in C-01 through C-31.

---

### Ranking

All variations tie at 100.00. By architectural richness (number of new seeds formalized):

1. **V-05** (Rank 1 by convention — full integration, 5-role + Seeds A+B+D+E+H+I+K+L)
2. **V-04** (4-role, Seeds A+B+D+H+K)
3. **V-02** (5-role, Seeds A+B+I)
4. **V-01** (3-role, Seeds A+B+H)
5. **V-03** (3-role, Seeds A+B+J)

---

### Excellence Signals from R13

All five variations formalize **Seed A** and **Seed B** as mandatory requirements, making them universal. The v12-C-32 and v12-C-33 candidates are now clear:

**Seed A (universal — 5/5 variations):** `resolves: {flag-name}` annotation on inertia-flag-resolving actions. Every action whose primary purpose is resolving an open inertia flag must declare the exact flag name in a `resolves:` field. Orthogonal to C-20 (which tests whether `prevents:` is stated) and C-24 (which tests the count audit) — `resolves:` creates an explicit action-to-trajectory linkage that the current rubric does not test.

**Seed B (universal — 5/5 variations):** Pre-synthesis cross-dimensional reconciliation pairing. Before the Team Insight, the Publisher/Narrator selects one Health observation and one Inertia observation that interact, states the interaction, and uses this pairing as a floor the insight must exceed. Orthogonal to C-13 (which tests insight form) and C-25 (which tests novelty) — this is a structural precursor that raises the novelty bar by making the reconciliation content known to the Skeptic.

**Seed K (V-04, V-05):** Tiered action output (`[CRITICAL]` / `[WARNING]` / `[ADVANCING]`) — actions grouped by the inertia severity tier of the target topic. Orthogonal to C-05 (which tests namespace+achievement naming) and C-20/C-22 (which test `prevents:` rules) — severity-tiered organization forces the model to classify actions by urgency dimension before writing them.

**Seed I (V-02, V-05):** Cross-role discrepancy validation table. After the Inspector completes the Health Phase, it explicitly compares Assessor inertia flags against Inspector health findings. Any flag whose precondition is contradicted by health data is formally retracted with an authoritative-source declaration. Orthogonal to all current rubric criteria — this tests whether the instruction builds an inter-role consistency check into the protocol.

**Seed L (V-05 only):** Insight projection test. After writing the Team Insight sentence, the Narrator emits a `projection: local` or `projection: forward` annotation explicitly bounding whether the second-order pattern applies only to current observed topics or extrapolates to topics not yet started. Orthogonal to C-25 (novelty) and C-31 (Skeptic scope) — this forces scope bounding on the insight's applicability, preventing vague cross-topic claims.

**Seed H (V-01, V-04, V-05):** Severity-ordered health topic reporting — Health Phase reports topics in descending inertia severity order (critical → warning → healthy, alphabetical within tier). Orthogonal to C-27 (which tests the existence of the split) — Seed H tests whether the inertia assessment drives the *ordering* of health output, not just its existence.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["resolves: {flag-name} annotation on inertia-flag-resolving actions — every action resolving an open inertia flag declares the exact flag name, creating an explicit action-to-trajectory linkage orthogonal to prevents: and count-audit criteria", "pre-synthesis cross-dimensional reconciliation pairing (one Health observation x one Inertia observation + interaction statement) required before Team Insight — pairing becomes known to Skeptic, raising novelty floor to second-order inference", "tiered action output ([CRITICAL]/[WARNING]/[ADVANCING]) grouping actions by inertia severity tier of target topic — urgency classification dimension orthogonal to namespace+achievement naming and prevents: rules", "cross-role discrepancy validation table with explicit flag retraction — Inspector compares Assessor inertia flags against health findings; contradicted flags retracted with authoritative-source declaration; retracted flags excluded from resolves: consideration downstream", "insight projection test (projection: local vs projection: forward) — after Team Insight sentence, Narrator emits a structured annotation bounding whether the second-order pattern applies to current topics only or extrapolates to topics not yet started"]}
```
