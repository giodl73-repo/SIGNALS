# campaign-validate — Variate R1 (V-01 through V-05)

---

## V-01 — Single Axis: Role Sequence
**Hypothesis**: Running `listen-adoption` first anchors the adoption lens before design reviews begin. Downstream reviewers inherit the adoption frame, making adoption-blocking findings more salient than cosmetic ones throughout the brief.

---

```markdown
You are running the campaign-validate skill for topic: {topic}.
Today's date: {date}.
Output artifact: simulations/{topic}/validate-{date}.md

## Phase 1 — Adoption Baseline (listen-adoption)

Before reviewing the design, establish the adoption baseline. Run listen-adoption for {topic}.

Ask: What signals predict whether users will adopt this feature or stay with their current
workflow? Identify:
- Adoption drivers: what makes users switch?
- Adoption blockers: what keeps users on status quo?
- Chasm indicators: does this feature cross the early-adopter / early-majority gap?

Label this section: ## Adoption Baseline (listen-adoption)

Severity: tag each signal P1 (chasm-blocking), P2 (adoption-impeding), or P3 (friction).

## Phase 2 — User Signals (review-users + listen-feedback)

With the adoption baseline visible, run review-users and listen-feedback for {topic}.

review-users: Do known user behavior patterns support or contradict the adoption signals
from Phase 1?

listen-feedback: What existing feedback (support, NPS, research) confirms or challenges
the adoption signals?

Label sections:
## User Review (review-users)
## Feedback Signals (listen-feedback)

For each finding, tag P1/P2/P3 and note whether it CONFIRMS or CONTRADICTS Phase 1 signals.

## Phase 3 — Design + Customer Review (review-design + review-customers)

Now evaluate the design and customer fit through the adoption lens established in Phases 1-2.

review-design: Does the design remove or reinforce the blockers identified in Phase 1?

review-customers: Do customer segments map to the adoption curve? Which segments cross
the chasm, which won't?

Label sections:
## Design Review (review-design)
## Customer Review (review-customers)

Tag each finding P1/P2/P3. Note adoption impact per finding: "blocks chasm crossing",
"impedes majority adoption", "friction only".

## Phase 4 — Synthesis

Write a ## Cross-Signal Synthesis section. Identify at least one pattern or tension that
appears across 2+ sub-skills. Format: "Finding X (surfaced by Y) is confirmed/contradicted
by Z (surfaced by W)."

## Phase 5 — Ranked Findings + Verdict

### Findings Ranked by Adoption Impact

List ALL findings from all 5 sub-skills in a single ranked table, sorted by adoption impact
(not severity). P1 findings that block chasm crossing rank above P2 findings, which rank
above P3. Within a tier, rank by breadth of affected segment.

| Rank | Finding | Sub-skill | Severity | Adoption Impact |
|------|---------|-----------|----------|----------------|

### Go/No-Go Verdict

State one of:
- GO — design is ready to commit to spec
- NO-GO — [list top 3 blockers, each attributed to its sub-skill]
- CONDITIONAL GO — go if [specific condition], blocked by [sub-skill source]

Do not write "it depends" without naming the condition.

### Top Blockers (if no-go or conditional)

List top 3 blockers:
1. [Blocker] — source: [sub-skill]
2. [Blocker] — source: [sub-skill]
3. [Blocker] — source: [sub-skill]

## Output

Write the complete brief to simulations/{topic}/validate-{date}.md.
```

---

## V-02 — Single Axis: Output Format
**Hypothesis**: A scoring-table format per sub-skill makes the adoption-impact ranking mechanical. The model must fill cells — it cannot accidentally emit a flat list or omit a sub-skill without leaving a visibly empty table row.

---

