# campaign-validate Rubric v4 — 5 Prompt Variations

---

## V-01 — Single axis: Role sequence
**Axis:** Run listen-adoption first (adoption framing before design critique)
**Hypothesis:** Surfacing adoption curve barriers before design review forces design findings to be expressed in adoption terms rather than retrofitted. C-02 (ranked by adoption impact) and C-14 (listen-feedback vs listen-adoption categorical separation) become natural outputs, not deliberate additions.

---

```
You are running the campaign-validate skill for topic: {topic}

Your job: run a full design validation campaign and produce a validation brief ranked by adoption impact. Orchestrate the five sub-skills below in the exact order given. Each sub-skill produces a named findings block. After all five run, synthesize into a single brief.

---

## Phase order

Run sub-skills in this sequence — adoption-first so design findings are framed against barriers, not added after:

1. listen-adoption
2. listen-feedback
3. review-users
4. review-customers
5. review-design

---

## Sub-skill instructions

### 1. listen-adoption
Simulate the adoption lifecycle for {topic}. Apply the Rogers diffusion curve. For each of the five segments (Innovators, Early Adopters, Early Majority, Late Majority, Laggards):
- State the adoption readiness: is this segment likely to adopt, resist, or defer?
- Identify the adoption barrier or enabler that governs this segment's decision
- Estimate the segment size as a rough % of the total addressable user base
- Name the status-quo workaround this segment uses today (what they do instead of {topic})
- Estimate switching cost: how much friction does abandoning the workaround require?

Output a labeled section: **listen-adoption findings**

### 2. listen-feedback
Simulate the support and feedback signal for {topic} at 90 days post-ship. Consider:
- What support tickets would be opened in the first 30 days?
- What feature requests would surface in weeks 4-12?
- What negative reviews would appear in public channels?
- Which of these signals would indicate a design flaw vs a documentation gap vs a scope mismatch?

Separate listen-feedback findings from listen-adoption findings. Do not merge these two sections. listen-feedback is retrospective (what would be said after ship). listen-adoption is predictive (who would adopt and why).

Output a labeled section: **listen-feedback findings**

### 3. review-users
Conduct a user experience review of the {topic} design. Focus on:
- Workflow integration: does this fit into the user's existing flow without a context switch?
- Learnability: can a new user produce a correct output on first attempt?
- Error recovery: when the user makes the most common mistake, what happens?
- Edge case coverage: are the 3 most likely non-happy-path scenarios handled?

Score each finding: P1 (blocks usage), P2 (degrades usage), P3 (polish item).

Output a labeled section: **review-users findings**

### 4. review-customers
Conduct a customer success review. Focus on:
- Will customers perceive this feature as solving the problem they reported?
- What is the risk that customers adopt the feature but do not achieve the promised outcome?
- Which customer segment has the shortest path from discovery to value?
- What competitive alternative are customers currently using for this need?

Output a labeled section: **review-customers findings**

### 5. review-design
Conduct a design coherence review. Focus on:
- Does the design solve the problem stated in the spec?
- Are there internal contradictions (two parts of the design that conflict)?
- Does the design handle the failure cases identified in review-users?
- Would a senior contributor approve this design as-is, or require a revision round?

Explicitly call out any design finding that was predicted by the listen-adoption or listen-feedback analysis. These cross-validated findings carry higher confidence.

Output a labeled section: **review-design findings**

---

## Synthesis instructions

After all five sub-skill sections are complete, produce a **Validation Brief** with the following structure:

### Ranked findings (by adoption impact)

Rank ALL findings across all five sub-skills by adoption impact, not severity. A finding that blocks the Early Majority outranks a P1 design flaw that affects only Innovators. Use this format per row:

| Rank | Finding | Source sub-skill | Severity | Adoption Impact | Segment Affected (~N%) | Status-Quo Workaround | Switching Cost |
|------|---------|-----------------|----------|-----------------|------------------------|----------------------|----------------|

### Cross-signal synthesis

Identify at least one pattern that appears across 2 or more sub-skills. Name the sub-skills involved. Explain why convergence here raises confidence. Do not write this section as a summary — it must identify a relationship not visible in any single sub-skill output.

### Go / No-go verdict

State the verdict: **GO**, **NO-GO**, or **CONDITIONAL GO (condition: [specific condition])**.

Rules:
- GO: no P1 finding blocks the Early Majority
- NO-GO: at least one P1 finding would prevent Early Majority adoption
- CONDITIONAL GO: P1 findings exist but have defined remediation paths; name the condition explicitly

If NO-GO or CONDITIONAL GO, attribute the top 3 blockers to their source sub-skill.

### Artifact

Write the complete validation brief to: `simulations/{topic}/validate-{date}.md`

Confirm with: `Artifact written: simulations/{topic}/validate-{date}.md`
```

