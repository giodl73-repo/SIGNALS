Written to `simulations/quest/rubrics/flow-resilience-rubric-v2-2026-03-15.md`.

---

**Three new aspirational criteria added:**

**C-11 — Confidence-Annotated Discovery Catalog** (from V-04)
The DS analysis phase assigns explicit confidence ratings (high/medium/low/impossible) to each failure mode before it enters the scenario table. "Impossible" entries are excluded with rationale; low-confidence entries are flagged and resolved before table population. The discovery phase becomes independently auditable and blocks invalid scenarios upstream.

**C-12 — Nil-Finding Norm for Gap Sections** (from V-05)
Each of the three typed gap sections explicitly states when no gaps of that type were found — "No OEG-type gaps identified for this deployment pattern." Silence is not a valid nil finding. This makes the three gap sections checkable even when empty, and prevents omission from looking like scope reduction.

**C-13 — Coverage Accountability Roster** (from V-03 + V-05)
Output opens with a pre-analysis roster committing to ≥2 scenarios per degradation class before analysis begins. Unfilled slots require an explicit impossibility argument or reclassification — not silent omission. The roster is independently checkable against the final scenario list.

**Scoring rebalance:** Aspirational band redistributed to PASS=2 / PARTIAL=1 / FAIL=0 across all five criteria (C-09 through C-13). Maximum composite stays at 100.
ay be lost, stale, or inconsistent; (4)
  recovery path -- how the system returns to a healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with
  non-trivial content (not placeholder, "N/A", or a single word). A scenario missing any
  field fails this criterion entirely.

### C-03 -- Gap Identification (Three Types)
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data
  consistency violation, and at least one missing recovery flow as distinct named findings.
  These are the three explicit output targets the skill defines.
- **Pass condition**: All three finding types appear, each labeled and actionable -- not merely
  implied or bundled. Generic statements like "offline support may be limited" without
  specificity fail.

### C-04 -- Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals. CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly wherever referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated
  error codes, invented protocols, or impossible consistency guarantees (e.g., strong
  consistency with no latency cost across a partition) fail this criterion.

### C-05 -- Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure
  scenarios reference realistic commerce flows -- checkout, inventory reservation, payment
  processing, order fulfillment, cart state -- rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation
  by name. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality -- 30% of score)

