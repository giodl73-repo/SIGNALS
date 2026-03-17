## crew-roles Scorecard — Round 3

**Rubric**: v3 | **Variations**: V-01 through V-05 | **Date**: 2026-03-17

---

### Scoring Key

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60 pts (12 each) | C-01–C-05 |
| Recommended | 30 pts (10 each) | C-06–C-08 |
| Aspirational | 10 pts (1.25 each) | C-09–C-16 |

PASS = 1.0 · PARTIAL = 0.5 · FAIL = 0.0

---

### Per-Criterion Evidence

#### Essential — C-01 through C-05

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All 5 fields | PASS | PASS | PASS | PASS | PASS |
| C-02 Inertia-advocate present | PASS | PASS | PASS | PASS | PASS |
| C-03 Correct output path | PASS | PASS | PASS | PASS | PASS |
| C-04 Domain specificity | PASS | PASS | PASS | PASS | PASS |
| C-05 Minimum 3 roles | PASS | PASS | PASS | PASS | PASS |

All variations pass all 5 essential criteria. Evidence:

- **C-01**: Every variation's role template includes `orientation` (frame, serves), `lens` (verify, simplify), `expertise` (depth, relevance), `scope`, `collaborates_with`, and a named heading.
- **C-02**: All variations explicitly include the inertia-advocate with `orientation.frame` naming the current system, and verify questions referencing Q1/Q2/Q3 dimensions.
- **C-03**: All write to `.craft/roles/{area}/` — stated in the opening instructions.
- **C-04**: All link `expertise.relevance` to domain-specific vocabulary from Phase 1 (or domain analysis in V-03). V-03 adds "no generic engineering language" as an explicit constraint.
- **C-05**: PM + Architect + inertia-advocate = 3 minimum, all variations explicit about this floor.

---

#### Recommended — C-06 through C-08

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Lens actionability | PASS | PASS | PASS | PASS | PASS |
| C-07 Collaborates_with resolves | PASS | PASS | PASS | PASS | PASS |
| C-08 Perspective diversity | PASS | PASS | PASS | PASS | PASS |

All variations pass all 3 recommended criteria. Evidence:

- **C-06**: Every template shows `verify: {question ending in ?}` and `simplify: {Imperative verb phrase}` with examples (Remove / Defer / Collapse / Merge).
- **C-07**: V-01 and V-05 have a dedicated CHECK 2 (Orphan Reference Resolution) in a blocking gate. V-02 Phase 4, V-03 Step 4, V-04 Phase 5 CHECK 2 all contain orphan checks with explicit fix instructions. All resolve at delivery.
- **C-08**: All variations produce PM (product), Architect (technical), inertia-advocate (inertia), and at least one domain specialist (domain) → ≥ 3 perspective categories.

---

#### Aspirational — C-09 through C-16

**C-09 — Scope gradient**

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | PASS | CHECK 3 in VERIFICATION GATE enforces post-write: if all same, identify and revise 1–2 roles; re-list values before PASS declaration |
| V-02 | PASS | Phase 4 scope gradient check says "revise 1–2 roles" if all identical — instruction has a correction action attached; output will be diverse |
| V-03 | PASS | SCOPE AUDIT gate in Step 2 blocks writing until ≥ 2 distinct values confirmed — enforced pre-write |
| V-04 | PASS | Phase 3 SCOPE AUDIT (pre-write) + Phase 5 CHECK 3 confirmation (post-write) — dual enforcement |
| V-05 | PASS | Phase 3 SCOPE AUDIT exit-gated; Phase 5 CHECK 3 re-confirms — both explicit, blocking |

