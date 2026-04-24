---
skill: campaign-validate
round: 3
date: 2026-03-16
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/campaign-validate-rubric-v3-2026-03-16.md
---

# campaign-validate -- Round 3 Variations

**Context**: Round 2 top scores were V-03: 113, V-04: 113, V-02: 112, V-01: 107. Three new v3
criteria were added from R2 excellence patterns: C-14 (phase-gate-categorical-separation),
C-15 (rogers-curve-as-completeness-skeleton), C-16 (inertia-baseline-as-adoption-anchor).
Max composite moves from 115 to 130.

**Round 3 axes chosen:**
- Single-axis: V-01 (phase-gate role sequence / C-14), V-02 (table skeleton format / C-11 + C-12),
  V-03 (inertia framing / C-16)
- Combined: V-04 (phase-gate sequence + two-phase lifecycle emphasis / C-14 + C-01),
  V-05 (table-first format + Rogers row skeleton + inertia column / C-15 + C-16 + C-09)

---

## V-01 -- Phase-Gate Role Sequence Axis

**Variation axis:** Phase-gate role sequence -- the campaign is structured as five named phases,
each terminated by an explicit GATE marker. The gate for Phase 4 (listen-feedback) includes a
categorical declaration that separates it from Phase 5 (listen-adoption) before Phase 5 begins.
No phase may be silently skipped; the gate is the only valid exit from a phase.

**Hypothesis:** Making each sub-skill a named phase with a required gate marker prevents listen-
adoption from being silently merged with listen-feedback (C-01 failure mode). The categorical
gate declaration between Phase 4 and Phase 5 forces C-14 to pass by construction -- the author
must write the declaration as the gate condition before proceeding, not as an optional note buried
in prose. Hardest remaining: C-15 (Rogers segments enumerated with % anchors -- the gate structure
does not force row-level enumeration) and C-16 (inertia workaround per blocker -- not structurally
required by the gate protocol).

---

Validate the design for: {{topic}}

Run the full design validation campaign. Execute all five phases in order. Complete each phase and
pass its gate before advancing. Do not reorder phases; do not merge phases.

---

**PHASE 1: review-design**
> Purpose: multi-expert design review through 6 disciplines and domain-selected experts

Walk the design through 6 review disciplines (architecture, usability, implementation, testing,
documentation, process) and 2-3 domain-selected experts based on the design's content signals.
For each reviewer, produce P1/P2/P3 severity findings. Record cross-reviewer consensus (same
finding flagged by 2+ reviewers) and unique catches (flagged by exactly one reviewer).

For each finding:
- Severity: P1 (blocking), P2 (major), P3 (minor)
- Source reviewer: which discipline or named expert
- Design section: where in the design the finding lives
- Summary: one sentence -- the problem, not the impact

---

**GATE 1 --> PHASE 2**: All review-design findings logged. Minimum 5 findings or state "No
findings -- reason: [explanation of why the design passed all 6 disciplines cleanly]". Proceed.

---

**PHASE 2: review-users**
> Purpose: five persona advocates walk through the design with usability scores

Walk five user personas through the design. For each persona: name them, state their role and
context, walk the primary task flow, identify friction points, and assign a usability score (1-10).
Cross-persona synthesis: which friction points appear across 2+ personas?

For each finding:
- Severity: P1 (blocks task completion), P2 (causes confusion or delay), P3 (minor friction)
- Source persona: which persona surfaced it
- Task flow step: where in the flow the friction occurs
- Summary: one sentence

---

**GATE 2 --> PHASE 3**: All review-users findings logged. Minimum 5 findings across 5 personas or
state why coverage is lower. Proceed.

---

**PHASE 3: review-customers**
> Purpose: twelve customer personas evaluate for usefulness, clarity, and would-adopt

Run all 12 customer personas (C-01 through C-12) through the design. Per-persona: usefulness score
(1-10), clarity score (1-10), would-adopt (yes / conditional / no), and top concern. Aggregate
across all 12: mean usefulness, mean clarity, would-adopt rate. Flag any persona whose would-adopt
is "no" or whose usefulness score is below 6.

For each finding:
- Severity: P1 (blocks adoption for this persona), P2 (reduces willingness), P3 (minor concern)
- Source persona: C-01 through C-12
- Summary: one sentence

---

**GATE 3 --> PHASE 4**: All review-customers findings logged. All 12 personas scored or state why
a persona was not applicable. Proceed.

---

**PHASE 4: listen-feedback**
> Purpose: pre-ship customer reaction to the design -- what customers say BEFORE it ships

> CATEGORICAL NOTE: This phase captures customer reaction to the design artifact before
> it ships. It is NOT the adoption trajectory. Do not include post-ship behavior here.
> listen-feedback asks: "What will customers say when they first see this design?"
> listen-adoption (Phase 5) asks: "Who will actually adopt this after it ships, and when?"
> These are categorically different questions. Do not merge Phase 4 and Phase 5 content.

Simulate all 12 customer personas reacting to the design. Per-persona: NPS prediction (1-10),
sentiment (positive / neutral / negative), and top verbatim reaction statement in first person.
Aggregate NPS threshold: 7.0. Below 7.0 means the design needs revision before ship.

