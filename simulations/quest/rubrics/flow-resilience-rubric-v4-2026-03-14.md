# Rubric: flow-resilience — v4

**Four new aspirational criteria added from Round 3 excellence signals:**

### C-17 — Unified Sequential Row Index Across Scenario Table *(E-4)*
The single contract table uses a continuous sequential row index (e.g., rows 1–10) with no sub-table boundaries, section breaks, or re-indexing between trace rows and chaos rows. The model fills the table in one pass and never makes a structural decision about whether to include chaos rows — they are simply the next rows in the sequence.

**Pass condition**: All scenario tables use a single unbroken row-index sequence with chaos rows numbered sequentially after trace rows. Any output that restarts row numbering, introduces a sub-table header, or places a section boundary between trace rows and chaos rows fails — even if every row is present.

### C-18 — Phase-Gate Sequencing as Structural Constraint *(E-5)*
The prompt architecture includes named phase gates (e.g., "Phase 2 Gate", "Phase 3 Gate") that are explicit stop conditions the model must satisfy before advancing. Gap identification and checklist completion are mandatory gate stops, not compliance annotations — this converts C-15 and C-16 from instructions the model may ignore into sequencing constraints the model cannot bypass.

**Pass condition**: At least two named phase gates appear with explicit advance conditions. An output built on "do not omit" language without gate sequencing fails this criterion even if C-15 and C-16 pass.

### C-19 — Slot-Level Imperative Commands Per Row *(E-6)*
Each fill point in the scenario table carries a co-located imperative command at slot granularity (e.g., "Write row 7 now. Do not advance to Scenario 2 until row 10 is filled."). This provides per-row omission prevention that operates below the level of section-level or table-level co-location instructions.

**Pass condition**: At least the first chaos row and the last chaos row per scenario carry slot-level imperative commands. An output that relies solely on table-level or section-level instructions without slot-level imperatives fails — section-level co-location alone does not satisfy this criterion.

### C-20 — Role-Ownership Column Without Section Separation *(E-7)*
Multi-role contribution is expressed as a column in the unified table (e.g., "Owned by: SME / Chaos Eng") rather than as separate document sections or role-sequence narrative blocks. Column-level accountability preserves the single-table structure while keeping multi-role contribution structurally traceable with no section-skip risk.

**Pass condition**: The unified table includes an "Owned by" or equivalent ownership column assigning each row to a named role. An output that achieves multi-role contribution via separate narrative sections or a role-sequence ordering fails this criterion even if it otherwise passes C-14.

---

**Updated scoring formula**: `aspirational_pass/12 * 10` (denominator bumped from 8 to 12).

**Under v4**: All five R3 variations score 100 under v3. Under v4 only variations that implement unified row indexing (C-17), phase-gate sequencing (C-18), slot-level imperatives (C-19), and column-based role ownership (C-20) simultaneously will reach the ceiling. V-01 passes C-17 but not C-18/C-19/C-20. V-03 passes C-18 but not C-17/C-19/C-20. V-04 passes C-20 but not C-17/C-18/C-19. No single R3 variation satisfies all four new criteria — the ceiling is open for Round 4.

---

## Essential Criteria (must pass all — 60% of score)

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
- **Pass condition**: At least one conflict resolution strategy is named and assessed for adequacy. Outputs that acknowledge conflicts exist without naming a resolution strategy fail.

---

## Aspirational Criteria (structural excellence — 10% of score)

### C-09 — Chaos Test Cases Per Scenario *(A-1)*
Each failure scenario includes a co-located chaos test block covering: (1) chaos injection method, (2) expected system behavior, (3) pass signal, (4) fail signal.

**Pass condition**: All three scenarios include a chaos test block. An output that consolidates all chaos tests into a standalone section fails even if chaos content is present.

### C-10 — Observability Hooks *(A-2)*
The output includes observability hooks (metric, alert, owner) for each gap finding. Hooks must be structurally adjacent to findings, not consolidated into a standalone observability section.

**Pass condition**: All gap findings carry observability hooks. A standalone observability section without per-finding hooks fails.

### C-11 — Named Actor Chain in Recovery *(A-3)*
Recovery paths use named actor notation identifying who initiates each step: client, server, operator, or user. The actor label precedes each step.

**Pass condition**: At least two recovery paths use named actor notation throughout. Recovery paths that only name actors in the final step fail.

### C-12 — Constrained Conflict Vocabulary *(A-4)*
Conflict resolution strategy selection uses a controlled vocabulary (last-write-wins / merge / manual-reconcile / reject-stale) with an explicit adequacy assessment. The model selects exactly one term; paraphrasing is not permitted.

