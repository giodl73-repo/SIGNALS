Written to `simulations/quest/rubrics/flow-ratelimit-rubric-v3-2026-03-17.md`.

---

**Two new aspirational criteria extracted from R2:**

**C-15 — Document-head Global Verdict** (parent: C-13)
Both V-01 and V-02 earned only PARTIAL on C-13 for the same reason: the labeled verdict appeared mid-document (V-01: Section 3, after the structural audit; V-02: within a mid-analysis section). C-13 as written allows section-local commitment — the label requirement is satisfied without anchoring the analysis at document head. C-15 closes that gap: the Verdict block must be the opening section, before any inventory, audit table, or volume mapping. It must be self-contained and referenced by the evidence.

**C-16 — Format Contract Preamble** (parent: C-12)
V-02's axis was "format contract preamble — BASELINE / PROTECTED dual-column on every table and mitigation." That preamble produced the strongest C-12 enforcement of either variation because declaring the column structure as a document-wide contract before sections removes per-section negotiation. C-12 only requires the dual-column to appear in the volume table; C-16 requires it to be declared upfront with scenario-specific meanings, a rejection clause, and compliance across at least two distinct tables.

**Scoring update:** Aspirational denominator changes from `/6 * 30` to `/8 * 30`. Composite max stays 120; grade band thresholds unchanged. Both new criteria follow the same superset pattern as C-11–C-14: a response cannot earn the child without satisfying the parent.
 how throttling at the first bottleneck propagates causally to at least one upstream or downstream component — showing the directional mechanism, not just a list of affected components. "Component B is also throttled" does not pass; "Component A's queue fills → Component B receives delayed events → Component B's own timeout fires" does pass. |
| C-03 | **User Experience at Each Throttle Tier** | coverage | essential | Output describes observable user-facing behavior at each distinct throttle tier reached (e.g., 429 with Retry-After shown in connector error, flow run queued and delayed, flow run failed with ActionThrottled, silent exponential backoff invisible to user). At least two distinct tiers described if the scenario spans multiple tiers. |
| C-04 | **Unprotected Burst Path Identification** | correctness | essential | Output identifies at least one structurally unprotected burst path — a trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between the source and the rate-limited endpoint. A path that has throttle controls but at a higher tier does not qualify. |
| C-05 | **Retry-After Handling Gap Check** | coverage | essential | Output explicitly evaluates whether the flow or connector handles Retry-After headers (or equivalent backoff signals such as `x-ms-ratelimit-remaining`, `Retry-After-Ms`) from throttled endpoints. Missing handling must be flagged as a finding with a description of the failure mode it causes (e.g., immediate retry storm, permanent failure after N retries). |

---

### Recommended (30 points total — output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Cascading Throttle Failure Scenario** | depth | recommended | Output constructs or identifies a specific scenario where throttling at one tier triggers a second distinct throttle event at a different tier — and describes the compounding effect on throughput or error rate. Two independent limits both hit under load do not constitute a cascade; the second throttle must be causally triggered by the first. |
| C-07 | **Numeric Rate Limit Specificity** | depth | recommended | At least one rate limit is cited with a concrete numeric threshold (e.g., "600 API calls per 60 seconds per connection", "5 concurrent runs per environment per flow") rather than described only in abstract or relative terms. Estimates are acceptable if labeled as such. |
| C-08 | **Volume-to-Behavior Mapping** | format | recommended | Output includes a structured mapping — table, tiered list, or equivalent — that shows which throttle behavior activates at which request volume range, enabling a reader to determine expected system behavior for a given load without re-reading the full analysis. |

---

