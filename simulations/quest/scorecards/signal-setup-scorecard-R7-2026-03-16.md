Now I have everything needed. Let me score all five variations.

---

# Quest Score: signal-setup — Round 7

**Rubric**: v7 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-21 aspirational; A denominator = 13)
**Date**: 2026-03-16
**Baseline**: V-05 R6 — predicted 100.0 against v6 rubric; C-21 PROBABLE PASS risk identified

---

## Criterion Evaluation — All Variations

### Essential (C-01–C-05) — Shared base; all variations identical here

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | File detection before write | PASS | PASS | PASS | PASS | PASS |
| C-02 | Preview shown before writing | PASS | PASS | PASS | PASS | PASS |
| C-03 | Confirmation required | PASS | PASS | PASS | PASS | PASS |
| C-04 | Signal section appended with skill advertising | PASS | PASS | PASS | PASS | PASS |
| C-05 | Idempotent re-run | PASS | PASS | PASS | PASS | PASS |

Evidence: GATE 0 reads and checks before any write; GATE 3 shows preview; GATE 4 requires explicit y/N; GATE 5 appends with Quick start + inertia rule; GATE 2 detects existing Signal section and halts all.

---

### Recommended (C-06–C-08) — Shared base; all variations identical here

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Inertia rule included | PASS | PASS | PASS | PASS | PASS |
| C-07 | Copilot instructions offered | PASS | PASS | PASS | PASS | PASS |
| C-08 | User feedback on outcome | PASS | PASS | PASS | PASS | PASS |

Evidence: GATE 3 preview contains explicit inertia rule ("the primary competitor is always inertia"); GATE 6 offers Copilot update; GATE 2/5/6/7 all produce explicit outcome messages.

---

### Aspirational (C-09–C-21)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Preview matches written output | PASS | PASS | PASS | PASS | PASS |
| C-10 | Handles missing CLAUDE.md gracefully | PASS | PASS | PASS | PASS | PASS |
| C-11 | Named gate checkpoints as explicit phase boundaries | PASS | PASS | PASS | PASS | PASS |
| C-12 | Edge-case paths promoted to first-class gates | PASS | PASS | PASS | PASS | PASS |
| C-13 | Skill opens with motivational preamble | PASS | PASS | PASS | PASS | PASS |
| C-14 | Decline path names its consequence | PASS | PASS | PASS | PASS | PASS |
| C-15 | Already-configured path affirms positive consequence | PASS | PASS | PASS | PASS | PASS |
| C-16 | Inertia named as adversary, not concept | PASS | PASS | PASS | PASS | PASS |
| C-17 | Preamble explains temporal persistence | PASS | PASS | PASS | PASS | PASS |
| C-18 | Decline path anchors to a future moment | PASS | PASS | PASS | PASS | PASS |
| C-19 | Key arguments threaded through all Signal-absent exits | PASS | PASS | PASS | PASS | PASS |
| C-20 | Already-configured gate names persistence mechanism | PASS | PASS | PASS | PASS | PASS |
| **C-21** | **Secondary optional gates: path-specific consequence anchors** | **PASS** | **PARTIAL** | **PASS** | **PASS** | **PASS** |

**C-21 evidence per variation:**

**V-01**: GATE 4 = "before the next build" (commit/planning); GATE 6 = "before Copilot writes the **first function body** for a new feature…implementing this." Phase separation: planning vs. implementation. "build" removed from GATE 6 vocabulary. No shared anchor. **PASS.**

