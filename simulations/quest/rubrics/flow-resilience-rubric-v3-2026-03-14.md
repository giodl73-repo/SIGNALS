Here is the complete v3 rubric:

---

# Rubric: flow-resilience — v3

**Three new aspirational criteria added from Round 2 excellence signals:**

### C-14 — Chaos Table Co-Located Per Scenario *(E-1)*
The 4-row chaos test block (Injection / Expected behavior / Pass signal / Fail signal) must live *inside* each scenario — as rows in the same contract table or appended immediately after the scenario's classification block — not consolidated into a standalone chaos section. Co-location means the model fills rows in sequence and never makes a structural decision about whether to include a chaos block.

**Pass condition**: All three scenarios include a co-located chaos block. An output that groups all chaos tests into a single separate section fails even if C-09 passes.

### C-15 — Per-Finding Inline Observability Hook *(E-2)*
Every numbered gap finding (GAP, DCV, MRF) carries `metric= | alert= | owner=` inline, structurally adjacent to the finding entry. Not a standalone observability section — co-location with the finding means it cannot be omitted by section-collapsing.

**Pass condition**: Every finding carries all three hook fields inline. Satisfying C-10 via a standalone section but no per-finding hooks fails this criterion.

### C-16 — Completeness Checklist as Output Content *(E-3)*
The artifact contains a fill-in checklist (three checkbox lines + "Finding types present: ___ of 3") as actual output content, not merely a prompt instruction. An output with "2 of 3" is visible failure evidence in the artifact itself.

**Pass condition**: Checklist appears in output with all three boxes checked and "3 of 3" confirmed. Satisfying C-13 via headers and "do not omit" annotations but no in-artifact checklist fails.

---

**Updated scoring formula**: `aspirational_pass/8 * 10` (denominator bumped from 5 to 8).

**Under v3**: V-05 is the only Round 2 variation that scores 100 (passes C-14, C-15, C-16). V-03 and V-04 score ~98.75 (7/8 aspirational each — V-03 misses C-15/C-16, V-04 misses C-16). The ceiling opens a Round 3 target: V-03's integration approach + V-05's output checklist in a single compact structure.


### C-01 — Scenario Coverage
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers all three resilience scenario classes: (1) full connectivity loss (client offline), (2) partial failure (dependent service unavailable), and (3) concurrent writes across a partition (split-brain / eventual-consistency conflict).
- **Pass condition**: All three classes are represented by distinct named scenarios. A single scenario that attempts to cover all three classes fails. Scenarios that collapse class 2 and class 3 into a single "network issue" fail.

### C-02 — Four-Field Structure Per Scenario
- **Weight**: essential
- **Category**: structure
- **Text**: Every failure scenario includes all four required fields: (1) state — what the system state is when failure occurs; (2) capability — what the user can still do; (3) data at risk — what data may be lost, stale, or inconsistent; (4) recovery path — how the system returns to a healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with non-trivial content (not placeholder or "N/A"). A scenario missing any field fails this criterion.

### C-03 — Gap Identification
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data consistency violation, and at least one missing recovery flow as distinct findings.
- **Pass condition**: All three finding types appear, each labeled and actionable (not just implied). Generic statements like "offline support may be limited" without specificity fail.

### C-04 — Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems fundamentals: CAP theorem trade-offs, retry semantics, idempotency requirements, and conflict-resolution strategies are used correctly where referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated error codes, invented protocols, or impossible consistency guarantees fail this criterion.

### C-05 — Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure scenarios reference realistic commerce flows (e.g., checkout, inventory reservation, payment processing, order fulfillment) rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality — 30% of score)

### C-06 — Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded / impaired / down) and a blast radius (what percentage or which segment of users is affected). This helps triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a blast-radius estimate or qualifier (e.g., "affects all users in offline mode", "affects <1% under split-brain").

