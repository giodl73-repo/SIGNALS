Here is the complete updated rubric — v3.

---

## What changed

**Three new aspirational criteria, 3 points each. Max score: 109 → 118.**

### C-14 — Named Phase Gate Enforcement
*Source: V-03 GATE 1/GATE 3, V-04 role-boundary gates*

At least one named gate (GATE N or equivalent) at a phase boundary, stating an explicit prerequisite and naming what it blocks. A section heading or numbered step without a conditional prerequisite does not pass.

### C-15 — Validator Independence Assertion
*Source: V-04 ROLE 2.1 "Do not assume ROLE 1 was accurate because it was confident"*

The second validation barrier contains an explicit imperative non-deference sentence directed at the evaluating agent. A second barrier that reviews the first barrier's output without an independence instruction collapses the two-barrier structure into one.

### C-16 — Barrier Scope Inheritance Boundary
*Source: V-03 "Round 1 only covered TABLE 1; Round 2 looks for constructs introduced in TABLES 3–5"*

The second barrier explicitly names at least one construct category it covers that wasn't present during the first barrier's scope window, with the structural reason. "Review all constructs" without scope extension does not pass.

---

**Also updated in v3** (no point changes, no pass/fail disruption):

- **C-11 pass condition** — added explicit note that physical role separation is not required; confirmed by V-01's in-phase double checkpoint.
- **C-13 pass condition** — clarified that [INERTIA-SEED] and CASCADE RESOLUTION STATEMENT are equally valid mechanisms; both ends must be structurally enforced; seeding alone (V-01 pattern) does not pass.
agation Trace
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The output traces how throttling at one tier propagates upstream or downstream — showing the causal chain from the first throttled component to the caller or downstream consumer.
- **Pass condition**: Output describes at least one propagation step: what signal travels (error code, retry-after header, queue depth, etc.), which component receives it, and what that component does in response. Stating only that "backpressure occurs" without a causal chain does not pass.

### C-04 — User Experience per Throttle Tier
- **Category**: coverage
- **Weight**: essential (12)
- **Text**: The output characterizes the user-facing experience at each identified throttle tier — distinguishing between transparent retry, visible delay, error surfaced to user, and silent data loss.
- **Pass condition**: Output maps at least two distinct throttle tiers to distinct UX outcomes (not the same outcome for all tiers). Each mapping must state what the user sees or experiences, not just what the system does internally.

### C-05 — Domain Grounding in Connectors / Power Automate
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The analysis uses terminology and limits specific to the Connectors / Power Automate throughput domain — not generic API rate-limiting theory.
- **Pass condition**: Output references at least one Power Automate or connector-specific construct (e.g., Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, or Microsoft 365 service protection limits). Generic HTTP 429 descriptions without connector context do not pass.

---

## Recommended Criteria (weight: 30)

### C-06 — Unprotected Burst Path Detection
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output identifies at least one path in the flow that can emit a burst of requests without a rate-limiting guard — e.g., an Apply to Each loop with no concurrency cap, a parallel branch with unbounded fan-out, or a trigger with no debounce.
- **Pass condition**: Output names a specific flow construct or pattern that creates unprotected burst exposure and explains why it bypasses or overwhelms the rate limit. Must be specific to the scenario, not a generic warning.

### C-07 — Missing Retry-After Handling
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output identifies gaps in retry-after handling — cases where a 429 response is received but the retry-after header value is ignored, not read, or results in a fixed backoff that undershoots or overshoots the required wait.
- **Pass condition**: Output describes at least one specific location where retry-after handling is absent or incorrect, explains the consequence (hammering, premature retry, extended outage), and links it to a specific action or connector call in the scenario.

### C-08 — Cascading Throttle Failure Analysis
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output traces at least one scenario where throttling at one tier causes a second tier to also throttle — a cascade — rather than treating each limit as independent.
- **Pass condition**: Output names two components in a cascade sequence, explains the causal link (e.g., "retry storm from connector A increases call volume to service B, which then hits its own limit"), and characterizes the resulting failure mode (brownout, full stop, partial data).

---

## Aspirational Criteria — Original (weight: 10)

### C-09 — Quantified Throughput Model
- **Category**: depth
- **Weight**: aspirational (5)
- **Text**: The output provides a quantified throughput model — actual numbers, formulas, or threshold comparisons that allow the reader to determine whether a given request volume is safe, marginal, or over-limit for the scenario.
- **Pass condition**: Output includes at least one numeric threshold (requests/minute, requests/day, concurrent runs) alongside the scenario's projected volume, and states whether the scenario is safe or at risk. Qualitative-only analysis does not pass this criterion.

