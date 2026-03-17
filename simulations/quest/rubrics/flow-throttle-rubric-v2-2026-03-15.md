Written to `simulations/quest/rubrics/flow-throttle-rubric-v2-2026-03-15.md`.

---

**What changed and why:**

**C-11 — Threshold sourcing provenance** (new aspirational)
V-01 scored PARTIAL on C-08 because it had numbers but the prompt never required them to be doc-attributed. The distinction matters: a model-invented "100 RPS" and a doc-cited "100 RPS per connection from the connector reference" are different quality signals. C-11 separates *has a number* (C-08) from *the number can be trusted* (C-11). The two criteria compose — PASS/PASS is verified, PASS/FAIL means the number is unverified inference.

**C-12 — Coverage self-verification** (new aspirational)
V-02's running scorecard and V-04's completion gates both discovered the same pattern from different angles: an output that self-checks before submission catches its own elisions rather than waiting for external scoring to surface them. The scorecard called V-02 a "genuine innovation for catching elision" while noting it "cannot generate content for structural gaps." C-12 formalizes this: the output must include a named self-check section. Notably, C-12 rewards honesty — an output that self-reports a gap earns partial credit on that criterion, which is strictly better than silent omission.

**Scoring formula update**: Aspirational raised from 10 pts (2 x 5) to 20 pts (4 x 5), max composite 100 → 110. Golden threshold unchanged at 80 + all essential pass.
for the scenario (e.g., per-connection, per-user, tenant, platform) and correctly matches each to the system component that enforces it. | coverage | At least two distinct rate-limit tiers are named with their enforcing component. Generic 'API limits apply' without tier distinction fails. |
| C-04 | **User experience at each throttle tier** -- For each throttle tier identified, the output describes the observable user experience (latency spike, error code, silent drop, queue delay, degraded mode). | depth | Every named tier from C-03 has a corresponding UX description. A tier named without UX consequence fails this criterion. |
| C-05 | **Unprotected burst path identification** -- The output explicitly calls out at least one path or scenario where burst traffic can bypass or overwhelm throttle controls. | correctness | A concrete burst scenario is named (e.g., parallel branch fan-out, retry storm, initial cold-start surge). Output that only describes steady-state throttle without any burst analysis fails. |

---

### Recommended (weight: 30 pts total -- output improves with these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Retry-after handling gaps** -- The output checks whether callers correctly consume and honor Retry-After (or equivalent) signals, and flags any caller that ignores them and contributes to retry storms. | behavior | At least one caller is evaluated for retry-after compliance, with a pass/fail verdict and consequence described. Omitting retry-after analysis entirely fails. |
| C-07 | **Cascading throttle failure scenario** -- The output describes at least one scenario where throttling at one tier causes a second downstream tier to also throttle, compounding the impact beyond the initial bottleneck. | depth | A two-tier cascade is named: Tier A throttles -> Tier B receives delayed/batched traffic -> Tier B throttles. Single-tier analysis only fails. |
| C-08 | **Quantified throughput thresholds** -- The output provides numeric context: requests-per-second, burst ceiling, queue depth, or timeout window for at least the primary bottleneck tier identified in C-01. | correctness | At least one threshold is stated as a number (even if approximate or from documentation). Purely qualitative descriptions fail. |

---

### Aspirational (weight: 20 pts total -- raise the bar)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Mitigation recommendations with tradeoffs** -- For each structural gap found (burst path, missing retry-after, cascade), the output proposes a concrete mitigation and states the tradeoff (e.g., adding a queue reduces burst but adds latency). | depth | At least two mitigations with explicit tradeoffs. Mitigations without tradeoffs, or tradeoffs without mitigations, score partial credit only. |
| C-10 | **Comparative severity ranking** -- The output ranks the identified throttle risks by user-visible severity (high/medium/low or ordered list) and justifies the ranking with reference to impact frequency or blast radius. | behavior | A ranked list of at least three risks with justification. Unranked lists or rankings without justification fail. |
| C-11 | **Threshold sourcing provenance** -- For each numeric threshold cited in C-08, the output attributes the value to a named source (Power Automate docs, connector reference page, platform SLA document) rather than asserting it from inference. | correctness | Every numeric threshold has a named source. A number stated without attribution (e.g., 'typically 100 RPS') fails; a number cited with a doc name or URL passes. If no documentation exists for a tier, the output must state 'not documented' rather than invent a value. |
| C-12 | **Coverage self-verification** -- Before closing, the output includes an explicit self-check mapping its own content against the analysis criteria (bottleneck identified, propagation traced, tiers enumerated, UX described, burst path found). Any criterion the output cannot self-confirm as addressed is flagged as a gap. | behavior | A self-check section appears in the output and names each criterion. Outputs that omit a criterion in both the body and the self-check score the criterion FAIL. An output that self-reports a gap earns partial credit on that criterion (acknowledging absence is better than silent elision). |

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 20)
```

Max composite: 110 (reflects raised aspirational bar in v2).

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Ready for golden artifact |
| Silver | >= 60, all essential pass | Useful, missing depth |
| Bronze | >= 40, some essential pass | Partial signal, not reliable |
| Fail | Any essential fails | Output not usable |

---

## Version Notes

**v2 changes (from Round 1 scorecard):**

- **C-11 added** (Threshold sourcing provenance): V-01 scored PARTIAL on C-08 because
  numbers were present but no prompt required doc attribution. A model-invented '100 RPS'
  and a doc-cited '100 RPS per connection' are not equivalent signals. C-11 separates
  quantification (C-08) from verification of source (C-11).

- **C-12 added** (Coverage self-verification): V-02 running scorecard and V-04 completion
  gates both showed the same insight -- structural self-check prevents elision that only
  appears as a gap during post-hoc rubric scoring. The scorecard finding was: 'genuine
  innovation for catching elision on criteria it does cover, but it cannot generate
  content for structural gaps.' C-12 rewards outputs that internalize the rubric before
  submitting rather than relying on external scoring to surface misses.

- **Aspirational weight** raised from 10 to 20 pts (4 criteria x 5 pts). Max composite
  raised from 100 to 110.

---

## Evaluation Notes

- C-01 and C-02 are the core of the skill -- a throttle simulation that cannot locate the
  bottleneck or trace propagation is not a simulation, it is speculation.
- C-05 (burst path) is the most commonly missed criterion in initial outputs; models tend
  to describe steady-state throttle only. V-01 set the gold standard: a dedicated burst
  scan that runs before tier enumeration, preventing false coverage confidence.
- C-08 (quantified thresholds) should be drawn from Power Automate / Connector
  documentation rates where applicable; invented numbers fail C-08 and also fail C-11.
- C-11 is the sourcing complement to C-08 -- a PASS on C-08 with a FAIL on C-11 indicates
  the number exists but cannot be trusted.
- C-12 rewards structural honesty: an output that self-reports 'I could not find a burst
  path' scores better than one that silently omits C-05 analysis.
- The stock role for this skill is Connectors / Power Automate throughput domain expert;
  the rubric assumes that framing when evaluating domain accuracy.
