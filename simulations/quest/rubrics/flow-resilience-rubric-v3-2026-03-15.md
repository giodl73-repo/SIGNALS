Written to `simulations/quest/rubrics/flow-resilience-rubric-v3-2026-03-15.md`.

---

**Two new aspirational criteria added:**

**C-14 — Conflict-Resolution Adequacy as DCV Source** (from V-02 + V-04)
When conflict-resolution analysis finds a strategy that is inadequate or undefined, that judgment is fed back as a named DCV entry in the gap identification section. The two sections are bidirectionally linked — "inadequate/undefined -> DCV" is a structural requirement, not a suggestion. Conflict-resolution weaknesses that never appear in the gap tally are invisible to the reader.

**C-15 — DS-Primitive-Grounded Impossibility Arguments** (from V-03)
When a coverage roster slot cannot be filled, the impossibility argument must cite a specific DS primitive — a CAP theorem guarantee, deployment topology constraint, or synchronous consistency guarantee. "'The topic doesn't mention X' is not an impossibility argument." Topic-scope absence is not an architectural argument.

**C-11 and C-12 also strengthened:**
- C-11: Low-confidence entries are now **barred** from the scenario table (not merely flagged); each rating requires a **cited basis**, not just a label — the confidence phase is a hard gate.
- C-12: Nil findings now require a **scope rationale** explaining why the gap type doesn't apply; bare "none found" no longer satisfies.

**Scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion across all 7 aspirational criteria (C-09 through C-15). Aspirational band **capped at 10**; uncapped maximum is 14, so the cap rewards breadth while holding the composite ceiling at 100.
 the output includes all four fields with
  non-trivial content (not placeholder, "N/A", or a single word). A scenario missing any
  field fails this criterion entirely.

### C-03 — Gap Identification (Three Types)
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data
  consistency violation, and at least one missing recovery flow as distinct named findings.
  These are the three explicit output targets the skill defines.
- **Pass condition**: All three finding types appear, each labeled and actionable — not merely
  implied or bundled. Generic statements like "offline support may be limited" without
  specificity fail.

### C-04 — Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals. CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly wherever referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated
  error codes, invented protocols, or impossible consistency guarantees (e.g., strong
  consistency with no latency cost across a partition) fail this criterion.

### C-05 — Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure
  scenarios reference realistic commerce flows — checkout, inventory reservation, payment
  processing, order fulfillment, cart state — rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation
  by name. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality — 30% of score)