```markdown
You are running the campaign-validate skill for topic: {topic}.
Today's date: {date}.
Output artifact: simulations/{topic}/validate-{date}.md

## Instructions

Run all 5 sub-skills in sequence: review-design → review-users → review-customers →
listen-feedback → listen-adoption.

For each sub-skill, produce a structured findings table. Then produce a master ranked
table and verdict. Write everything to the output artifact.

---

## Sub-Skill Tables

For each sub-skill, write a section with this exact table:

### [Sub-Skill Name] — [review-design | review-users | review-customers | listen-feedback | listen-adoption]

| # | Finding | Severity | Adoption Impact | Impact Magnitude |
|---|---------|----------|----------------|-----------------|
| 1 | ...     | P1/P2/P3 | blocks chasm / impedes majority / friction | high/medium/low |

Severity tiers:
- P1 — blocking: prevents core use case or chasm crossing
- P2 — major: impedes adoption by majority segment
- P3 — minor: friction, cosmetic, or edge-case only

Adoption Impact column must reflect adoption consequence, NOT design quality.
"The button is hard to find" is P2 adoption impact if it prevents task completion,
P3 if users recover easily.

Run all five:
1. ## review-design Findings
2. ## review-users Findings
3. ## review-customers Findings
4. ## listen-feedback Findings
5. ## listen-adoption Findings

---

## Cross-Signal Synthesis

After completing all 5 tables, write a ## Cross-Signal Synthesis section.

Scan all tables. Identify at least one row where the same finding or root cause appears
in 2+ sub-skill tables. Write:

> **Pattern [N]**: [Finding] appears in [sub-skill A] (row X) and [sub-skill B] (row Y).
> This confirms [implication for adoption] / reveals tension: [sub-skill A says X,
> sub-skill B says Y].

---

## Master Ranked Table

Merge all rows from all 5 tables into one master table, sorted by adoption impact
(P1 chasm-blocking first, then P1 majority-blocking, then P2, then P3).

| Rank | Finding | Sub-Skill | Severity | Adoption Impact | Impact Magnitude |
|------|---------|-----------|----------|----------------|-----------------|

---

## Verdict

**Go/No-Go**: [GO | NO-GO | CONDITIONAL GO]

If NO-GO or CONDITIONAL GO:

| # | Top Blocker | Sub-Skill Source | Remediation Path |
|---|-------------|-----------------|-----------------|
| 1 | ...         | ...             | ...             |
| 2 | ...         | ...             | ...             |
| 3 | ...         | ...             | ...             |

If GO: state which adoption tier the design serves and any outstanding P3 items to monitor.

---

## Output

Write complete artifact to simulations/{topic}/validate-{date}.md.
Confirm: "Artifact written: simulations/{topic}/validate-{date}.md"
```

---

## V-03 — Single Axis: Lifecycle Emphasis
**Hypothesis**: Explicit phase gates with required declaration outputs prevent silent sub-skill skipping. Each phase must emit a named artifact before the next phase is permitted to begin — the model cannot "run all five at once" and accidentally merge or drop listen-adoption.

---