**C-10 — Inertia domain-grounded**

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Phase 2 produces Q1 (current system), Q2 (migration cost), Q3 (user habit); inertia-advocate frame names Q1 verbatim; verify references Q1/Q2/Q3 dimensions |
| V-02 | PASS | Phase 2 with `[vocab]` annotation surfaces specific named entities; inertia-advocate verify maps Q1/Q2/Q3 vocab terms per-question |
| V-03 | PARTIAL | Step 1 domain analysis captures "current system or approach" but it's a general analysis, not a structured Q1/Q2/Q3 pre-characterization; inertia constraints reference it but without the three-dimension structure |
| V-04 | PASS | Phase 2 Q1/Q2/Q3; inertia-advocate verify 3 questions each referencing a Q1/Q2/Q3 dimension |
| V-05 | PASS | Phase 2 Q1/Q2/Q3 with `[vocab]` exit condition; Phase 4 inertia frame is a fill-in template: "Challenge every proposal with evidence that [Q1 current system] remains sufficient given [Q2 migration cost]" — Q1+Q2 integrated structurally |

**C-11 — Vocabulary-forced-field**

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Phase 1 produces formal vocabulary list; Phase 3 template requires `expertise.relevance` to reference a Phase 1 term; CHECK 4 in VERIFICATION GATE verifies and fixes any that don't |
| V-02 | PASS | Phase 1 formal vocabulary list; Phase 3 template requires Phase 1 term in `relevance`; Phase 4 doesn't gate it but the inline instruction + inertia-advocate constraints both enforce it |
| V-03 | PARTIAL | Step 1 identifies "key systems, tools, or patterns" but produces no formal named vocabulary list; template says "specific to this domain — no generic engineering language" but doesn't require a Step 1 vocabulary term specifically |
| V-04 | PARTIAL | Phase 1 formal vocabulary list; Phase 4 template requires Phase 1 term; but Phase 5 only has 3 checks (table, orphan, scope) — no vocabulary coverage check in gate; instructed but not gated |
| V-05 | PASS | Phase 1 formal vocabulary list; Phase 4 template requires Phase 1 term; Phase 4 exit condition explicitly: "every `expertise.relevance` references a Phase 1 vocabulary term"; Phase 5 CHECK 4 gates it |

**C-12 — Inertia pre-characterization**

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Phase 2 answers Q1 (current system name), Q2 (migration cost), Q3 (user habit); inertia-advocate verify must reference "at least 2 of Q1/Q2/Q3 dimensions by name" |
| V-02 | PASS | Phase 2 with structured Q1/Q2/Q3; inertia-advocate verify 3 questions each mapped to Q1/Q2/Q3 vocab terms individually |
| V-03 | PARTIAL | No structured Phase 2; Step 1 analysis covers "current system" but not migration costs or user habits as discrete named answers; inertia constraints say "2 questions reference current-system name, migration cost, or user habit" but without a structured pre-characterization |
| V-04 | PASS | Phase 2 Q1/Q2/Q3 structured; inertia-advocate verify 3 questions covering Q1/Q2/Q3 dimensions |
| V-05 | PASS | Phase 2 exit condition requires all 3 answers; Phase 4 inertia verify has per-question vocabulary term distribution (Q1 term → Question 1, Q2 term → Question 2, Q3 term → Question 3) |

**C-13 — Registry summary table**

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | PASS | CHECK 1 in VERIFICATION GATE writes `Role | Frame | Scope | Collaborates With` table; explicit PASS declaration required |
| V-02 | PASS | Phase 4 table written before checks |
| V-03 | PASS | Step 4 table written before orphan check |
| V-04 | PASS | Phase 5 CHECK 1 writes table with PASS declaration |
| V-05 | PASS | Phase 5 CHECK 1 writes table; "Role column must match file stems exactly"; PASS declaration required |