**V-02**: GATE 4 = "before the next **build**"; GATE 6 = "before the next Copilot session reaches for a **build suggestion**." Both anchors use "build" as the semantic key. Distinction is tool-name only (Claude vs. Copilot), not phase. C-21 requires tools with distinct roles carry distinct consequence language; "build"/"build suggestion" does not achieve that. **PARTIAL** — tool-distinct but not phase-distinct. Counts as FAIL in formula (consistent with R7 doc's 99.2 risk case).

**V-03**: GATE 4 = "before the **spec is committed**…at the **planning stage**"; GATE 6 = "before Copilot starts **implementing the first endpoint**…instead of **shipping** this." Explicit phase labels. Vocabulary: spec/planning vs. implementing/endpoint/shipping. Zero shared anchor terms. **PASS.**

**V-04**: GATE 4 = "before the next build" (planning); GATE 6 = "before Copilot writes the **first function body**…implementing this." "function body" is an implementation-phase artifact; "build" is planning/commit vocabulary. No shared vocabulary in GATE 6. **PASS.**

**V-05**: GATE 4 = "before the spec is committed…at the **planning stage**"; GATE 6 = "before Copilot starts **implementing the first endpoint**…instead of **shipping** this." Explicit phase labels throughout; planning vocabulary (spec, committed) does not appear in GATE 6; implementation vocabulary (endpoint, implementing, shipping) does not appear in GATE 4. **PASS.**

---

## Score Computation

```
Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/13 * 10)
Golden:  all 5 essential PASS AND composite >= 80
```

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 5/5 = 60.0 | 3/3 = 30.0 | 13/13 = 10.00 | **100.0** | YES |
| V-02 | 5/5 = 60.0 | 3/3 = 30.0 | 12/13 = 9.23 | **99.2** | YES |
| V-03 | 5/5 = 60.0 | 3/3 = 30.0 | 13/13 = 10.00 | **100.0** | YES |
| V-04 | 5/5 = 60.0 | 3/3 = 30.0 | 13/13 = 10.00 | **100.0** | YES |
| V-05 | 5/5 = 60.0 | 3/3 = 30.0 | 13/13 = 10.00 | **100.0** | YES |

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tie) | V-01 | 100.0 | Minimum change: single-phrase swap at GATE 6 eliminates "build" vocabulary |
| 1 (tie) | V-03 | 100.0 | Structural clarity: all three decline exits carry explicit phase labels |
| 1 (tie) | V-04 | 100.0 | Phase-concrete anchor + GATE 6 already-configured affirm |
| 1 (tie) | V-05 | 100.0 | Maximum coverage: concrete anchor + affirm + explicit phase labels |
| 5 | V-02 | 99.2 | C-21 partial: GATE 6 decline unchanged; "build"/"build suggestion" shared vocabulary |

---

## Excellence Signals

Top variation: **V-05 (A+B+C)** — structural maximum; every gap closed.

**Signal 1: Implementation-phase artifact naming resolves tool-role ambiguity**
The word "build" is planning-phase vocabulary — it belongs to "should we build this?" GATE 6 protects Copilot's code-generation role (not the build decision). Replacing "build suggestion" with "first function body" or "implementing the first endpoint" roots the consequence in what Copilot actually *produces*. The anchor is no longer about a decision event; it's about a code-output event. This is the minimal, irreducible change that satisfies C-21.

**Signal 2: Lifecycle-ordered decline exits create a phase ladder**
V-05 distributes the three decline exits across the actual development lifecycle: GATE 1 (design) → GATE 4 (spec/planning) → GATE 6 (implementation). The user encounters each gate at the phase in their workflow where that tool would be active. This isn't just C-21 compliance — it means the consequence language is self-locating: the user reading GATE 6 knows they are past planning and about to write code, so the future moment named ("before Copilot starts implementing") is immediately legible as "now."

**Signal 3: Optional gate already-configured path with mechanism naming (structural C-20 parity)**
V-02, V-04, V-05 add an already-configured sub-path to GATE 6: when copilot-instructions.md already contains Signal, the response names *how* that configuration persists ("Copilot Chat loads workspace instructions at session start"). This mirrors exactly what GATE 2 does for CLAUDE.md (C-20). The pattern: every gate that detects an already-configured state should name the persistence mechanism, not merely confirm existence. Optional secondary gates are not exempt from this principle.

---

## Carry-Forward Recommendation

**R8 candidate: V-01** — score 100.0 with the minimum change. One-phrase swap ("first function body" replaces "before the next Copilot session reaches for a build suggestion"). Per the CLAUDE.md preference for minimum necessary complexity, if V-01 achieves the same score as V-05, V-01 ships.

**V-05 as fallback**: if a future criterion requires explicit phase labels at all decline exits or C-20 parity for secondary optional gates, V-05 is already correct. Consider it the hedge.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["implementation-phase artifact naming at optional decline gates: consequence anchors should name what the tool produces (function body, endpoint) not the planning decision (build), rooting the future moment in the tool's actual role", "lifecycle-ordered decline exit phases: distribute GATE 1/4/6 declines across design, planning, and implementation phases so each consequence is self-locating to the user's current workflow stage", "secondary optional gates carry mechanism-naming affirm paths: when an optional gate detects already-configured state, name the auto-load mechanism (parallel to C-20 for primary gate)"]}
```