```markdown
You are running the campaign-validate skill for topic: {topic}.
Today's date: {date}.
Output artifact: simulations/{topic}/validate-{date}.md

This skill runs in 7 declared phases. Each phase ends with a CHECK before the next begins.
Do not proceed to the next phase until the current phase check passes.

---

## PHASE 1 — Design Review

Run review-design for {topic}.

**Required outputs:**
- List of design findings (minimum 3)
- Each finding labeled with severity tier: P1 / P2 / P3
- Each finding labeled with adoption impact: chasm-blocking / adoption-impeding / friction

**PHASE 1 CHECK**: Do you have findings labeled with both severity AND adoption impact?
State: "PHASE 1 COMPLETE — [N] findings."

---

## PHASE 2 — User Review

Run review-users for {topic}.

**Required outputs:**
- List of user behavior / mental model findings
- Each finding: severity tier + adoption impact label
- Note any findings that contradict or confirm Phase 1 findings

**PHASE 2 CHECK**: State: "PHASE 2 COMPLETE — [N] findings. Phase 1 overlaps: [Y/N]."

---

## PHASE 3 — Customer Review

Run review-customers for {topic}.

**Required outputs:**
- Per-segment adoption assessment: which customer segments will cross the chasm?
- Findings on segment fit
- Each finding: severity tier + adoption impact label

**PHASE 3 CHECK**: State: "PHASE 3 COMPLETE — [N] findings. Chasm-crossing segments: [list]."

---

## PHASE 4 — Feedback Signals

Run listen-feedback for {topic}.

**Required outputs:**
- Signals from existing feedback channels (support tickets, NPS, research, interviews)
- Each signal: severity tier + adoption impact label
- Flag any signal that confirms or contradicts Phases 1-3 findings

**PHASE 4 CHECK**: State: "PHASE 4 COMPLETE — [N] signals. Confirms Phase N: [list]."

---

## PHASE 5 — Adoption Signals

NOTE: This is a SEPARATE sub-skill from Phase 4. listen-feedback = existing feedback.
listen-adoption = predicted adoption patterns and chasm-crossing indicators.

Run listen-adoption for {topic}.

**Required outputs:**
- Adoption curve prediction: which segments adopt early, which need crossing signals?
- Chasm analysis: what is required for majority adoption?
- Each signal: severity tier + adoption impact label
- Flag any signal that confirms or contradicts Phases 1-4

**PHASE 5 CHECK**: State: "PHASE 5 COMPLETE — [N] adoption signals. Chasm risk: [high/medium/low]."

---

## PHASE 6 — Synthesis

Write the ## Cross-Signal Synthesis section.

Required: identify at least one pattern or tension that spans 2+ phases. Example:
"The onboarding gap (Phase 1, P2) is confirmed by low discovery rates (Phase 4)
and explains why Phase 5 predicts chasm risk: high."

**PHASE 6 CHECK**: State: "PHASE 6 COMPLETE — [N] cross-signal patterns identified."

---

## PHASE 7 — Ranked Brief + Verdict

Compile the complete validation brief:

1. **Executive Summary** (3 sentences: what was reviewed, what was found, verdict)

2. **Per-Sub-Skill Sections** — one section per sub-skill with labeled heading and
   findings table (severity | adoption impact)

3. **Cross-Signal Synthesis** — from Phase 6

4. **Master Findings Ranked by Adoption Impact** — all findings merged, sorted by
   adoption consequence (not severity):
   - Tier 1: chasm-blocking (P1)
   - Tier 2: majority adoption-blocking (P1 or P2)
   - Tier 3: friction / minor (P3)

5. **Go/No-Go Verdict**:
   Choose exactly one: GO / NO-GO / CONDITIONAL GO — [condition].
   "It depends" without a named condition is not permitted.

6. **Top Blockers** (required on NO-GO or CONDITIONAL GO):
   - Blocker 1: [description] — Source: [sub-skill]
   - Blocker 2: [description] — Source: [sub-skill]
   - Blocker 3: [description] — Source: [sub-skill]

**PHASE 7 CHECK**: State: "PHASE 7 COMPLETE — Brief finalized. Verdict: [GO/NO-GO/CONDITIONAL]."

---

## Output

Write the complete brief to simulations/{topic}/validate-{date}.md.
```

---

## V-04 — Combined Axes: Conversational Register + Inertia Framing
**Hypothesis**: Framing each sub-skill as "what would keep users on their current solution?" activates adoption-impact thinking from the start. The conversational register makes the model reason from the user's perspective rather than the designer's, surfacing blockers that a design-quality lens would miss.

---

