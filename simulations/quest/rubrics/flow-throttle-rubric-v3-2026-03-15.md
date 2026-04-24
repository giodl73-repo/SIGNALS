`flow-throttle-rubric-v3-2026-03-15.md` already exists in the rubrics directory (from a prior session). The task asks to output the complete updated rubric as Markdown — here it is:

---

# flow-throttle Rubric — v3

**Skill**: `flow:throttle` | **Version**: v3 | **Date**: 2026-03-15
**Max composite**: 120 | **Golden threshold**: all 5 essential PASS + composite >= 80

---

## What Changed and Why

**C-13 — Pre-analysis source commitment** (new aspirational)
V-03's Phase 0 source register revealed a failure mode that C-11 alone cannot prevent: retroactive citation, where a model states a number and then vaguely attributes it after the fact. C-11 checks that every number has a named source; C-13 checks that the source was *committed before the analysis began*. An output can pass C-11 (attribution present) while failing C-13 (attribution assembled post-hoc). Together they form a two-gate evidence integrity check: C-11 asks "is there a source?", C-13 asks "was the evidence base locked before the claims were built?" The required form is a named source register section that appears before any tier or threshold in the body; tiers without a register entry must be flagged `undocumented` rather than assigned inferred values.

**C-14 — Binding constraint exclusivity statement** (new aspirational)
V-01 and V-04 both enforced an at-most-one binding tier constraint (a single Binding? = Y per inventory). The signal: designating a primary bottleneck without explaining why competing tiers are *not* the binding constraint is an assertion, not an argument. C-01 requires naming the primary bottleneck and its causal reason; C-14 requires contrastive reasoning for at least one non-binding tier — naming the mechanism that prevents it from failing before the primary bottleneck under the described load pattern (e.g., "Tier B's limit of 500 RPS is not reached before Tier A's 100 RPS connection limit because parallel branch fan-out hits the connection tier first"). Without C-14, a multi-tier analysis cannot distinguish genuine causal priority from arbitrary selection.

**Scoring formula update**: Aspirational raised from 20 pts (4 x 5) to 30 pts (6 x 5), max composite 110 → 120. Golden threshold unchanged at 80 + all essential pass.

---

## Criteria

### Essential (weight: 60 pts total — output fails without these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Primary bottleneck identification with causal reason** — The output identifies the single throttle tier that will bind first under the described load pattern and explains *why* that tier binds before all others (e.g., the causal mechanism that makes it the first failure point). | correctness | A named tier is identified as primary with a stated causal reason. Outputs that list multiple tiers as equally binding, or that name a tier without a causal reason, fail. |
| C-02 | **Backpressure propagation traced minimum 2 hops** — Starting from the primary bottleneck, the output traces how throttle pressure propagates downstream or upstream for at least two hops, naming the mechanism at each hop (queue fill, connection hold, retry accumulation, etc.) and the observable effect. | depth | At least two hops are named with mechanism and observable effect per hop. Stopping at one hop fails. |
| C-03 | **At least 2 throttle tiers with enforcing component and scope** — The output enumerates the distinct rate-limit tiers relevant for the scenario (e.g., per-connection, per-user, tenant, platform) and correctly matches each to the system component that enforces it. | coverage | At least two distinct rate-limit tiers are named with their enforcing component. Generic "API limits apply" without tier distinction fails. |
| C-04 | **User experience at each throttle tier** — For each throttle tier identified, the output describes the observable user experience (latency spike, error code, silent drop, queue delay, degraded mode). | depth | Every named tier from C-03 has a corresponding UX description. A tier named without UX consequence fails this criterion. |
| C-05 | **Unprotected burst path identification** — The output explicitly calls out at least one path or scenario where burst traffic can bypass or overwhelm throttle controls. | correctness | A concrete burst scenario is named (e.g., parallel branch fan-out, retry storm, initial cold-start surge). Output that only describes steady-state throttle without any burst analysis fails. |

---

### Recommended (weight: 30 pts total — output improves with these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Retry-after handling gaps** — The output checks whether callers correctly consume and honor Retry-After (or equivalent) signals, and flags any caller that ignores them and contributes to retry storms. | behavior | At least one caller is evaluated for retry-after compliance, with a pass/fail verdict and consequence described. Omitting retry-after analysis entirely fails. |
| C-07 | **Cascading throttle failure scenario** — The output describes at least one scenario where throttling at one tier causes a second downstream tier to also throttle, compounding the impact beyond the initial bottleneck. | depth | A two-tier cascade is named: Tier A throttles -> Tier B receives delayed/batched traffic -> Tier B throttles. Single-tier analysis only fails. |
| C-08 | **Quantified throughput thresholds** — The output provides numeric context: requests-per-second, burst ceiling, queue depth, or timeout window for at least the primary bottleneck tier identified in C-01. | correctness | At least one threshold is stated as a number (even if approximate or from documentation). Purely qualitative descriptions fail. |

---

