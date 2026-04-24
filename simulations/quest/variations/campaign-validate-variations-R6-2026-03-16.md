## campaign-validate Skill Body — R6 Variations

---

### V-01
**Axis:** Role sequence — `review-code` anchors first
**Hypothesis:** Running `review-code` first establishes a hard technical floor before UX and adoption signals layer in, ensuring code-level blockers are never discovered late and buried in the adoption narrative.

---

```
You are running a full design validation campaign for topic: {{topic}}.

The campaign orchestrates five sub-skills in this sequence:
  1. review-code      — technical floor (what breaks or blocks shipment)
  2. review-design    — design quality and spec coherence
  3. review-users     — usability and user-task alignment
  4. listen-feedback  — existing feedback signal from users or stakeholders
  5. listen-adoption  — Rogers diffusion readiness across innovators → laggards

Run each sub-skill in order. Do not skip or reorder. Do not substitute
review-customers for review-code — these are different lenses and
review-customers does not satisfy C-01.

---

PHASE 1 — review-code

Analyze the implementation or spec for: correctness of contracts, edge-case
handling, schema constraints, performance implications, and any hard blockers
to shipment. Label all findings P1 (blocker), P2 (significant), or P3 (minor).
For every P1 finding, name the status-quo workaround users currently rely on.

---

PHASE 2 — review-design

Analyze the design for: internal consistency, alignment with prior spec signals,
conceptual integrity, and adherence to platform conventions. Rate each finding
by its adoption impact (not its severity). A conceptual confusion that will
block early-majority adoption outranks a polish gap that affects only power users.

---

PHASE 3 — review-users

Analyze the user experience for: task completion clarity, friction points,
cognitive load, and discoverability. For each finding, estimate the user segment
most affected: innovators, early adopters, early majority, late majority,
or laggards. Weight your finding's adoption-impact score accordingly.

---

PHASE 4 — listen-feedback

Synthesize existing feedback signals (interviews, support tickets, prior
research, or stated user pain points). Distinguish feedback from adoption
posture: feedback is what users said; adoption posture is what that implies
about their switching readiness. Do not collapse these into one signal.

---

PHASE 5 — listen-adoption

Apply the Rogers diffusion model. For each segment (innovators ~2.5%,
early adopters ~13.5%, early majority ~34%, late majority ~34%, laggards ~16%),
estimate whether the design as-is would unlock or block adoption. Name the
single biggest friction per segment. This is the input to the adoption-impact
ranking in your final output.

---

OUTPUT FORMAT

Write your validation brief in this structure:

## Sub-Skill Results

For each of the five sub-skills, write a labeled section:
### review-code | review-design | review-users | listen-feedback | listen-adoption
Include a table skeleton per sub-skill:
| Finding | Severity | Affected Segment | Adoption Impact |
Even if empty, the table must appear (confirmed-empty if no findings).
Adoption Impact and Severity are separate columns — do not merge them.

## Ranked Findings

Rank all findings across all five sub-skills by adoption impact (not severity).
Adoption impact = estimated % of user base for whom this finding is a friction
or blocker at or before the early-majority crossing.

Format:
| Rank | Finding | Source Sub-Skill | Severity | Adoption Impact (segment, ~N%) |

## P1 Blockers and Remediation

List all P1 findings. For each:
| Blocker | Source Sub-Skill | Status-Quo Workaround | Remediation Path |

Remediation paths belong in this table as a required column.
Do not move remediation into the verdict section prose.

## Cross-Signal Synthesis

Name at least 3 relationships that are not visible in any single sub-skill alone.
Each row must name a relationship that only emerges when two or more sub-skills
are read together.

| Signal A | Signal B | Emergent Relationship (not visible in either alone) |

## Rogers Readiness

| Segment | ~% | Adoption Status | Primary Blocker |
Name all five segments. Include % anchors.

## Verdict

State one of: GO / NO-GO / CONDITIONAL GO (condition: [specific, actionable]).
"It depends" without a named condition is not a valid verdict.

---

After writing the brief, write the artifact to:
  simulations/{{topic}}/validate-{{date}}.md

Confirm with: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`
```

---

### V-02
**Axis:** Output format — five dedicated tables, one per analytical concern
**Hypothesis:** Mandating exactly one table per analytical concern makes absent content a visible blank rather than absent prose, enforcing completeness structurally rather than through author discipline.

---

```
You are running a design validation campaign for topic: {{topic}}.

Your output must be organized as exactly five tables, each serving one analytical
concern and no other. No table covers two concerns. No concern shares a table.
A missing table is a failing gap, not missing prose.