**Pass condition**: Exactly one controlled-vocabulary term is selected per conflict scenario with an adequacy flag. Paraphrased or invented strategy names fail.

### C-13 — Structural Gap-Merge Prevention *(A-5)*
The gap findings section is structurally protected from being merged into or collapsed with scenario content. Structural markers (e.g., mandatory section headers, "do not omit or merge" annotations) prevent model-side consolidation.

**Pass condition**: The gap findings section carries structural protection annotations. An output where gap findings and scenario content are interspersed or merged fails.

### C-14 — Chaos Table Co-Located Per Scenario *(E-1)*
The 4-row chaos test block (Injection / Expected behavior / Pass signal / Fail signal) must live *inside* each scenario — as rows in the same contract table or appended immediately after the scenario's classification block — not consolidated into a standalone chaos section. Co-location means the model fills rows in sequence and never makes a structural decision about whether to include a chaos block.

**Pass condition**: All three scenarios include a co-located chaos block. An output that groups all chaos tests into a single separate section fails even if C-09 passes.

### C-15 — Per-Finding Inline Observability Hook *(E-2)*
Every numbered gap finding (GAP, DCV, MRF) carries `metric= | alert= | owner=` inline, structurally adjacent to the finding entry. Not a standalone observability section — co-location with the finding means it cannot be omitted by section-collapsing.

**Pass condition**: Every finding carries all three hook fields inline. Satisfying C-10 via a standalone section but no per-finding hooks fails this criterion.

### C-16 — Completeness Checklist as Output Content *(E-3)*
The artifact contains a fill-in checklist (three checkbox lines + "Finding types present: ___ of 3") as actual output content, not merely a prompt instruction. An output with "2 of 3" is visible failure evidence in the artifact itself.

**Pass condition**: Checklist appears in output with all three boxes checked and "3 of 3" confirmed. Satisfying C-13 via headers and "do not omit" annotations but no in-artifact checklist fails.

### C-17 — Unified Sequential Row Index Across Scenario Table *(E-4)*
The single contract table uses a continuous sequential row index (e.g., rows 1–10) with no sub-table boundaries, section breaks, or re-indexing between trace rows and chaos rows. The model fills the table in one pass and never makes a structural decision about whether to include chaos rows.

**Pass condition**: All scenario tables use a single unbroken row-index sequence with chaos rows numbered sequentially after trace rows. Any output that restarts row numbering, introduces a sub-table header, or places a section boundary between trace rows and chaos rows fails — even if every row is present.

### C-18 — Phase-Gate Sequencing as Structural Constraint *(E-5)*
The prompt architecture includes named phase gates (e.g., "Phase 2 Gate", "Phase 3 Gate") that are explicit stop conditions the model must satisfy before advancing. Gap identification and checklist completion are mandatory gate stops, not compliance annotations — converting C-15 and C-16 from instructions into sequencing constraints the model cannot bypass.

**Pass condition**: At least two named phase gates appear with explicit advance conditions. An output built on "do not omit" language without gate sequencing fails even if C-15 and C-16 pass.

### C-19 — Slot-Level Imperative Commands Per Row *(E-6)*
Each fill point in the scenario table carries a co-located imperative command at slot granularity (e.g., "Write row 7 now. Do not advance to Scenario 2 until row 10 is filled."). This provides per-row omission prevention that operates below the level of section-level or table-level co-location instructions.

**Pass condition**: At least the first chaos row and the last chaos row per scenario carry slot-level imperative commands. An output that relies solely on table-level or section-level instructions without slot-level imperatives fails.

### C-20 — Role-Ownership Column Without Section Separation *(E-7)*
Multi-role contribution is expressed as a column in the unified table (e.g., "Owned by: SME / Chaos Eng") rather than as separate document sections or role-sequence narrative blocks. Column-level accountability preserves the single-table structure while keeping multi-role contribution traceable with no section-skip risk.

**Pass condition**: The unified table includes an "Owned by" or equivalent ownership column assigning each row to a named role. An output that achieves multi-role contribution via separate narrative sections or role-sequence ordering fails even if it otherwise passes C-14.

---

## Scoring Formula

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/12 * 10)
```

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 to C-05 | 60% |
| Recommended | C-06 to C-08 | 30% |
| Aspirational | C-09 to C-20 | 10% |

**Ceiling under v4**: A variation must pass all 12 aspirational criteria simultaneously to score 100. No R3 variation achieves this — the ceiling is open for Round 4.