For each finding:
- Severity: P1 (NPS < 5), P2 (NPS 5-6.9), P3 (NPS 7-8, with a notable concern)
- Source persona: C-01 through C-12
- Summary: the top concern driving the NPS prediction

---

**GATE 4 --> PHASE 5**: All listen-feedback findings logged. Aggregate NPS computed and stated.
CATEGORICAL GATE: Phase 5 covers post-ship adoption trajectory -- categorically different from
pre-ship reaction. Phase 4 content must not be carried forward as Phase 5 content. Proceed only
after this declaration is satisfied.

---

**PHASE 5: listen-adoption**
> Purpose: post-ship adoption trajectory by segment -- what happens AFTER it ships

> CATEGORICAL NOTE: This phase covers what happens after the feature ships. It is NOT a
> repeat of pre-ship feedback. listen-adoption asks: "Who will adopt, at what rate, and
> what stops the chasm crossing?" Every entry in this phase must describe post-ship
> adoption behavior, not design reaction. This is categorically distinct from Phase 4.

Simulate the adoption curve. Map each customer persona to a Rogers archetype and estimate when
they adopt. Identify chasm risk (gap between early adopter and early majority segments).
Champion network analysis: who drives early spread? Intervention recommendations: ranked by
adoption delta.

For each finding:
- Segment: which Rogers archetype is affected
- Adoption impact: estimated % of target population affected
- Summary: the adoption blocker or accelerator

---

**GATE 5 --> SYNTHESIS**: All listen-adoption findings logged. All five Rogers segments addressed
(innovators ~2.5%, early adopters ~13.5%, early majority ~34%, late majority ~34%, laggards ~16%).
Proceed.

---

**SYNTHESIS**

**Cross-Signal Patterns**

Before building the ranked findings table, identify at least one pattern or tension that appears
across 2+ phases. A pattern is a finding confirmed or amplified by a different sub-skill.
A concatenation (simply listing outputs in order) is not synthesis.

| P-ID | Pattern | Phases Linked | Summary |
|------|---------|--------------|---------|
| | | | |

If no cross-signal patterns exist: "No cross-signal patterns detected. Each phase's findings
describe distinct problems with no shared root cause or amplifying confirmation. [Brief reason.]"

---

**FINDINGS TABLE**

All findings from all five phases, in adoption-impact order (highest adoption impact first).

| F-ID | Phase | Sub-Skill | Severity | Finding Summary | Adoption Impact (segment, ~N%) |
|------|-------|-----------|----------|----------------|-------------------------------|
| | | | P1/P2/P3 | | |

Ranking rule: rank by adoption impact magnitude, not by severity. A P2 finding that blocks the
chasm crossing (early majority, ~34%) ranks above a P1 cosmetic issue affecting only innovators
(~2.5%). When adoption impact is equal, rank by severity.

---

**TOP BLOCKERS**

List the top 3 blockers in adoption-impact order.

| Rank | F-ID | Source Sub-Skill | Blocker Summary | Adoption Impact (segment, ~N%) | Remediation |
|------|------|-----------------|----------------|-------------------------------|-------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

Remediation: name the specific design decision that resolves the blocker. "Fix the design" fails.
Source sub-skill: attribute each blocker to the phase that surfaced it.

---

**VERDICT**

Go / No-Go / Go with Conditions: [state one]

Rationale: [2-3 sentences referencing the top blockers and adoption impact]

If "Go with Conditions": state the exact condition that must be resolved before committing to spec.
"It depends" without a named condition fails this section.

---

**EXECUTION LOG**

| Phase | Sub-Skill | Status | Finding Count |
|-------|-----------|--------|--------------|
| 1 | review-design | executed / no findings | |
| 2 | review-users | executed / no findings | |
| 3 | review-customers | executed / no findings | |
| 4 | listen-feedback | executed / no findings | |
| 5 | listen-adoption | executed / no findings | |

A phase with "no findings" must state why. A phase absent from this log was skipped.

---

**OUTPUT**

Write findings to: simulations/{{topic}}/validate-{{date}}.md

Required sections in order: Phase 1-5 outputs > Cross-Signal Patterns > Findings Table (ranked
by adoption impact) > Top Blockers > Verdict > Execution Log.

After writing, emit: Artifact written: simulations/{{topic}}/validate-{{date}}.md

---

## V-02 -- Table Skeleton Format Axis

**Variation axis:** Table skeleton format -- the complete findings table structure (with all
required columns including Severity and Adoption Impact as separate columns) is declared before
execution begins. Each sub-skill writes into a named table section. An empty table means "ran,
found nothing"; an absent table means "skipped". The skeleton makes omission visually detectable.

**Hypothesis:** Pre-declaring table skeletons per sub-skill simultaneously enforces C-11 (table
skeleton as completeness gate) and C-12 (Adoption Impact as a dedicated column, separate from
Severity) before the author runs a single sub-skill. The Rogers segment column in the listen-
adoption table structurally requires segment identification for every adoption finding, enforcing
C-09 at the layout level. Hardest remaining: C-14 (categorical separation must still be declared
explicitly) and C-16 (inertia workaround not required by the column schema alone).

---

Validate the design for: {{topic}}

Run the full design validation campaign across five sub-skills. Use the pre-declared table
skeletons below to record all findings. Each sub-skill writes into its own named table. An empty
row in a table means no findings for that sub-skill -- leave the header row and write "No findings"
as the first data row. Do not omit a table because a sub-skill found nothing.