The five tables and their single purposes:
  T1 — Sub-skill coverage (one row per sub-skill; confirms execution)
  T2 — Ranked findings (all findings sorted by adoption impact)
  T3 — P1 blockers with remediation (blockers only; remediation as column)
  T4 — Cross-signal synthesis (relationships invisible in any single sub-skill)
  T5 — Rogers segment readiness (all five segments with % anchors)

---

EXECUTION SEQUENCE

Run these five sub-skills. Do not omit any. Do not substitute review-customers
for review-code.

  review-design    — spec coherence, design quality, conceptual integrity
  review-users     — task completion, friction, discoverability
  listen-feedback  — existing user feedback synthesized as signals
  listen-adoption  — Rogers diffusion readiness per segment
  review-code      — technical correctness, contracts, hard blockers

Listen-feedback and listen-adoption are categorically separate: feedback is what
users said; adoption posture is what that implies about switching readiness.
Treat them as distinct inputs. Do not let one substitute for the other.

---

T1 — Sub-Skill Coverage

| Sub-Skill | Status | Finding Count | Notes |
|---|---|---|---|
| review-design | [RAN / EMPTY] | N | |
| review-users | [RAN / EMPTY] | N | |
| listen-feedback | [RAN / EMPTY] | N | |
| listen-adoption | [RAN / EMPTY] | N | |
| review-code | [RAN / EMPTY] | N | |

All five rows required. EMPTY is valid; absent row is not.

---

T2 — Ranked Findings

Rank by adoption impact. Adoption impact = estimated % of user base for whom
this finding creates friction or blocks crossing at or before the early majority.
Severity is noted but does not govern rank order.

| Rank | Finding | Source Sub-Skill | Severity (P1/P2/P3) | Adoption Impact (segment, ~N%) |
|---|---|---|---|---|

Adoption Impact is a dedicated column. It must not be merged with Severity.

---

T3 — P1 Blockers and Remediation

Include only P1 findings here. Remediation appears as a required column in this
table. Remediation paths must NOT appear in the verdict section prose — placing
them there instead of here fails this criterion unconditionally.

| Blocker | Source Sub-Skill | Status-Quo Workaround | Remediation Path |
|---|---|---|---|

If no P1 blockers, write one row: "No P1 blockers identified | — | — | —"

---

T4 — Cross-Signal Synthesis

Each row names a relationship that is invisible in either contributing sub-skill
alone. A row that summarizes a single sub-skill's finding fails the per-row
anti-concatenation constraint.

Anti-concatenation test: "Would this relationship be apparent if I read only
Sub-skill A? Only Sub-skill B? If yes to either, rewrite the row."

| Signal A (sub-skill + finding) | Signal B (sub-skill + finding) | Emergent Relationship — not visible in either alone |
|---|---|---|

Minimum 3 rows. Each row must pass the anti-concatenation test.

---

T5 — Rogers Segment Readiness

| Segment | ~% | Adoption Status (READY / AT RISK / BLOCKED) | Primary Friction |
|---|---|---|---|
| Innovators | ~2.5% | | |
| Early Adopters | ~13.5% | | |
| Early Majority | ~34% | | |
| Late Majority | ~34% | | |
| Laggards | ~16% | | |

All five rows required with % anchors filled in.

---

VERDICT

State: GO / NO-GO / CONDITIONAL GO (condition: [specific, actionable]).
Conditional GO requires the condition to be named exactly — not "when issues
are resolved" but "when P1 blocker [name] receives remediation [path]."

---

Write the artifact to: simulations/{{topic}}/validate-{{date}}.md
Confirm: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`
```

---

### V-03
**Axis:** Inertia framing — status-quo competitor foregrounded throughout
**Hypothesis:** Anchoring every sub-skill analysis to the named status-quo behavior produces adoption-impact scores grounded in switching cost rather than abstract UX quality, making the ranked findings list directly actionable for adoption decisions.

---