### C-06 — Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded /
  impaired / down) and a blast radius describing what fraction or segment of users is
  affected. These labels enable triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a
  blast-radius estimate or qualifier (e.g., "affects all users in offline mode", "affects
  <1% under split-brain"). Scenarios with severity but no blast radius, or vice versa, do
  not satisfy this criterion.

### C-07 — Recovery Path Specificity with Actor Labels
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors — not just outcomes.
  Each step names who or what initiates the action: client, server, operator, or user.
  Example: "Client retries with exponential back-off up to 5 attempts; on exhaustion,
  server surfaces a manual reconcile UI to the user."
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that
  describe only the end state ("system recovers", "data is synchronized") without
  mechanism fail.

### C-08 — Conflict Resolution Strategy for Eventual Consistency
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

## Aspirational Criteria (raise the bar — 10% of score)

**Scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Max aspirational score = 10 (capped).

### C-09 — Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that
  could be scheduled in a test harness. Each scenario specifies: (1) what to inject (network
  partition, latency spike, service kill, packet loss), (2) expected observable behavior, and
  (3) a binary pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three elements.
  Vague suggestions to "test resilience" or "add chaos testing" without specifics fail.
- **Partial**: Chaos scenario present but missing one of the three required elements.
- **Fail**: No chaos engineering content, or suggestions without runnable specifics.

### C-10 — Observability Hooks Tied to Named Gaps
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals — metrics, logs, traces, or
  alerts — that would surface each identified gap in production. Each recommendation is tied
  to a specific named gap or scenario from the analysis with a rationale.
- **Pass condition**: At least two observability recommendations are present, each linked to a
  named gap or scenario with a rationale for why that signal would detect the failure early.
  Generic "add monitoring" suggestions without specifics fail.
- **Partial**: Observability recommendations present but fewer than two are tied to named
  gaps with rationale.
- **Fail**: No observability content, or generic recommendations without gap linkage.

### C-11 — Confidence-Annotated Discovery Catalog
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The distributed-systems analysis phase carries explicit confidence ratings
  (high / medium / low / impossible) for each failure mode before scenarios are committed to
  the output. Each rating cites its basis — an architecture constraint or DS theory reference
  — not just a label. Entries rated "impossible" are excluded from the scenario table but
  retained in the discovery phase with their rationale. Entries rated "low confidence" are
  barred from the scenario table until the confidence basis is resolved; flagging alone does
  not satisfy this gate. This triage gate prevents technically invalid scenarios from
  polluting the output and makes the discovery phase independently auditable. (Signal: V-01,
  V-04.)
- **Pass condition**: Every failure mode in the discovery phase carries a confidence rating
  with a cited basis; "impossible" entries are excluded from the table with retained rationale;
  "low confidence" entries are barred from the table until resolved — not merely flagged.
- **Partial**: Confidence ratings present on some entries but not all; or impossible entries
  excluded without cited basis; or low-confidence entries flagged but not gated.
- **Fail**: No confidence annotation on discovery-phase entries; impossible scenarios enter
  the output without challenge.

### C-12 — Nil-Finding Norm for Gap Sections
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Each of the three typed gap sections (offline experience gaps / data consistency
  violations / missing recovery flows) includes an explicit nil finding when no gaps of that
  type are identified for the given topology or load pattern. A nil finding reads as: "No
  offline-experience gaps identified for this deployment pattern — all critical paths include
  local-fallback state." The nil finding includes a scope rationale explaining why the gap
  type does not apply; a bare "none found" statement does not satisfy this criterion. Silence
  is not a valid nil finding. (Signal: V-01, V-02, V-03.)
- **Pass condition**: All three gap sections are explicitly present; sections with no findings
  carry a labeled nil finding that includes a brief scope rationale explaining why the gap
  type does not apply for this deployment pattern.
- **Partial**: Some nil findings present but not all three sections covered, or nil findings
  appear without scope rationale (bare "none found" statement).
- **Fail**: Missing gap sections are silently absent; reader cannot distinguish "no gaps
  found" from "gaps not analyzed."

### C-13 — Coverage Accountability Roster
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The output opens with a pre-analysis roster that commits to minimum per-class
  coverage — at least two scenarios per degradation class — before scenario analysis begins.
  The roster is checkable: the reader can verify class coverage against the final scenario
  list without reading the full analysis. When a class slot cannot be filled, the output
  provides an explicit impossibility argument or reclassification — it does not silently
  reduce coverage below the committed minimum. The challenge mechanism ("why can't you fill
  this slot?") is answered inline, not omitted. (Signal: V-03, V-05.)
- **Pass condition**: Pre-analysis roster is present and commits to >=2 scenarios per class;
  all committed slots are filled or explicitly argued impossible / reclassified; roster is
  independently checkable against the final scenario list.
- **Partial**: Roster present but commits to fewer than 2 per class without argument; or
  roster absent but coverage gaps are argued inline rather than silently dropped.
- **Fail**: No coverage accountability mechanism; degradation-class gaps are silently absent.

### C-14 — Conflict-Resolution Adequacy as DCV Source
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When conflict-resolution analysis judges a strategy to be inadequate or undefined
  for a given data type, that judgment is explicitly fed back into the data-consistency-
  violation (DCV) gap section as a named DCV finding. The conflict-resolution section and the
  gap identification section are bidirectionally linked — an inadequate or undefined strategy
  is always a DCV, not a standalone note. This prevents conflict-resolution weaknesses from
  being isolated in one section and invisible to the gap tally. (Signal: V-02, V-04 —
  "inadequate/undefined -> DCV" pattern.)
- **Pass condition**: At least one conflict-resolution adequacy judgment of "inadequate" or
  "undefined" generates an explicit, named DCV entry in the gap identification section. The
  linkage is visible: the DCV entry references the conflict-resolution finding that produced it.
- **Partial**: Inadequate strategies are noted in conflict-resolution analysis but not linked
  to a named DCV finding in the gap section; or a DCV entry is present without tracing back
  to its conflict-resolution source.
- **Fail**: Conflict-resolution analysis and gap sections are independent silos with no
  cross-referencing; inadequate strategies do not produce DCV entries.

### C-15 — DS-Primitive-Grounded Impossibility Arguments
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a coverage slot in the accountability roster cannot be filled, the
  impossibility argument cites a specific distributed systems primitive — a named CAP theorem
  guarantee, a deployment topology constraint, or a synchronous consistency guarantee that
  forecloses the failure class. Topic-scope arguments ("the topic doesn't mention caching",
  "the system description is too simple for this class") are not valid impossibility
  arguments. The argument must address the architecture, not the description. (Signal: V-03 —
  "'The topic doesn't mention X' is not an impossibility argument.")
- **Pass condition**: Every impossibility argument in the coverage roster cites a specific DS
  primitive with an architecture basis. No topic-scope arguments are present; any argument
  that invokes description absence rather than architecture constraint fails this criterion.
- **Partial**: Some impossibility arguments cite DS primitives; others rely on topic scope or
  description absence.
- **Fail**: Impossibility arguments rely solely on topic scope or description absence; no DS
  primitive is cited; or the challenge mechanism is absent entirely.

---

## Scoring Formula

| Tier | Weight | Criteria | Per-criterion |
|------|--------|----------|--------------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 | PASS=12, PARTIAL=6, FAIL=0 |
| Recommended | 30% | C-06, C-07, C-08 | PASS=10, PARTIAL=5, FAIL=0 |
| Aspirational | 10% | C-09 through C-15 | PASS=2, PARTIAL=1, FAIL=0 |

```
composite = sum(essential_scores)          # max 60
          + sum(recommended_scores)        # max 30
          + min(sum(aspirational_scores), 10)  # max 10 (capped)
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

**v3 changes from v2:**

- **C-14 (new)** — Conflict-resolution adequacy as DCV source: extracted from V-02 and V-04
  Round 2 excellence signals. An "inadequate/undefined" conflict-resolution judgment must
  produce a named DCV entry in the gap section — the two sections are bidirectionally linked,
  not independent silos.
- **C-15 (new)** — DS-primitive-grounded impossibility arguments: extracted from V-03 Round 2
  excellence signal. "'The topic doesn't mention X' is not an impossibility argument" — the
  impossibility argument must cite a CAP guarantee, deployment topology, or synchronous
  consistency guarantee, not topic-scope absence.
- **C-11 strengthened** — Low-confidence entries are now explicitly barred from the scenario
  table until resolved (not merely flagged). Confidence ratings now require a cited basis
  (architecture constraint or DS theory reference), not just a label. Reflects V-01 signal
  that the confidence phase is a hard gate, not an annotation layer.
- **C-12 strengthened** — Nil findings now require a scope rationale explaining why the gap
  type does not apply; a bare "none found" statement is no longer sufficient. Reflects
  V-01/V-02 signal that the nil finding must be independently verifiable.
- **Aspirational scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Aspirational band capped
  at 10. With 7 aspirational criteria the uncapped maximum is 14; the cap ensures the overall
  composite stays at 100 while rewarding incremental aspirational coverage.

**v2 changes from v1:**

- **C-11 (added)** — Confidence-annotated discovery catalog: extracted from V-04 excellence
  signal. Confidence ratings (high/medium/low/impossible) on DS-phase entries create a
  triage gate before scenarios enter the output table.
- **C-12 (added)** — Nil-finding norm: extracted from V-05 excellence signal. Explicit nil
  findings in all three gap sections prevent silent omission from masking incomplete analysis.
- **C-13 (added)** — Coverage accountability roster: extracted from V-03 and V-05 excellence
  signals. Pre-analysis roster with minimum-per-class commitment and challenge mechanism for
  unfilled slots.
- **Aspirational scoring rebalanced**: C-09 and C-10 reduced from PASS=5 to PASS=2 to
  accommodate five aspirational criteria while keeping maximum composite score at 100.