---

**TABLE SKELETONS**

The following tables are the output containers for this campaign. All fields are required.
Severity and Adoption Impact are separate columns -- they are never merged into a single cell.

**Table 1: review-design findings**

| F-ID | Discipline / Expert | Severity | Design Section | Finding Summary | Adoption Impact (segment, ~N%) |
|------|--------------------|---------|--------------|-----------------|---------------------------------|

Note: If no findings, write: "No findings -- [reason: which disciplines ran, what was checked,
why no gaps were identified]"

---

**Table 2: review-users findings**

| F-ID | Persona | Task Flow Step | Severity | Finding Summary | Adoption Impact (segment, ~N%) |
|------|---------|--------------|----------|----------------|-------------------------------|

Note: If no findings, write: "No findings -- [reason: usability scores for each persona listed]"

---

**Table 3: review-customers findings**

| F-ID | Persona (C-ID) | Would-Adopt | Severity | Finding Summary | Adoption Impact (segment, ~N%) |
|------|--------------|------------|---------|----------------|-------------------------------|

Note: All 12 customer personas (C-01 through C-12) must appear. A persona row with no finding is
written as: "[C-ID] | yes | -- | No concern flagged | --". A missing persona row is a missing row.

---

**Table 4: listen-feedback findings**
> SCOPE: listen-feedback = pre-ship customer reaction to the design. What customers SAY before
> it ships. This table does NOT cover post-ship adoption behavior; that is Table 5.
> A merged or unlabeled table combining feedback and adoption fails C-14 unconditionally.

| F-ID | Persona (C-ID) | NPS Prediction | Severity | Reaction Summary | Adoption Impact (segment, ~N%) |
|------|--------------|--------------|---------|-----------------|-------------------------------|

Aggregate NPS: [compute from per-persona NPS column after filling table]
Threshold: 7.0. Below threshold = design needs revision.

Note: If no findings above threshold, write the NPS aggregate and state "NPS above threshold,
no blocking findings."

---

**Table 5: listen-adoption findings**
> SCOPE: listen-adoption = post-ship adoption trajectory. What customers DO after it ships.
> Categorically different from Table 4. Do not carry Table 4 content forward.
> Required rows: all five Rogers segments must appear. A missing segment is a missing row.

| Rogers Segment | Population (~%) | Month-of-Adoption Estimate | Chasm Risk | Severity | Finding Summary | Adoption Impact |
|--------------|----------------|--------------------------|------------|---------|-----------------|----------------|
| Innovators | ~2.5% | | | | | |
| Early Adopters | ~13.5% | | | | | |
| Early Majority | ~34% | | | | | |
| Late Majority | ~34% | | | | | |
| Laggards | ~16% | | | | | |

Chasm analysis: [after filling, identify the chasm gap -- the point where adoption stalls between
early adopters and early majority, if one exists. State which segment is the chasm risk and why.]

---

**EXECUTION**

Run each sub-skill in order. Fill in the corresponding table as you go.

1. review-design --> fill Table 1
2. review-users --> fill Table 2
3. review-customers --> fill Table 3
4. listen-feedback --> fill Table 4
5. listen-adoption --> fill Table 5

After all five tables are filled, proceed to Synthesis.

---

**SYNTHESIS**

**Cross-Signal Patterns**

Review all five tables and identify findings that appear across 2+ sub-skills -- the same problem
surfaced by different observers. These are cross-signal patterns, not concatenation.

| P-ID | Finding Summary | Tables Linked | What the Cross-Signal Means |
|------|----------------|--------------|---------------------------|

If none: "No cross-signal patterns detected. [Name any findings that appeared similar across
tables and explain why they are distinct rather than the same root cause.]"

---

**RANKED FINDINGS TABLE**

All findings from Tables 1-5, ranked by adoption impact (highest adoption impact first).

| Rank | F-ID | Sub-Skill | Severity | Finding Summary | Adoption Impact (segment, ~N%) |
|------|------|-----------|---------|----------------|-------------------------------|

Ranking rule: adoption impact is the sort key. Severity is the tiebreaker within the same
adoption impact tier. A P3 finding blocking chasm crossing (early majority, ~34%) ranks above
a P1 cosmetic issue affecting innovators only (~2.5%).

---

**TOP BLOCKERS**

The top 3 findings by adoption impact, with remediation.

| Rank | F-ID | Source Sub-Skill | Blocker Summary | Adoption Impact (segment, ~N%) | Remediation |
|------|------|-----------------|----------------|-------------------------------|-------------|

Remediation: name the specific change that resolves this blocker. Which design section, which
persona concern, which friction point. Not "fix the UX" -- the named change at the named location.

---

**VERDICT**

Go / No-Go / Go with Conditions: [state one]

State explicitly which top blocker(s) drove the verdict, which segment they affect, and what
the adoption impact would be if shipped with the blocker unresolved.

If "Go with Conditions": name the condition as a testable gate, not a general direction.

---

**EXECUTION LOG**

| Sub-Skill | Table | Status | Row Count |
|-----------|-------|--------|----------|
| review-design | Table 1 | filled / empty (no findings) | |
| review-users | Table 2 | filled / empty (no findings) | |
| review-customers | Table 3 | filled / empty (no findings) | |
| listen-feedback | Table 4 | filled / empty (no findings) | |
| listen-adoption | Table 5 | filled / empty (no findings) | |

