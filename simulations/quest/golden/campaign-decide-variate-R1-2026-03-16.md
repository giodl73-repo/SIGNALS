---
skill: quest-variate
skill_target: campaign-decide
round: 1
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-decide-rubric-v1-2026-03-16.md
---

# Variations — campaign-decide / Round 1

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

---

## V-01 — Axis: Inertia Framing

**Hypothesis**: Naming inertia as "Competitor Zero" and enforcing it as a mandatory
opening section forces C-04 (inertia-first) to pass structurally, not by convention.
The phrase "before naming any product or company" is the constraint that generic prompts
omit.

```
Run the full pre-commitment decision campaign for: {{topic}}

COMPETITOR ZERO RULE: Before naming any product or company, the first question is always:
"Why would someone do nothing?" Inertia — the status quo, switching cost, good-enough
solutions, habit, risk aversion — is the primary competitor. Run scout-competitors with
inertia as the mandatory opening section.

Execute in sequence:

1. scout-competitors
   Section 1 — Inertia Analysis (required before named rivals):
     - Why people don't switch: switching cost, habit, risk, "good enough" threshold
     - What it would take for the status quo to lose
   Section 2 — Named Rivals: only after inertia is documented

2. scout-feasibility — technical constraints, team capability, timeline risk

3. scout-market — addressable market, target segment, fit score by segment

4. prove-hypothesis — core product claim + falsification condition + confidence prior

5. prove-websearch — external evidence for the hypothesis; include direct quotes

6. prove-synthesize
   Answer first: COMMIT / PAUSE / PIVOT / ABANDON
   State confidence: High / Medium / Low
   Cite evidence from steps 1-5 by section reference

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (structural enforcement), C-05 (cite by section reference).
**Risk**: The Competitor Zero framing is novel phrasing — a model unfamiliar with it may
treat it as a metaphor and skip the structural requirement.

---

## V-02 — Axis: Output Format (Table-Driven Brief)

**Hypothesis**: Providing a pre-defined table schema for each phase turns coverage into
a fill-in exercise. C-03 (all domains) and C-06 (structured format) pass by construction.
The explicit column for "Inertia / status quo" in the competitor table hard-wires C-04.

```
Run the full pre-commitment decision campaign for: {{topic}}

Execute the six sub-skills below in order. For each phase, produce the structured output
shown. Capture everything in a single decision brief artifact.

---

## Phase 1 — scout-competitors

| Force | Type | Strength (1-5) | Notes |
|-------|------|----------------|-------|
| Inertia / status quo | inertia | | Why people don't change |
| Switching cost | inertia | | What users lose by changing |
| [Named Rival A] | named | | |
| [Named Rival B] | named | | |

(Inertia rows must appear before any named rival rows.)

## Phase 2 — scout-feasibility

| Dimension | Rating (R/Y/G) | Notes |
|-----------|----------------|-------|
| Technical complexity | | |
| Team capability | | |
| Timeline | | |
| Cost | | |

## Phase 3 — scout-market

| Segment | Est. Size | Fit Score (1-10) | Priority |
|---------|-----------|-----------------|----------|
| | | | |

Primary target segment: [name it]

## Phase 4 — prove-hypothesis

Claim: [one sentence]
Falsification condition: [what would disprove this]
Confidence prior: [Low / Medium / High] — [reason]
Experiments: [list 2-3]

## Phase 5 — prove-websearch

| Source | Direct Quote | Strength | Supports / Refutes |
|--------|--------------|----------|--------------------|
| | | Weak / Moderate / Strong | |

## Phase 6 — prove-synthesize

Hypothesis outcome: [Confirmed / Refuted / Inconclusive]
Recommendation: [COMMIT / PAUSE / PIVOT / ABANDON]
Confidence: [High / Medium / Low]
Confidence rationale: [name the specific evidence gaps or strengths that drove this rating]
Because (cite by Phase):
  - [claim] because Phase [N], [section]
  - [claim] because Phase [N], [section]
Counter-evidence: [one risk or caveat]
Next step: [if COMMIT: concrete action | if no-build: exit condition or revisit trigger]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-03 (table schema per domain), C-04 (inertia rows first in table),
C-05 (explicit "because Phase N" citation), C-06 (structured format), C-08 (hypothesis
outcome row), C-09 (confidence rationale row), C-10 (next step row).
**Risk**: Table-heavy output is verbose. A model filling the schema mechanically may
satisfy the structure but produce shallow cell content.

