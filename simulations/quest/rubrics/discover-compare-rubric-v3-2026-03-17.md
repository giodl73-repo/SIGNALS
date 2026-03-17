Here is the complete v3 rubric:

---

# discover-compare rubric — v3

**4 essential / 3 recommended / 6 aspirational**
**Total: 120 pts** (Essential 60 · Recommended 30 · Aspirational 30)

---

## Change Log

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | Added C-10, C-11, C-12 from R1 excellence signals; aspirational grows to 5 criteria (25 pts); scoring guide thresholds updated |
| v3 | Added C-13 from R2 excellence signals; aspirational grows to 6 criteria (30 pts); scoring guide thresholds updated |

**New in v3:**
- C-13 — Competitive axis distinctness rule (explicit enforcement that options must claim distinct axes -- stronger than C-09)

**Pattern from R2:** All four scored variations got PARTIAL on C-09 for the same reason -- "no RULE 3 equivalent" / "no enforcement of distinct axes." V-04 named the gap explicitly. C-13 captures the enforcement-layer upgrade, completing the C-06->C-11 / C-09->C-13 symmetry.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | All four dimensions evaluated per option | coverage | essential | Feasibility, inertia, risk, and competitive analysis are each present for every option being compared -- not just for the preferred option |
| C-02 | Inertia framed as "do nothing vs THIS option" *(highest-signal)* | correctness | essential | For each option, inertia is the specific resistance to adopting THAT option -- not generic "teams resist change" or rollout risk |
| C-03 | Decision matrix present and scannable | format | essential | A structured comparison (table or equivalent side-by-side summary) exists that maps options to dimensions -- scannable at a glance |
| C-04 | Recommendation given with rationale | correctness | essential | Output states which option (or neither) is recommended, and the rationale is grounded in the comparison results -- not a generic "it depends" |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | Inertia analysis is substantive | depth | recommended | Inertia reasoning goes beyond "teams will adopt it" -- identifies a specific friction, habit, or status quo that the option must overcome (or fails to overcome) |
| C-06 | Risk assessment is concrete and option-specific | depth | recommended | Each option's risks are distinct and specific -- not interchangeable generic risks like "complexity" or "timeline" that could apply to any feature |
| C-07 | "Neither worth building" outcome explicitly considered | coverage | recommended | Output either surfaces "neither option clears the inertia bar" as a live finding, or explicitly rules it out with reasoning -- not silently assumed away |

---

## Aspirational Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | AMEND paths surfaced | behavior | aspirational | Output invites or suggests at least one amendment: a third option, a dimension weight adjustment, or an audience variant (exec vs engineering) -- either inline or as a closing prompt |
| C-09 | Competitive positioning is strategically differentiated | depth | aspirational | Each option's competitive positioning tells a distinct story about differentiation or market fit -- not just "Option A has feature X, Option B does not" |
| C-10 | Inertia hard gate present | structure | aspirational | Output contains a blocking mechanism -- explicit or structural -- that halts matrix generation and recommendation if inertia does not clear for any option. Goes beyond C-07: not "considers neither" but "refuses to proceed past a gate." Pass condition: gate is named, triggers on a stated inertia condition, and specifies what must change before the comparison can continue |
| C-11 | Cross-option risk disqualifier applied | depth | aspirational | Output contains an explicit rule -- stated or applied -- that a risk appearing identically for both options is invalid and excluded. Goes beyond C-06: not "risks are specific" but "shared risks are actively disqualified." Pass condition: at least one risk is tested against this rule, or the rule is stated as a constraint on the risk assessment |
| C-12 | Recommendation traces to matrix cells | correctness | aspirational | Recommendation cites specific matrix cells (by option x dimension) as evidence. Goes beyond C-04: not "grounded in comparison" but traceable to named data points. Pass condition: recommendation identifies at least two specific option-dimension intersections that drove the conclusion |
| C-13 | Competitive axis distinctness rule enforced | structure | aspirational | Output contains an explicit rule -- stated or applied -- that options must claim distinct competitive axes or differentiation targets. Goes beyond C-09: not "distinct story per option" but "converging on the same axis is invalid." Pass condition: the rule is stated before analysis begins, OR at least one option's positioning is tested against this rule with a find-distinct-axis requirement on convergence |

---

## Scoring Guide

| Score Range | Meaning |
|-------------|---------|
| All essential pass + composite >= 94 | Golden -- meets bar |
| All essential pass + composite 79-93 | Near-golden -- one recommended or aspirational gap |
| 3/4 essential pass | Failing -- one must-have missing |
| < 3 essential pass | Reject -- not a valid compare output |

*Thresholds adjusted from v2 (90/75 of 115 pts) to maintain equivalent percentages at 120 pts total.*

---

## Notes

- **C-02** is the highest-signal essential.
- **C-07 vs C-10**: gate mechanism vs. consideration.
- **C-06 vs C-11**: active disqualification rule vs. specificity requirement.
- **C-09 vs C-13**: C-09 requires a distinct story per option. C-13 requires an enforcement mechanism that flags axis convergence and demands resolution. Mirrors the C-06→C-11 upgrade pattern applied to competitive positioning.
- **C-04 vs C-12**: named cell traceability vs. general grounding.
- **C-08** reflects the AMEND capability; aspirational because the skill is useful without it.

| New | Paired against | What makes it aspirational |
|-----|---------------|---------------------------|
| C-10 | C-07 | Gate mechanism vs. consideration |
| C-11 | C-06 | Active disqualification rule vs. specificity requirement |
| C-12 | C-04 | Named cell traceability vs. general grounding |
| C-13 | C-09 | Axis convergence enforcement vs. distinct-story requirement |

---

**One new criterion.** The R2 signal was unambiguous: four consecutive PARTIAL verdicts on C-09, all citing the same missing piece. C-13 completes the enforcement-layer upgrade series — every "rigor dimension" (inertia, risk, competitive, recommendation) now has both a quality criterion (C-05/C-06/C-09/C-04) and a structural enforcement criterion (C-10/C-11/C-13/C-12).
 consideration |
| C-11 | C-06 | Active disqualification rule vs. specificity requirement |
| C-12 | C-04 | Named cell traceability vs. general grounding |
| C-13 | C-09 | Axis convergence enforcement vs. distinct-story requirement |