An empty table is not a skipped table. A missing table is a skipped sub-skill.

---

**OUTPUT**

Write all five tables plus Synthesis, Ranked Findings, Top Blockers, Verdict, and Execution Log
to: simulations/{{topic}}/validate-{{date}}.md

After writing, emit: Artifact written: simulations/{{topic}}/validate-{{date}}.md

---

## V-03 -- Inertia Framing Axis

**Variation axis:** Inertia framing -- the status-quo workaround is established as the adoption
anchor before any sub-skill runs. Every blocker is then framed as a switching cost against that
baseline: "Users today do X to solve this problem. This feature asks them to give up X because Y.
The population still doing X after ship is the adoption risk segment."

**Hypothesis:** Naming the status-quo workaround per blocker does two things simultaneously:
it satisfies C-16 (inertia citation per blocker) and structurally identifies the adoption risk
segment for C-09 quantification (the workaround's users ARE the segment at risk). This removes
the need for a separate C-09 enforcement point. The inertia framing also grounds listen-feedback
persona reactions in real behavior rather than hypothetical response, strengthening C-06 cross-
signal synthesis. Hardest remaining: C-11 (table skeleton as completeness gate -- this variation
uses prose framing per blocker, not pre-declared table skeletons) and C-15 (Rogers segments
enumerated -- not forced by inertia framing alone).

---

Validate the design for: {{topic}}

Before running the validation campaign, establish the inertia baseline. The primary competitor
is not another product -- it is what users do today in the absence of this feature. Every adoption
blocker you find should be evaluated against this baseline: does the feature ask users to give up
a behavior they already rely on? If yes, the population still doing that behavior after ship is
your adoption risk segment.

---

**INERTIA BASELINE**

Before running any sub-skill, answer these questions about {{topic}}:

1. What problem does this feature solve?
2. What do users do today (without this feature) to solve that problem? Name the specific
   behavior or workaround -- not "they use other tools" but the named action.
3. Which user segments rely most heavily on that workaround today?
4. What does this feature require users to give up in order to adopt it? Name the switching cost.

**Inertia baseline statement**: "Users today [specific behavior / workaround]. This feature asks
them to [specific change required for adoption] because [reason the feature requires this change].
The population still doing [workaround] after ship is the adoption risk segment."

Establish this statement before proceeding. It is the anchor for all adoption impact estimates.

---

**PHASE 1: review-design**

Walk the design through 6 review disciplines and 2-3 domain-selected experts. For each finding,
assess whether the design friction is connected to the inertia baseline. A finding connected to
the status-quo workaround has higher adoption impact than an isolated usability issue.

For each finding:
- Severity: P1 (blocking), P2 (major), P3 (minor)
- Source reviewer: discipline name or expert name
- Inertia connection: yes / no -- does this finding ask users to change the workaround behavior?
- Summary: one sentence

---

**PHASE 2: review-users**

Walk five user personas through the design. For each persona: name them, state their current
workaround behavior (from the inertia baseline), walk the primary task flow, and identify
where the design conflicts with their existing behavior patterns.

For each finding:
- Severity: P1, P2, P3
- Source persona
- Workaround conflict: how does this finding connect to the persona's current behavior?
- Summary: one sentence

---

**PHASE 3: review-customers**

All 12 customer personas evaluate the feature. For each persona: usefulness (1-10), clarity (1-10),
would-adopt (yes / conditional / no), and whether their would-adopt decision is driven by workaround
inertia or design quality. A "conditional" or "no" driven by inertia has different remediation than
one driven by usability or clarity.

For each finding:
- Severity: P1, P2, P3
- Source persona
- Adoption driver: inertia (would-not-adopt because of switching cost) or design (would-not-adopt
  because of design quality issue) -- this distinction matters for remediation
- Summary: one sentence

---

**PHASE 4: listen-feedback**
> listen-feedback = pre-ship customer reaction to the design artifact.
> This phase captures what customers SAY when they first see the design.
> It does not capture what they will DO after it ships. That is Phase 5.

Simulate all 12 customer personas reacting to the design. For each persona: NPS prediction (1-10),
and what drives the NPS (positive or negative aspect of the design). For low NPS predictors (< 7):
does the concern connect to the inertia baseline? A concern rooted in workaround switching cost
predicts lower adoption even if the design quality is high.

Aggregate NPS: compute the mean. Threshold 7.0.

---

**PHASE 5: listen-adoption**
> listen-adoption = post-ship adoption trajectory. Categorically distinct from Phase 4.
> Phase 4 asked: "What do customers say?" Phase 5 asks: "What do customers DO, and when?"
> Do not merge Phase 5 content with Phase 4. Do not carry Phase 4 reaction into Phase 5.

Simulate the adoption curve using the Rogers diffusion model. For each segment, estimate adoption
trajectory using the inertia baseline as the primary adoption friction:

**Innovators (~2.5%)**: Will they try it despite the switching cost? What will they give up?
**Early Adopters (~13.5%)**: When do they adopt? What's the workaround still in use for them?
**Early Majority (~34%)**: What must happen before they cross the chasm? Workaround still present?
**Late Majority (~34%)**: At what point does the workaround become more painful than adoption?
**Laggards (~16%)**: Will the workaround remain viable long enough to keep them from ever adopting?

For each segment finding:
- Segment and % anchor
- Current workaround behavior for this segment
- Switching cost: what do they give up when they adopt?
- Adoption blocker or accelerator
- Estimated adoption timeline relative to ship date

Chasm analysis: identify the chasm risk segment (typically the gap between early adopters and
early majority). What workaround still in play is the primary barrier to the chasm crossing?

---

**CROSS-SIGNAL SYNTHESIS**

Before ranking, scan for patterns across phases. The most common cross-signal pattern in
validation campaigns: a usability finding from review-users confirmed by a workaround inertia
finding from listen-adoption (the friction is both a design problem and a behavior switching cost).
These compounding findings have higher adoption impact than either signal alone.

| P-ID | Pattern | Phases Linked | Adoption Impact Amplification |
|------|---------|--------------|------------------------------|

If none: "No cross-signal patterns detected. Each phase's findings describe distinct problems.
[Brief reason why the review findings and adoption findings do not share a root cause.]"

---

**FINDINGS TABLE**

All findings, ranked by adoption impact. For each finding, the Adoption Impact column includes
the Rogers segment and population % affected.

| F-ID | Sub-Skill | Severity | Finding Summary | Inertia Connection | Adoption Impact (segment, ~N%) |
|------|-----------|---------|----------------|-------------------|-------------------------------|

Ranking: adoption impact is the sort key, not severity. Use the inertia baseline as the guide:
findings connected to the workaround behavior affect a larger, more precisely identifiable
population than findings about design aesthetics or minor UX friction.

---

**TOP BLOCKERS WITH INERTIA ANCHORS**

The top 3 blockers, each with its inertia anchor and adoption risk segment.

For each blocker:
- **Blocker**: one sentence summary
- **Source sub-skill**: which phase surfaced it
- **Adoption impact**: (segment, ~N%)
- **Inertia anchor**: "Users today [specific workaround behavior]. This feature requires them to
  give up [behavior] because [reason]. The population still doing [behavior] after ship is
  [segment], approximately N% of the target population."
- **Remediation**: the specific design decision that reduces the switching cost or resolves the
  blocker. Which section of the design, which UX change, which capability addition.

---

**VERDICT**

Go / No-Go / Go with Conditions: [state one]

State which top blocker carries the highest adoption risk, which segment it affects, and what
the post-ship trajectory looks like if the blocker ships unresolved. Reference the inertia
baseline explicitly: does the blocker mean the workaround remains viable long enough to stall
chasm crossing?

---

**EXECUTION LOG**

| Phase | Sub-Skill | Status | Findings | Inertia-Connected |
|-------|-----------|--------|---------|------------------|
| 1 | review-design | executed / no findings | | |
| 2 | review-users | executed / no findings | | |
| 3 | review-customers | executed / no findings | | |
| 4 | listen-feedback | executed / no findings | | |
| 5 | listen-adoption | executed / no findings | | |

---

**OUTPUT**

Write the Inertia Baseline, Phase 1-5 outputs, Cross-Signal Synthesis, Findings Table, Top
Blockers with Inertia Anchors, Verdict, and Execution Log to:
simulations/{{topic}}/validate-{{date}}.md

After writing, emit: Artifact written: simulations/{{topic}}/validate-{{date}}.md

---

## V-04 -- Combined (Phase-Gate Sequence + Two-Phase Lifecycle Emphasis)

**Variation axes combined:**
1. Phase-gate role sequence (V-01) -- explicit gates prevent silent skipping
2. Two-phase lifecycle emphasis -- the campaign is structurally divided into Phase 1 (design
   evidence: review-design, review-users, review-customers) and Phase 2 (customer signal:
   listen-feedback, listen-adoption), with the Phase 1 --> Phase 2 transition as the categorical
   boundary between design evaluation and customer adoption analysis

**Hypothesis:** The two-phase structure makes C-14 structural: the boundary between Phase 1
and Phase 2 is the categorical declaration that separates "what the design looks like" from "what
customers will do." Within Phase 2, the gate between listen-feedback and listen-adoption enforces
the categorical distinction between pre-ship reaction and post-ship trajectory. C-01 is enforced
by the gate protocol: each of the 5 sub-skills has a named gate exit, so skipping one leaves an
obvious absent gate marker. C-14 is the strongest pattern this variation targets.

---

Validate the design for: {{topic}}

This campaign runs in two phases. Phase 1 evaluates the design. Phase 2 evaluates the customer
response. Do not merge the phases. Do not reorder sub-skills within a phase.

---

## PHASE 1: DESIGN EVIDENCE

Phase 1 asks: "Is the design sound?" Three sub-skills run in order. Phase 1 findings are
categorized as design quality findings. They are not adoption trajectory findings.

---

**Phase 1 / Step 1: review-design**

Multi-expert design review through 6 disciplines and domain-selected experts.
Auto-select 2-3 domain experts based on the design's content signals.

For each finding:
- Reviewer: discipline name or named expert
- Severity: P1 (blocking), P2 (major), P3 (minor)
- Section: where in the design
- Summary: one sentence (problem only, no adoption impact here)

If no findings: "review-design found no issues. Disciplines run: [list]. No gaps identified
because [reason]."

---

**Phase 1 / Step 2: review-users**

Five persona advocates walk through the design. Each persona: name, role, primary task flow,
friction points, usability score (1-10). Cross-persona synthesis: friction shared by 2+ personas.

For each finding:
- Persona: name and role
- Task step: where friction occurs
- Severity: P1, P2, P3
- Summary: one sentence

If no findings: "review-users found no friction above threshold. Per-persona usability scores: [list]."

---

**Phase 1 / Step 3: review-customers**

All 12 customer personas evaluate the design (C-01 through C-12). Per-persona: usefulness (1-10),
clarity (1-10), would-adopt (yes / conditional / no), top concern.

For each finding:
- Persona: C-ID
- Would-adopt verdict
- Severity: P1, P2, P3
- Summary: top concern in one sentence

All 12 personas must appear. A persona with no concern: "C-ID | yes | -- | No concern."

---

**PHASE 1 GATE --> PHASE 2**

Phase 1 complete. Before advancing:
- [ ] All three Phase 1 sub-skills ran and are logged
- [ ] Phase 1 findings summarized (adoption impact may be estimated but not the primary ranking
     axis for Phase 1 -- Phase 2 will determine adoption trajectory)
- [ ] Phase 1 cross-design patterns identified (same friction across review-design, review-users,
     or review-customers?)

> PHASE BOUNDARY DECLARATION: Phase 1 evaluated design quality. Phase 2 evaluates customer
> response -- what customers will say and do. These are categorically different analytical modes.
> Phase 1 findings are carried forward for cross-signal synthesis but not re-run in Phase 2.

Proceed to Phase 2.

---

## PHASE 2: CUSTOMER SIGNAL

Phase 2 asks: "How will customers respond?" Two sub-skills run in order. Phase 2 is divided into
two sub-phases: customer reaction (listen-feedback) and adoption trajectory (listen-adoption).
These are categorically different. They are not combined into a single "listen" section.

---

**Phase 2 / Step 4: listen-feedback**
> listen-feedback: pre-ship customer reaction to the design.
> Question answered: "What will customers say when they first see this?"
> This is NOT the adoption trajectory. Do not carry post-ship behavior into this step.
> Categorical scope: customer reaction to the design artifact, before ship.

Simulate all 12 customer personas (C-01 through C-12) reacting to the design. Per-persona: NPS
prediction (1-10), primary reaction (positive / neutral / negative), top reaction statement as
first-person verbatim ("I would..."). Aggregate NPS. Threshold: 7.0.

For each finding (personas with NPS < 7.0 or blocking concern):
- Persona: C-ID
- NPS prediction
- Severity: P1 (NPS < 5), P2 (NPS 5-6.9), P3 (NPS 7-7.9 with notable concern)
- Reaction summary: the specific concern driving the NPS

Aggregate NPS: [mean of all 12 persona NPS predictions]

---

**Phase 2 / Step 4 Gate --> Step 5**
> CATEGORICAL GATE: listen-feedback (Step 4) covers pre-ship customer reaction to the design.
> listen-adoption (Step 5) covers post-ship adoption trajectory by segment.
> These are categorically different: one captures what customers SAY; the other captures what
> they DO. Step 5 content must not duplicate or simply re-frame Step 4 content.
> A merged or unlabeled combined section fails unconditionally.

---

**Phase 2 / Step 5: listen-adoption**
> listen-adoption: post-ship adoption trajectory. Categorically distinct from Step 4.
> Question answered: "Who will actually adopt this after it ships, and when?"
> Every finding in this step must describe post-ship behavior, not design reaction.

Simulate the adoption curve across all five Rogers segments:

| Rogers Segment | Population (~%) | Adoption Trigger | Chasm Risk | Key Blocker |
|--------------|----------------|-----------------|-----------|------------|
| Innovators | ~2.5% | | | |
| Early Adopters | ~13.5% | | | |
| Early Majority | ~34% | | | |
| Late Majority | ~34% | | | |
| Laggards | ~16% | | | |

All five rows are required. A missing row is a missing required entry.

Chasm analysis: identify the chasm (the gap between early adopters and early majority). What
is the key blocker preventing early majority adoption? Champion network: who drives spread from
innovators to early adopters?

For each adoption finding:
- Segment and % anchor
- Adoption blocker or accelerator
- Estimated month-of-adoption relative to ship date

---

**PHASE 2 GATE --> SYNTHESIS**

Phase 2 complete. Both Step 4 (listen-feedback) and Step 5 (listen-adoption) logged as separate
sections. Confirm: does the output show two visibly distinct sections with distinct content?
If not, re-run the appropriate step before proceeding.

Proceed to Synthesis.

---

**CROSS-SIGNAL SYNTHESIS**

Scan for patterns across Phase 1 and Phase 2. The most powerful patterns cross the phase boundary:
a Phase 1 design friction finding confirmed by a Phase 2 adoption blocker means the design problem
has a measurable adoption impact.

| P-ID | Phase 1 Finding | Phase 2 Finding | Cross-Signal Pattern |
|------|----------------|----------------|---------------------|

If none: "No cross-phase patterns detected. Phase 1 and Phase 2 findings describe distinct
problems. [Reason: Phase 1 issues are design quality gaps; Phase 2 blockers are adoption behavior
gaps; they do not share a root cause in this case.]"

---

**FINDINGS TABLE**

All findings from both phases, ranked by adoption impact.

| F-ID | Phase | Sub-Skill | Severity | Finding Summary | Adoption Impact (segment, ~N%) |
|------|-------|-----------|---------|----------------|-------------------------------|

Adoption Impact field: required for every finding. Phase 1 findings should estimate the
downstream adoption impact even if the finding is a design quality issue -- a design quality
gap that blocks chasm crossing has a higher adoption impact than one that impedes innovators only.

Ranking: sort by Adoption Impact magnitude, not by Phase number or Severity.

---

**TOP BLOCKERS**

Top 3 findings by adoption impact, with source sub-skill and remediation.

| Rank | F-ID | Source Sub-Skill | Blocker Summary | Adoption Impact (segment, ~N%) | Remediation |
|------|------|-----------------|----------------|-------------------------------|-------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

---

**VERDICT**

Go / No-Go / Go with Conditions: [state one]

Reference the top adoption blocker, the affected segment, and the post-ship trajectory if
shipped unresolved. State which phase's findings drove the verdict.

---

**EXECUTION LOG**

| Phase | Sub-Skill | Status | Finding Count |
|-------|-----------|--------|--------------|
| 1 | review-design | executed / no findings | |
| 1 | review-users | executed / no findings | |
| 1 | review-customers | executed / no findings | |
| 2 | listen-feedback | executed / no findings | |
| 2 | listen-adoption | executed / no findings | |

---

**OUTPUT**

Write Phase 1 outputs (Steps 1-3), Phase 2 outputs (Steps 4-5), Cross-Signal Synthesis, Findings
Table, Top Blockers, Verdict, and Execution Log to:
simulations/{{topic}}/validate-{{date}}.md

After writing, emit: Artifact written: simulations/{{topic}}/validate-{{date}}.md

---

## V-05 -- Combined (Table-First Format + Rogers Row Skeleton + Inertia Column)

**Variation axes combined:**
1. Table-first format (V-02) -- all output tables declared before execution begins
2. Rogers curve as required row skeleton -- all five Rogers segments pre-declared as required rows
   in the listen-adoption table; a missing row is a missing required entry
3. Inertia column -- "Status-Quo Workaround" is a required column in the Top Blockers table;
   every blocker must name the specific behavior users employ today and the switching cost

**Hypothesis:** This is the structural maximum. Rogers segments as required rows (C-15 by
construction) + Inertia as required column (C-16 by construction) force C-09 compliance (one
adoption impact estimate per required row) without a separate enforcement point. The table
skeleton for listen-adoption with Rogers rows forces listen-adoption to be a distinct section
(C-14 by construction). Pre-declared table structure per sub-skill enforces C-11 and C-12. The
only criteria requiring author discipline rather than structural enforcement are C-06 (cross-
signal synthesis) and C-03 (go/no-go verdict).

---

Validate the design for: {{topic}}

Run the full design validation campaign. All output is written into the pre-declared tables below.
Fill each table as you run the corresponding sub-skill. Do not omit a table because it is empty --
an empty table (headers with a "No findings" row) signals that the sub-skill ran and found nothing.
A missing table signals that the sub-skill was skipped.

---

**PRE-DECLARED OUTPUT TABLES**

The following tables are the complete output structure for this campaign. All column fields are
required. Severity and Adoption Impact are always separate columns. They are never merged.

---

**Table 1: review-design**

| F-ID | Discipline / Expert | Severity | Design Section | Finding Summary | Adoption Impact (segment, ~N%) |
|------|--------------------|---------|--------------|-----------------|---------------------------------|

Rules: Severity = P1 / P2 / P3. Adoption Impact = (segment, ~N%) -- which Rogers segment does
this finding most affect, and what % of the target population is in that segment?
Empty state: "| -- | All disciplines ran: [list] | -- | -- | No findings | -- |"

---

**Table 2: review-users**

| F-ID | Persona | Usability Score (1-10) | Severity | Finding Summary | Adoption Impact (segment, ~N%) |
|------|---------|----------------------|---------|----------------|-------------------------------|

Rules: all 5 personas run; usability score is per-persona. Empty state: "| -- | [persona names] |
[scores] | -- | No friction above P3 | -- |"

---

**Table 3: review-customers**

| F-ID | Persona (C-ID) | Usefulness (1-10) | Clarity (1-10) | Would-Adopt | Severity | Finding Summary | Adoption Impact (segment, ~N%) |
|------|--------------|-----------------|--------------|------------|---------|-----------------|-------------------------------|

Rules: all 12 personas (C-01 through C-12) must appear. A persona with no concern: use severity
"--" and Finding Summary "No concern." Would-Adopt: yes / conditional / no.
Empty state: all 12 rows present with no-concern entries.

---

**Table 4: listen-feedback**
> SCOPE: pre-ship customer reaction -- what customers SAY when they first see this design.
> This table does NOT cover post-ship adoption behavior. That is Table 5.
> A merged or unlabeled combined Table 4+5 fails C-14 unconditionally.

| F-ID | Persona (C-ID) | NPS Prediction (1-10) | Severity | Reaction Summary | Adoption Impact (segment, ~N%) |
|------|--------------|---------------------|---------|-----------------|-------------------------------|

Aggregate NPS: [computed from column after filling] | Threshold: 7.0
Empty state: "Aggregate NPS: [N]. All personas above 7.0 threshold. No blocking findings."

---

**Table 5: listen-adoption**
> SCOPE: post-ship adoption trajectory -- what customers DO after it ships.
> Categorically distinct from Table 4. Every row must describe post-ship behavior.
> All five Rogers segments are required rows. A missing segment is a missing required entry.

| Rogers Segment | Population (~%) | Status-Quo Workaround | Switching Cost | Month-of-Adoption | Chasm Risk | Severity | Finding Summary | Adoption Impact |
|--------------|----------------|----------------------|--------------|-----------------|-----------|---------|-----------------|----------------|
| Innovators | ~2.5% | | | | | | | |
| Early Adopters | ~13.5% | | | | | | | |
| Early Majority | ~34% | | | | | | | |
| Late Majority | ~34% | | | | | | | |
| Laggards | ~16% | | | | | | | |

Column definitions:
- **Status-Quo Workaround**: the specific behavior this segment uses today, without this feature.
  "They use spreadsheets" fails -- name the actual behavior. "They copy the data manually from
  the export screen into a shared doc" passes.
- **Switching Cost**: what this segment gives up when they adopt. Name the behavior and why it is
  a cost: "They give up [behavior] because [reason the feature requires this change]."
- **Chasm Risk**: high / medium / low -- how likely is this segment to stall adoption?
- **Adoption Impact**: (segment, ~N%) -- for this segment row, the self-referential adoption
  impact is the segment % anchor in the Population column.

Chasm analysis (below Table 5): [identify the chasm gap after filling. Name the segment pair
where the gap is widest. Identify the workaround that keeps the chasm in place.]

---

**EXECUTION**

Fill each table in order:

1. Run review-design --> fill Table 1
2. Run review-users --> fill Table 2
3. Run review-customers --> fill Table 3
4. Run listen-feedback --> fill Table 4
5. Run listen-adoption --> fill Table 5 (all five Rogers rows required)

After all five tables are filled, proceed to Synthesis.

---

**CROSS-SIGNAL SYNTHESIS**

Identify at least one finding confirmed or amplified across 2+ tables. The strongest cross-signal
patterns in validation campaigns: a Table 1/2/3 design friction finding whose root cause also
appears as a Table 5 adoption blocker for the same user population. When a design problem and
an inertia problem share the same population, the adoption impact is compounded.

| P-ID | Tables Linked | Finding IDs | Cross-Signal Pattern | Adoption Impact Amplification |
|------|--------------|-------------|---------------------|------------------------------|

If none: "No cross-signal patterns detected. [Name any findings that appeared related across
tables and state why they are distinct rather than the same root cause.]"