### C-06 -- Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded /
  impaired / down) and a blast radius describing what fraction or segment of users is
  affected. These labels enable triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a
  blast-radius estimate or qualifier (e.g., "affects all users in offline mode", "affects
  <1% under split-brain"). Scenarios with severity but no blast radius, or vice versa, do
  not satisfy this criterion.

### C-07 -- Recovery Path Specificity with Actor Labels
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors -- not just outcomes.
  Each step names who or what initiates the action: client, server, operator, or user.
  Example: "Client retries with exponential back-off up to 5 attempts; on exhaustion,
  server surfaces a manual reconcile UI to the user."
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that
  describe only the end state ("system recovers", "data is synchronized") without
  mechanism fail.

### C-08 -- Conflict Resolution Strategy for Eventual Consistency
- **Weight**: recommended
- **Category**: coverage
- **Text**: For eventual-consistency scenarios, the output specifies what conflict resolution
  strategy is assumed (last-write-wins, merge, manual reconcile, reject-stale) and flags
  whether that strategy is adequate for the data type involved (e.g., LWW is inadequate for
  inventory counts).
- **Pass condition**: At least one eventual-consistency scenario names a conflict-resolution
  strategy and includes a brief adequacy judgment. Scenarios that describe lag or divergence
  without naming a resolution strategy fail.

---

## Aspirational Criteria (raise the bar -- 10% of score)

**Scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Max aspirational score = 10.

### C-09 -- Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that
  could be scheduled in a test harness. Each scenario specifies: (1) what to inject (network
  partition, latency spike, service kill, packet loss), (2) expected observable behavior, and
  (3) a binary pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three elements.
  Vague suggestions to "test resilience" or "add chaos testing" without specifics fail.

### C-10 -- Observability Hooks Tied to Named Gaps
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals -- metrics, logs, traces, or
  alerts -- that would surface each identified gap in production. Each recommendation is tied
  to a specific named gap or scenario from the analysis with a rationale.
- **Pass condition**: At least two observability recommendations are present, each linked to a
  named gap or scenario with a rationale for why that signal would detect the failure early.
  Generic "add monitoring" suggestions without specifics fail.

### C-11 -- Confidence-Annotated Discovery Catalog
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The distributed-systems analysis phase carries explicit confidence ratings
  (high / medium / low / impossible) for each failure mode before scenarios are committed to
  the output. Entries rated "impossible" are excluded with a brief rationale (e.g., "strong
  consistency guarantee impossible across WAN partition"). Entries rated "low confidence" or
  lacking a confirmed commerce mapping are flagged for review before they enter the scenario
  table. This triage gate prevents technically invalid scenarios from polluting the output
  and makes the discovery phase independently auditable. (Signal: V-04 -- DS Expert First +
  Scenario Table, confidence annotation as explicit review layer.)
- **Pass condition**: Every failure mode in the discovery phase carries a confidence rating;
  "impossible" entries are excluded with rationale; flagged entries are explicitly resolved
  or discarded before the scenario table is populated.
- **Partial**: Confidence ratings present on some entries but not all; or impossible entries
  excluded without rationale; or flagging present but resolution not documented.
- **Fail**: No confidence annotation on discovery-phase entries; impossible scenarios enter
  the output without challenge.

### C-12 -- Nil-Finding Norm for Gap Sections
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Each of the three typed gap sections (offline experience gaps / data consistency
  violations / missing recovery flows) includes an explicit nil finding when no gaps of that
  type are identified for the given topology or load pattern. A nil finding reads as: "No
  offline-experience gaps identified for this deployment pattern -- all critical paths
  include local-fallback state." Silence is not a valid nil finding. This norm prevents
  omission from being misread as scope reduction and makes gap sections checkable even when
  empty. (Signal: V-05 -- Table + Gate + Conversational, explicit nil-finding norm prevents
  silent omission.)
- **Pass condition**: All three gap sections are explicitly present; sections with no findings
  carry a labeled nil finding that includes a brief scope rationale explaining why the gap
  type does not apply.
- **Partial**: Some nil findings present but not all three sections covered, or nil findings
  appear without scope rationale.
- **Fail**: Missing gap sections are silently absent; reader cannot distinguish "no gaps
  found" from "gaps not analyzed."

### C-13 -- Coverage Accountability Roster
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The output opens with a pre-analysis roster that commits to minimum per-class
  coverage -- at least two scenarios per degradation class -- before scenario analysis begins.
  The roster is checkable: the reader can verify class coverage against the final scenario
  list without reading the full analysis. When a class slot cannot be filled, the output
  provides an explicit impossibility argument or reclassification -- it does not silently
  reduce coverage below the committed minimum. The challenge mechanism ("why can't you fill
  this slot?") is answered inline, not omitted. (Signal: V-03 -- Pre-Classification Gate,
  "minimum 2 per class" as a visible coverage contract; V-05 -- conversational
  accountability for unfilled slots.)
- **Pass condition**: Pre-analysis roster is present and commits to >=2 scenarios per class;
  all committed slots are filled or explicitly argued impossible / reclassified; roster is
  independently checkable against the final scenario list.
- **Partial**: Roster present but commits to fewer than 2 per class without argument; or
  roster absent but coverage gaps are argued inline rather than silently dropped.
- **Fail**: No coverage accountability mechanism; degradation-class gaps are silently absent.

---

## Scoring Formula

| Tier | Weight | Criteria | Per-criterion |
|------|--------|----------|--------------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 | PASS=12, PARTIAL=6, FAIL=0 |
| Recommended | 30% | C-06, C-07, C-08 | PASS=10, PARTIAL=5, FAIL=0 |
| Aspirational | 10% | C-09, C-10, C-11, C-12, C-13 | PASS=2, PARTIAL=1, FAIL=0 |

```
composite = sum(essential_scores)    # max 60
          + sum(recommended_scores)  # max 30
          + sum(aspirational_scores) # max 10
```

Maximum possible score: **100**

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

---

## Failure Fast-Paths

The following conditions automatically fail scoring regardless of composite score:

- Output contains no explicit failure scenarios (pure prose advice with no scenario structure)
- Output is domain-agnostic (no commerce or distributed systems grounding anywhere)
- Recovery paths are all identical or all trivially "restart the service" / "wait for recovery"
- Fewer than three degradation classes are represented (offline, partial failure, eventual consistency)

---

## Version Notes

**v2 changes from v1:**

- **C-11 (new)** -- Confidence-annotated discovery catalog: extracted from V-04 excellence
  signal. Confidence ratings (high/medium/low/impossible) on DS-phase entries create a
  triage gate before scenarios enter the output table.
- **C-12 (new)** -- Nil-finding norm: extracted from V-05 excellence signal. Explicit nil
  findings in all three gap sections prevent silent omission from masking incomplete analysis.
- **C-13 (new)** -- Coverage accountability roster: extracted from V-03 and V-05 excellence
  signals. Pre-analysis roster with minimum-per-class commitment and challenge mechanism for
  unfilled slots.
- **Aspirational scoring rebalanced**: C-09 and C-10 reduced from PASS=5 to PASS=2 to
  accommodate five aspirational criteria while keeping maximum composite score at 100.
