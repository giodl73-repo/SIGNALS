Done. Here is the complete updated rubric:

---

# Rubric: flow-resilience — v2
**Skill**: `/flow:resilience`
**Updated**: 2026-03-14
**Version**: v2 (Round 1 excellence signals incorporated)

---

## Structure

- **5 essential** (60%): scenario coverage (3 classes), four-field structure per scenario, gap identification (3 types), distributed systems accuracy, commerce domain grounding
- **3 recommended** (30%): severity + blast-radius classification, recovery path specificity with actor labels, conflict resolution strategy for eventual consistency
- **5 aspirational** (10%): chaos engineering test cases, observability hooks, named actor chain in Recovery field, constrained conflict-resolution vocabulary, structural gap-merge prevention markers

## Design Decisions

- C-02 is the spine — the four-field structure (state / capability / data-at-risk / recovery) is literally what the skill spec defines, so it is essential and per-scenario, not just overall.
- C-03 catches the skill's three named output targets (offline gaps, consistency violations, missing recovery flows) — all three must appear, not just one.
- **C-11 through C-13 are elevated from Round 1 excellence signals (V-05)**: structural mechanisms that shift output quality from model-designs-the-format to model-fills-a-template. No Round 1 variation fully exercised all three; they represent the next quality tier.
- Fast-paths catch the most common failure modes: pure prose output, domain-agnostic analysis, and trivial recovery paths that add no signal.

---

## Essential Criteria (gate quality — 60% of score)

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
*(unchanged from v1)*

### C-07 — Recovery Path Specificity
*(unchanged from v1)*

### C-08 — Conflict Resolution Strategy
*(unchanged from v1)*

---

## Aspirational Criteria (raise the bar — 10% of score)

### C-09 — Chaos Engineering Test Cases
*(unchanged from v1)*

### C-10 — Observability Hooks
*(unchanged from v1)*

### C-11 — Named Actor Chain in Recovery Fields *(new)*
- **Weight**: aspirational
- **Category**: structure
- **Text**: Recovery paths use a standard actor-chain label (`client -> server -> operator -> user`) as a structural prefix or template slot, so that actor attribution is a fill-in rather than a free-form design choice per scenario. The chain need not use all four actors, but the actors present must be drawn from the canonical set and labelled explicitly, not inferred from prose.
- **Pass condition**: At least two recovery paths use actor-chain notation (`client ->`, `server ->`, `operator ->`, or `user ->`) as explicit step labels, not just words embedded in prose sentences. Recovery paths that describe what each actor does without labelling the handoff boundary fail.
- **Excellence signal source**: V-05 Round 1 — pre-naming the actor chain in the Recovery field template produced consistent attribution across all three scenarios; variations that only asked the model to "include actor labels" produced partial or inconsistent results.

### C-12 — Constrained Conflict Resolution Vocabulary *(new)*
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Conflict resolution strategies are named using canonical vocabulary — `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale` — rather than free-text descriptions. Each strategy name appears as a discrete labeled choice, not paraphrased (e.g., "the most recent write wins" fails; "last-write-wins" passes).
- **Pass condition**: Every conflict-resolution strategy reference uses one of the four canonical terms. Any scenario that describes a strategy in free text without naming the canonical type fails.
- **Excellence signal source**: V-05 Round 1 — providing the constrained choice list `last-write-wins | merge | manual-reconcile | reject-stale` eliminated the free-text description failure mode that produced PARTIAL scores on C-08 in V-01 and V-03.

### C-13 — Structural Gap-Merge Prevention *(new)*
- **Weight**: aspirational
- **Category**: completeness
- **Text**: The gap-identification section carries an explicit completeness marker — either a labeled checklist, a "do not omit or merge" annotation, or a per-finding-type header — that signals all three required finding types are present and structurally distinct. The marker must appear in the output itself, not only in the prompt instruction.
- **Pass condition**: All three finding types are visually distinct (separate headers, rows, or labeled blocks) and the output contains at least one structural signal that they are intentionally complete. A single undifferentiated "Gaps" section containing all three types fails.
- **Excellence signal source**: V-05 Round 1 — the "do not omit or merge" instruction blocked the most common gap-section failure mode by naming it structurally, rather than relying on a section header that models routinely collapsed.

---

## Scoring Formula

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01 through C-05 |
| Recommended | 30% | C-06, C-07, C-08 |
| Aspirational | 10% | C-09, C-10, C-11, C-12, C-13 |

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/5 * 10)
```

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

---

## Key changes from v1

| Change | Detail |
|--------|--------|
| Aspirational tier: 2 → 5 criteria | Added C-11, C-12, C-13 from V-05 excellence signals |
| Scoring denominator | Aspirational now divides by 5, not 2 |
| C-11 source | V-05 actor chain template > "include actor labels" instruction |
| C-12 source | V-05 constrained vocab > free-text strategy description |
| C-13 source | V-05 "do not omit or merge" > section header alone |

The three new criteria all target the same root pattern: structural constraints in the prompt produce structurally reliable output; instructions alone do not.
ion strategy reference in the output uses one of
  the four canonical terms. Any scenario that describes a strategy in free text without naming
  the canonical type fails this criterion.
- **Excellence signal source**: V-05 Round 1 — providing the constrained choice list
  `last-write-wins | merge | manual-reconcile | reject-stale` eliminated the free-text
  description failure mode that produced PARTIAL scores on C-08 in V-01 and V-03.

### C-13 — Structural Gap-Merge Prevention
- **Weight**: aspirational
- **Category**: completeness
- **Text**: The gap-identification section carries an explicit completeness marker — either a
  labeled checklist, a "do not omit or merge" annotation, or a per-finding-type header — that
  signals all three required finding types (offline experience gap, data consistency violation,
  missing recovery flow) are present and structurally distinct. The marker must appear in the
  output itself, not only in the prompt instruction.
- **Pass condition**: All three finding types are visually distinct (separate headers,
  separate rows, or separate labeled blocks) and the output contains at least one structural
  signal that they are intentionally complete (e.g., a checklist with all three checked, a
  "3 of 3 finding types present" summary line, or a per-type header with explicit type label).
  A single undifferentiated "Gaps" section containing all three types fails.
- **Excellence signal source**: V-05 Round 1 — the "do not omit or merge" section instruction
  blocked the most common gap-section failure mode by naming it structurally, rather than
  relying on a section header that models routinely collapsed.

---

## Scoring Formula

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 |
| Recommended | 30% | C-06, C-07, C-08 |
| Aspirational | 10% | C-09, C-10, C-11, C-12, C-13 |

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/5 * 10)
```

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

---

## Failure Fast-Paths

The following conditions automatically fail scoring regardless of composite score:

- Output contains no explicit failure scenarios (no structure, just prose advice)
- Output is domain-agnostic (no commerce or distributed systems grounding)
- Recovery paths are all identical or all trivially "restart the service"
