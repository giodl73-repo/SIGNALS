# Quest:Score — signal-setup Round 13 (Rubric v12)

## Scoring Basis

V-01 spec text is provided (truncated at GATE 4); GATE 5/5A/5B and GATE 6 inferred from the gate-structure declaration and base-behaviors list. V-02–V-05 are projected from their axis descriptions against the same base.

---

## Per-Variation Scoring

### V-01 — Axis A (Pure Letter-Slot Identifiers)

**Hypothesis under test**: Whether explicit letter-slot scheme annotation alone lifts the score over R12 base. Consequence anchors are intentionally left as v12-inadequate ("there is no X" style) to isolate the effect of Axis A.

#### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | GATE 1 reads CLAUDE.md before any write operation |
| C-02 | PASS | GATE 2 shows preview before GATE 3 confirmation |
| C-03 | PASS | GATE 3: "Add this Signal section to your CLAUDE.md? [y/N]" |
| C-04 | PASS | GATE 4 appends Signal section with 9 namespaces + inertia rule |
| C-05 | PASS | GATE 1B detects existing Signal section and stops |

Essential: **5/5 → 60.00 pts**

#### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | "### Inertia Rule" with full rule text in GATE 2 preview |
| C-07 | PASS | GATE 1B offers Copilot extension; GATE 5/5A/5B in gate structure (inferred) |
| C-08 | PASS | Final report: "Inertia now has a named opponent" (base behavior) |

Recommended: **3/3 → 30.00 pts**

#### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | GATE 4: "exactly as shown in GATE 2" |
| C-10 | PASS | GATE 1A creates new CLAUDE.md with Signal section |
| C-11 | PASS | Five named gate phases; no phase can be implicitly skipped |
| C-12 | PASS | GATE 1A and GATE 1B are `###`-headed sub-gates, not inline conditionals |
| C-13 | PASS | Preamble opens with inertia-as-force framing before any procedural content |
| C-14 | PASS | GATE 3 N: "Inertia remains unnamed in this workspace" — names what was forfeited |
| C-15 | PASS | GATE 1B: "Inertia already has a named opponent here" |
| C-16 | PASS | Preamble: "primary competitor"; GATE 1B: "named opponent" |
| C-17 | PASS | Preamble: "This configuration runs once. But it must persist: CLAUDE.md loads at the start of every session" — explicitly explains why the write endures |
| C-18 | **FAIL** | GATE 1A N and GATE 3 N both use "there is no inertia question in Claude's context" — absence statement, not outcome proposition; C-32 cascade → C-18 FAIL |
| C-19 | **FAIL** | C-18 fails; no valid future-moment anchor exists to thread across Signal-absent exits |
| C-20 | PASS | GATE 1B: "That is the mechanism: the load itself keeps the question present, not you remembering to ask" — names auto-load persistence explicitly |
| C-21 | **FAIL** | GATE 5B decline anchor uses same absence pattern (inferred from V-01 hypothesis); C-32 cascade → C-21 FAIL |
| C-22 | **FAIL** | Anchors have phase-appropriate vocabulary but fail C-32 completeness; C-32 cascade → C-22 FAIL |
| C-23 | PASS | "At the planning stage" is an explicit phase label in both decline anchors; C-32 cascade does not extend to C-23 |
| C-24 | PASS | GATE 5A affirms Copilot-local consequence (base behavior preserved) |
| C-25 | PASS | GATE 1A/1B encode parent 1 + position A/B; GATE 5A/5B encode parent 5 + position A/B — pure letter-slot |
| C-26 | PASS | GATE 5A and 5B are heading-delimited sub-gates (base behavior; gate structure declaration) |
| C-27 | PASS | All gate and sub-gate boundaries use `##`/`###` headings; no bold inline pseudo-gate labels visible |
| C-28 | PASS | GATE 1A/1B promoted to `###`-headed sub-gates; GATE 5 inline already-configured detection with annotation (base behavior) |
| C-29 | PASS | GATE 1 routing: "Three cases follow. If CLAUDE.md is not found, see GATE 1A. If CLAUDE.md is found and already contains a Signal section, see GATE 1B. If CLAUDE.md is found and has no Signal section, continue to GATE 2." — all three branches with (condition, destination gate ID) in single contiguous paragraph |
| C-30 | PASS | GATE 5 inline Copilot detection carries annotation (base behavior preserved per C-30) |
| C-31 | PASS | GATE 1A, 1B, 5A, 5B — pure letter-slot throughout; no word-suffix variants anywhere |
| C-32 | **FAIL** | GATE 1A N: "there is no inertia question in Claude's context" matches the rubric's explicit C-32 FAIL example exactly — states absence of a check, not the downstream consequence of that absence |

Aspirational: **19/26 → 7.31 pts**

**V-01 Composite: 97.31**

---

### V-02 — Axis B (Complete, Assertable Consequence Anchor Sentences)

**Changes from V-01**: Every decline and abort anchor is rewritten as a subject–predicate–outcome proposition. Letter-slot identifiers inherited from base (C-31 preserved). Example rewrite: "there is no inertia question in Claude's context" → "Inertia wins the default choice at the planning stage: the spec is committed without a named competitor, and the question never gets asked."

All C-01..C-31 criteria: identical to V-01 (all PASS). Changes:

