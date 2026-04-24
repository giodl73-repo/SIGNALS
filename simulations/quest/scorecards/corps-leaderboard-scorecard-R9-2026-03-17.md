## Quest Score — corps-leaderboard Round 9

### Scoring Formula
`score = 90 + (aspirational_passed / 19) × 10`
Essential tier: C-01–C-05 (12 pts each, 60 pts base → 90 when all pass)
Aspirational tier: 19 criteria × ~0.526 pts each = 10 pts

---

## V-01 — MUST/SHALL Formal Spec

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Signal Registry Scan | PASS | Globs `simulations/**/*.md`; records topic_path, namespace, contributor, file; empty-workspace HALT with exact phrase |
| C-02 Per-Topic Achievement Evaluation | PASS | All five exact names present in template; every topic from Section 1 MUST appear; all five rows required per topic |
| C-03 All Three Team Milestones | PASS | Exact names: `first team signal`, `shared coverage`, `debate starter`; evidence non-empty required |
| C-04 Contributor Leaderboard | PASS | Descending by total signal count; ties alphabetical; `unknown` case handled with exact fallback row |
| C-05 Next Actions | PASS | At least 3 actions; each names namespace + topic path + exact achievement/milestone name |

All essential: **PASS**

### Aspirational Criteria (selected)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-22 Dual-Statement prevents-rule | PASS | "MUST be applied inside the action template below AND enforced in the pre-write check above. These are two structurally independent enforcement points." |
| C-23 Two-Level Nearest-Miss Cascade | PASS | Level 1 and Level 2 both defined; Level 2 conditioned on Level 1 empty via WHEN |
| C-24 prevents: Count Audit Gate | PASS | "you SHALL output exactly this line… `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`" |
| C-25 Synthesis Novelty Constraint | PASS | Skeptic gate present; explicit failure condition: "restates a visible achievement count or milestone status fails the gate"; cross-topic pattern required |
| C-26 Named Role-Sequence Architecture | FAIL | Sections only (SECTION 1–4). No named roles, no "does NOT" scope constraints, no handoff points |
| C-27 Health/Inertia Structural Separation | FAIL | Single-stream analysis. No health phase vs. inertia phase separation |

**Aspirational passed: 17/19**
**Score: 90 + (17/19) × 10 = 98.95**

---

## V-02 — Role Sequence: Archivist → Analyst → Publisher

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Signal Registry Scan | PASS | Archivist globs with four fields; empty-workspace gate halts all roles |
| C-02 Per-Topic Achievement Evaluation | PASS | Analyst evaluates all five exact-name achievements; every topic must appear; all five rows required |
| C-03 All Three Team Milestones | PASS | Exact names in §2.2; evidence non-empty |
| C-04 Contributor Leaderboard | PASS | Publisher ranks descending; ties alphabetical; unknown fallback |
| C-05 Next Actions | PASS | At least 3 actions; namespace + topic + exact achievement in Publisher §3.3 |

All essential: **PASS**

### Aspirational Criteria (selected)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-22 Dual-Statement prevents-rule | PASS | "stated here for the Pre-Write Check AND embedded in the action template" — two independent locations |
| C-23 Two-Level Nearest-Miss Cascade | PASS | Analyst §2.3: Level 1 and Level 2 both defined with conditional |
| C-24 prevents: Count Audit Gate | PASS | "output exactly this line (substitute N with the actual count…) `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`" |
| C-25 Synthesis Novelty Constraint | PASS | Publisher §3.2: "Analyst's output is now public knowledge"; "insight that restates a tally or status already visible in sections 2.1–2.2 fails"; requires "(4) contains information the skeptic acknowledges as new" |
| C-26 Named Role-Sequence Architecture | PASS | Three named roles (Archivist, Analyst, Publisher); each has explicit "does NOT" constraints; two handoff points with named artifact sets ("full registry and contributor index are handed to the Analyst"; "achievement tables, milestone table, and nearest-miss assessment are handed to the Publisher") |
| C-27 Health/Inertia Structural Separation | FAIL | No health vs. inertia phase separation. Archivist does scan + contributor index; Analyst does evaluation — no named trajectory phase |

