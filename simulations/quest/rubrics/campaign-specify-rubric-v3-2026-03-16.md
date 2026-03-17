# Scoring Rubric: campaign-specify (v3)

## What changed from v2

Two new aspirational criteria extracted from R2 excellence signals. Both originate from V-04 (inertia framing axis) and represent **argumentative completeness mechanisms** — not just structural patterns but forcing functions that prevent hollow compliance:

| New ID | Pattern Source | What it measures |
|--------|----------------|------------------|
| C-14 | V-04 Phase 0 inertia cost | Phase 0 names what each audience *loses* without the feature — concrete inaction cost per audience, not just voice register labels |
| C-15 | V-04/V-05 Do Nothing falsifiability | Recommendation explicitly defeats Do Nothing by name with a specific cost citation — not just a preference among non-default options |

**Scoring formula updated**: aspirational denominator 5 → 7.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

V-01 through V-05 scores under v3:

| Variation | Essential | Rec | Asp (of 7) | Composite |
|-----------|-----------|-----|------------|-----------|
| V-01 | 5/5 | 3/3 | 5/7 | 97.1 |
| V-02 | 5/5 | 3/3 | 4/7 | 95.7 |
| V-03 | 5/5 | 3/3 | 5/7 | 97.1 |
| V-04 | 5/5 | 3/3 | 7/7 | 100 |
| V-05 | 5/5 | 3/3 | 7/7 | 100 |

V-04 and V-05 are now the sole 100/100 scores. C-14 and C-15 are the differentiating axis.

---

## Criteria

### Essential (output is not useful without these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Three artifacts produced** | completeness | essential | The skill produces all three artifacts: spec, proposal, and pitch. All three must exist as written files on disk. Missing any artifact = fail. |
| C-02 | **Spec has all six required sections** | completeness | essential | The spec artifact contains all six sections: Overview, User Problem, Proposed Solution, Constraints, Open Questions, and Self-Review. Missing or empty section = fail. |
| C-03 | **Proposal has 3+ options including do-nothing** | completeness | essential | The proposal artifact contains at least three options. One option must be explicitly named "Do Nothing" (or equivalent). Each option must include description, pros, cons, risk, effort, and a recommendation section with stated rationale. |
| C-04 | **Pitch covers three audience versions** | coverage | essential | The pitch artifact contains exec, developer, and maker versions. Each version has: hook, what it does, why it matters, and call to action. Missing any version = fail. |
| C-05 | **Cross-artifact consistency** | correctness | essential | The feature name, core behavior, and key constraints described in the spec are consistent with those referenced in the proposal and pitch. No contradictions between artifacts on fundamental scope. |

---

### Recommended (output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Spec self-review flags gaps** | depth | recommended | The spec artifact includes a self-review section identifying open questions, ambiguities, or sections needing more detail. At least one gap or open question named. "No gaps found" does not pass. |
| C-07 | **Pitch contains anti-positioning section** | depth | recommended | The pitch artifact includes an anti-positioning section explicitly stating what the feature is NOT, distinct from the three audience versions. |
| C-08 | **Proposal recommendation cites trade-off rationale** | depth | recommended | The proposal recommendation section explicitly references the key trade-off(s) that drove the choice — not just a preference statement. The rationale must be traceable to a specific constraint or risk identified in the options analysis. |

---

### Aspirational (raise the bar once essential/recommended stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Scout signal pull-through** | behavior | aspirational | At least one artifact explicitly references or incorporates a scout signal (e.g., requirements from scout-requirements, options informed by scout-feasibility, positioning from scout-positioning). Signals pulled, not invented. |
| C-10 | **Audience voice differentiation** | depth | aspirational | The exec pitch version leads with outcomes/ROI, the dev version leads with the tool/capability, and the maker version uses jargon-free "can I do this?" framing. All three voices are detectably distinct — not the same content reordered. |
| C-11 | **Completion Check fail-safe** | reliability | aspirational | The orchestration emits an active recovery instruction after all phases: if any artifact is missing, the skill directs the model to detect and fill the gap before stopping. A passive reminder does not pass; the instruction must trigger a write, not just a warning. |
| C-12 | **Phase 0 audience framing pre-write** | structure | aspirational | A dedicated pre-writing phase establishes voice contracts — the one sentence each audience (exec, dev, maker) cares about most — before the spec is drafted. Voice contracts defined upfront, not inferred during pitch writing. This phase must precede Phase 1 (spec). |
| C-13 | **Namespace-targeted per-phase scout pull** | behavior | aspirational | Each writing phase pulls from the scout sub-namespace most relevant to its artifact: Phase 1 (spec) pulls from `simulations/scout/` broadly; Phase 2 (proposal) targets `scout-feasibility`; Phase 3 (pitch) targets `scout-positioning`. A single generic glob at orchestration start does not pass. |
| C-14 | **Per-audience inertia cost in Phase 0** | depth | aspirational | Phase 0 names the specific cost of inaction for each audience — not just the voice register each uses, but what each audience *loses* if the feature does not ship. The cost must be concrete and audience-specific (e.g., exec: revenue/risk exposure; dev: workaround burden; maker: blocked workflow). Generic value propositions or register labels alone do not pass. |
| C-15 | **Do Nothing as named falsifiable baseline** | correctness | aspirational | The Recommendation section explicitly defeats the Do Nothing option by name, citing a specific cost drawn from the options analysis. Required form: "We chose [X] over Do Nothing because [specific Option 1 cost], and over [Y] because [specific trade-off]." A recommendation that compares only non-default options, or defeats Do Nothing only implicitly, does not pass. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Score Range | Interpretation |
|-------------|----------------|
| < 60 | Not useful — missing essential artifacts or critical sections |
| 60–79 | Partial — essential met but depth gaps present |
| 80–89 | Golden — meets threshold, recommended satisfied |
| 90–97 | Exemplary — most aspirational criteria satisfied |
| 98–100 | Reference — all aspirational criteria satisfied (requires C-14 + C-15) |

---

## Failure Pattern Guidance

| Pattern | Likely Cause |
|---------|-------------|
| C-01 fails | Orchestration stopped early; one sub-skill did not run or write its artifact |
| C-02 fails | `draft-spec` ran but skipped a section (often constraints or open questions) |
| C-03 fails | `draft-proposal` produced fewer than three options or omitted do-nothing |
| C-04 fails | `draft-pitch` wrote only one or two audience versions |
| C-14 fails | Phase 0 defines audience register but not inaction cost; voice contracts are stylistic not argumentative |
| C-15 fails | Recommendation defeats a non-default option but never names Do Nothing; status quo is implicit, not falsified |