```
You are running a design validation campaign for topic: {{topic}}.

Before beginning, name the status-quo: what do users do today, without this
feature? Name it explicitly. This is the incumbent behavior. Every finding you
surface must answer: does this finding increase or decrease the switching cost
relative to the incumbent? Adoption-impact scores are meaningless without a
baseline to switch from.

---

STATUS-QUO DECLARATION

State:
- Current workaround (what users do today)
- Why they do it (job-to-be-done the workaround satisfies)
- Switching friction today (what makes the status quo sticky)

This declaration is the inertia anchor for all five sub-skills below.

---

PHASE 1 — review-design

Review the design for spec coherence, conceptual integrity, and alignment with
platform conventions. For each finding, state:
- Does it increase switching cost? (makes the new feature harder to adopt than
  the incumbent workaround)
- Does it decrease switching cost? (removes friction versus the incumbent)

Only findings that reduce switching cost below the incumbent's level are genuine
adoption accelerators. Flag any design choice that preserves incumbent friction
without a deliberate reason.

---

PHASE 2 — review-users

Review the user experience for task completion, friction, and discoverability.
For each finding, compare against the equivalent step in the incumbent workflow.
A friction point that is equal to or worse than the incumbent is an adoption risk,
regardless of its absolute UX quality. Rate adoption impact using:
  HIGH — blocks early-majority crossing
  MEDIUM — slows early-majority crossing
  LOW — friction exists but does not impede crossing

---

PHASE 3 — listen-feedback

Synthesize existing feedback signals. Frame each signal relative to the incumbent:
is this feedback about the new feature failing to match what users already do, or
about the new feature failing to exceed it? These are distinct failure modes.

Do not merge feedback signals with adoption posture. Feedback is what users said;
adoption posture is what that implies about their willingness to switch.

---

PHASE 4 — listen-adoption

Apply the Rogers diffusion model with the incumbent as the reference.

For each segment, answer: "Given the status quo, would a user in this segment
switch today? What is the single friction preventing or enabling that switch?"

| Segment | ~% | Switch? (YES/AT-RISK/NO) | Key Switching Friction vs Incumbent |
|---|---|---|---|
| Innovators | ~2.5% | | |
| Early Adopters | ~13.5% | | |
| Early Majority | ~34% | | |
| Late Majority | ~34% | | |
| Laggards | ~16% | | |

---

PHASE 5 — review-code

Review the implementation for correctness, contract integrity, and hard blockers.
For each P1 finding, state: does this blocker exist in the incumbent? If the
incumbent has no equivalent failure mode, the switching cost is asymmetric and
the finding is an adoption blocker, not just a technical bug.

For every P1 blocker, name:
- Status-quo workaround (what users do today when this scenario arises)
- Remediation path (specific, actionable fix)

---

OUTPUT

## Sub-Skill Results
One labeled section per sub-skill. Table skeleton in each:
| Finding | Severity | Incumbent Comparison | Adoption Impact |
Adoption Impact and Severity are separate columns.

## Ranked Findings
Rank by adoption impact (% blocked at or before early-majority crossing).
| Rank | Finding | Source Sub-Skill | Severity | Adoption Impact (segment, ~N%) | vs Incumbent |

## P1 Blockers
| Blocker | Source Sub-Skill | Incumbent Has This? | Status-Quo Workaround | Remediation Path |
Remediation is a column here. It does not appear in the verdict section.

## Cross-Signal Synthesis
At least 3 rows. Each row names a relationship across two or more sub-skills
that is not visible in either sub-skill alone. Inertia patterns that emerge
across multiple sub-skills are strong candidates.
| Signal A | Signal B | Emergent Relationship (not visible in either alone) |

## Verdict
GO / NO-GO / CONDITIONAL GO (condition: [specific, actionable]).
State the verdict relative to the incumbent: does this feature create enough
switching motivation to move the early majority off the status quo?

---

Write artifact to: simulations/{{topic}}/validate-{{date}}.md
Confirm: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`
```

---

### V-04
**Axis:** Phrasing register — imperative with explicit completion gates
**Hypothesis:** Imperative phrasing with named completion checkpoints between sub-skills eliminates silent omission by making each phase's completion a required condition for proceeding, not an assumption.

---

```
Run a full design validation campaign for: {{topic}}.

You must complete all five phases. Each phase has a completion gate. Do not
proceed to the next phase until you have satisfied the gate condition for the
current phase.

---

PHASE 1 — review-code
Gate: You have found and labeled all findings P1/P2/P3. Every P1 finding has
      a status-quo workaround named and a remediation path named.

Review the implementation or spec for technical correctness, contract integrity,
edge-case handling, and hard blockers to shipment. Label P1 (blocker), P2
(significant), P3 (minor). Do not skip this phase. Do not rename it to
review-customers. A completed phase produces at minimum an empty confirmed table.

Gate check: "Have I labeled all findings? Have I named a workaround and
remediation for every P1? If not, complete this phase before continuing."

---

PHASE 2 — review-design
Gate: You have rated every finding by adoption impact (not severity).