**Aspirational passed: 18/19**
**Score: 90 + (18/19) × 10 = 99.47**

---

## V-03 — Output Format: Gate-Driven Checklist

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Signal Registry Scan | PASS | Globs with four fields; empty-workspace halt; Phase 1 Gate confirms |
| C-02 Per-Topic Achievement Evaluation | PASS | All five exact names; Phase 2 Gate requires "All five achievement names appear verbatim per topic" |
| C-03 All Three Team Milestones | PASS | Exact names; Phase 2 Gate requires "All three milestone names appear verbatim" |
| C-04 Contributor Leaderboard | PASS | Phase 3: descending, ties alphabetical, unknown fallback |
| C-05 Next Actions | PASS | Phase 4: at least 3 actions; namespace + topic + exact achievement |

All essential: **PASS**

### Aspirational Criteria (selected)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-22 Dual-Statement prevents-rule | PASS | "applies at two structurally independent points: (1) here in the Pre-Write Check… (2) inside each action row" |
| C-23 Two-Level Nearest-Miss Cascade | PASS | Level 1 and Level 2 both defined; Level 2 conditional |
| C-24 prevents: Count Audit Gate | PASS | Phase 4 Gate checklist: "[ ] ACTIONS GATE line written with actual N count substituted"; also `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` as required output line |
| C-25 Synthesis Novelty Constraint | PASS | Phase 3 Gate: "[ ] Team Insight passes the Skeptic gate (contains a cross-topic inference not derivable from any single Phase 2 block)" — checklist item enforces novelty structurally |
| C-26 Named Role-Sequence Architecture | FAIL | Phases only (1–4). No named roles with scope constraints or handoff points |
| C-27 Health/Inertia Structural Separation | FAIL | No health vs. inertia separation |

**Aspirational passed: 17/19**
**Score: 90 + (17/19) × 10 = 98.95**

---

## V-04 — Lifecycle (Milestones-First) + Decision-Table Pre-Write

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Signal Registry Scan | PASS | Phase 1 registry with four fields; empty-workspace halt |
| C-02 Per-Topic Achievement Evaluation | PASS | Phase 3: all five exact names; every registry topic must appear; five-row block required |
| C-03 All Three Team Milestones | PASS | Phase 2a: exact names; evidence non-empty |
| C-04 Contributor Leaderboard | PASS | Phase 2b: descending, ties alphabetical, unknown fallback |
| C-05 Next Actions | PASS | Phase 4c: at least 3 actions; namespace + topic + exact achievement |

All essential: **PASS**

### Aspirational Criteria (selected)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-22 Dual-Statement prevents-rule | PASS | "stated here inside the pre-write table AND must be applied to each relevant action row below" |
| C-23 Two-Level Nearest-Miss Cascade | PASS | Level 1 and Level 2 both defined; Level 2 conditional on Level 1 empty |
| C-24 prevents: Count Audit Gate | PASS | `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` required output; N must match Y rows in decision table |
| C-25 Synthesis Novelty Constraint | PASS | Phase 2c Skeptic gate: "a reader who has just seen the milestone table (2a) and leaderboard (2b) already knows… The Team Insight must contain something that reader would not already know from 2a and 2b alone" |
| C-26 Named Role-Sequence Architecture | FAIL | No named roles |
| C-27 Health/Inertia Structural Separation | FAIL | No health/inertia separation |

**Aspirational passed: 17/19**
**Score: 90 + (17/19) × 10 = 98.95**

---

## V-05 — Inertia Framing: Health / Inertia Structural Separation + Archivist / Skeptic Roles

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Signal Registry Scan | PASS | Pass 1 §1.1 globs with four fields; empty-workspace halt |
| C-02 Per-Topic Achievement Evaluation | PASS | Health Phase §1.2: all five exact names; per-topic block with five rows |
| C-03 All Three Team Milestones | PASS | Exact names in §1.2 milestone table; evidence non-empty |
| C-04 Contributor Leaderboard | PASS | Pass 2 §2.1: descending, ties alphabetical, unknown fallback |
| C-05 Next Actions | PASS | Pass 3 §3.2: at least 3 actions; namespace + topic + exact achievement |

All essential: **PASS**