---

## V-02 — Single axis: Output format
**Axis:** Table skeleton with pre-declared rows as completeness gate
**Hypothesis:** Prescribing every required table upfront with named rows (Rogers segments in Table 5, all sub-skills in the findings table) makes missing content a visible blank rather than absent prose. C-11, C-15, C-17, C-18, C-19 pass by construction from the skeleton alone.

---

```
You are running the campaign-validate skill for topic: {topic}

Produce a validation brief for {topic}. The brief must be populated by running all five sub-skills. The output format is strictly table-driven. Every table is pre-declared below — your job is to fill in the cells, not to design the schema.

---

## Required output tables

Populate every table in order. Do not skip tables. Do not remove rows. A blank mandatory row indicates a gap in the analysis — leave it visibly blank rather than omitting it.

---

### Table 1 — Sub-skill findings index (fill one row per sub-skill, all five required)

| Sub-skill | Finding count | Highest severity | Primary adoption barrier surfaced | Cross-signal match |
|-----------|--------------|-----------------|----------------------------------|-------------------|
| review-design | | | | |
| review-users | | | | |
| review-customers | | | | |
| listen-feedback | | | | |
| listen-adoption | | | | |

---

### Table 2 — All findings ranked by adoption impact

One row per finding. Rank 1 = highest adoption impact. Severity column is informational — it does not govern rank.

| Rank | Finding summary | Source sub-skill | Severity (P1/P2/P3) | Adoption Impact | Segment blocked (~N%) | Status-Quo Workaround | Switching Cost |
|------|----------------|-----------------|--------------------|-----------------|-----------------------|----------------------|----------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| ... | | | | | | | |

Required columns:
- **Status-Quo Workaround**: what does this segment do today instead of {topic}? Required for every row — not just P1s.
- **Switching Cost**: how much effort does abandoning the workaround require? Use: Low / Medium / High / Blocking.

---

### Table 3 — P1 blockers with remediation paths (fill only if P1s exist)

| Blocker | Source sub-skill | Remediation path | Owner | Unblocks segment (~N%) |
|---------|-----------------|-----------------|-------|------------------------|
| | | | | |

---

### Table 4 — Cross-signal synthesis

| Pattern | Sub-skills involved | Why convergence raises confidence | Adoption implication |
|---------|--------------------|----------------------------------|---------------------|

Minimum 1 row required. Concatenation of findings fails — each row must name a relationship not visible in either sub-skill alone.

---

### Table 5 — Adoption curve by Rogers segment (all five rows required)

| Segment | ~% of base | Adoption readiness | Primary barrier | Status-Quo Workaround | Switching Cost | Adoption prediction |
|---------|-----------|-------------------|-----------------|----------------------|----------------|---------------------|
| Innovators | | | | | | |
| Early Adopters | | | | | | |
| Early Majority | | | | | | |
| Late Majority | | | | | | |
| Laggards | | | | | | |

Required columns:
- **Status-Quo Workaround**: what does this segment use today? Required for every segment row.
- **Switching Cost**: Low / Medium / High / Blocking.
- **Adoption prediction**: Will adopt / Will defer / Will resist / Will not reach.

---

### Table 6 — Go / No-go verdict

| Verdict | Condition (if conditional) | Blocking segments | Top 3 blockers (if no-go) |
|---------|--------------------------|------------------|--------------------------|
| | | | |

Verdict must be one of: GO / NO-GO / CONDITIONAL GO. If CONDITIONAL GO, the condition cell must be specific and actionable — "needs more work" fails.

---

## Sub-skill execution instructions

For each sub-skill, produce the findings needed to populate the tables above. Run them in this order:

1. **review-design** — design coherence, internal contradictions, spec coverage
2. **review-users** — workflow fit, learnability, error recovery, P1/P2/P3 scoring
3. **review-customers** — customer-perceived value, outcome risk, competitive alternative
4. **listen-feedback** — 90-day post-ship support ticket and review signal prediction
5. **listen-adoption** — Rogers curve analysis, segment-by-segment adoption/resistance prediction

listen-feedback and listen-adoption are categorically different:
- listen-feedback = what users say after they have used the feature (retrospective)
- listen-adoption = whether users will adopt the feature at all, and why (predictive)

Do not merge findings from these two sub-skills into a single block.

---

## Completion checklist

Before writing the artifact, verify:
- [ ] All 5 rows in Table 1 are filled
- [ ] Table 2 has at least one row per sub-skill
- [ ] Table 5 has all 5 Rogers segment rows populated (no blanks in required columns)
- [ ] Table 4 has at least 1 cross-signal row
- [ ] Table 6 has an unambiguous verdict

Write output to: `simulations/{topic}/validate-{date}.md`

Confirm with: `Artifact written: simulations/{topic}/validate-{date}.md`
```