Review the design for spec coherence, conceptual integrity, and design quality.
For each finding, rate its adoption impact: HIGH (blocks early-majority crossing),
MEDIUM (slows crossing), LOW (friction, does not impede crossing).

Gate check: "Does every finding have an adoption impact rating separate from
its severity tier? If not, add the column before continuing."

---

PHASE 3 — review-users
Gate: You have named the affected Rogers segment for every finding.

Review the user experience for task completion, friction, cognitive load, and
discoverability. For each finding, name the segment most likely to be blocked:
innovators, early adopters, early majority, late majority, or laggards.

Gate check: "Does every finding have an affected segment? If not, fill it in
before continuing."

---

PHASE 4 — listen-feedback
Gate: You have distinguished feedback (what users said) from adoption posture
      (what that implies about switching readiness). These are different signals.

Synthesize existing feedback signals. Write findings as feedback observations,
not adoption conclusions. You will connect them to adoption posture in Phase 5
and in the cross-signal synthesis table — not here.

Gate check: "Are my feedback findings stated as observations, not as adoption
verdicts? If adoption posture has crept into this section, move it to Phase 5."

---

PHASE 5 — listen-adoption
Gate: All five Rogers segments named with % anchors and a finding per segment.

Apply the Rogers diffusion model. For each segment, name the single largest
friction point and estimate whether the design as-is would enable or block
adoption crossing.

Segments: Innovators (~2.5%), Early Adopters (~13.5%), Early Majority (~34%),
Late Majority (~34%), Laggards (~16%).

Gate check: "Are all five segments represented? Do all have % anchors? If any
segment is missing, complete it before writing the output."

---

OUTPUT

Write the validation brief. Use this structure exactly.

### review-code
Table: | Finding | Severity | Status-Quo Workaround | Adoption Impact |
(Confirmed empty if no findings — do not omit the section.)

### review-design
Table: | Finding | Severity | Adoption Impact (HIGH/MEDIUM/LOW) |

### review-users
Table: | Finding | Severity | Affected Segment | Adoption Impact |

### listen-feedback
Table: | Feedback Signal | Source | Severity |

### listen-adoption
Table: | Segment | ~% | Adoption Status | Primary Friction |

## Ranked Findings
Rank by adoption impact. Severity informs but does not govern rank.
Table: | Rank | Finding | Source Sub-Skill | Severity | Adoption Impact (segment, ~N%) |

## P1 Blockers and Remediation
Table: | Blocker | Source Sub-Skill | Status-Quo Workaround | Remediation Path |
Remediation is a column in this table. It must not appear as prose in the verdict.

## Cross-Signal Synthesis
Table: | Signal A | Signal B | Emergent Relationship — not visible in either alone |
Minimum 3 rows. Per-row test: "Is this relationship visible in Signal A alone?
In Signal B alone? If yes to either, the row fails — rewrite it."

## Rogers Readiness
Table: | Segment | ~% | Status (READY / AT RISK / BLOCKED) | Primary Blocker |
All five segments. % anchors required.

## Verdict
State: GO / NO-GO / CONDITIONAL GO (condition: [specific]).
"It depends" is not a verdict. A conditional verdict names the exact condition.

---

Write artifact to: simulations/{{topic}}/validate-{{date}}.md
Confirm with: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`
```

---

### V-05
**Axis:** Combined — table architecture (V-02) + inertia framing (V-03) + Rogers-cascade-by-schema
**Hypothesis:** Designing the schema so that each criterion cluster is satisfied by a single structural decision — one table, one column, one constraint — maximizes aspirational criteria density while keeping the prompt learnable. Inertia framing grounds adoption-impact scores in switching cost rather than abstract quality.

---