**C-14 — Scope-gradient-enforcement**

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | PASS | CHECK 3 in blocking gate: if all same → identify 1–2, revise scope field, state change, re-list values to confirm ≥ 2 → structural gate, not soft instruction |
| V-02 | PARTIAL | Phase 4 scope check says "revise 1–2 roles to reflect their actual organizational reach" — correction action present, but buried in a bullet point alongside orphan check; no explicit PASS declaration or blocking language; "note the gap" phrasing is softer than a structural gate |
| V-03 | PASS | SCOPE AUDIT gate in Step 2 fires pre-write: "Do not write any role file until the table contains at least 2 distinct scope values"; `SCOPE AUDIT PASS` required before proceeding — pre-write structural gate |
| V-04 | PASS | Phase 3 SCOPE AUDIT fires pre-write with explicit `SCOPE AUDIT PASS` required; Phase 5 CHECK 3 confirms post-write; dual enforcement |
| V-05 | PASS | Phase 3 SCOPE AUDIT exit-gated (Entry/Exit structure); Phase 5 CHECK 3 PASS declaration required; pre-write prevention + post-write confirmation |

**C-15 — Verification-gate-phase**

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Phase 4 named "VERIFICATION GATE"; "DELIVERY IS BLOCKED" declared at top; 4 checks with per-check `CHECK N: PASS` or `CHECK N: FAIL — [issue]` declarations; gate lifts only when all 4 declare PASS |
| V-02 | FAIL | Phase 4 named "Registry Summary and Self-Check" — not a verification gate; checks listed as bullets without per-check PASS/FAIL declarations; no blocking language; orphan and scope checks can fail independently without any gate mechanism |
| V-03 | PARTIAL | Post-write Step 4 has table + orphan check but no blocking language or PASS declarations; scope-gradient check is pre-write (Step 2), not in Step 4 — so the three post-write checks are not all bundled; Step 4 is an ungated check, not a named blocking gate |
| V-04 | PASS | Phase 5 named "VERIFICATION GATE"; "DELIVERY IS BLOCKED. All 3 checks must declare PASS before output is delivered"; 3 checks (table, orphan, scope) with per-check declarations; gate clears when all 3 pass |
| V-05 | PASS | Phase 5 named "VERIFICATION GATE"; "DELIVERY IS BLOCKED. Complete all 4 checks in order. Each must declare PASS before the next opens. Fix defects found in earlier checks before proceeding to later ones."; 4 checks (table, orphan, scope, vocabulary) with per-check declarations |

**C-16 — Vocabulary-linked inertia Q&A**

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | Phase 2 Q1/Q2/Q3 answers have no `[vocab]` annotation requirement; Q1 format is `Current system: [named entity]` — no linkage to Phase 1 vocabulary; Q3 has no vocabulary reference |
| V-02 | PASS | Required format per question: `[answer] [vocab: {term-from-Phase-1}]`; "An answer without a `[vocab]` annotation fails this phase"; all 3 answers must carry the annotation; C-11 and C-12 structurally wired |
| V-03 | FAIL | No Phase 2 Q1/Q2/Q3 phase at all; no possibility of `[vocab]` annotations |
| V-04 | PARTIAL | Q2 explicitly says "Reference a vocabulary term"; Q1 has `[named entity]` and Q3 has `[named workflow or behavior]` — no vocabulary requirement; only one of three answers is vocabulary-linked |
| V-05 | PASS | Phase 2 exit condition: "all 3 answers written; each contains a `[vocab: {term}]` annotation referencing a Phase 1 term; no answer is missing its annotation"; per-question format enforced; phase fails and rewrites required before Phase 3 |

---

### Composite Scores

**V-01**

| Tier | Pass | Partial | Fail | Pts |
|------|------|---------|------|-----|
| Essential (5) | 5 | 0 | 0 | 60.00 |
| Recommended (3) | 3 | 0 | 0 | 30.00 |
| Aspirational (8) | 7 | 0 | 1 (C-16) | 8.75 |
| **Total** | | | | **98.75** |

**V-02**

| Tier | Pass | Partial | Fail | Pts |
|------|------|---------|------|-----|
| Essential (5) | 5 | 0 | 0 | 60.00 |
| Recommended (3) | 3 | 0 | 0 | 30.00 |
| Aspirational (8) | 6 | 1 (C-14) | 1 (C-15) | 8.125 |
| **Total** | | | | **98.125** |

