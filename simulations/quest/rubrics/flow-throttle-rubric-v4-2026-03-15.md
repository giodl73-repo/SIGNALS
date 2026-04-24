Reading the scorecard carefully to identify which excellence signals are genuinely new (not already covered by C-01–C-14).

**Signal inventory:**
1. Three-role pipeline with locked sequencing → **new** → C-15
2. Pre-analysis source register as first output → already covered by C-13
3. At-most-one binding constraint with contrastive reasoning → already C-14

One new criterion: C-15. Aspirational grows from 6 → 7 criteria (7 × 5 = 35 pts), composite max 120 → 125.

---

# flow-throttle Rubric — v4

**Skill**: `flow:throttle` | **Version**: v4 | **Date**: 2026-03-16
**Max composite**: 125 | **Golden threshold**: all 5 essential PASS + composite >= 80

---

## What Changed and Why

**C-13 — Pre-analysis source commitment** (aspirational, carried from v3)
V-03's Phase 0 source register revealed a failure mode that C-11 alone cannot prevent: retroactive citation, where a model states a number and then vaguely attributes it after the fact. C-11 checks that every number has a named source; C-13 checks that the source was *committed before the analysis began*. An output can pass C-11 (attribution present) while failing C-13 (attribution assembled post-hoc). Together they form a two-gate evidence integrity check: C-11 asks "is there a source?", C-13 asks "was the evidence base locked before the claims were built?" The required form is a named source register section that appears before any tier or threshold in the body; tiers without a register entry must be flagged `undocumented` rather than assigned inferred values.

**C-14 — Binding constraint exclusivity statement** (aspirational, carried from v3)
V-01 and V-04 both enforced an at-most-one binding tier constraint (a single Binding? = Y per inventory). The signal: designating a primary bottleneck without explaining why competing tiers are *not* the binding constraint is an assertion, not an argument. C-01 requires naming the primary bottleneck and its causal reason; C-14 requires contrastive reasoning for at least one non-binding tier — naming the mechanism that prevents it from failing before the primary bottleneck under the described load pattern (e.g., "Tier B's limit of 500 RPS is not reached before Tier A's 100 RPS connection limit because parallel branch fan-out hits the connection tier first"). Without C-14, a multi-tier analysis cannot distinguish genuine causal priority from arbitrary selection.

**C-15 — Role-locked sequencing pipeline** (new aspirational)
V-01 and V-05 both scored 120/120. The distinguishing structural mechanism: a three-role pipeline with locked inter-phase dependencies. Domain Expert commits the evidence base first; Architect traces only from that base; UX Advocate accounts for every tier the Expert named and no others. The critical property is that no role may introduce data that a prior role did not produce — the handoff between phases is explicit and one-directional. This locked sequencing eliminates retroactive citation more reliably than any single instruction (including C-13), because it makes out-of-order claims architecturally impossible rather than merely discouraged. C-13 requires that the source register appear before the first number; C-15 requires that the entire analysis honor a phase boundary: evidence committed → claims built from evidence → UX derived from claims. An output that organizes all analysis in a single undifferentiated block fails C-15 even if every number is individually attributed, because the structural dependency that prevents late evidence injection is absent.

**Scoring formula update**: Aspirational raised from 30 pts (6 × 5) to 35 pts (7 × 5), max composite 120 → 125. Golden threshold unchanged at 80 + all essential pass.

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

### Aspirational (weight: 35 pts total — raise the bar)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Mitigation recommendations with tradeoffs** — For each structural gap found (burst path, missing retry-after, cascade), the output proposes a concrete mitigation and states the tradeoff (e.g., adding a queue reduces burst but adds latency). | depth | At least two mitigations with explicit tradeoffs. Mitigations without tradeoffs, or tradeoffs without mitigations, score partial credit only. |
| C-10 | **Comparative severity ranking** — The output ranks the identified throttle risks by user-visible severity (high/medium/low or ordered list) and justifies the ranking with reference to impact frequency or blast radius. | behavior | A ranked list of at least three risks with justification. Unranked lists or rankings without justification fail. |
| C-11 | **Threshold sourcing provenance** — For each numeric threshold cited in C-08, the output attributes the value to a named source (Power Automate docs, connector reference page, platform SLA document) rather than asserting it from inference. | correctness | Every numeric threshold has a named source. A number stated without attribution (e.g., "typically 100 RPS") fails; a number cited with a doc name or URL passes. If no documentation exists for a tier, the output must state "not documented" rather than invent a value. |
| C-12 | **Coverage self-verification** — Before closing, the output includes an explicit self-check mapping its own content against the analysis criteria (bottleneck identified, propagation traced, tiers enumerated, UX described, burst path found). Any criterion the output cannot self-confirm as addressed is flagged as a gap. | behavior | A self-check section appears in the output and names each criterion. Outputs that omit a criterion in both the body and the self-check score the criterion FAIL. An output that self-reports a gap earns partial credit on that criterion (acknowledging absence is better than silent elision). |
| C-13 | **Pre-analysis source commitment** — Before any tier, threshold, or numeric claim appears, the output opens with a named source register listing the documentation it will draw from. Every number in the body cross-references a register entry; any tier with no register entry is flagged undocumented rather than given an inferred value. | correctness | A source register section appears before the first tier or number in the output. At least two named sources are listed. Numbers in the body without a register entry fail. If no documentation exists for a tier, the output must state "not documented" and may not substitute an inferred value. |
| C-14 | **Binding constraint exclusivity statement** — When multiple throttle tiers are identified, the output designates exactly one as the binding constraint and includes contrastive reasoning for at least one non-binding tier, explaining the mechanism that prevents it from failing before the primary bottleneck under the described load pattern. | correctness | The primary bottleneck is designated with an at-most-one constraint (no output may designate two tiers as co-equal binding constraints). At least one non-binding tier includes a named mechanism explaining why it does not fail first (e.g., its limit is not reached before the primary tier throttles under the described fan-out). Outputs that designate a binding tier without any contrastive reasoning for alternatives fail. |
| C-15 | **Role-locked sequencing pipeline** — The output is organized as an explicit multi-phase pipeline with one-directional inter-phase dependencies: an evidence phase (source register + tier inventory committed) followed by an analysis phase (bottleneck and propagation derived only from evidence-phase artifacts) followed by a consequence phase (UX and mitigations scoped only to tiers named in the evidence phase). No phase may introduce data that a prior phase did not produce; the handoff boundary between phases is explicitly stated. | correctness | At least two named phases appear with explicit handoff statements (e.g., "Analysis draws from the source register above"). The analysis phase introduces no new data sources. The consequence phase names no tiers absent from the evidence phase. An output with all correct content in a single undifferentiated block fails — the structural dependency that prevents late evidence injection must be visible in the output shape, not inferred from correct results. |

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 35)
```

PARTIAL = 0.5 pass for any criterion.

Max composite: 125 (reflects raised aspirational bar in v4).

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Ready for golden artifact |
| Silver | >= 60, all essential pass | Useful, missing depth |
| Bronze | >= 40, some essential pass | Partial signal, not reliable |
| Fail | Any essential fails | Output not usable |