### Aspirational Criteria (selected)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-22 Dual-Statement prevents-rule | PASS | "stated here for the Pre-Write Check AND applied inside each relevant action row below" |
| C-23 Two-Level Nearest-Miss Cascade | PASS | Level 1 and Level 2 both defined; Level 2 conditional |
| C-24 prevents: Count Audit Gate | PASS | "output exactly this line (substitute N with the actual count of `prevents:`-prefixed actions): `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`" |
| C-25 Synthesis Novelty Constraint | PASS | Pass 2 §2.2: Skeptic "has read Pass 1 in full"; explicit failure conditions; insight must have "(4) contains information the Skeptic acknowledges as new given full knowledge of Pass 1" |
| C-26 Named Role-Sequence Architecture | FAIL | Archivist and Skeptic named but Skeptic is a gate function embedded in Pass 2, not a role with "does NOT" scope constraints or a named handoff. Archivist runs three sub-phases without explicit exclusion language ("does NOT"). Two-role minimum met but scope-boundary and handoff-point requirements of C-26 are not fully satisfied |
| C-27 Health/Inertia Structural Separation | PASS | §1.2 "Health Phase" explicitly named with prohibition: "This phase does NOT report trajectory or momentum — those belong to the Inertia Phase below." §1.3 "Inertia Phase" explicitly named: "structurally separate from 1.2 — the Health Phase reports what exists; the Inertia Phase reports direction of change." Both phases defined, both sequentially required |

**Aspirational passed: 18/19**
**Score: 90 + (18/19) × 10 = 99.47**

---

## Summary Scorecard

| Variation | C-24 | C-25 | C-26 | C-27 | Aspirational | Score |
|-----------|------|------|------|------|--------------|-------|
| V-01 MUST/SHALL | PASS | PASS | FAIL | FAIL | 17/19 | 98.95 |
| V-02 Role Sequence | PASS | PASS | PASS | FAIL | 18/19 | **99.47** |
| V-03 Checklist | PASS | PASS | FAIL | FAIL | 17/19 | 98.95 |
| V-04 Decision Table | PASS | PASS | FAIL | FAIL | 17/19 | 98.95 |
| V-05 Inertia Framing | PASS | PASS | FAIL | PASS | 18/19 | **99.47** |

**Top score: 99.47** (V-02 and V-05 co-ceiling)
**All essential pass: YES**

---

## Excellence Signals

**From V-02 (top, C-26 carrier):**
The handoff description enumerates the *artifacts* transferred at each role boundary, not just the handoff point. "The full registry and contributor index are handed to the Analyst. The Analyst begins with these artifacts — it does not re-scan." / "The achievement tables, milestone table, and nearest-miss assessment are handed to the Publisher. The Publisher begins with these artifacts — it does not re-evaluate." This creates **handoff artifact enumeration**: each boundary specifies what object set crosses it and explicitly prohibits the receiving role from regenerating it. C-26 requires the handoff point; this pattern adds the transferred object set as an auditable contract.

**From V-05 (top, C-27 carrier):**
The inertia phase defines a closed 4-flag taxonomy (`stuck-at-first`, `solo-hold`, `namespace-thin`, `healthy-momentum`) with exact conditions, replacing free-form trajectory prose with a per-topic classification table (`topic_path | flags | trajectory note`). The taxonomy is closed — a topic with no flags must emit `flags = none`. This is **named inertia flag taxonomy**: the inertia phase not only separates from health structurally (C-27) but constrains the output to a defined finite vocabulary of states, making inertia assessments comparable across topics and auditable.

---

```json
{"top_score": 99.47, "all_essential_pass": true, "new_patterns": ["Handoff artifact enumeration — V-02 specifies the exact artifact set transferred at each role boundary (registry+contributor-index to Analyst; achievement tables+milestone table+nearest-miss to Publisher) and prohibits the receiving role from regenerating it, creating an auditable handoff contract beyond C-26's handoff-point requirement", "Named inertia flag taxonomy — V-05 defines a closed 4-flag set (stuck-at-first, solo-hold, namespace-thin, healthy-momentum) with exact conditions and requires per-topic classification against that taxonomy, constraining the inertia phase output to a finite comparable vocabulary beyond C-27's structural separation requirement"]}
```