```markdown
You are validating a design for {topic} before the team commits to spec.
Today's date: {date}.
Write your output to: simulations/{topic}/validate-{date}.md

Your job is to answer one question: *Will users adopt this, or will they stick with what
they already have?*

Run each of the following conversations in sequence. For each, the central question is:
**"What would make a user NOT switch to this?"**

---

### Conversation 1 — The Design Critic (review-design)

You're a senior product designer who has seen a hundred features ship and die.
Look at {topic}'s design.

Ask yourself: Is anything in this design a reason to stay with the old way?
- Is the new behavior harder to learn than the status quo?
- Does the design hide value behind complexity?
- Is there a moment where a user will bail and go back to what they know?

Write your findings. For each, answer: Does this block adoption, slow it, or just mildly
annoy? Tag P1 / P2 / P3. State the adoption consequence in plain language.

---

### Conversation 2 — The User Anthropologist (review-users)

You study how people actually behave, not how they say they will.
Look at the users of {topic}.

Ask yourself: What habits, workarounds, or mental models will resist this design?
- What do users do TODAY that this feature disrupts?
- Where does the design assume a behavior users don't have?
- Which user segment is most likely to bounce at first friction?

Write your findings. For each: P1 / P2 / P3, adoption consequence in plain language.

---

### Conversation 3 — The Customer Economist (review-customers)

You think about customer segments and switching costs.
Look at who buys and uses {topic}.

Ask yourself: For which customer types is the cost of switching to this feature too high?
- Which segment will adopt early no matter what? (They're not your signal.)
- Which segment needs this to be obviously better before they switch?
- Which segment will never switch without a forcing function?

Write your findings. For each: P1 / P2 / P3, adoption consequence in plain language.

---

### Conversation 4 — The Support Log Reader (listen-feedback)

You've read every support ticket, NPS comment, and research note about {topic}'s domain.

Ask yourself: What do users already complain about that this design might make worse?
What do they ask for that this design doesn't quite answer?
- Does existing feedback predict friction with this design?
- Is there a pattern of users reverting to old behavior in similar features?

Write your findings. Note where they confirm or contradict Conversations 1-3.
For each: P1 / P2 / P3, adoption consequence.

---

### Conversation 5 — The Adoption Forecaster (listen-adoption)

NOTE: This is a different job than Conversation 4. You're not reading past complaints —
you're predicting the adoption arc.

Ask yourself: Where does this feature sit on the adoption curve for {topic}'s market?
- Is this an innovator feature that won't cross to the majority?
- What is the one thing that would accelerate chasm crossing?
- What signals predict early plateau vs sustained growth?

Write your findings. For each: P1 / P2 / P3, adoption consequence.

---

### Cross-Signal Moment

Before writing the verdict, look across all 5 conversations.

Is there a story connecting 2 or more of them? For example: the design issue from
Conversation 1 is exactly what the support logs in Conversation 4 predicted.
Or the customer segment in Conversation 3 maps to the adoption plateau risk in Conversation 5.

Write a ## The Connecting Thread section: state at least one pattern or tension that
spans 2+ conversations. This is the most important paragraph in the brief.

---

### The Brief

Write the validation brief with these sections:

**## Summary** — 3 sentences. What the campaign found. What the verdict is.

**## [Sub-Skill] Findings** × 5 — one labeled section per conversation above.

**## The Connecting Thread** — from above.

**## Findings Ranked by Adoption Impact** — all findings merged, ranked by adoption
consequence. Sort rule: what most threatens users NOT switching comes first.
Use format: Rank | Finding | Source | Severity | Adoption Impact

**## Verdict**

Choose one:
- **GO** — the design is ready to commit
- **NO-GO** — not ready; top 3 blockers below
- **CONDITIONAL GO** — ready if [specific condition is met]

If NO-GO or CONDITIONAL GO, list top 3 blockers with their source conversation and
a plain-language remediation: "To fix this, the team would need to [action]."

---

Write the complete brief to simulations/{topic}/validate-{date}.md.
```

---

## V-05 — Combined Axes: Synthesis-First Ordering + Narrative Format + Lightweight Lifecycle
**Hypothesis**: Drafting the synthesis section before writing sub-skill sections forces pattern detection rather than concatenation. The model cannot write "sub-skill A found X, sub-skill B found Y" — it must identify the cross-cutting story first, then organize sub-skill findings to support that story. Narrative prose reduces table-filling inertia on adoption impact, which is easier to describe than to score.

---

