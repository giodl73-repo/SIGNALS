The v4 rubric is written to `simulations/quest/rubrics/discover-causal-rubric-v4-2026-03-17.md`.

---

Here is the complete updated rubric:

---

# discover-causal Rubric v4

**Skill:** `discover-causal` | **Date:** 2026-03-17

---

## What changed from v3

**2 new aspirational criteria (C-19 through C-20), sourced from R3 scorecard:**

| ID | Signal source | What it captures |
|----|---------------|-----------------|
| C-19 | R3 pattern #2 / V-04 C-15 partial | AMEND names evidence gap (list of gap steps) and evidence tier (T1/T2/T3 aggregate rating) as two separate fields — having one does not satisfy the other ("AMEND evidence gap and evidence tier are separate fields") |
| C-20 | R3 pattern #3 / V-02 V-03 C-14 partial | AMEND incorporates the inertia verdict unconditionally — conditioning on "if Competing/Unclear" leaves a Not-competing escape hatch and does not pass ("AMEND inertia incorporation is unconditional") |

**Scoring impact:**
- Aspirational tier: 50 pts → 60 pts (12 criteria × 5 pts each)
- Grand total: 140 → **150 pts**
- Thresholds: Golden **>= 140**, Acceptable **125–139**, Passing **115–124**

**R3 ceiling observation:** All four v3 aspirational criteria (C-15/C-16/C-17/C-18) layer on the R2 V-05 phase structure without conflict — the 140/140 ceiling was achievable in a single combined variation. C-19 and C-20 are the next-tier requirements revealed by V-04 and V-02/V-03 partial scores.

---

## Criteria summary

| Tier | IDs | Pts |
|------|-----|-----|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-20 | 60 |

**C-19/C-20 relationship to C-14/C-15:** C-19 and C-20 do not replace C-14 and C-15 — they capture the stricter pass conditions that C-14 and C-15 require at full depth. A response can pass C-14 and C-15 at partial credit while failing C-19 and C-20.

---

## Aspirational Criteria (60 pts total) — new additions

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-19 | **AMEND evidence gap and evidence tier are separate fields** | integration | The AMEND section produces two distinct named outputs: (1) the evidence gap — the list of pathway step labels that lack supporting evidence — and (2) the evidence tier — the T1/T2/T3 aggregate quality rating for all evidence evaluated. A response where these appear merged, or where one is present and the other omitted, does not pass. |
| C-20 | **AMEND inertia incorporation is unconditional** | integration | The amended causal claim incorporates the inertia verdict regardless of verdict value — not only when the verdict is Competing or Unclear. Even when the verdict is Not competing, the amended claim must explicitly reference the inertia finding. A response conditioned on the verdict being Competing or Unclear leaves a Not-competing escape hatch and does not pass. |

---

**Design rationale:**

- **C-19** closes the gap exposed by V-04's C-15 partial: having a list of gap steps is not the same as having a T1/T2/T3 aggregate tier rating. A pathway where all steps have T1 evidence has *no* gap steps but still carries an evidence tier. These are different fields and must appear separately.
- **C-20** closes the gap exposed by V-02 and V-03's C-14 partials: both used a conditional form ("incorporates inertia if Competing or Unclear"), which silently drops the inertia finding in the most common Not-competing case. The universal rule — inertia verdict always in the amended claim — is the correct bar.
ns, or population than the input hypothesis. Restating the original does not pass. |
| C-05 | **Context evidence assessed** | correctness | essential | Response evaluates whether evidence that the mechanism holds exists in the feature's specific context (team, product, users). "We don't have evidence yet" is a valid answer; silence is not. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Mechanism pathway is testable** | depth | recommended | The described pathway is specific enough that a team could design an observation or test to confirm or deny it. Vague pathways ("X leads to better outcomes") do not pass; named measurable steps do. |
| C-07 | **At least one confounder or alternative cause identified** | depth | recommended | Response names at least one plausible alternative explanation for Y that does not involve X, or a confounding variable that could create the appearance of X causing Y. |
| C-08 | **AMEND output is actionable** | behavior | recommended | The narrowed claim in AMEND is concrete enough to act on — includes a bounded scope (user segment, condition, timeframe) or a mechanism qualifier. Generic narrowings ("add more evidence") do not pass. |

---