---

## V-03 — Axis: Phrasing Register (Conversational)

**Hypothesis**: Question-driven framing ("start by asking...") reduces structural
friction and may produce more natural evidence threading. A conversational register
encourages the model to reason aloud, which tends to produce organic "because" chains
satisfying C-05.

```
You're running a full decision campaign before committing to build {{topic}}.
The goal is a recommendation you can defend — not a confirmation of a prior belief.

Work through these questions in order:

1. Who are we really competing against?
   Start with inertia: what are people doing today, and why is that good enough?
   What would it cost them to switch, even to something better?
   Only after you've answered that: who are the named alternatives?

2. Can we actually build this?
   Be honest about technical complexity, team gaps, and timeline pressure.
   Use traffic-light ratings so the feasibility picture is scannable.

3. Is there a real market?
   Size it. Pick the segment with the best fit and explain why.

4. What do we actually believe — and what would change our mind?
   Write the hypothesis: one sentence, falsifiable.
   What evidence would kill it?

5. What does the outside world say?
   Search for evidence. Quote your sources directly.
   Rate each source: weak, moderate, or strong.

6. What's the verdict?
   Answer first: COMMIT / PAUSE / PIVOT / ABANDON.
   State your confidence: High / Medium / Low.
   Explain the rating — name what drove it, not just the label.
   Show your work: link the recommendation explicitly to the evidence above.
   If committing: what is the next concrete step?
   If not: what would need to change to revisit?

Write the decision brief to: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (question 1 enforces inertia-first before named rivals),
C-05 (question 6 asks to "link the recommendation explicitly to the evidence").
**Risk**: No explicit section headers — C-06 (structured format) may not pass unless the
model naturally adds headers. The conversational tone may also reduce coverage discipline
on C-03.

---

## V-04 — Combined Axes: Lifecycle Emphasis + Inertia Framing

**Hypothesis**: Combining explicit phase gates with the inertia-first constraint turns
the campaign into a checklist that must be completed in order. Gates prevent shallow
passes and ensure each domain section exists before synthesis starts. C-04 is enforced
by the INERTIA GATE label on Phase 1; C-08 by the hypothesis outcome requirement at
Phase 6.

```
Run the full pre-commitment decision campaign for: {{topic}}

This skill runs 6 sub-skills in sequence with explicit gates. Do not advance to the
next phase until the current output is complete. Each output feeds the next.

---

### PHASE 1 — scout-competitors [INERTIA GATE]

Complete the inertia analysis before listing any named competitor:

Inertia forces (required):
- Status-quo cost: what is the hidden price of the current approach?
- Switching cost: what does a user lose by changing?
- Good-enough threshold: at what point does the current solution feel acceptable?

Only after documenting inertia: list named rivals with threat rating.

Gate check: inertia forces documented? --> proceed to Phase 2.

---

### PHASE 2 — scout-feasibility

Assess buildability across: technical complexity, team capability, timeline, cost.
Use traffic-light ratings (R/Y/G) per dimension. Surface the top risk.

Gate check: all dimensions rated, top risk named? --> proceed to Phase 3.

---

### PHASE 3 — scout-market

Size the addressable market. Rank segments by fit score (1-10).
Name the primary target segment and justify the ranking.

Gate check: primary segment named? --> proceed to Phase 4.

---

### PHASE 4 — prove-hypothesis

State the core product hypothesis. Define its falsification condition.
State confidence prior. List 2-3 experiments that would test it.

Gate check: falsification condition defined? --> proceed to Phase 5.

---

### PHASE 5 — prove-websearch

Gather external evidence for the hypothesis. For each source: direct quote, URL,
strength rating (Weak / Moderate / Strong), and whether it supports or refutes.

Gate check: minimum 3 sources gathered? --> proceed to Phase 6.

---

### PHASE 6 — prove-synthesize [DECISION GATE]