### C-07 — Recovery Path Specificity
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors (e.g., "client retries with exponential back-off up to 5 attempts, then surfaces manual reconcile UI"), not just outcomes (e.g., "system recovers"). Steps should include who/what initiates each action: client, server, operator, or user.
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that only describe the end state (system is back online) without mechanism fail.

### C-08 — Conflict Resolution Strategy
- **Weight**: recommended
- **Category**: coverage
- **Text**: For eventual-consistency scenarios, the output specifies what conflict resolution strategy is assumed (last-write-wins, merge, manual reconcile, reject-stale) and flags whether the strategy is adequate for the data type involved.
- **Pass condition**: At least one eventual-consistency scenario names a conflict-resolution strategy and includes a brief adequacy judgment. Scenarios that describe lag without resolution strategy fail.

---

## Aspirational Criteria (raise the bar — 10% of score)

### C-09 — Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that could be executed in a test harness: what to inject (network partition, latency spike, service kill), expected observable behavior, and pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three elements (injection, expected behavior, pass/fail signal). Vague suggestions to "test resilience" fail.

### C-10 — Observability Hooks
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals (metrics, logs, traces, alerts) that would surface each identified gap in production. Each recommendation is tied to a specific gap or scenario from the analysis.
- **Pass condition**: At least two observability recommendations are present, each linked to a named gap or scenario with a rationale for why that signal would detect the failure.

### C-11 — Named Actor Chain in Recovery Fields
- **Weight**: aspirational
- **Category**: structure
- **Text**: Recovery paths use a standard actor-chain label (`client -> server -> operator -> user`) as a structural prefix or template slot, so that actor attribution is a fill-in rather than a free-form design choice per scenario. The chain need not use all four actors, but the actors present must be drawn from the canonical set and labelled explicitly, not inferred from prose.
- **Pass condition**: At least two recovery paths use actor-chain notation (`client ->`, `server ->`, `operator ->`, or `user ->`) as explicit step labels, not just words embedded in prose sentences. Recovery paths that describe what each actor does without labelling the handoff boundary fail.
- **Excellence signal source**: V-05 Round 1 — pre-naming the actor chain in the Recovery field template produced consistent attribution across all three scenarios; instructions to "include actor labels" produced partial or inconsistent results.

### C-12 — Constrained Conflict Resolution Vocabulary
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Conflict resolution strategies are named using canonical vocabulary — `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale` — rather than free-text descriptions. Each strategy name appears as a discrete labeled choice, not paraphrased (e.g., "the most recent write wins" fails; "last-write-wins" passes).
- **Pass condition**: Every conflict-resolution strategy reference uses one of the four canonical terms. Any scenario that describes a strategy in free text without naming the canonical type fails.
- **Excellence signal source**: V-05 Round 1 — providing the constrained choice list `last-write-wins | merge | manual-reconcile | reject-stale` eliminated the free-text description failure mode that produced partial C-08 scores in V-01 and V-03.

### C-13 — Structural Gap-Merge Prevention
- **Weight**: aspirational
- **Category**: completeness
- **Text**: The gap-identification section carries an explicit completeness marker — either a labeled checklist, a "do not omit or merge" annotation, or a per-finding-type header — that signals all three required finding types (offline experience gap, data consistency violation, missing recovery flow) are present and structurally distinct. The marker must appear in the output itself, not only in the prompt instruction.
- **Pass condition**: All three finding types are visually distinct (separate headers, separate rows, or separate labeled blocks) and the output contains at least one structural signal that they are intentionally complete (e.g., a checklist with all three checked, a "3 of 3 finding types present" summary line, or a per-type header with explicit type label). A single undifferentiated "Gaps" section containing all three types fails.
- **Excellence signal source**: V-05 Round 1 — the "do not omit or merge" section instruction blocked the most common gap-section failure mode by naming it structurally, rather than relying on a section header that models routinely collapsed.