---

**RANKED FINDINGS TABLE**

All findings from Tables 1-5 that received a severity rating, ranked by Adoption Impact.

| Rank | F-ID | Table | Sub-Skill | Severity | Finding Summary | Adoption Impact (segment, ~N%) |
|------|------|-------|-----------|---------|----------------|-------------------------------|

Sort by: Adoption Impact magnitude (largest segment % first). Tiebreaker: severity (P1 > P2 > P3).
A P3 finding blocking early majority (~34%) ranks above a P1 finding affecting innovators (~2.5%).

---

**TOP BLOCKERS TABLE**

| Rank | F-ID | Source Sub-Skill | Severity | Blocker Summary | Adoption Impact (segment, ~N%) | Status-Quo Workaround | Switching Cost | Remediation |
|------|------|-----------------|---------|----------------|-------------------------------|----------------------|--------------|-------------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

Column rules:
- **Status-Quo Workaround**: "Users today [specific behavior]." Not "users have workarounds."
- **Switching Cost**: "This feature requires giving up [behavior] because [reason]."
- **Remediation**: the specific design decision that reduces the switching cost or resolves the
  blocker. Name the target: which section, which interaction, which capability.

A blocker row with a blank Status-Quo Workaround or Switching Cost field fails C-16.

---

**VERDICT**