---

## V-03 — Single axis: Inertia framing
**Axis:** Status-quo competitor named and foregrounded in every sub-skill section
**Hypothesis:** Requiring each sub-skill to open with "What does the user do today instead of {topic}?" before producing findings makes switching cost analysis structural rather than optional. C-16 (status-quo workaround per blocker) and C-18 (switching cost as required column) emerge naturally.

---

```
You are running the campaign-validate skill for topic: {topic}

Core assumption: every user you are evaluating already has a solution to the problem {topic} solves. It may be a workaround, a competing tool, a manual process, or learned helplessness. Your job is not just to evaluate {topic} — it is to evaluate whether {topic} is better enough than what users do today to justify switching.

Run all five sub-skills. For each sub-skill, identify the status-quo behavior before evaluating the design. The status quo is the real competitor.

---

## Sub-skill execution

### review-design

Before reviewing the design, state: **What does the design assume the user is currently doing?** Name the implicit status-quo behavior.

Then conduct the design review:
- Does the design account for users who are deeply habituated to the status-quo behavior?
- Are there friction points where the new design forces a behavior change?
- Does the design offer a migration path from the status-quo, or does it require cold-switch?
- Score each finding: P1 / P2 / P3

Label this section: **review-design findings**

### review-users

Before reviewing the user experience, state: **What is the user's current workflow step that {topic} replaces or augments?**

Then conduct the UX review:
- Workflow integration: does {topic} fit into the existing step, or require the user to leave their current tool?
- Learnability: how much does the user need to unlearn before they can use {topic} correctly?
- Error recovery: when the user applies their status-quo mental model to {topic}, what breaks?
- Score each finding: P1 / P2 / P3

Label this section: **review-users findings**

### review-customers

Before reviewing customer value, state: **What do customers currently buy, use, or cobble together to solve this problem?** Name the most common substitutes (product, process, or workaround).

Then assess:
- Will customers perceive {topic} as superior to their current solution, or merely different?
- What is the switching cost from their current solution to {topic} (effort, retraining, migration)?
- Which customer segment has the lowest switching cost and therefore the fastest time-to-adoption?
- What would a customer need to see in a demo to decide to abandon their current solution?

Label this section: **review-customers findings**

### listen-feedback

listen-feedback is categorically different from listen-adoption. This section asks: if users adopt {topic}, what do they say about it 90 days later?

Before predicting feedback, state: **What status-quo behaviors will users try to replicate in {topic} that it does not support?** These are the gaps that produce the highest-volume support tickets.

Then predict:
- Top 3 support ticket types in the first 30 days
- Top 2 feature requests in weeks 4-12 (often: "can it also do what my old tool did?")
- Negative review themes in public channels
- Which feedback indicates a design flaw vs a documentation gap vs a scope mismatch

Label this section: **listen-feedback findings**

### listen-adoption

listen-adoption asks whether users will adopt {topic} at all, given what they do today.

Apply the Rogers diffusion curve. For each segment, the question is not "do they like {topic}?" but "is {topic} better enough than their current behavior to justify the switch?"

For each segment:

**Innovators (~2.5%):**
- Current behavior: [what do innovators do today for this problem?]
- Switching cost: [how hard is it to switch from that behavior to {topic}?]
- Adoption prediction: Will adopt / Will defer / Will resist
- Barrier or enabler: [primary factor]

**Early Adopters (~13.5%):**
- Current behavior: [what do early adopters use today?]
- Switching cost: [Low / Medium / High / Blocking]
- Adoption prediction: Will adopt / Will defer / Will resist
- Barrier or enabler: [primary factor]

**Early Majority (~34%):**
- Current behavior: [most common status-quo behavior for this segment]
- Switching cost: [Low / Medium / High / Blocking]
- Adoption prediction: Will adopt / Will defer / Will resist
- Barrier or enabler: [primary factor]

**Late Majority (~34%):**
- Current behavior: [what does this segment do instead?]
- Switching cost: [Low / Medium / High / Blocking]
- Adoption prediction: Will adopt / Will defer / Will resist
- Barrier or enabler: [primary factor]

**Laggards (~16%):**
- Current behavior: [what is the deeply entrenched workaround?]
- Switching cost: [Low / Medium / High / Blocking]
- Adoption prediction: Will adopt / Will defer / Will resist
- Barrier or enabler: [primary factor]

Label this section: **listen-adoption findings**

---

## Synthesis

### Ranked findings — by adoption impact

Rank all findings from all five sub-skills. Rank 1 = the finding that most blocks adoption by volume-weighted segment. Include the status-quo behavior and switching cost for every finding.

| Rank | Finding | Source | Severity | Adoption Impact | Segment (~N%) | Status-Quo Workaround | Switching Cost |
|------|---------|--------|----------|-----------------|---------------|-----------------------|----------------|

### Cross-signal inertia pattern

Identify where the same status-quo behavior shows up across 2+ sub-skills. This convergence indicates deep inertia — the user's attachment to the current behavior is load-bearing, not incidental. Name the behavior and the sub-skills that confirm it.

### Go / No-go verdict

Is {topic} better enough than the status quo to win adoption from the Early Majority?

State: **GO**, **NO-GO**, or **CONDITIONAL GO (condition: [specific switching-cost reduction required])**

If NO-GO or CONDITIONAL GO, name the top 3 blockers and their source sub-skills.

---

Write output to: `simulations/{topic}/validate-{date}.md`

Confirm with: `Artifact written: simulations/{topic}/validate-{date}.md`
```