```
You are running a design validation campaign for topic: {{topic}}.

This campaign satisfies its scoring criteria through schema design, not
author discipline. Every criterion you need to satisfy is encoded as a
structural requirement: a required table, a required column, or a required
per-row constraint. Follow the schema and the criteria are satisfied by
construction.

---

PRE-FLIGHT: NAME THE INCUMBENT

Before running any sub-skill, state:
  Incumbent: [what users do today without this feature]
  Switching friction: [why the incumbent is sticky]

This is the inertia anchor. Every adoption-impact rating is relative to it.

---

EXECUTION

Run these five sub-skills. Do not omit any. Do not reorder the listen phases —
listen-feedback (what users said) runs before listen-adoption (what that means
for switching). They are categorically separate; do not let one absorb the other.

  1. review-design
  2. review-users
  3. listen-feedback
  4. listen-adoption
  5. review-code

For each sub-skill, produce the phase table below, then proceed to the next.

Phase table schema (required for every sub-skill):
| Finding | Severity (P1/P2/P3) | Adoption Impact (segment, ~N%) | vs Incumbent |

"vs Incumbent" is: BETTER (lower switching cost) / SAME / WORSE (higher switching cost).
Adoption Impact and Severity are separate columns. Do not merge them.

---

FIVE OUTPUT TABLES — ONE PER ANALYTICAL CONCERN

After running all five sub-skills, produce exactly five tables.
No table combines two concerns. A missing table is a visible gap.

---

TABLE 1 — Sub-Skill Coverage

One row per sub-skill. Confirms execution. Status must be RAN or EMPTY-CONFIRMED.
An absent row means the sub-skill was silently skipped — this fails C-01.

| Sub-Skill | Status | Finding Count | P1 Count |
|---|---|---|---|
| review-design | | | |
| review-users | | | |
| listen-feedback | | | |
| listen-adoption | | | |
| review-code | | | |

---

TABLE 2 — Ranked Findings

All findings across all five sub-skills. Rank by adoption impact.
Adoption impact = % of user base for whom this finding creates friction
at or before the early-majority crossing. Severity informs but does not govern.

| Rank | Finding | Source Sub-Skill | Severity | Adoption Impact (segment, ~N%) | vs Incumbent |
|---|---|---|---|---|---|

---

TABLE 3 — P1 Blockers and Remediation

P1 findings only. Remediation is a required column in this table.
Remediation paths must NOT appear in the verdict section.
This column enforces: every P1 blocker gets a remediation path by construction.

| Blocker | Source Sub-Skill | Status-Quo Workaround | Remediation Path |
|---|---|---|---|

If no P1 blockers: one row — "No P1 blockers | — | — | —"

---

TABLE 4 — Cross-Signal Synthesis

Each row must satisfy the anti-concatenation constraint:
"This relationship is NOT visible in Signal A alone. NOT visible in Signal B alone.
It only emerges when both are read together."

If a row would be visible by reading only one sub-skill, rewrite it.

| Signal A (sub-skill: finding) | Signal B (sub-skill: finding) | Emergent Relationship — not visible in either alone |
|---|---|---|

Minimum 3 rows. Each row is independently testable against the constraint.

---

TABLE 5 — Rogers Segment Readiness

Schema designed so that one pass through this table satisfies:
C-09 (% anchors), C-15 (all five segments named), and the Rogers dimension
of C-02 (adoption impact grounding).

| Segment | ~% | Switch Readiness vs Incumbent | Primary Friction | Inertia Driver |
|---|---|---|---|---|
| Innovators | ~2.5% | | | |
| Early Adopters | ~13.5% | | | |
| Early Majority | ~34% | | | |
| Late Majority | ~34% | | | |
| Laggards | ~16% | | | |

"Switch Readiness vs Incumbent": READY / AT RISK / BLOCKED.
"Inertia Driver": the specific incumbent behavior that makes this segment sticky.

---

VERDICT

State: GO / NO-GO / CONDITIONAL GO (condition: [specific, actionable]).
The verdict must reference the Rogers readiness table: which segment gates GO?
"It depends" without a named condition fails unconditionally.

If CONDITIONAL GO, the condition must be traceable to a row in Table 3
(a P1 blocker with a named remediation path).

---

Write artifact to: simulations/{{topic}}/validate-{{date}}.md
Confirm: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`
```

---

## Variation Summary

| ID | Axis | Key Structural Bet | Primary Criteria Targeted |
|----|------|--------------------|--------------------------|
| V-01 | Role sequence (review-code first) | Technical floor established before UX signals; blockers can't be buried | C-01, C-04, C-10, C-16 |
| V-02 | Output format (5 dedicated tables) | Missing table = visible gap; remediation column enforced by table structure | C-20, C-21, C-22, C-11, C-12 |
| V-03 | Inertia framing throughout | Every finding rated relative to incumbent; adoption-impact scores grounded in switching cost | C-16, C-18, C-09, C-02 |
| V-04 | Imperative register + completion gates | Phase gate forces author to satisfy column requirements before proceeding | C-01, C-07, C-14, C-08 |
| V-05 | Combined (tables + inertia + Rogers-cascade-by-schema) | Schema designed so one structural decision satisfies an entire criterion cluster | C-17, C-20, C-21, C-22, C-15, C-09 |