### C-14 — Chaos Table Co-Located Per Scenario *(new)*
- **Weight**: aspirational
- **Category**: structure
- **Text**: The chaos engineering test block for each scenario is co-located *within* the scenario structure — either as rows in the same table as the four-field trace, or appended immediately after the scenario's classification block — not consolidated into a standalone chaos section at the end of the output. Co-location means the model fills table rows in sequence without making a structural decision about whether to include a chaos block.
- **Pass condition**: All three scenarios include a chaos test block (satisfying C-09) and each block appears within or immediately adjacent to its parent scenario. An output that groups all chaos tests into a single separate section fails even if C-09 passes.
- **Excellence signal source**: V-03 Round 2 — placing chaos rows in the same contract table as the four-field trace eliminates section-skip risk entirely; V-01/V-04/V-05 confirmed that appending the 4-row table immediately after Classification achieves the same structural effect.

### C-15 — Per-Finding Inline Observability Hook *(new)*
- **Weight**: aspirational
- **Category**: depth
- **Text**: Every numbered gap finding (offline experience gap, data consistency violation, missing recovery flow) carries an inline observability annotation in the form `metric= | alert= | owner=`. The hook is structurally adjacent to the finding entry, not consolidated into a standalone observability section. This prevents omission by section-collapsing: if the finding exists, the hook must exist at the same structural location.
- **Pass condition**: Every finding in the gap-identification section carries all three hook fields (metric, alert, owner) inline. An output that satisfies C-10 via a standalone observability section but has no per-finding inline hooks fails this criterion.
- **Excellence signal source**: V-02/V-04/V-05 Round 2 — inline per-finding hooks cannot be omitted by collapsing the observability section, because the hook is co-located with the finding rather than in a separate section that the model can decide to abbreviate.

### C-16 — Completeness Checklist as Output Content *(new)*
- **Weight**: aspirational
- **Category**: completeness
- **Text**: The artifact contains a fill-in completeness checklist for the gap-identification section, including three checkbox lines (one per finding type: offline experience gap, data consistency violation, missing recovery flow) and a "Finding types present: ___ of 3" counter. The checklist must appear as output content — not merely as a prompt instruction or header — so that an incomplete output is self-annotating evidence of failure.
- **Pass condition**: The output contains a completeness checklist with all three boxes checked (or equivalent notation) and "Finding types present: 3 of 3" confirmed. An output that satisfies C-13 via headers and "do not omit" annotations but contains no in-artifact checklist fails. An output with "2 of 3" is a visible failure signal in the artifact itself, not just a rubric miss.
- **Excellence signal source**: V-05 Round 2 — the completeness checklist closes the gap between C-13's "marker must appear in output" requirement and full structural enforcement; V-01 through V-04 used "do not omit or merge" as a prompt instruction that produced output-level separation but no in-artifact completeness evidence.

---

## Scoring Formula

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 |
| Recommended | 30% | C-06, C-07, C-08 |
| Aspirational | 10% | C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16 |

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/8 * 10)
```

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

---

## Failure Fast-Paths

The following conditions automatically fail scoring regardless of composite score:

- Output contains no explicit failure scenarios (no structure, just prose advice)
- Output is domain-agnostic (no commerce or distributed systems grounding)
- Recovery paths are all identical or all trivially "restart the service"

---

## Key Changes from v2

| Change | Detail |
|--------|--------|
| Aspirational tier: 5 → 8 criteria | Added C-14, C-15, C-16 from Round 2 excellence signals E-1, E-2, E-3 |
| Scoring denominator | Aspirational now divides by 8, not 5 |
| C-14 source | V-03/V-04/V-05 Round 2 — chaos table inside scenario eliminates section-skip risk vs. chaos in separate section |
| C-15 source | V-02/V-04/V-05 Round 2 — per-finding inline hooks prevent C-10 omission by section-collapsing |
| C-16 source | V-05 Round 2 — in-artifact checklist makes incompleteness self-annotating; "2 of 3" is visible output failure |

All three new criteria target the same root pattern established in v2: co-location eliminates structural decisions. C-14 co-locates the chaos table with its scenario. C-15 co-locates the observability hook with its finding. C-16 makes the completeness marker live in the output, not the prompt.