**V-03**

| Tier | Pass | Partial | Fail | Pts |
|------|------|---------|------|-----|
| Essential (5) | 5 | 0 | 0 | 60.00 |
| Recommended (3) | 3 | 0 | 0 | 30.00 |
| Aspirational (8) | 3 | 4 (C-10, C-11, C-12, C-15) | 1 (C-16) | 6.25 |
| **Total** | | | | **96.25** |

**V-04**

| Tier | Pass | Partial | Fail | Pts |
|------|------|---------|------|-----|
| Essential (5) | 5 | 0 | 0 | 60.00 |
| Recommended (3) | 3 | 0 | 0 | 30.00 |
| Aspirational (8) | 6 | 2 (C-11, C-16) | 0 | 8.75 |
| **Total** | | | | **98.75** |

**V-05**

| Tier | Pass | Partial | Fail | Pts |
|------|------|---------|------|-----|
| Essential (5) | 5 | 0 | 0 | 60.00 |
| Recommended (3) | 3 | 0 | 0 | 30.00 |
| Aspirational (8) | 8 | 0 | 0 | 10.00 |
| **Total** | | | | **100** |

---

### Rankings

| Rank | Variation | Score | Gap |
|------|-----------|-------|-----|
| 1 | V-05 | 100.00 | — |
| 2 (tie) | V-01 | 98.75 | −1.25 |
| 2 (tie) | V-04 | 98.75 | −1.25 |
| 4 | V-02 | 98.125 | −1.875 |
| 5 | V-03 | 96.25 | −3.75 |

---

### Excellence Signals from V-05

**1. Phase-boundary exit conditions**

V-05 is the only variation to give each phase an explicit `Entry:` and `Exit:` condition. This creates a sequential dependency contract: Phase 2 cannot start until Phase 1's exit condition is met; Phase 3 cannot start until Phase 2's exit condition is met. The exit conditions are quantified ("3 answers written; each contains a `[vocab: {term}]` annotation") rather than implied. This prevents the inter-phase leakage where Phase 1 vocabulary extraction "succeeds" but Phase 2 proceeds without ever touching it. None of the other variations structure execution this way.

**2. Inertia frame as fill-in sentence template**

V-05 gives the inertia-advocate's `orientation.frame` as a fill-in pattern: `"Challenge every proposal with evidence that [current system from Q1] remains sufficient given [migration cost from Q2]."` This is structurally different from "must name the current system from Q1" — it forces Q1 and Q2 to appear in the same sentence in a fixed relation. V-01 through V-04 say "must name" or "must reference," which allows satisfying each constraint independently with separate sentences. The sentence template approach makes the Q1+Q2 integration non-negotiable at generation time.

**3. Layered constraint enforcement at three distinct execution points**

V-05 implements vocabulary linkage at three non-redundant points:
- Phase 1: extraction (vocabulary is produced)
- Phase 2: `[vocab: {term}]` annotation (linkage declared at answer-generation time)
- Phase 4 exit condition: "every `expertise.relevance` references a Phase 1 term" (linkage required at role-write time)
- Phase 5 CHECK 4: vocabulary coverage audit (linkage verified at delivery time)

V-01 enforces at Phase 1 + Phase 3 template + Phase 4 CHECK 4. V-04 enforces at Phase 1 + Phase 4 template only. V-05's four-layer depth means each layer catches a different class of failure: annotation catches Q&A drift, exit conditions catch role-write drift, CHECK 4 catches residual cases under model drift. No single layer is sufficient alone; the combination makes silent failure impractical.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-boundary exit conditions per phase prevent inter-phase leakage that per-instruction constraints cannot catch", "inertia frame as fill-in sentence template forces multi-field integration at generation time rather than per-field compliance"]}
```