---

## V-04 — Combined: Role sequence + Lifecycle emphasis
**Axes:** Listener-first sequence (adoption → feedback → users → customers → design) + explicit phase handoffs with stated inputs per phase
**Hypothesis:** Treating the campaign as a pipeline where each phase's output is the named input to the next phase produces a brief where findings are genealogically linked. The lifecycle boundary produces C-06 (cross-signal synthesis) organically because each phase explicitly inherits from the last.

---

```
You are running the campaign-validate skill for topic: {topic}

Run the five sub-skills as a sequential pipeline. Each phase receives a named input from the previous phase. This is not a parallel review — it is a staged signal refinement process. Earlier phases shape the lens of later phases.

---

## Pipeline

```
Phase 1: listen-adoption  →  Phase 2: listen-feedback  →  Phase 3: review-users  →  Phase 4: review-customers  →  Phase 5: review-design
         ↑                            ↑                           ↑                          ↑                          ↑
         [starting state]        [phase 1 output]           [phase 1+2 output]         [phase 3 output]           [all prior output]
```

---

## Phase 1 — listen-adoption

**Input:** No prior phase. Start fresh.

Analyze the Rogers adoption curve for {topic}. For each of the five segments, answer:
1. What does this segment use today instead of {topic}? (status-quo behavior)
2. What is the primary reason they would switch to {topic}?
3. What is the primary reason they would not switch?
4. Estimate switching cost: Low / Medium / High / Blocking
5. Estimate segment size as a rough % of the target user base
6. Adoption prediction for 12 months post-ship: Will adopt / Will defer / Will resist

Segments: Innovators (~2.5%), Early Adopters (~13.5%), Early Majority (~34%), Late Majority (~34%), Laggards (~16%)

**Phase 1 output:**
- Adoption-resistance profile: which segments are likely, which are at risk
- Key switching-cost barriers (these will be tested in phases 3-5)
- The status-quo behaviors that phase 2 should use as baseline feedback predictions

Label section: **Phase 1 — listen-adoption**

---

## Phase 2 — listen-feedback

**Input from Phase 1:** The adoption-resistance profile and identified switching-cost barriers.

Using the Phase 1 adoption profile as your baseline: if users in the adopting segments (Innovators + Early Adopters + Early Majority) use {topic} for 90 days, what feedback do they produce?

Predict:
- Support tickets weeks 1-4: focus on features users expected (from status-quo behavior) that {topic} doesn't have
- Feature requests weeks 4-12: what will early adopters ask for after initial use?
- Negative signals: what do dissatisfied users say in reviews?
- Signal classification: for each feedback item, is it: design flaw / documentation gap / scope mismatch / switching-cost friction?

Note: listen-feedback and listen-adoption are categorically different. listen-feedback assumes users have already adopted. listen-adoption asks whether they will.

**Phase 2 output:** Predicted feedback profile with classification per item. Flag items that would also confirm or challenge Phase 1 adoption predictions — these are early cross-signal candidates.

Label section: **Phase 2 — listen-feedback**

---

## Phase 3 — review-users

**Input from Phases 1+2:** The switching-cost barriers from Phase 1 and the predicted feedback profile from Phase 2.

Conduct a UX review of the {topic} design. Your review should specifically test whether the design handles the switching-cost barriers identified in Phase 1.

For each Phase 1 switching-cost barrier (High or Blocking), ask: does the design provide a path that reduces this cost? If yes, how? If no, name the gap.

Additionally review:
- Workflow integration: does {topic} fit into the user's existing step without a context switch?
- Learnability for users coming from the status-quo behavior (not blank-slate users)
- Error recovery for the most common Phase 2 predicted mistake (the top support ticket type)
- Score each finding: P1 / P2 / P3

**Phase 3 output:** UX findings with explicit linkage to Phase 1 barriers where applicable.

Label section: **Phase 3 — review-users**

---

## Phase 4 — review-customers

**Input from Phase 3:** UX findings, especially P1s.

Conduct a customer success review. Your review should test whether customers who adopt {topic} (Phases 1-2) and use it as designed (Phase 3) will actually achieve the outcome they expected.

Assess:
- Outcome gap: will customers reach the promised result, or will they plateau at partial value?
- Competitive pressure: what is the risk that a customer compares {topic} to their prior solution and reverts?
- Which customer segment has the clearest path from adoption to outcome? (Fastest ROI)
- Do the Phase 3 P1 UX findings affect the customer's ability to demonstrate value to stakeholders?

**Phase 4 output:** Customer-value risk assessment. Flag any P1 from Phase 3 that also creates a customer-outcome risk — these are double-flagged blockers.

Label section: **Phase 4 — review-customers**

---

## Phase 5 — review-design

**Input from all prior phases:** Adoption profile (P1), feedback prediction (P2), UX findings (P3), customer-value risk (P4).

Conduct a design review. Your review is informed by all prior phases — you are not reviewing the design in isolation.

For each double-flagged blocker from Phase 4, ask: is there a design change that would reduce the UX gap AND reduce the switching cost simultaneously? These are high-leverage design changes.

Also review:
- Design coherence: does the design solve the problem stated in the spec?
- Internal contradictions: do any two parts of the design conflict?
- Coverage: does the design handle the failure cases Phase 2 predicted?
- Confidence: would you approve this design for implementation as-is?

**Phase 5 output:** Design verdict with specific linkage to earlier phases where applicable.

Label section: **Phase 5 — review-design**

---

## Validation Brief

After all five phases, produce the brief:

### Ranked findings

Rank all findings by adoption impact. A finding that blocks the Early Majority outranks a P1 that affects only Innovators.

| Rank | Finding | Phase | Source sub-skill | Severity | Adoption Impact | Segment (~N%) | Status-Quo Workaround | Switching Cost |
|------|---------|-------|-----------------|----------|-----------------|---------------|-----------------------|----------------|

### Cross-signal synthesis

Identify patterns that appear across 2+ phases. For each pattern, name:
- Which phases surface it
- Why the convergence raises confidence
- What it implies for adoption

### Go / No-go verdict

**GO** / **NO-GO** / **CONDITIONAL GO (condition: [specific condition])**

If NO-GO or CONDITIONAL GO: list top 3 blockers with source sub-skill.

---

Write output to: `simulations/{topic}/validate-{date}.md`

Confirm with: `Artifact written: simulations/{topic}/validate-{date}.md`
```

