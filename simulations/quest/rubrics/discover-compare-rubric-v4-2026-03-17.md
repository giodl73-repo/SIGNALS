Reading the two patterns from the scorecard:

1. **Pattern 1** — Belt-and-suspenders: structural pre-check gate + inline `invalid` vocabulary independently close C-13; having both is a stronger enforcement form than either alone.
2. **Pattern 2** — RULE 4 binary fill-in template: machine-parseable recommendation evidence format is the single gap separating V-01/V-02 from a perfect score; goes beyond C-12's "traces to cells" into a structured slot-filling contract.

These become C-14 and C-15. Total grows from 120 → 130 pts (8 aspirational × 5 pts = 40). Thresholds scale proportionally (~78% golden, ~66% near-golden).

---

# discover-compare rubric — v4

**4 essential / 3 recommended / 8 aspirational**
**Total: 130 pts** (Essential 60 · Recommended 30 · Aspirational 40)

---

## Change Log

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | Added C-10, C-11, C-12 from R1 excellence signals; aspirational grows to 5 criteria (25 pts); scoring guide thresholds updated |
| v3 | Added C-13 from R2 excellence signals; aspirational grows to 6 criteria (30 pts); scoring guide thresholds updated |
| v4 | Added C-14, C-15 from R3 excellence signals; aspirational grows to 8 criteria (40 pts); total grows to 130 pts; scoring guide thresholds updated |