Hypothesis outcome: [Confirmed / Refuted / Inconclusive]
Recommendation: [COMMIT / PAUSE / PIVOT / ABANDON]
Confidence: [High / Medium / Low]
Confidence rationale: [name the specific evidence gaps or strengths that drove the rating]
Evidence chain: [cite Phase 1-5 findings by section]
Counter-evidence: [at least one risk or caveat]
Next step if COMMIT: [concrete action, not "do more research"]
Next step if no-build: [exit condition or revisit trigger]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-03 (gate per domain forces all six to exist), C-04 (INERTIA
GATE label + explicit pre-requisite), C-07 (counter-evidence required at Phase 6),
C-08 (hypothesis outcome required), C-09 (confidence rationale required), C-10
(conditioned next step required).
**Risk**: Gate language adds verbosity. A model may write the gate checks as prose
commentary rather than completing the actual sub-skill output.

---

## V-05 — Combined Axes: Inertia Framing + Evidence Traceability

**Hypothesis**: Targeting the two hardest essential criteria (C-04 and C-05) together
with named rules — "INERTIA-FIRST RULE" and "CITATION RULE" — makes failure on those
criteria a visible violation rather than an omission. Models respond better to
explicit prohibitions ("Floating recommendations are not acceptable") than to
implicit expectations.

```
Run the full pre-commitment decision campaign for: {{topic}}

Produce a decision brief. Every claim in the recommendation must trace back to a
specific section of the brief. Floating recommendations are not acceptable.

---

INERTIA-FIRST RULE: The competitor analysis must open with the "do nothing" analysis —
status-quo cost, switching friction, good-enough threshold — before naming any product
or company. This ordering is required, not optional.

CITATION RULE: The recommendation section must include at least three explicit
"because [Phase N, section]" citations. If you cannot cite a claim, do not assert it.

---

Execute in sequence:

1. scout-competitors
   Required: inertia forces section (status-quo cost, switching cost, good-enough
   threshold) before named rivals.
   Output: competitor table with type column (inertia / named) and threat rating.

2. scout-feasibility
   Traffic-light ratings (R/Y/G) per dimension.
   Output: feasibility summary with overall rating and top risk.

3. scout-market
   Market sizing + segment ranking by fit score (1-10).
   Output: segment table ranked by fit score; primary segment named.

4. prove-hypothesis
   Core product claim + falsification condition + confidence prior + experiments.
   Output: hypothesis card with explicit falsification condition.

5. prove-websearch
   Direct quotes, URLs, strength ratings (Weak / Moderate / Strong).
   Output: evidence table with support / refute column.

6. prove-synthesize
   Write the decision brief with this required structure:

   **Hypothesis Outcome**: [Confirmed / Refuted / Inconclusive]
   **Recommendation**: [COMMIT / PAUSE / PIVOT / ABANDON]
   **Confidence**: [High / Medium / Low]
   **Confidence rationale**: [explain what drove the rating — name specific evidence]
   **Evidence chain**:
   - [claim] because Phase [N], [section]
   - [claim] because Phase [N], [section]
   - [claim] because Phase [N], [section]
   **Counter-evidence**: [one risk or caveat that could undermine the recommendation]
   **Next step**: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting**: C-04 (INERTIA-FIRST RULE + required type column), C-05 (CITATION
RULE + at-least-three "because Phase N" citations), C-07 (counter-evidence required),
C-08 (hypothesis outcome required), C-09 (confidence rationale required), C-10
(conditioned next step required).
**Risk**: Named rules may feel heavy-handed if the model treats them as style guidance
rather than structural requirements. The output structure for Phase 6 is prescriptive —
a model that paraphrases the template headers may satisfy the form without the substance.

---

## Variation Summary

| ID | Axes | Primary Rubric Targets | Risk |
|----|------|----------------------|------|
| V-01 | Inertia framing | C-04, C-05 | Novel phrasing may not be understood as structural |
| V-02 | Output format (tables) | C-03, C-04, C-05, C-06, C-08, C-09, C-10 | Mechanical filling; shallow cell content |
| V-03 | Phrasing register (conversational) | C-04, C-05 | No explicit headers; C-06 may not pass |
| V-04 | Lifecycle emphasis + inertia framing | C-03, C-04, C-07, C-08, C-09, C-10 | Gate language may become prose commentary |
| V-05 | Inertia framing + evidence traceability | C-04, C-05, C-07, C-08, C-09, C-10 | Named rules may be treated as style, not structure |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-02 > V-01 > V-03.
V-05 directly names and enforces the two hardest essential criteria. V-03 is the most
likely to fail C-06 (format) and C-03 (coverage) due to its unstructured register.