### C-10 — Actionable Remediation with Connector Specifics
- **Category**: behavior
- **Weight**: aspirational (5)
- **Text**: The output concludes with specific, implementable mitigations — not generic advice — that reference Power Automate or connector controls available to the developer (e.g., concurrency control settings, chunking strategies, premium entitlement upgrades, scheduled trigger spreading, or service principal pooling).
- **Pass condition**: Output provides at least two distinct remediations, each naming a specific Power Automate feature or setting (not "add retries" or "reduce load"), and explains which identified problem each remediation addresses.

---

## Aspirational Criteria — R1 Patterns (weight: 9)

These criteria capture prompt-structural excellence signals identified in Round 1. They reward outputs whose internal organization reflects the two-barrier, pre-printed-table, and inertia-seeding patterns that distinguish V-05 from all other variations.

### C-11 — Two-Barrier Domain Validation
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R1 Signal 1 — two-barrier essential enforcement
- **Text**: The output demonstrates PA domain accuracy through two independent checks — not just presence of PA terminology but contextual precision. This is evidenced when the output both (a) names exact PA constructs and (b) explicitly validates or corrects earlier construct usage at a dedicated review step.
- **Pass condition**: Output contains at least two distinct moments of PA domain validation: one where PA constructs are named in context (first barrier) and one where the accuracy of those construct names is confirmed or corrected against actual PA behavior (second barrier). The two barriers must have different scopes — the first barrier covers constructs named during initial analysis; the second barrier covers constructs introduced during propagation, cascade, or remediation analysis that the first barrier never reviewed. An output that lists PA terms once without self-verification does not pass. Physical role separation (ROLE 1 / ROLE 2) satisfies C-11 but is not required — two mandatory, per-construct, differently-scoped validation moments in a single role sequence also satisfy it. Batch confirmation ("all constructs are correct") for the second barrier does not pass; validation must be per-construct.

### C-12 — Structured Tabular Analysis within Gated Phases
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R1 Signal 2 — pre-printed tables within gated phases
- **Text**: The output organizes ordered, comparative, or enumerated analysis in tables — not prose lists — for criteria where both prose shortcuts and section omission are plausible failure modes. This combines format discipline (table columns prevent compression) with coverage discipline (all required rows present).
- **Pass condition**: Output presents at least two of the following in table form rather than prose: throttle tier ordering, backpressure hop chain, burst path enumeration, cascade sequence, or quantified risk register. Each table must have columns that structurally enforce the criterion's hardest requirement (e.g., a "Hit order" column for C-02, a "Load added" column for C-08, a "Status" column for C-09). Prose descriptions with inline numbers do not pass even if the numbers are correct.

### C-13 — Inertia-to-Cascade Causal Thread
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R1 Signal 3 — inertia framing as cross-phase cascade catalyst
- **Text**: The bottleneck statement explicitly names the naive assumption that the scenario invalidates, and this framing carries forward into the cascade analysis — creating a continuous causal thread rather than treating bottleneck identification and cascade analysis as isolated observations.
- **Pass condition**: The bottleneck statement (C-01) must name the naive assumption that fails (e.g., "the assumption that tier limits are independent fails here because..."). The cascade section (C-08) must then structurally require an explicit back-reference to that assumption — through a labeled marker ([INERTIA-SEED] back-reference or equivalent) or a required CASCADE RESOLUTION STATEMENT that names the specific naive assumption from C-01 and explains how the causal chain proves it false. C-01 seeding alone without a structurally enforced close at the cascade section does not pass — the thread must be closed at both ends. An output where the cascade implies resolution without explicitly naming the naive assumption does not pass. [INERTIA-SEED] is one valid mechanism; an explicit cascade resolution instruction referencing "the naive assumption from the bottleneck statement" is equally valid.

---

## Aspirational Criteria — R2 Patterns (weight: 9)

These criteria capture prompt-structural excellence signals identified in Round 2. All three top-scoring variations (V-03, V-04, V-05) scored 109 on the v2 rubric — these criteria raise the ceiling by rewarding the gating, independence-assertion, and scope-declaration mechanisms that distinguished their structural designs.

### C-14 — Named Phase Gate Enforcement
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R2 Signal 1 — V-03 GATE 1/GATE 3, V-04 role-boundary gate
- **Text**: The output structures its analysis around at least one named, numbered phase gate — an explicit stop-and-verify checkpoint that states a prerequisite condition and names what is blocked until that condition is met. Gates are not section headings; they are conditional go/no-go instructions that enforce phase ordering.
- **Pass condition**: At least one named gate (GATE N, CHECKPOINT N, or labeled equivalent) appears at a phase boundary, states an explicit prerequisite that must be satisfied before proceeding (e.g., "GATE 1: PA validation Round 1 must be complete before tier ordering"), and identifies the section or action it blocks. A numbered step, section heading, or "note" without a conditional prerequisite statement does not pass.