---

## V-05 — Combined: Output format + Inertia framing + pre-declared rows (full criterion-cascade)
**Axes:** Schema designed so one structural choice satisfies a criterion cluster (C-17) + switching cost as required columns (C-18) + Rogers rows pre-declared so absence is visible (C-19) + inertia foregrounded
**Hypothesis:** A single schema decision — pre-declaring the five Rogers rows with Status-Quo Workaround and Switching Cost as required columns — causes C-09, C-14, C-15, C-16, C-17, C-18, C-19 to pass by construction. The author fills cells; they cannot accidentally omit the analysis.

---

```
You are running the campaign-validate skill for topic: {topic}

Your job: validate the design for {topic} by running all five sub-skills and writing a brief that is structured so that completeness failures are visible rather than absent.

Every required analysis element below is pre-declared as a named row or required column. A blank in a required cell is a visible gap. Missing prose is not.

---

## Sub-skill execution (run all five)

Run sub-skills in standard order: review-design, review-users, review-customers, listen-feedback, listen-adoption.

For each sub-skill: identify the findings, classify severity (P1/P2/P3), note the status-quo behavior relevant to each finding, and estimate adoption impact by segment.

Keep listen-feedback and listen-adoption findings in separate labeled sections. These are categorically different:
- **listen-feedback** = post-adoption signal (what users say after they have used the feature)
- **listen-adoption** = pre-adoption signal (whether users will adopt at all, given what they do today)

Do not merge them.

---

## Required output — fill all tables completely

The tables below are your output schema. Fill every cell. Do not restructure the tables. Do not remove pre-declared rows. A blank mandatory row is a visible gap in the analysis.

---

### Table A — Sub-skill index (all five rows required)

| Sub-skill | Status | Finding count | Highest severity | Primary cross-signal candidate |
|-----------|--------|--------------|-----------------|-------------------------------|
| review-design | | | | |
| review-users | | | | |
| review-customers | | | | |
| listen-feedback | | | | |
| listen-adoption | | | | |

All five rows are required. A blank row in this table = a sub-skill that was not run.

---

### Table B — All findings, ranked by adoption impact

One row per finding from all five sub-skills. Rank 1 = greatest adoption impact.

Severity column is informational only — it does not govern rank position.

| Rank | Finding | Sub-skill | Severity | Adoption Impact | Segment blocked (~N%) | Status-Quo Workaround | Switching Cost |
|------|---------|-----------|----------|-----------------|----------------------|-----------------------|----------------|

Required columns — fill for every row, not just P1s:
- **Status-Quo Workaround**: what does the affected segment do today instead of {topic}?
- **Switching Cost**: Low / Medium / High / Blocking

---

### Table C — Rogers adoption curve (all five segment rows required)

Pre-declared rows: Innovators, Early Adopters, Early Majority, Late Majority, Laggards. All five are required. A blank row = missing required adoption analysis.

| Segment | ~% of base | Adoption readiness | Primary barrier | Status-Quo Workaround | Switching Cost | 12-month prediction |
|---------|-----------|-------------------|-----------------|----------------------|----------------|---------------------|
| Innovators | ~2.5% | | | | | |
| Early Adopters | ~13.5% | | | | | |
| Early Majority | ~34% | | | | | |
| Late Majority | ~34% | | | | | |
| Laggards | ~16% | | | | | |

Required columns — fill for every row:
- **Status-Quo Workaround**: what does this segment use today? (the real competitor)
- **Switching Cost**: Low / Medium / High / Blocking
- **12-month prediction**: Will adopt / Will defer / Will resist / Will not reach

The % anchors are pre-filled. Do not remove them.

---

### Table D — P1 blockers with remediation (fill rows only if P1s exist; leave empty if GO)

| Blocker | Source sub-skill | Affected segment (~N%) | Status-Quo Workaround | Switching Cost | Remediation path | Resolves if... |
|---------|-----------------|----------------------|-----------------------|----------------|-----------------|----------------|

If no P1s exist, write: `No P1 blockers identified. Verdict: GO.` and skip remaining rows.

---

### Table E — Cross-signal synthesis (minimum 1 row required)

| Pattern | Sub-skills that surface it | Why convergence raises confidence | Adoption implication |
|---------|--------------------------|----------------------------------|---------------------|

Each row must identify a relationship not visible in either sub-skill alone. Summary of sub-skill outputs fails.

---

### Table F — Verdict

| Verdict | Condition (if conditional) | Early Majority impact | Blocking segments |
|---------|--------------------------|----------------------|------------------|

Verdict must be one of:
- **GO** — no P1 finding blocks the Early Majority
- **NO-GO** — at least one P1 finding prevents Early Majority adoption
- **CONDITIONAL GO** — P1 findings exist with defined remediation; condition cell must be specific and actionable

"It depends" without a condition fails. "Needs further review" fails.

---

## Schema rationale (for your reference, not output)

Table C with pre-declared Rogers rows causes the following criteria to pass by construction:
- All five Rogers segments named with % anchors (C-15) — rows are pre-declared
- listen-adoption as a distinct section (C-14) — Table C is dedicated to adoption curve
- Adoption impact quantified per segment (C-09) — % column is required in every row
- Status-quo workaround per segment (C-16) — required column in Table C and Table B
- Switching cost as a column, not prose (C-18) — required column in both tables

This means: correctly filling Table C satisfies six criteria simultaneously. One schema decision, six criteria.

---

Write completed brief to: `simulations/{topic}/validate-{date}.md`

Confirm with: `Artifact written: simulations/{topic}/validate-{date}.md`
```

---

## Variation summary

| ID | Axis | Primary hypothesis | New v4 criteria targeted |
|----|------|-------------------|--------------------------|
| V-01 | Role sequence (adoption-first) | Listen-adoption first forces design findings to be expressed in adoption terms | C-02, C-14 by sequence |
| V-02 | Output format (table skeleton + pre-declared rows) | Pre-declared skeleton makes absence visible; completeness enforced by structure | C-11, C-15, C-17, C-18, C-19 |
| V-03 | Inertia framing (status-quo foregrounded per sub-skill) | Requiring status-quo behavior named before each review makes C-16 structural | C-16, C-18 by foregrounding |
| V-04 | Role sequence + lifecycle emphasis (pipeline handoffs) | Genealogical linkage between phases produces C-06 cross-signal synthesis organically | C-06, C-14 by pipeline structure |
| V-05 | Output format + inertia framing + pre-declared rows (criterion-cascade) | Single schema decision (Rogers rows + required columns) satisfies 6 criteria by construction | C-09, C-14, C-15, C-16, C-17, C-18, C-19 |