| ID | V-01 | V-02 | Evidence |
|----|------|------|----------|
| C-32 | FAIL | **PASS** | Anchors are syntactically complete, extractable claims with stated outcomes |
| C-18 | FAIL | **PASS** | C-32 satisfied; anchor names specific future moment ("before the spec is committed") AND states outcome consequence |
| C-22 | FAIL | **PASS** | C-32 satisfied; planning-stage vocabulary (GATE 3) vs. implementation-stage vocabulary (GATE 5B) — non-overlapping, phase-native |
| C-21 | FAIL | **PASS** | C-32 satisfied; GATE 5B anchor uses Copilot/implementation-stage framing distinct from planning-stage framing |
| C-19 | FAIL | **PASS** | Valid future-moment anchor (C-18 now PASS) present at both Signal-absent exits (GATE 1A and GATE 3) |

Aspirational: **24/26 → 9.23 pts**

**V-02 Composite: 99.23**

---

### V-03 — Axis C (Contiguous Routing Blocks with Explicit Route: prefix)

**Changes from V-01**: Each parent gate body opens with an explicit `Route:` block listing every branch as `(condition → GATE NX)` pairs on separate lines. Consequence anchors are unchanged (absence-statement style).

C-29 in V-01 already passes (contiguous prose routing with all branch destinations named). V-03's `Route:` blocks are cleaner but don't change the pass/fail outcome for C-29. No other criterion is affected by Axis C.

| ID | V-01 | V-03 | Evidence |
|----|------|------|----------|
| All C-01..C-32 | same | **same** | Route blocks don't touch consequence anchors; C-32 and its cascade (C-18, C-19, C-21, C-22) still FAIL |
| C-29 | PASS | PASS | Already passing in V-01; Route blocks are an improvement in presentation but not a criteria state change |

Aspirational: **19/26 → 7.31 pts**

**V-03 Composite: 97.31** *(identical to V-01)*

---

### V-04 — Axes A+B (Letter-Slot + Complete Anchors)

**Changes from V-02**: V-02 already inherits letter-slot identifiers from the R12 base. V-04 makes the choice explicitly architectural. No criteria change from V-02 — C-31 already PASS in V-02 via inherited base.

All criteria: identical to V-02. Aspirational: **24/26 → 9.23 pts**

**V-04 Composite: 99.23** *(identical to V-02)*

---

### V-05 — Axes A+B+C (Letter-Slot + Complete Anchors + Route Blocks)

**Changes from V-04**: Adds explicit `Route:` blocks. C-29 already passes in V-04. No criteria state change.

All criteria: identical to V-04. Aspirational: **24/26 → 9.23 pts**

**V-05 Composite: 99.23** *(identical to V-02/V-04)*

---

## Score Summary

| Variation | Axes | Essential | Recommended | Asp Fails | Composite |
|-----------|------|-----------|-------------|-----------|-----------|
| **V-02** | B | 5/5 | 3/3 | — | **99.23** |
| **V-04** | A+B | 5/5 | 3/3 | — | **99.23** |
| **V-05** | A+B+C | 5/5 | 3/3 | — | **99.23** |
| V-01 | A | 5/5 | 3/3 | C-18,19,21,22,32 | 97.31 |
| V-03 | C | 5/5 | 3/3 | C-18,19,21,22,32 | 97.31 |

Golden threshold (all 5 essentials PASS AND composite ≥ 80): **all variations qualify**.

---

## Excellence Signals

**From V-02/V-04/V-05 (top tier):**

1. **Outcome propositions over absence statements.** C-32 draws a hard line between "there is no X" (absence of a check) and "X happens when Y is absent" (downstream consequence). The v12 rubric provides its own counter-example: the phrase "there is no inertia question" explicitly fails. Winning anchors assert what inertia *does* when Signal is absent — "Inertia wins the default choice at the planning stage" — not what Signal *doesn't provide*.

2. **Axis B is the sole load-bearing axis in R13.** Axis A (explicit letter-slot annotation) provides architectural clarity and satisfies C-31 under the letter-slot preference, but the R12 base already used letter-slot. Axis C (Route blocks) improves routing prose readability but C-29 was already passing. Only Axis B changes criteria outcomes — it lifts five FAILs (C-18, C-19, C-21, C-22, C-32) to PASS, moving the composite from 97.31 to 99.23. The 2-point aspiration gap is entirely attributable to one axis.

3. **C-32 acts as a gateway criterion.** A single structural failure in C-32 cascades to four behavioral criteria (C-18, C-19, C-21, C-22). Specs that pass all 28 other criteria still lose 5/26 of their aspirational budget because the anchor sentences aren't complete assertable propositions.

---

## Ceiling Analysis

The maximum achievable score under v12 with 24 visible aspirational criteria is **24/26 × 10 = 9.23**, producing a composite ceiling of **99.23**. The 2-unit gap between the visible denominator (24) and A=26 suggests two aspirational criteria beyond C-32 have not yet been formalized — V-05 is the R13 champion but is not the definitive v12 100-point spec.

---

```json
{"top_score": 99.23, "all_essential_pass": true, "new_patterns": ["Outcome anchors required over absence anchors: C-32 fails absence-of-check statements ('there is no X') regardless of phase vocabulary — anchors must assert the downstream consequence of Signal being absent, not merely name what is missing", "Axis B is the sole score-determining axis in R13: Axes A and C provide structural uniformity and routing clarity but neither resolves C-32 cascade failures; only complete assertable outcome propositions move the composite from 97.31 to 99.23"]}
```
