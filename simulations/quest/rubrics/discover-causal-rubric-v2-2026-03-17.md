Written to `simulations/quest/rubrics/discover-causal-rubric-v2-2026-03-17.md`.

Here's what changed from v1:

**4 new aspirational criteria (C-11 through C-14), sourced from R1 scorecard:**

| ID | Signal source | What it captures |
|----|---------------|-----------------|
| C-11 | V-04, V-05 | Model explicitly flags when it can't trace 3+ observable steps, rather than fabricating a weak pathway ("mechanism incompleteness acknowledged") |
| C-12 | V-05 | Falsification break is pinned to a specific step number/label from the pathway — not just a generic break description ("falsification step-anchored") |
| C-13 | V-05 `evidence_gap_steps` | Evidence section names which specific steps lack contextual support — per-step accounting vs. summary verdict ("evidence gap localized to steps") |
| C-14 | V-03, V-05 | AMEND's narrowed claim explicitly incorporates the inertia finding — the two outputs are integrated, not parallel ("AMEND conditioned on inertia finding") |

**Scoring impact:**
- Aspirational tier: 10 pts → 30 pts (6 criteria × 5 pts each)
- Grand total: 100 → 120 pts
- Scoring guide thresholds updated: Golden ≥ 110, Acceptable 95–109, Passing 85–94

**Why these four specifically:** C-07 (confounders) was already recommended and just universally failing — not an excellence signal, it's a gap. These four only appeared in the highest-complexity variations and represent genuine precision above what the current tier structure rewards.
ing criteria do not capture.
- **C-12 (falsification step-anchored)** — V-05's row-number tie ("name the row number from the Phase 2
  table") is the most precise falsification anchor observed. C-02 only requires a mechanism break; C-12
  requires that break to be pinned to a named step.
- **C-13 (evidence gap per step)** — V-05's `evidence_gap_steps` field goes beyond C-05's binary
  presence/absence check to identify which specific mechanism steps lack contextual support. A structural
  precision above what C-05 requires.
- **C-14 (AMEND conditioned on inertia finding)** — V-03 and V-05 both require the narrowed claim to
  incorporate the inertia check result (e.g., "in contexts where the status quo does not already...").
  C-08 requires actionability; C-14 requires that the inertia finding is visible in the AMEND output.

Aspirational tier expands from 10 pts to 30 pts (6 criteria x 5 pts). Grand total moves from 100 to 120.
Scoring guide thresholds updated proportionally.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Mechanism traced as pathway** | correctness | essential | Response traces the causal pathway as a sequence of named, observable steps from X to Y. Each step must name what changes, who or what drives the change, and how the change would be observable. A pathway that reads "X leads to better outcomes" does not pass. |
| C-02 | **Falsification is a mechanism break** | correctness | essential | Response states what a broken mechanism looks like — not "if metric Y doesn't improve" but a specific step in the causal chain that fails to occur (e.g., users see the feature but behavior doesn't change at the expected step). Must reference a specific step in the mechanism pathway. |
| C-03 | **Inertia check performed** | coverage | essential | Response directly asks and answers whether doing nothing (no feature, status quo) would also produce outcome Y. Must not omit this check or treat it as optional. |
| C-04 | **Causal claim narrowed in AMEND** | behavior | essential | Output includes an AMEND section that produces a revised, narrower version of the original causal claim — more precise scope, conditions, or population than the input hypothesis. Restating the original does not pass. |
| C-05 | **Context evidence assessed** | correctness | essential | Response evaluates whether evidence that the mechanism holds exists in the feature's specific context (team, product, users). "We don't have evidence yet" is a valid answer; silence is not. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Mechanism pathway is testable** | depth | recommended | The described pathway is specific enough that a team could design an observation or test to confirm or deny it. Vague pathways ("X leads to better outcomes") do not pass; named measurable steps do. |
| C-07 | **At least one confounder or alternative cause identified** | depth | recommended | Response names at least one plausible alternative explanation for Y that does not involve X, or a confounding variable that could create the appearance of X causing Y. |
| C-08 | **AMEND output is actionable** | behavior | recommended | The narrowed claim in AMEND is concrete enough to act on — includes a bounded scope (user segment, condition, timeframe) or a mechanism qualifier. Generic narrowings ("add more evidence") do not pass. |

---

## Aspirational Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Evidence quality rated** | depth | aspirational | Response distinguishes between evidence types (anecdotal, observed correlation, controlled measurement) and rates the current strength of causal evidence, not just its presence or absence. |
| C-10 | **Multiple causal pathways considered** | depth | aspirational | Response identifies more than one possible causal pathway from X to Y and notes whether they are complementary, competing, or independently falsifiable. |
| C-11 | **Mechanism incompleteness acknowledged** | honesty | aspirational | When the response cannot name 3 or more observable intermediate steps, it explicitly says so rather than fabricating a weak or vague pathway to appear complete. Self-disclosure ("mechanism not fully traceable") passes; a thin 3-step pathway that papers over the gap does not. |
| C-12 | **Falsification break anchored to named step** | precision | aspirational | The mechanism-break statement names the specific step number or label from the causal pathway (e.g., "Step 2 — user sees the prompt — does not occur"), not just a generic break description. Requires a pathway with named steps to be gradeable. |
| C-13 | **Evidence gap localized to pathway steps** | precision | aspirational | The context evidence section identifies which specific steps in the mechanism lack supporting evidence, not just whether evidence exists in aggregate. Output must name at least one step with missing evidence or confirm all steps have support — a per-step accounting, not a summary verdict. |
| C-14 | **AMEND conditioned on inertia finding** | integration | aspirational | The narrowed causal claim in AMEND explicitly incorporates the inertia check result — e.g., scopes the claim to contexts where the status quo does not already produce Y, or flags the claim as invalid if the inertia check shows the feature is redundant. A narrowed claim that ignores the inertia finding does not pass. |

---

## Scoring Guide

| Range | Interpretation |
|-------|---------------|
| All essential pass + >= 110 | Golden — meets bar for production use |
| All essential pass + 95-109 | Acceptable — useful but shallow on aspirational |
| All essential pass + 85-94 | Passing — essential + recommended coverage only |
| Any essential fail | Below bar — output is unreliable regardless of score |
| < 85 | Below bar |

**Maximum: 120 pts** (60 essential + 30 recommended + 30 aspirational)

---

## Common Failure Modes

- **C-01 fail**: Output confirms the claim ("yes, X causes Y") without tracing the mechanism
- **C-02 fail**: Falsification is stated as a metric threshold ("if retention doesn't go up") rather than a mechanism break
- **C-03 fail**: Inertia check skipped entirely — most common failure per skill description
- **C-04 fail**: AMEND section restates the original hypothesis or broadens instead of narrows
- **C-05 fail**: Evidence section is generic ("studies show...") without reference to the team's actual context
- **C-07 fail** (common): Inertia check surfaces status-quo alternative but no independent confounders named — easy to satisfy C-03 while missing C-07 entirely
- **C-11 fail**: Model fabricates 3 weak steps to avoid appearing incomplete instead of flagging the gap
- **C-14 fail**: AMEND narrows the claim but does not incorporate what the inertia check found — the two outputs are not integrated
---