### C-15 — Validator Independence Assertion
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R2 Signal 2 — V-04 ROLE 2.1 "Do not assume ROLE 1 was accurate because it was confident"
- **Text**: The second validation barrier includes an explicit instruction to distrust the prior analysis layer — a direct command stating that the first barrier's confidence or completeness is not evidence for the second barrier. Without this instruction, a model following the prompt may defer to the first barrier's self-assessment, collapsing the two-barrier structure into one effective barrier.
- **Pass condition**: The second barrier contains at least one explicit non-deference sentence directed at the evaluating agent (e.g., "Do not assume [prior step/role] was accurate because it was confident," or "Treat [prior analysis] as unverified," or equivalent). The instruction must be imperative and specific to the prior layer — a general note about thoroughness does not pass. A second barrier that reviews the same output without an independence instruction does not pass, even if it is mandatory and per-construct.

### C-16 — Barrier Scope Inheritance Boundary
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R2 Signal 3 — V-03 "Round 1 only covered TABLE 1; Round 2 looks for constructs introduced in TABLES 3–5"
- **Text**: The second validation barrier explicitly declares which construct categories it covers that were out of scope for the first barrier, naming the structural reason first-barrier coverage was insufficient for those constructs. A second barrier that re-reviews the same construct population as the first provides redundancy, not scope extension, and does not satisfy the independence requirement of the two-barrier design.
- **Pass condition**: The second barrier names at least one construct category not present during the first barrier's scope window (e.g., "constructs introduced during cascade analysis that were not identified at tier-mapping time") and states why the first barrier could not have covered them. A second barrier defined as "review all constructs" or "check everything again" without an explicit scope extension statement does not pass.

---

## Criterion Summary

| ID   | Category    | Weight        | Points | Short Title                          |
|------|-------------|---------------|--------|--------------------------------------|
| C-01 | correctness | essential     | 12     | Bottleneck localization              |
| C-02 | correctness | essential     | 12     | Rate limit hit ordering              |
| C-03 | correctness | essential     | 12     | Backpressure propagation trace       |
| C-04 | coverage    | essential     | 12     | UX per throttle tier                 |
| C-05 | correctness | essential     | 12     | Domain grounding (Connectors/PA)     |
| C-06 | depth       | recommended   | 10     | Unprotected burst path detection     |
| C-07 | depth       | recommended   | 10     | Missing retry-after handling         |
| C-08 | depth       | recommended   | 10     | Cascading throttle failure           |
| C-09 | depth       | aspirational  | 5      | Quantified throughput model          |
| C-10 | behavior    | aspirational  | 5      | Actionable PA-specific remediation   |
| C-11 | structure   | aspirational  | 3      | Two-barrier domain validation        |
| C-12 | structure   | aspirational  | 3      | Structured tabular analysis          |
| C-13 | structure   | aspirational  | 3      | Inertia-to-cascade causal thread     |
| C-14 | structure   | aspirational  | 3      | Named phase gate enforcement         |
| C-15 | structure   | aspirational  | 3      | Validator independence assertion     |
| C-16 | structure   | aspirational  | 3      | Barrier scope inheritance boundary   |
| | | **Total** | **118** | |

---

## Scoring Examples

**Below threshold**
- All 5 essential pass, 0 recommended, 0 aspirational
- Score = 60 — does NOT meet >= 80

**Minimal pass (golden threshold)**
- All 5 essential pass, 2/3 recommended pass, 0 aspirational
- Score = 60 + 20 + 0 = 80 — exactly meets threshold

**Strong output**
- All 5 essential, all 3 recommended, 1 original aspirational
- Score = 60 + 30 + 5 = 95

**Full original sweep (V-05 R1 equivalent)**
- All 5 essential, all 3 recommended, both original aspirational
- Score = 60 + 30 + 10 = 100

**R1 pattern bonus (v2 maximum)**
- All 5 essential, all 3 recommended, both original aspirational, all 3 R1 patterns
- Score = 60 + 30 + 10 + 9 = 109

**R2 pattern bonus (v3 maximum)**
- All 5 essential, all 3 recommended, both original aspirational, all 3 R1 patterns, all 3 R2 patterns
- Score = 60 + 30 + 10 + 9 + 9 = 118

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric — 10 criteria (C-01–C-10), max score 100, golden threshold 80 |
| v2 | 2026-03-14 | Added C-11–C-13 from Round 1 excellence signals; max score 109; golden threshold unchanged |
| v3 | 2026-03-14 | Added C-14–C-16 from Round 2 excellence signals; max score 118; golden threshold unchanged. Updated C-11 pass condition: physical role separation not required, confirmed by V-01. Updated C-13 pass condition: [INERTIA-SEED] is one valid mechanism; CASCADE RESOLUTION STATEMENT is equally valid; both ends must be structurally enforced (V-01 PARTIAL confirmed seeding alone is insufficient). |
