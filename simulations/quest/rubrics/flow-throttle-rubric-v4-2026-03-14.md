Here is the complete v4 rubric.

---

## What changed (v3 → v4)

**Four new aspirational criteria, 3 points each. Max score: 118 → 130.**

### C-17 — Pre-Barrier Independence Instruction Placement
*Source: R3 V-02 single-sentence C-15 isolation*

The non-deference sentence must appear **before** the second barrier's first evaluative output. An instruction placed inside or after barrier output was absent when the barrier opened. Pass condition: sentence in preamble/header, before any construct-by-construct output, naming the prior layer and asserting confidence-is-not-evidence. One sentence in the correct position is sufficient.

### C-18 — Structural Closure Reason for Scope Extension
*Source: R3 V-03 single-axis C-16 isolation*

The scope declaration must name the **structural reason** why the first barrier's execution window excluded those categories — not just which categories are covered. Without the closure reason, the declaration is a preference, not a structural argument. Pass condition: at least one closure reason (e.g., "introduced after the first barrier's window had closed"). Naming categories without a reason does not pass.

### C-19 — Label-Enforced Co-location Independence
*Source: R3 V-04 C-15+C-16 co-location finding*

When two independent directives occupy the same block, each must carry a **distinct named label**. Unlabeled co-location scores as one mechanism for both criteria. Labels are structurally load-bearing, not decoration. Pass condition: a single preamble can carry both C-15 and C-16 and score them independently when both are labeled (e.g., "Independence:" / "Scope extension:").

### C-20 — Gate Mechanism Prose Portability
*Source: R3 V-01 gate syntax confirmation*

A gate defined in prose satisfies C-14 when it carries all three structural elements: **(a)** name/label, **(b)** conditional prerequisite, **(c)** named block target. Format is decorative. This criterion distinguishes conditional instructions from advisory notes: advice can carry a label and recommendation without naming what it blocks.

---

**Pass condition updates** (no point changes):
- **C-14**: tabular structure and role separation not required — confirmed by V-01
- **C-15**: one sentence is the minimum sufficient mechanism — confirmed by V-02
- **C-16**: named populations + structural closure reason satisfies criterion alone — confirmed by V-03
l Criteria (weight: 60)

### C-01 — Bottleneck Localization
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The output identifies the primary throughput bottleneck in the scenario — naming the specific component, PA construct, and volume condition that causes throttling first.
- **Pass condition**: Output names a specific system component (not a generic "the API") as the bottleneck and states the request volume or rate at which it saturates. Vague statements like "the system slows down" do not pass.

### C-02 — Rate Limit Hit Ordering
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The output establishes which rate limits are hit first, second, and so on — producing a ranked sequence rather than a flat list of limits.
- **Pass condition**: Output presents at least two throttle tiers in explicit order (e.g., "connector-level at 600 req/min hits before tenant-level at 1200 req/min") and explains why that ordering holds for the scenario's request volume. An unordered list of limits does not pass.

### C-03 — Backpressure Propagation Trace
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
- **Pass condition**: At least one named gate (GATE N, CHECKPOINT N, or labeled equivalent) appears at a phase boundary, states an explicit prerequisite that must be satisfied before proceeding (e.g., "GATE 1: PA validation Round 1 must be complete before tier ordering"), and identifies the section or action it blocks. A numbered step, section heading, or "note" without a conditional prerequisite statement does not pass. Tabular structure and role separation are not required — a gate defined in prose satisfies this criterion when all three elements are present (name, conditional prerequisite, named block target); confirmed by R3 V-01 diagnostic.

### C-15 — Validator Independence Assertion
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R2 Signal 2 — V-04 ROLE 2.1 "Do not assume ROLE 1 was accurate because it was confident"
- **Text**: The second validation barrier includes an explicit instruction to distrust the prior analysis layer — a direct command stating that the first barrier's confidence or completeness is not evidence for the second barrier. Without this instruction, a model following the prompt may defer to the first barrier's self-assessment, collapsing the two-barrier structure into one effective barrier.
- **Pass condition**: The second barrier contains at least one explicit non-deference sentence directed at the evaluating agent (e.g., "Do not assume [prior step/role] was accurate because it was confident," or "Treat [prior analysis] as unverified," or equivalent). The instruction must be imperative and specific to the prior layer — a general note about thoroughness does not pass. A second barrier that reviews the same output without an independence instruction does not pass, even if it is mandatory and per-construct. One sentence is the minimum sufficient mechanism when it names the prior layer and asserts that confidence is not evidence of precision; confirmed by R3 V-02 single-sentence isolation.