## Aspirational Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Evidence quality rated** | depth | aspirational | Response distinguishes between evidence types (anecdotal, observed correlation, controlled measurement) and rates the current strength of causal evidence, not just its presence or absence. |
| C-10 | **Multiple causal pathways considered** | depth | aspirational | Response identifies more than one possible causal pathway from X to Y and notes whether they are complementary, competing, or independently falsifiable. |
| C-11 | **Mechanism incompleteness acknowledged** | honesty | aspirational | When the response cannot name 3 or more observable intermediate steps, it explicitly says so rather than fabricating a weak or vague pathway to appear complete. Self-disclosure ("mechanism not fully traceable") passes; a thin 3-step pathway that papers over the gap does not. |
| C-12 | **Falsification break anchored to named step** | precision | aspirational | The mechanism-break statement names the specific step number or label from the causal pathway (e.g., "Step 2 — user sees the prompt — does not occur"), not just a generic break description. Requires a pathway with named steps to be gradeable. |
| C-13 | **Evidence gap localized to pathway steps** | precision | aspirational | The context evidence section identifies which specific steps in the mechanism lack supporting evidence, not just whether evidence exists in aggregate. Output must name at least one step with missing evidence or confirm all steps have support — a per-step accounting, not a summary verdict. |
| C-14 | **AMEND conditioned on inertia finding** | integration | aspirational | The narrowed causal claim in AMEND explicitly incorporates the inertia check result — e.g., scopes the claim to contexts where the status quo does not already produce Y, or flags the claim as invalid if the inertia check shows the feature is redundant. A narrowed claim that ignores the inertia finding does not pass. |
| C-15 | **AMEND synthesizes all phase outputs** | integration | aspirational | The AMEND section explicitly names and incorporates the outputs of every prior analytical phase — inertia verdict, mechanism completeness status, evidence tier, and confounder finding — rather than summarizing in aggregate or selectively ignoring phases. An AMEND that references only some phase outputs does not pass. Partial integration (e.g., evidence tier present, inertia absent) does not pass. |
| C-16 | **Pathway steps formally labeled** | precision | aspirational | Each step in the causal pathway carries a persistent formal label (e.g., "Step N — [Name]:") that the falsification and evidence sections can reference by name. Positional references only ("the second step") and prose bullet lists without persistent labels do not pass. Formal labeling is the prerequisite that makes C-12 and C-13 mechanically gradeable — this criterion rewards having that prerequisite in place. |
| C-17 | **Confounder explicitly distinguished from inertia** | coverage | aspirational | When naming alternative explanations for Y, the response explicitly excludes the inertia/status-quo case from the confounder analysis — treating "does nothing also cause Y?" and "what else independently causes Y?" as separate analytical questions. A response where the only named alternative is the inertia case, or where confounder and inertia analysis are merged in a single section without explicit separation, does not pass. |
| C-18 | **Incomplete pathway still anchors falsification** | honesty | aspirational | When mechanism incompleteness is declared (per C-11), the falsification break is still anchored to the highest-confidence labeled step traced rather than deferred, omitted, or replaced with a metric threshold. An incomplete pathway that names a specific step-anchored failure point passes; one that declares incompleteness and then offers no step-level falsification does not. Requires C-11 PASS and C-12 PASS to be gradeable — if either fails, this criterion is not scored. |
| C-19 | **AMEND evidence gap and evidence tier are separate fields** | integration | aspirational | The AMEND section produces two distinct named outputs: (1) the evidence gap — the list of pathway step labels that lack supporting evidence — and (2) the evidence tier — the T1/T2/T3 aggregate quality rating for all evidence evaluated. A response where these appear merged into a single entry, or where one is present and the other omitted, does not pass. The distinction matters: a pathway where all steps have T1 evidence has no gap steps but still carries an evidence tier; a pathway with gap steps may still carry a tier rating for the steps that do have evidence. |
| C-20 | **AMEND inertia incorporation is unconditional** | integration | aspirational | The amended causal claim in AMEND incorporates the inertia verdict regardless of verdict value — not only when the verdict is Competing or Unclear. Even when the verdict is Not competing, the amended claim must explicitly reference the inertia finding (e.g., confirming that the feature adds causal effect beyond what the status quo already produces). A response where inertia incorporation is conditioned on the verdict being Competing or Unclear leaves a Not-competing escape hatch and does not pass. |

---

## Scoring Guide

| Range | Interpretation |
|-------|---------------|
| All essential pass + >= 140 | Golden — meets bar for production use |
| All essential pass + 125-139 | Acceptable — useful but shallow on aspirational |
| All essential pass + 115-124 | Passing — essential + recommended coverage only |
| Any essential fail | Below bar — output is unreliable regardless of score |
| < 115 | Below bar |

**Maximum: 150 pts** (60 essential + 30 recommended + 60 aspirational)

**Note on C-18 gradeability:** C-18 is only scored when both C-11 (incompleteness acknowledged) and C-12 (falsification step-anchored) pass. If the pathway is complete and C-11 does not trigger, C-18 is marked N/A and excluded from the denominator. Scorecards should document this explicitly.

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
- **C-15 fail**: AMEND synthesizes some phases but silently drops others — e.g., narrowed claim incorporates evidence tier but ignores the inertia verdict or confounder finding
- **C-16 fail**: Steps are listed as prose bullets or numbered without names — "1. User sees the feature" does not give falsification a stable referent to anchor to
- **C-17 fail**: Confounder section names only "the feature isn't needed because the status quo already does this" — that is the inertia case restated, not an independent alternative cause
- **C-18 fail**: Response declares incompleteness in C-11 and then offers a metric-threshold falsification or defers ("cannot falsify until mechanism is clearer") instead of anchoring to the best-traced step
- **C-19 fail**: AMEND has a single combined evidence entry that lists gap steps and assigns a tier in the same field — or lists gap steps but omits the aggregate tier entirely, or states an aggregate tier without naming which steps are gaps
- **C-20 fail**: Amended claim conditions inertia incorporation on the verdict value — e.g., scopes to contexts where status quo does not already produce Y only if Competing or Unclear — leaving Not-competing cases where the inertia finding is silently dropped from the amended claim