### Aspirational (30 points total — raise the bar once essential/recommended are stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Per-bottleneck Mitigation Prescriptions** | depth | aspirational | For each identified bottleneck or unprotected burst path, output proposes a concrete remediation specific to the component and limit type (e.g., "enable concurrency control on the For Each action capped at 5 parallel branches", "add exponential backoff with Retry-After header parsing to the HTTP action", "split batch trigger into N sequential calls with 1s delay"). Generic advice ("add retry logic") does not pass — the prescription must name the specific action, setting, or pattern. |
| C-10 | **Quantified Impact at Load Spike** | depth | aspirational | Output provides numeric estimates of degradation at a specific load multiplier (e.g., "at 5x normal volume with a 600 req/min limit, 42% of requests are queued beyond 30s, 11% fail after exhausting 3 retry attempts") using the rate limits cited in C-07 as the arithmetic basis. The estimate must be derivable from the stated limits — not asserted as a generic percentage. |
| C-11 | **Burst Gap Classification (Structural vs. Incidental)** | depth | aspirational | *R1 excellence signal: V-05 was the only variation with an explicit structural-vs-incidental sub-test, identified as the sharpest C-04 enforcement across all variations.* Beyond identifying the unprotected burst path (C-04), output explicitly classifies whether the gap is structural (no mechanism exists on this path) vs. incidental (mechanism exists but is misconfigured, bypassable, or absent only under specific conditions). Classification must be stated and justified — not merely implied by framing. Requires C-04 to pass. |
| C-12 | **Dual-state Volume Mapping (Baseline vs. Protected)** | depth | aspirational | *R1 excellence signal: V-05 produced unique dual-state volume mapping (inertia vs. protected) across volume tiers, identified as satisfying C-08 more richly than any other variation.* The volume-to-behavior mapping extends C-08 to compare two states at each volume level: the current/unprotected baseline and the mitigated/protected state. Each volume tier shows what changes when protections are applied — not just what happens at that tier in isolation. Requires C-08 to pass. |
| C-13 | **Verdict-before-Evidence Structure** | format | aspirational | *R1 excellence signal: V-04's commitment-before-evidence (VERDICT-first) structure produced the clearest binding-order statements of any variation.* Output states the binding constraint or primary gap as an explicit labeled finding — a verdict or claim — before the supporting evidence section. The pre-commitment forces an analytical position rather than narration toward a conclusion. The evidence section must then confirm or explicitly revise the verdict; evidence that drifts without revisiting the verdict does not pass. |
| C-14 | **Baseline-delta Mitigation** | depth | aspirational | *R1 excellence signal: V-05's "Improvement over inertia" column dual-enforced that mitigations move from baseline state, rejecting both generic advice and improvements that don't change the baseline condition.* Each mitigation explicitly states the before-state (baseline behavior at the bottleneck) and the after-state (system behavior with the mitigation applied). Mitigations that could apply to any system without referencing the specific baseline condition do not pass. Requires C-09 to pass. |
| C-15 | **Document-head Global Verdict** | format | aspirational | *R2 excellence signal: Both V-01 and V-02 scored PARTIAL on C-13 — V-01 placed the binding constraint label in Section 3 (after Sections 1-2 audit); V-02 placed it within a mid-document analysis section. Neither enforced a standalone verdict block before any evidence or inventory. C-13 as written permits section-local verdicts that satisfy the label requirement without anchoring the analysis at document head.* Output opens with a standalone Verdict block — appearing before any rate limit inventory, burst path audit table, or volume mapping section — that states: (a) the binding constraint by component name and numeric threshold, (b) the primary gap (e.g., unprotected burst path at a named action, or Retry-After not handled at a named connector), and (c) the current system status at the stated load (safe / degraded / failing). The Verdict block must be self-contained: a reader who reads only it knows the core finding without proceeding to the evidence. Evidence sections must confirm or explicitly revise each Verdict claim; a Verdict that no evidence section references does not pass. Requires C-01 and C-04 to pass. |
| C-16 | **Format Contract Preamble** | format | aspirational | *R2 excellence signal: V-02's axis — "format contract preamble — BASELINE / PROTECTED dual-column on every table and mitigation" — produced the strongest C-12 enforcement of either variation. Declaring the dual-column structure as a document-wide contract before sections removes per-section negotiation about whether the dual-column applies and enforces consistency across all comparative tables simultaneously. Neither V-01 nor any prior variation captured this as an explicit structural discipline.* Output includes a Format Contract section placed before the first analysis section that declares: (a) the column structure that applies to every comparative table in the document (e.g., BASELINE | PROTECTED | Delta), (b) what BASELINE and PROTECTED mean in the specific scenario context — not generic definitions, but names tied to the scenario's components or states, and (c) a rejection clause stating that tables or mitigation rows omitting the declared structure are flagged as incomplete. At least two distinct tables elsewhere in the document must comply with the declared format; a format contract with only one compliant table does not pass. Requires C-08 and C-12 to pass. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 30)
```

**Golden threshold**: all 5 essential criteria pass **AND** composite >= 95.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 95, all essential pass | Ready for golden file |
| Silver | >= 78, all essential pass | Usable, missing depth |
| Bronze | >= 60, >= 4 essential pass | Partial — gap in core coverage |
| Fail | < 60 or any essential fail | Not useful — regenerate |

---

## Evaluator Notes

*(all v1-v2 notes retained; new notes for C-15-C-16 added below)*

- **C-01 vs C-07** — C-01 requires ordering reasoning; C-07 requires a numeric threshold. Both needed for Silver.
- **C-02 causal chain** — look for explicit causal connectors: "because", "causes", "triggers", "fills the queue", "delays downstream".
- **C-04 unprotected path** — structural absence, not high headroom.
- **C-05 Retry-After** — must be explicit, must name the failure mode.
- **C-06 cascading** — directional: first throttle causes second throttle.
- **C-08 structure** — any structured form passes; prose does not.
- **C-09 vs C-04** — C-04 identifies; C-09 prescribes per-finding.
- **C-10 vs C-07** — C-10 arithmetic must trace back to the limits cited in C-07.
- **C-11 vs C-04** — C-04 identifies the gap; C-11 classifies it. C-11 cannot pass if C-04 fails.
- **C-12 vs C-08** — C-08 passes with single-state map; C-12 requires both states at every tier. C-12 cannot pass if C-08 fails.
- **C-13 format** — look for a "Finding:", "Verdict:", or "Binding constraint:" label before the evidence block; the evidence section must then reference or revise that finding.
- **C-14 vs C-09** — C-09 passes with named-parameter prescription ("set `max-concurrency=5`"). C-14 requires additionally stating what the system does at the bottleneck before that setting is applied, and what it does after. C-14 PARTIAL = C-09 PASS level. C-14 cannot pass if C-09 fails.
- **C-15 vs C-13** — C-13 passes if a labeled verdict appears anywhere before its evidence block (including mid-document). C-15 requires the verdict to be the opening section of the entire document — before any inventory, audit table, or analysis section. A response can earn C-13 without earning C-15. C-15 PARTIAL = C-13 PASS level (verdict exists but is not at document head). C-15 cannot pass if C-01 and C-04 do not pass.
- **C-16 vs C-12** — C-12 passes if the volume-to-behavior table has BASELINE and PROTECTED columns. C-16 requires that a Format Contract section precedes all analysis sections and explicitly names the column structure, scenario-specific meanings, and a rejection clause — and that at least two tables comply. A response can earn C-12 without earning C-16. C-16 cannot pass if C-08 and C-12 do not pass.

---

## What changed and why

### v2 -> v3 (R2 excellence signals)

| New ID | Source observation | Parent criterion | R2 signal |
|--------|--------------------|-----------------|-----------|
| C-15 | Both V-01 and V-02 PARTIAL on C-13: verdict appeared mid-document (V-01 Section 3; V-02 mid-analysis section) — neither enforced a global verdict at document head | C-13 | C-13 permits section-local commitment; C-15 requires doc-head commitment before any evidence |
| C-16 | V-02 axis "format contract preamble — BASELINE / PROTECTED dual-column on every table" produced strongest C-12 enforcement of any variation — declaring format as a document-wide contract before sections removes per-section negotiation | C-12 | The preamble pattern was the structural discipline behind V-02's C-12 PASS; not yet codified as a criterion |

Both new criteria are strict supersets of their parents: C-15 cannot pass if C-13's pre-conditions are not met; C-16 cannot pass if C-12's pre-conditions are not met. The scoring denominator moves from /6 to /8 with composite max unchanged at 120.

### v1 -> v2 (R1 excellence signals)

| New ID | Source observation | Parent criterion |
|--------|--------------------|-----------------|
| C-11 | V-05 C-04: "the only variation with an explicit structural-vs-incidental sub-test" | C-04 |
| C-12 | V-05 C-08: "unique dual-state mapping... satisfies C-08 more richly than any other variation" | C-08 |
| C-13 | V-04 C-01: "commitment-before-evidence structure produces the clearest binding-order statements of any variation" | C-01 |
| C-14 | V-05 C-09: "`Improvement over inertia` column — dual enforcement that rejects... improvements that don't move from baseline" | C-09 |

Each new criterion is strictly a superset of its parent — a response cannot earn the child without first satisfying the parent.

---

## v1 design decisions retained

- C-05 (Retry-After) remains Essential — explicitly called out in the skill description as a required identification target.
- C-01 is distinct from C-07: ordering reasoning can pass without a number; both needed for Silver.
- C-06 (cascading) remains Recommended — a useful analysis can identify the first bottleneck without constructing a full cascade scenario.
