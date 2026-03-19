Here is the complete v3 rubric as written:

---

# discover-causal Rubric v3

**Skill:** `discover-causal` | **Date:** 2026-03-17

---

## What changed from v2

**4 new aspirational criteria (C-15 through C-18), sourced from R2 scorecard:**

| ID | Signal source | What it captures |
|----|---------------|-----------------|
| C-15 | V-05 pattern #1 | AMEND names and incorporates outputs from every prior phase — inertia verdict, mechanism completeness, evidence tier, confounder finding ("AMEND synthesizes all phase outputs") |
| C-16 | V-05 pattern #2 / V-02 partial | Steps carry persistent formal labels ("Step N — [Name]:") that falsification and evidence can reference — positional references and prose bullets not sufficient ("pathway steps formally labeled") |
| C-17 | V-05 pattern #3 / V-03 partial | Confounder analysis explicitly excludes the inertia case by name — shared section conflation does not pass ("confounder explicitly distinguished from inertia") |
| C-18 | V-04/V-05 pattern #4 | When incompleteness declared (C-11), falsification still anchors to the highest-confidence labeled step rather than deferring ("incomplete pathway still anchors falsification") |

**Scoring impact:**
- Aspirational tier: 30 pts → 50 pts (10 criteria × 5 pts each)
- Grand total: 120 → **140 pts**
- Thresholds: Golden **>= 130**, Acceptable **115–129**, Passing **105–114**

---

## Criteria summary

| Tier | IDs | Pts |
|------|-----|-----|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-18 | 50 |

**Key design note on C-18:** Only graded when both C-11 and C-12 pass (incompleteness was declared and pathway has labeled steps). If C-11 doesn't trigger (pathway is complete), C-18 is N/A and excluded from the denominator.

**C-16 is a structural prerequisite note:** It rewards having the labeled-step format that makes C-12 and C-13 mechanically gradeable. V-02's partial scores on C-12/C-13 traced directly to unlabeled steps — this criterion makes that dependency explicit.
0 pts → 50 pts (10 criteria × 5 pts each)
- Grand total: 120 → 140 pts
- Scoring guide thresholds updated: Golden >= 130, Acceptable 115-129, Passing 105-114

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

## Aspirational Criteria (50 pts total)

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

---

## Scoring Guide

| Range | Interpretation |
|-------|---------------|
| All essential pass + >= 130 | Golden — meets bar for production use |
| All essential pass + 115-129 | Acceptable — useful but shallow on aspirational |
| All essential pass + 105-114 | Passing — essential + recommended coverage only |
| Any essential fail | Below bar — output is unreliable regardless of score |
| < 105 | Below bar |

**Maximum: 140 pts** (60 essential + 30 recommended + 50 aspirational)

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
