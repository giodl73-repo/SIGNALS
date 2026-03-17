# Rubric: quest-golden (v3)

**Version**: v3 — updated after Round 2 scorecard (2026-03-14)
**Quest**: `quest-golden` — converge a skill prompt through iterative rubric evolution
**Change from v2**: Added C-12 (aspirational, structure) from R2-P1 and C-13 (aspirational, structure) from R2-P2.

---

## Criteria

### Essential (60 pts total)

The loop must actually run.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Full 4-phase loop executed | essential | behavior | The run executes all four phases in order: (1) generate variations, (2) score each variation per criterion, (3) identify excellence patterns from the spread, (4) propose new rubric criteria. A run that picks a winner by inspection or skips any phase does not pass. |
| C-02 | Per-criterion pass/fail shown for every variation | essential | behavior | The scorecard shows a pass/fail result for each criterion for each variation -- not a composite summary alone. A run that reports only totals or "all pass" without per-criterion breakdown is unauditable and does not pass. |
| C-03 | Both convergence conditions checked | essential | behavior | The run evaluates two independent gates: (1) TRIAL -- all variations pass all essential criteria; (2) PLATEAU -- the last two consecutive rounds each produced zero new excellence patterns. Both must be satisfied to declare golden. Declaring convergence when only one condition holds is a hard fail. |
| C-04 | Golden prompt artifact written | essential | behavior | The converged prompt body is written to the skill artifact path (`simulations/quest/golden/{skill}-golden-{date}.md`). An artifact that contains only metadata or a summary without the prompt body is a hard fail. |
| C-05 | Final rubric artifact written | essential | behavior | The final rubric (with all criteria accumulated across rounds) is written to a rubric artifact path (`simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md`). A run that scores but never persists the rubric is a hard fail. |

### Recommended (30 pts total)

The quest produces signal, not just a winner.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Excellence pattern named and abstracted | recommended | depth | For each round where a variation outperforms others, the run explicitly names what structural property caused the score difference -- not just which variation won. The pattern must be stated as a reusable principle not an instance description. |
| C-07 | Rubric criterion proposed with full fields | recommended | correctness | Each new rubric criterion proposed includes all five required fields: ID, text, weight, category, and a clear pass condition. A proposal missing any field does not pass. |
| C-08 | Plateau detection cites both rounds | recommended | behavior | When declaring quest plateau, the run explicitly states which two consecutive rounds produced no new excellence patterns, naming them. A plateau declaration without citing the round evidence does not pass. |

### Aspirational (10 pts total)

The variations do useful work.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Score separation across variations | aspirational | depth | Variations are designed or selected so that at least one scores lower than the rest in each round. A round where all variations produce identical composite scores does not pass -- no signal was extracted from the spread. |
| C-10 | Pattern generalizability stated | aspirational | coverage | Each extracted excellence pattern is explicitly tagged as either skill-specific or transferable. Patterns without a scope statement do not pass. |
| C-11 | Skill prompt explains why uninformative rounds stall plateau detection | aspirational | structure | The skill prompt contains an explicit statement that rounds in which all variations produce identical composite scores do not advance plateau detection -- in either the generation section or the convergence gate. A prompt that leaves this implicit relies on the operator to infer it, and operators who omit spread-design produce uninformative rounds that silently stall convergence. |
| **C-12** | **Generation phase contains an active spread-design instruction** | **aspirational** | **structure** | The generation step contains an explicit instruction that causes the operator to produce divergent variations -- either a causal explanation of why spread matters, competitive framing (champion-defense, inertia), or an explicit divergence rule. A prompt that provides only post-hoc score matrix visibility (e.g., a RANK row) without a generation-phase instruction does not pass. Visibility of spread after it exists is not a substitute for structural instruction that causes divergent variation design. |
| **C-13** | **Causal explanation for stalled plateau not substituted by competitive framing alone** | **aspirational** | **structure** | The prompt contains an explicit causal statement that rounds where all variations produce identical composite scores do not advance plateau detection -- regardless of whether competitive or inertia framing is also present. A prompt that relies solely on competitive framing (champion-defense, inertia pressure) to incentivize spread, without the causal explanation, does not pass C-11 and therefore does not pass this criterion. Competitive framing and causal explanation address the same underlying problem through distinct mechanisms; only the causal explanation satisfies the plateau-stall criterion. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| QG-01 | C-03 | Run declares convergence after trial gate but before plateau is confirmed |
| QG-02 | C-02 | Run reports "all pass" without per-criterion breakdown -- unauditable |
| QG-03 | C-06 | Pattern buried in scorecard ("V-03 won") rather than extracted as principle |
| QG-04 | C-04 | Golden prompt identified in prose but artifact never written |
| QG-05 | C-07 | Criterion proposed without pass condition -- cannot be scored next round |
| QG-06 | C-01 | Winner picked by inspection, 4-phase loop never executed |
| QG-07 | C-11 | Prompt requires score spread (C-09) but never explains why uniform rounds stall plateau detection -- operators omit spread-design without understanding the consequence |
| **QG-08** | **C-12** | **Prompt includes RANK row or score matrix but no generation-phase spread-design instruction -- structural visibility of spread does not cause divergent variation design** |
| **QG-09** | **C-13** | **Prompt uses competitive or inertia framing to incentivize divergence but omits the causal statement that uniform-composite rounds do not advance plateau detection -- the two mechanisms are non-substitutes** |

---

## Revision History

| Version | Round | Change |
|---------|-------|--------|
| v1 | -- | Initial rubric: C-01 through C-10 |
| v2 | R1 | Added C-11 from E-1: prompts that explain why uniform scores stall plateau detection produce spread-design incentives that instruction-only approaches lack. Source: V-05 vs V-01/V-03 divergence on C-09. Scope: transferable. |
| v3 | R2 | Added C-12 from R2-P1: active generation-phase spread-design instruction is necessary; RANK row alone is not sufficient. Source: V-03 FAIL vs V-01/V-02/V-04/V-05 PASS on C-09. Scope: transferable. Added C-13 from R2-P2: competitive framing and causal explanation are non-substitutes for C-11. Source: V-01 FAIL vs V-02/V-04/V-05 PASS on C-11. Scope: transferable. Scoring formula denominator updated from aspirational/3 to aspirational/5. |