**New in v4:**
- C-14 — Dual-mechanism axis enforcement (belt-and-suspenders: structural pre-check gate AND inline disqualification vocabulary both present, each independently sufficient)
- C-15 — Recommendation evidence template (RULE 4 binary fill-in format: machine-parseable slot structure for matrix cell citations, goes beyond C-12's traceability requirement)

**Pattern from R3:** V-04/V-05 demonstrate that structural gate (named Pre-Check section) and inline vocabulary (`invalid — not incomplete`) independently close C-13 — either mechanism alone is sufficient, but both together provide belt-and-suspenders enforcement that no axis ambiguity can survive. V-01/V-02 reach 118/120 under v3; the single remaining gap is the RULE 4 binary evidence template in the recommendation section, which makes citation machine-parseable rather than prose-traceable. C-14 captures the dual-mechanism upgrade; C-15 captures the evidence-template upgrade.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | All four dimensions evaluated per option | coverage | essential | Feasibility, inertia, risk, and competitive analysis are each present for every option being compared — not just for the preferred option |
| C-02 | Inertia framed as "do nothing vs THIS option" *(highest-signal)* | correctness | essential | For each option, inertia is the specific resistance to adopting THAT option — not generic "teams resist change" or rollout risk |
| C-03 | Decision matrix present and scannable | format | essential | A structured comparison (table or equivalent side-by-side summary) exists that maps options to dimensions — scannable at a glance |
| C-04 | Recommendation given with rationale | correctness | essential | Output states which option (or neither) is recommended, and the rationale is grounded in the comparison results — not a generic "it depends" |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | Inertia analysis is substantive | depth | recommended | Inertia reasoning goes beyond "teams will adopt it" — identifies a specific friction, habit, or status quo that the option must overcome (or fails to overcome) |
| C-06 | Risk assessment is concrete and option-specific | depth | recommended | Each option's risks are distinct and specific — not interchangeable generic risks like "complexity" or "timeline" that could apply to any feature |
| C-07 | "Neither worth building" outcome explicitly considered | coverage | recommended | Output either surfaces "neither option clears the inertia bar" as a live finding, or explicitly rules it out with reasoning — not silently assumed away |

---

## Aspirational Criteria (40 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | AMEND paths surfaced | behavior | aspirational | Output invites or suggests at least one amendment: a third option, a dimension weight adjustment, or an audience variant (exec vs engineering) — either inline or as a closing prompt |
| C-09 | Competitive positioning is strategically differentiated | depth | aspirational | Each option's competitive positioning tells a distinct story about differentiation or market fit — not just "Option A has feature X, Option B does not" |
| C-10 | Inertia hard gate present | structure | aspirational | Output contains a blocking mechanism — explicit or structural — that halts matrix generation and recommendation if inertia does not clear for any option. Goes beyond C-07: not "considers neither" but "refuses to proceed past a gate." Pass condition: gate is named, triggers on a stated inertia condition, and specifies what must change before the comparison can continue |
| C-11 | Cross-option risk disqualifier applied | depth | aspirational | Output contains an explicit rule — stated or applied — that a risk appearing identically for both options is invalid and excluded. Goes beyond C-06: not "risks are specific" but "shared risks are actively disqualified." Pass condition: at least one risk is tested against this rule, or the rule is stated as a constraint on the risk assessment |
| C-12 | Recommendation traces to matrix cells | correctness | aspirational | Recommendation cites specific matrix cells (by option × dimension) as evidence. Goes beyond C-04: not "grounded in comparison" but traceable to named data points. Pass condition: recommendation identifies at least two specific option-dimension intersections that drove the conclusion |
| C-13 | Competitive axis distinctness rule enforced | structure | aspirational | Output contains an explicit rule — stated or applied — that options must claim distinct competitive axes or differentiation targets. Goes beyond C-09: not "distinct story per option" but "converging on the same axis is invalid." Pass condition: the rule is stated before analysis begins, OR at least one option's positioning is tested against this rule with a find-distinct-axis requirement on convergence |
| C-14 | Dual-mechanism axis enforcement (belt-and-suspenders) | structure | aspirational | Output contains BOTH a structural pre-check gate (a named section where axes are declared and locked before analysis begins) AND inline disqualification vocabulary (e.g., `invalid — not incomplete`) at the point of competitive analysis. Goes beyond C-13: not "either mechanism closes the rule" but "both mechanisms are independently present." Pass condition: a named pre-check section exists with explicit axis slots, AND the competitive analysis section uses disqualification language on convergence — each mechanism sufficient alone, both present for redundancy |
| C-15 | Recommendation evidence template (machine-parseable format) | correctness | aspirational | Recommendation section contains a structured fill-in template — not prose traceability — with explicit named slots for matrix cell citations (e.g., `[Option × Dimension] = [finding] → [direction]`). Goes beyond C-12: not "traces to named data points" but "provides a binary fill-in contract that makes evidence machine-parseable." Pass condition: recommendation uses a named template (e.g., RULE 4 format) with at least two explicit option-dimension citation slots completed |

---

## Scoring Guide

| Score Range | Meaning |
|-------------|---------|
| All essential pass + composite >= 102 | Golden — meets bar |
| All essential pass + composite 86–101 | Near-golden — one recommended or aspirational gap |
| 3/4 essential pass | Failing — one must-have missing |
| < 3 essential pass | Reject — not a valid compare output |

*Thresholds adjusted from v3 (94/79 of 120 pts) to maintain equivalent percentages (~78% / ~66%) at 130 pts total.*

---

## Notes

- **C-02** is the highest-signal essential.
- **C-07 vs C-10**: gate mechanism vs. consideration.
- **C-06 vs C-11**: active disqualification rule vs. specificity requirement.
- **C-09 vs C-13**: C-09 requires a distinct story per option. C-13 requires an enforcement mechanism that flags axis convergence and demands resolution.
- **C-13 vs C-14**: C-13 requires one mechanism (structural gate OR inline vocabulary). C-14 requires both — belt-and-suspenders. Either mechanism alone closes C-13; only having both closes C-14.
- **C-04 vs C-12 vs C-15**: C-04 requires a grounded rationale. C-12 requires traceable cell citations (named intersections). C-15 requires a machine-parseable fill-in template — structured slots, not prose.
- **Upgrade symmetry**: C-06→C-11 (risk specificity → shared-risk disqualifier), C-09→C-13 (distinct story → axis-convergence rule), C-13→C-14 (one mechanism → dual mechanism), C-12→C-15 (prose traceability → fill-in evidence template).