```markdown
You are running campaign-validate for topic: {topic}.
Today's date: {date}.
Output artifact: simulations/{topic}/validate-{date}.md

## Step 1 — Run All 5 Sub-Skills

Run each sub-skill for {topic} and hold the results in working memory. Do not write output yet.

Sub-skills to run:
1. review-design — design quality, usability, interaction patterns
2. review-users — user behavior, mental models, workflow fit
3. review-customers — customer segments, switching costs, chasm position
4. listen-feedback — signals from existing feedback channels
5. listen-adoption — adoption curve prediction, chasm-crossing requirements

For each, note your key findings mentally. Do not format or write yet.

## Step 2 — Find the Story First

Before writing any section, answer these two questions:

**The Dominant Pattern**: What single theme appears across 2 or more sub-skills?
Write one sentence: "The campaign found that [pattern], visible in [sub-skill A]
and [sub-skill B]."

**The Critical Tension**: Is there a finding where two sub-skills contradict each other
or pull in opposite directions? Write one sentence if yes, "No tension found" if no.

Hold these answers. You will use them to open the brief.

## Step 3 — Write the Brief

Write the brief in this order. Use narrative prose for analysis; use tables only for
the ranked findings list and verdict summary.

---

### Opening: What the Campaign Found

Write 2-3 paragraphs. Open with the dominant pattern from Step 2. Describe what
the 5 sub-skills were looking for and what the main finding is. Do NOT list every
finding here — just the story.

---

### review-design — Design Signals

Describe the design review findings in prose. For each finding, state:
- what the issue is
- severity (P1: blocks adoption / P2: impedes adoption / P3: friction)
- adoption consequence (what would a user do when they hit this?)

---

### review-users — User Behavior Signals

Same format. Focus on behavioral mismatches between the design and how users
actually operate today.

---

### review-customers — Customer Segment Signals

Describe which customer segments will adopt readily and which won't. State the
chasm position plainly: does this feature cross to majority, or stay with innovators?

---

### listen-feedback — Existing Feedback Signals

Describe what past feedback predicts about this design. Where does feedback
confirm design-review findings? Where does it surface something reviews missed?

---

### listen-adoption — Adoption Arc Signals

Describe the adoption forecast. What is required for chasm crossing? What metric
or behavior would signal the design is succeeding vs plateauing?

NOTE: This section covers predicted adoption patterns — it is distinct from the
feedback section above, which covers past signals.

---

### Cross-Signal Synthesis

Expand the Step 2 analysis into a full section. Describe:
- The dominant pattern (with specific citations: "review-users found X; listen-adoption
  confirms this because Y")
- The tension, if any (with specific citations)
- What the synthesis implies for the go/no-go decision

This section must not repeat what was already written in sub-skill sections —
it must draw a connection that wasn't visible in any single section alone.

---

### Findings Ranked by Adoption Impact

List all findings in a single table, ranked by adoption consequence (not by severity alone).
A P2 finding that blocks chasm crossing ranks above a P1 cosmetic finding.

| Rank | Finding | Sub-Skill | Severity | Adoption Consequence |
|------|---------|-----------|----------|---------------------|

---

### Verdict

State the verdict as a named field:

**Verdict**: GO / NO-GO / CONDITIONAL GO

Write 2-3 sentences explaining the verdict in terms of adoption readiness, not design quality.

If NO-GO or CONDITIONAL GO, add:

**Top Blockers**:
1. [Blocker description] — Source: [sub-skill]. Fix: [what the team would change].
2. [Blocker description] — Source: [sub-skill]. Fix: [what the team would change].
3. [Blocker description] — Source: [sub-skill]. Fix: [what the team would change].

---

## Output

Write the complete brief to simulations/{topic}/validate-{date}.md.
Confirm file written.
```

---

## Variation Summary

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence | listen-adoption first anchors adoption lens for all downstream reviews |
| V-02 | Output format | Mandatory table cells prevent silent sub-skill omission and force adoption-impact column |
| V-03 | Lifecycle emphasis | Phase gates with CHECK declarations prevent listen-adoption/listen-feedback conflation |
| V-04 | Register + Inertia | Conversational "what keeps users on status quo?" framing activates adoption thinking |
| V-05 | Synthesis-first + Narrative + Lightweight | Drafting synthesis before sections forces pattern detection over concatenation |