### Aspirational (weight: 30 pts total — raise the bar)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Mitigation recommendations with tradeoffs** — For each structural gap found (burst path, missing retry-after, cascade), the output proposes a concrete mitigation and states the tradeoff (e.g., adding a queue reduces burst but adds latency). | depth | At least two mitigations with explicit tradeoffs. Mitigations without tradeoffs, or tradeoffs without mitigations, score partial credit only. |
| C-10 | **Comparative severity ranking** — The output ranks the identified throttle risks by user-visible severity (high/medium/low or ordered list) and justifies the ranking with reference to impact frequency or blast radius. | behavior | A ranked list of at least three risks with justification. Unranked lists or rankings without justification fail. |
| C-11 | **Threshold sourcing provenance** — For each numeric threshold cited in C-08, the output attributes the value to a named source (Power Automate docs, connector reference page, platform SLA document) rather than asserting it from inference. | correctness | Every numeric threshold has a named source. A number stated without attribution (e.g., "typically 100 RPS") fails; a number cited with a doc name or URL passes. If no documentation exists for a tier, the output must state "not documented" rather than invent a value. |
| C-12 | **Coverage self-verification** — Before closing, the output includes an explicit self-check mapping its own content against the analysis criteria (bottleneck identified, propagation traced, tiers enumerated, UX described, burst path found). Any criterion the output cannot self-confirm as addressed is flagged as a gap. | behavior | A self-check section appears in the output and names each criterion. Outputs that omit a criterion in both the body and the self-check score the criterion FAIL. An output that self-reports a gap earns partial credit on that criterion (acknowledging absence is better than silent elision). |
| C-13 | **Pre-analysis source commitment** — Before any tier, threshold, or numeric claim appears, the output opens with a named source register listing the documentation it will draw from. Every number in the body cross-references a register entry; any tier with no register entry is flagged undocumented rather than given an inferred value. | correctness | A source register section appears before the first tier or number in the output. At least two named sources are listed. Numbers in the body without a register entry fail. If no documentation exists for a tier, the output must state "not documented" and may not substitute an inferred value. |
| C-14 | **Binding constraint exclusivity statement** — When multiple throttle tiers are identified, the output designates exactly one as the binding constraint and includes contrastive reasoning for at least one non-binding tier, explaining the mechanism that prevents it from failing before the primary bottleneck under the described load pattern. | correctness | The primary bottleneck is designated with an at-most-one constraint (no output may designate two tiers as co-equal binding constraints). At least one non-binding tier includes a named mechanism explaining why it does not fail first (e.g., its limit is not reached before the primary tier throttles under the described fan-out). Outputs that designate a binding tier without any contrastive reasoning for alternatives fail. |

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 30)
```

PARTIAL = 0.5 pass for any criterion.

Max composite: 120 (reflects raised aspirational bar in v3).

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Ready for golden artifact |
| Silver | >= 60, all essential pass | Useful, missing depth |
| Bronze | >= 40, some essential pass | Partial signal, not reliable |
| Fail | Any essential fails | Output not usable |

---

## Version Notes

**v3 changes (from Round 2 scorecard):**

- **C-13 added** (Pre-analysis source commitment): V-03's Phase 0 source register showed that retroactive citation is a distinct failure mode from absent citation. C-11 checks that every number has a named source; C-13 checks that the source was committed before the number was stated. Together they form a two-gate evidence integrity check. An output can pass C-11 and fail C-13 if attribution was assembled post-hoc.

- **C-14 added** (Binding constraint exclusivity statement): V-01 and V-04 enforced an at-most-one Binding? = Y constraint across their tier inventories. The insight is that naming a primary bottleneck without explaining why competing tiers are NOT binding first is an assertion without argument. C-14 requires contrastive reasoning for at least one non-binding tier, elevating bottleneck designation from selection to causal argument.

- **Aspirational weight** raised from 20 to 30 pts (6 criteria x 5 pts). Max composite raised from 110 to 120. Golden threshold unchanged at 80 + all essential pass.

**v2 changes (from Round 1 scorecard):**

- **C-11 added** (Threshold sourcing provenance): V-01 scored PARTIAL on C-08 because numbers were present but no prompt required doc attribution. A model-invented "100 RPS" and a doc-cited "100 RPS per connection" are not equivalent signals. C-11 separates quantification (C-08) from verification of source (C-11).

- **C-12 added** (Coverage self-verification): V-02 running scorecard and V-04 completion gates both showed the same insight — structural self-check prevents elision that only appears as a gap during post-hoc rubric scoring. C-12 rewards outputs that internalize the rubric before submitting rather than relying on external scoring to surface misses.

- **Aspirational weight** raised from 10 to 20 pts (4 criteria x 5 pts). Max composite raised from 100 to 110.

---

## Evaluation Notes

- C-01 and C-02 are the core of the skill — a throttle simulation that cannot locate the bottleneck or trace propagation is not a simulation, it is speculation.
- C-05 (burst path) is the most commonly missed criterion in initial outputs; models tend to describe steady-state throttle only.
- C-08 (quantified thresholds) should be drawn from Power Automate / Connector documentation rates where applicable; invented numbers fail C-08 and also fail C-11.
- C-11 and C-13 compose: C-11 asks "is there a source?", C-13 asks "was the evidence base locked before the claims were built?" PASS/PASS is verified. PASS on C-11 with FAIL on C-13 means attribution may be retroactive.
- C-12 rewards structural honesty: an output that self-reports "I could not find a burst path" scores better than one that silently omits C-05 analysis.
- C-14 is the argument complement to C-01: C-01 names the binding tier, C-14 defends the choice by ruling out alternatives. Together they constitute a falsifiable bottleneck claim.
- The stock role for this skill is Connectors / Power Automate throughput domain expert; the rubric assumes that framing when evaluating domain accuracy.

---

**Summary of changes:**

| | v1 | v2 | v3 |
|--|--|--|--|
| Essential | C-01–C-05 (60 pts) | unchanged | unchanged |
| Recommended | C-06–C-08 (30 pts) | unchanged | unchanged |
| Aspirational | C-09–C-10 (10 pts) | + C-11, C-12 (20 pts) | + C-13, C-14 (30 pts) |
| Max composite | 100 | 110 | 120 |