### C-16 — Barrier Scope Inheritance Boundary
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R2 Signal 3 — V-03 "Round 1 only covered TABLE 1; Round 2 looks for constructs introduced in TABLES 3–5"
- **Text**: The second validation barrier explicitly declares which construct categories it covers that were out of scope for the first barrier, naming the structural reason first-barrier coverage was insufficient for those constructs. A second barrier that re-reviews the same construct population as the first provides redundancy, not scope extension, and does not satisfy the independence requirement of the two-barrier design.
- **Pass condition**: The second barrier names at least one construct category not present during the first barrier's scope window (e.g., "constructs introduced during cascade analysis that were not identified at tier-mapping time") and states why the first barrier could not have covered them. A second barrier defined as "review all constructs" or "check everything again" without an explicit scope extension statement does not pass. Naming three construct populations with a structural closure reason (e.g., "introduced after the first barrier's execution window had closed") satisfies this criterion alone; confirmed by R3 V-03 single-axis isolation.

---

## Aspirational Criteria — R3 Patterns (weight: 12)

These criteria capture prompt-structural excellence signals identified in Round 3. Four variations hit the 118/118 ceiling. These criteria raise the ceiling by rewarding the placement, closure-reason, co-location-label, and prose-portability mechanisms that the R3 isolation and combination experiments confirmed.

### C-17 — Pre-Barrier Independence Instruction Placement
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R3 Signal 1 — V-02 minimum C-15 mechanism confirmation
- **Text**: The non-deference sentence (C-15) appears in the second barrier's preamble or opening instruction — before any evaluative output from that barrier — ensuring the independence instruction is active at the moment evaluation begins. A non-deference sentence placed inside or after barrier output was absent when the barrier opened and cannot retroactively constrain the analysis already produced.
- **Pass condition**: The imperative non-deference sentence appears before any construct-by-construct or evaluative content from the second barrier (e.g., in a header, opening rule block, or pre-analysis instruction). The sentence must name the prior layer and assert that confidence is not evidence. A note appended after analysis has begun does not pass. One sentence in the correct position is sufficient; no structural redesign is required.

### C-18 — Structural Closure Reason for Scope Extension
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R3 Signal 2 — V-03 minimum C-16 mechanism confirmation
- **Text**: The second barrier's scope declaration names the structural reason why the first barrier's execution window excluded those construct categories — not just which categories are covered. Without a closure reason, the scope declaration asserts coverage preferences rather than structural necessity, and a model may choose to ignore it.
- **Pass condition**: The scope extension names at least one structural reason why first-barrier coverage of those categories was impossible (e.g., "introduced after the first barrier's execution window had closed," "not yet instantiated at tier-mapping time," "created by downstream analysis that followed first-barrier execution"). Listing construct categories without a structural closure reason does not pass. The closure reason is load-bearing: it is what distinguishes scope extension from scope preference.

### C-19 — Label-Enforced Co-location Independence
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R3 Signal 3 — V-04 C-15+C-16 co-location finding
- **Text**: When two or more independent structural directives (e.g., a validator independence assertion and a scope inheritance declaration) occupy the same section or block, each carries a distinct named label that identifies it as a separate mechanism. Unlabeled co-location produces a structurally ambiguous block — a reader or model cannot determine whether it is one mechanism or two — and the block is scored as one mechanism regardless of how much it contains.
- **Pass condition**: If C-15 and C-16 (or any two independent structural directives) appear within the same block, each must carry a distinct label (e.g., "Independence:" / "Scope extension:", or "ASSERTION:" / "SCOPE:", or any named pair that marks them as separate). Unlabeled co-location of two directives scores both as one criterion. Labels are structurally load-bearing: they are the mechanism, not decoration. A single preamble block can carry both C-15 and C-16 and score them independently when both are labeled.