Go / No-Go / Go with Conditions: [state one]

Rationale (2-3 sentences):
- Which top blocker drives the verdict?
- Which Rogers segment is at risk? (~N% of target population)
- If "Go with Conditions": state the condition as a testable gate. Not "improve the UX" but
  the named change that, if made, would change the verdict.

---

**EXECUTION LOG**

| Table | Sub-Skill | Status | Row Count | Empty-State Used? |
|-------|-----------|--------|----------|------------------|
| Table 1 | review-design | filled / empty | | yes / no |
| Table 2 | review-users | filled / empty | | yes / no |
| Table 3 | review-customers | filled / empty | | yes / no |
| Table 4 | listen-feedback | filled / empty | | yes / no |
| Table 5 | listen-adoption | filled / empty | 5 rows required | yes / no |

Table 5 row count must be exactly 5 (one per Rogers segment). Fewer than 5 rows = missing segment.

---

**OUTPUT**

Write all five tables (with Rogers skeleton in Table 5 and all rows filled), Cross-Signal
Synthesis, Ranked Findings, Top Blockers (with Status-Quo Workaround and Switching Cost columns),
Verdict, and Execution Log to:
simulations/{{topic}}/validate-{{date}}.md

After writing, emit: Artifact written: simulations/{{topic}}/validate-{{date}}.md