### C-20 — Gate Mechanism Prose Portability
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R3 Signal 4 — V-01 gate syntax confirmation across formats
- **Text**: A named gate mechanism satisfies C-14 regardless of structural format — prose paragraphs, tabular rows, and role-labeled blocks are all valid carriers. The three structural elements (name, conditional prerequisite, block statement) are load-bearing; the format that contains them is not. This distinguishes conditional instructions from advisory notes: advice may carry a label and a recommendation without naming what is blocked.
- **Pass condition**: A gate defined entirely in prose (no table, no role label) satisfies C-14 when it carries all three elements: (a) a name or label (GATE N, CHECKPOINT, or named equivalent), (b) an explicit conditional prerequisite ("until X is complete," "if Y is not satisfied, this gate does not open"), and (c) an explicit named block target ("this gate blocks section Z," "STEP N is blocked until this condition is met"). An advisory note that recommends an action without naming a blocked target does not pass even if it carries a gate-style label. All three elements must be present; the format carrying them is unrestricted.

---

## Criterion Summary

| ID   | Category    | Weight        | Points | Short Title                              |
|------|-------------|---------------|--------|------------------------------------------|
| C-01 | correctness | essential     | 12     | Bottleneck localization                  |
| C-02 | correctness | essential     | 12     | Rate limit hit ordering                  |
| C-03 | correctness | essential     | 12     | Backpressure propagation trace           |
| C-04 | coverage    | essential     | 12     | UX per throttle tier                     |
| C-05 | correctness | essential     | 12     | Domain grounding (Connectors/PA)         |
| C-06 | depth       | recommended   | 10     | Unprotected burst path detection         |
| C-07 | depth       | recommended   | 10     | Missing retry-after handling             |
| C-08 | depth       | recommended   | 10     | Cascading throttle failure               |
| C-09 | depth       | aspirational  | 5      | Quantified throughput model              |
| C-10 | behavior    | aspirational  | 5      | Actionable PA-specific remediation       |
| C-11 | structure   | aspirational  | 3      | Two-barrier domain validation            |
| C-12 | structure   | aspirational  | 3      | Structured tabular analysis              |
| C-13 | structure   | aspirational  | 3      | Inertia-to-cascade causal thread         |
| C-14 | structure   | aspirational  | 3      | Named phase gate enforcement             |
| C-15 | structure   | aspirational  | 3      | Validator independence assertion         |
| C-16 | structure   | aspirational  | 3      | Barrier scope inheritance boundary       |
| C-17 | structure   | aspirational  | 3      | Pre-barrier independence placement       |
| C-18 | structure   | aspirational  | 3      | Structural closure reason                |
| C-19 | structure   | aspirational  | 3      | Label-enforced co-location independence  |
| C-20 | structure   | aspirational  | 3      | Gate mechanism prose portability         |
|      |             | **Total**     | **130**|                                          |

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

**R3 pattern bonus (v4 maximum)**
- All 5 essential, all 3 recommended, both original aspirational, all 3 R1 patterns, all 3 R2 patterns, all 4 R3 patterns
- Score = 60 + 30 + 10 + 9 + 9 + 12 = 130

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric — 10 criteria (C-01–C-10), max score 100, golden threshold 80 |
| v2 | 2026-03-14 | Added C-11–C-13 from Round 1 excellence signals; max score 109; golden threshold unchanged |
| v3 | 2026-03-14 | Added C-14–C-16 from Round 2 excellence signals; max score 118; golden threshold unchanged. Updated C-11 pass condition: physical role separation not required. Updated C-13 pass condition: CASCADE RESOLUTION STATEMENT is equally valid to [INERTIA-SEED]; both ends must be structurally enforced. |
| v4 | 2026-03-14 | Added C-17–C-20 from Round 3 excellence signals; max score 130; golden threshold unchanged. Updated C-14 pass condition: tabular structure and role separation not required (confirmed V-01). Updated C-15 pass condition: one sentence is minimum sufficient mechanism (confirmed V-02). Updated C-16 pass condition: named populations + structural closure reason satisfies criterion alone (confirmed V-03). |
