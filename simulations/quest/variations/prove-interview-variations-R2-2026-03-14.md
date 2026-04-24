Written to `simulations/quest/variations/prove-interview-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — prove-interview

Five complete prompts targeting the new v2 criteria (C-11 Disposition arc, C-12 Critical contradiction ranked).

---

### V-01: Role Sequence + Pre-Synthesis Arc Diagnosis (C-11 primary)
**Single-axis.** Inherits R1 V-03's Champion/Neutral/Skeptic ordering. New element: a mandatory **Arc Diagnosis checkpoint** after the Skeptic and *before* synthesis. Forces a binary commitment (convergence-dominant / contradiction-dominant) with a rationale before conclusions are written. Includes an explicit arc red-flag check (Skeptic confirmed Champion without resistance = profile failure). Once committed, C-11 in synthesis is a structural carrythrough.

### V-02: Output Format — Ranked Contradiction Inventory (C-12 primary)
**Single-axis.** Minimal structural change: one new section (Contradiction Inventory) inserted between evidence extraction and synthesis. **Column asymmetry is the mechanism**: Rank 1 has a required `Evidential weight` field; lower ranks do not. The model cannot treat all contradictions as equal when one row has a required column others lack. Does not require disposition ordering — tests whether C-12 is format-neutral for role sequence.

### V-03: Lifecycle — Two-Phase Synthesis (C-11 + C-12 via dedicated phase)
**Single-axis.** Synthesis splits into Phase 4A (C-09 content: patterns, convergences, strongest signal) and Phase 4B (arc analysis: C-11/C-12 content). Phase 4A gate prevents arc analysis from merging with evidence summary. Phase 4B questions are explicitly unanswerable by restating Phase 4A — "Was convergence despite skepticism dominant?" cannot be answered with an evidence list. Tests lifecycle separation alone, without role-sequence enforcement.

### V-04: Disposition Arc + Current-Practice Q1 (C-05 + C-11 combination)
**Combination.** Direct answer to R1's open research question: combine R1 V-03 (disposition ordering) with R1 V-05 (current-practice Q1 anchor). Each disposition gets a declared `current-practice` field. The Skeptic's current practice grounds their resistance in behavior ("three past automation attempts failed at vendor questionnaire stage") rather than just stance. Addresses both R1 partial-credit gaps simultaneously — C-05 (behavioral baseline) and C-11 (disposition arc) — plus named critical contradiction targeting C-12.

### V-05: Full R2 Ceiling Candidate (all axes)
**Combination.** All primary mechanisms: disposition ordering, current-practice Q1, INTERVIEWER:/SUBJECT: transcript format, EVIDENCE PULL with verbatim Quote column, ranked Contradiction Inventory with **both-sides SUBJECT quotes required at Rank 1**, and **quote-required arc synthesis** (every C-11/C-12 claim must cite a SUBJECT turn). Quote-anchoring the arc synthesis makes C-11 and C-12 structurally gradable rather than asserted — the same shift C-04/C-10 made for evidence and confidence.

---

**R2 open research questions:**
1. Arc Diagnosis checkpoint (V-01) vs. Phase 4B arc phase (V-03) — which produces more reliable C-11 coverage?
2. Does Rank 1 column asymmetry alone produce C-12 PASS (V-02), or does the content instruction for "evidential weight" also matter?
3. Does SUBJECT quote requirement on arc synthesis (V-05) make C-11/C-12 structurally gradable — and if so, should quote-anchoring become the standard mechanism for all aspirational criteria across prove-* skills?
oring makes C-11 and C-12 structurally gradable rather than asserted.

---

## V-01: Role Sequence with Pre-Synthesis Arc Diagnosis (C-11 primary)

**Axis:** Role sequence (disposition order: Champion -> Neutral -> Skeptic) + mandatory Arc
Diagnosis checkpoint inserted after the Skeptic interview and before synthesis. The checkpoint
forces explicit naming of the dominant arc signal before synthesis conclusions are written.

**Hypothesis:** C-11 fails when dispositions are declared but the synthesis does not address
what their relationship revealed. A synthesis table row labeled "Convergence" can be populated
without ever asking whether convergence *despite skepticism* or convergence *because the Skeptic
was never actually resistant* is the signal. The Arc Diagnosis checkpoint closes this gap by
requiring a binary commitment (convergence-dominant or contradiction-dominant) with a one-sentence
rationale before synthesis begins. Once committed pre-synthesis, C-11 compliance in the synthesis
becomes a structural carrythrough rather than an optional depth item.

```
You are running /prove-interview. Subjects run in disposition order: Champion, then Neutral,
then Skeptic. An Arc Diagnosis checkpoint runs after the Skeptic interview and before synthesis.
The Skeptic's resistance must be role-grounded. "Change is hard" does not qualify.

---

## SETUP

Prior signals: [Search simulations/prove/ for prior artifacts on this topic. List files
found with one-line summaries, or write "None -- starting fresh."]
Interview question: [One sentence: what question does this session collectively answer?]

---

## SUBJECT PROFILES

Declare all three subjects before any interview begins. Disposition must be honest --
a Champion who has no real enthusiasm, or a Skeptic with no real resistance, fails the
profile requirement. Profiles are locked after this section.

**S-01 -- CHAMPION**
Role: [Title and domain]
Disposition: Champion -- [why they are favorable: specific benefit they receive, or problem
             they have that this addresses directly. Not "they like new tools."]
Prior knowledge: [What they know from direct experience. What shaped their enthusiasm --
                 a pain they have lived, or a success they have seen.]
Concern: [The condition that would reduce their support. Champions have limits; name the limit.]

**S-02 -- NEUTRAL**
Role: [Title and domain]
Disposition: Neutral -- [what makes them uncommitted: they care about outcome, not idea.
             What outcome are they optimizing for?]
Prior knowledge: [Their domain background and direct experience with this problem space.]
Concern: [What they are most likely to ask about: reliability, cost, team load, timeline,
         integration -- something concrete from their role.]

**S-03 -- SKEPTIC**
Role: [Title and domain]
Disposition: Skeptic -- [the specific role-based reason for resistance. Must be one of:
             (a) a prior failure in this space they witnessed or caused,
             (b) a competing priority their role demands,
             (c) a different model of the problem that makes this solution look wrong, or
             (d) a concrete constraint their role owns (compliance, budget, architecture).
             Generic reluctance or change-aversion is not a valid disposition rationale.]
Prior knowledge: [Their background -- the Skeptic is not uninformed. They have a different
                 frame built from real experience. What experience built that frame?]
Concern: [What specifically drives the skepticism -- named in the Skeptic's terms.]

---

## INTERVIEW: S-01 (CHAMPION)

At least one question must probe the Champion's declared concern -- unbounded enthusiasm
is not a credible signal. Follow up on their strongest assertion. Minimum 3 exchanges.

Q1: [Open-ended -- leaves room for enthusiasm and qualification both]
A1 (Champion): [Answer grounded in Champion's declared prior knowledge -- informed,
                favorable, but domain-specific. References what they know about the problem,
                not generic advocacy. Vocabulary is the Champion's role vocabulary.]

Q2: [FOLLOW-UP on A1: (what you are following up on)] OR [Next question]
A2 (Champion): [Answer]

Q3: [Probe the Champion's declared concern -- what would make them less supportive?]
A3 (Champion): [Answer -- shows limits, not unlimited positivity. The concern declared
                in the profile should appear here in the Champion's own voice.]

Surprising moment: [Did the Champion reveal a tension, a limit, or a concern the opening
question did not suggest? Label it and note what it changes about the signal. Or write:
"Champion confirmed favorable baseline -- no tension detected."]

Evidence extracted:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Specific insight, concern, requirement, contradiction, or signal. Must reference Champion's declared domain knowledge.] | insight / concern / requirement / contradiction / signal | HIGH / MEDIUM / LOW | [One line: why this confidence? Anchored in Champion's role and prior knowledge.] |
[Add E-02 and beyond as needed.]

---

## INTERVIEW: S-02 (NEUTRAL)

The Neutral has no agenda. They want to know if this actually works. Use what the Champion
revealed to shape one question here without naming the Champion as the source. Minimum 3 exchanges.

Q1: [Practical, outcome-focused question grounded in Neutral's declared concerns]
A1 (Neutral): [Answer in Neutral voice -- pragmatic, skeptical of abstractions, wants
               specifics. References their domain background and stated concern. Not the
               same vocabulary or frame as the Champion.]

Q2: [FOLLOW-UP on A1 or next question]
A2 (Neutral): [Answer]

Q3: [Ask the Neutral to evaluate a claim implicit in the Champion's strongest answer --
     do not name the Champion as the source]
A3 (Neutral): [Answer -- may converge with or diverge from Champion's baseline. If it
               diverges, this is the session's first arc signal.]

Surprising moment: [Unexpected answer, tension with Champion baseline, or practical concern
the Champion did not raise. Or: "Neutral confirmed pragmatic framing -- no divergence detected."]

Evidence extracted:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence item] | [type] | [confidence] | [rationale anchored in Neutral's role] |
[Add E-02 and beyond.]

---

## INTERVIEW: S-03 (SKEPTIC)

Most important interview. The Skeptic's objections must be grounded in the specific
resistance reason declared in their profile -- not generic reluctance. At least one
question must probe the declared resistance directly. Ask whether the objection is
conditional (satisfiable) or fundamental (a blocker). Minimum 3 exchanges.

Q1: [Open -- let the Skeptic frame the problem in their own terms first]
A1 (Skeptic): [Answer in Skeptic voice -- a different frame, different vocabulary, different
               concerns from both Champion and Neutral. References the Skeptic's declared
               background and specific resistance reason from their profile. The resistance
               is recognizable as role-specific, not generic.]

Q2: [FOLLOW-UP: probe the root of the resistance -- what specifically is the problem,
     in the Skeptic's role terms?]
A2 (Skeptic): [Answer -- drill into the specific concern declared in the profile. Traceable
               to the Skeptic's declared prior experience.]

Q3: [Ask: under what conditions would your objection be fully satisfied?]
A3 (Skeptic): [Answer -- reveals whether resistance is conditional (a requirement surface)
               or fundamental (a blocker). A Skeptic who cannot name conditions has named
               a blocker. A Skeptic who names conditions has given the team a requirement.]

Surprising moment: [Did the Skeptic reveal latent openness, a deeper concern than declared,
a direct contradiction with the Champion, or a new constraint that reframes the whole session?
This is where the arc pays off. Or: "Skeptic confirmed declared resistance -- no arc shift detected."]

Evidence extracted:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence -- especially the conditions-for-satisfaction answer from Q3] | [type] | [confidence] | [rationale anchored in Skeptic's declared role and background] |
[Add E-02 and beyond.]

---

## ARC DIAGNOSIS

[Complete this section before writing synthesis. This checkpoint commits to the arc's
dominant signal. Synthesis must be consistent with what is declared here.]

Arc outcome: CONVERGENCE-DOMINANT or CONTRADICTION-DOMINANT
[Choose one. Cannot be "mixed" -- if both are present, which is the dominant signal?]

Rationale: [One sentence: what happened in the Skeptic interview that determines this?
           Cite the specific exchange or evidence item that clinches it. If the Skeptic's
           resistance survived the full interview intact and contradicts the Champion's
           strongest claim, the arc is contradiction-dominant. If the Skeptic named
           conditions that the Champion's evidence already satisfies, convergence is dominant.]

Arc red flag check: [Did the Skeptic confirm the Champion's view without any role-grounded
                    pushback? If yes, name this as a profile failure: the Skeptic was not
                    actually resistant. A red flag means C-11 has a compliance problem
                    regardless of synthesis content.]

---

## SYNTHESIS

[Must be consistent with the Arc Diagnosis above. Synthesis that contradicts the Arc
Diagnosis is a structural inconsistency -- update whichever is wrong, not whichever
is easier to update.]

Champion-to-Skeptic arc: [What did the Champion claim that the Skeptic challenged or
                           confirmed? What specific evidence changed meaning when the
                           Skeptic weighed in?]
Neutral verdict: [Did the Neutral's evidence side closer to Champion or Skeptic? Does
                 the Neutral's position strengthen or weaken the arc's dominant signal?]
Convergence across dispositions: [What all three subjects pointed toward even from
                                  different positions -- especially if the Skeptic
                                  contributed to this convergence]
Critical contradiction: [The most important place where evidence across subjects conflicts.
                        Name it, state which E-IDs are in tension, and explain its
                        evidential weight: what does this contradiction confirm, undermine,
                        or leave unresolved?]
Dominant arc signal: [Restate the Arc Diagnosis conclusion and what it means for the
                      topic under investigation. Convergence despite skepticism = strong
                      signal. Contradiction that survived the full arc = most important
                      finding. Skeptic confirming Champion without resistance = weak signal,
                      profile may be defective.]
Open question: [What these three interviews fail to resolve despite the arc]

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count (3), disposition_order (champion/neutral/skeptic),
             arc_outcome (convergence-dominant / contradiction-dominant / red-flag),
             evidence_count, surprising_moments (count), synthesis_present (true),
             prior_signals_found (true/false).
```

---

## V-02: Output Format -- Ranked Contradiction Inventory (C-12 primary)

**Axis:** Output format -- after evidence extraction across all subjects, a required
Contradiction Inventory table forces all contradictions to be listed and ranked before
synthesis begins. Rank 1 has a required Evidential Weight field absent from lower ranks.
The column asymmetry makes ranking a structural requirement, not a formatting suggestion.

**Hypothesis:** C-12 fails when synthesis enumerates contradictions at equal depth -- three
bullets in parallel, none called most significant. The structural fix is a ranked table where
Rank 1 has more required columns than Rank 2+. The model cannot treat all contradictions
equally when one row has a required column that others do not. The Contradiction Inventory
runs as its own section between extraction and synthesis, so the ranking commitment is made
before synthesis conclusions are written. This variation does not require disposition ordering --
C-12 is a format question, not a role-sequence question. That independence is testable: if
V-02 scores C-12 PASS without disposition ordering, C-12 and C-11 are independent criteria.

```
You are running /prove-interview. Declare all subjects before any interviews begin.
After all evidence is extracted, complete the Contradiction Inventory before synthesis.
The Contradiction Inventory ranks contradictions in order of evidential importance.
Rank 1 is the critical contradiction -- it has a required Evidential Weight field.

---

## SETUP

Prior signals: [Search simulations/prove/ for prior artifacts on this topic. List files
with one-line summaries, or write "None -- starting fresh."]
Interview question: [One sentence: what question does this session collectively answer?]

---

## SUBJECT PROFILES

Declare all subjects before any interviews begin. Minimum two for the Contradiction
Inventory and synthesis to be gradable.

| # | Role / Title | Prior knowledge (what they know) | Knowledge gaps | Primary concern | Disposition |
|---|-------------|----------------------------------|----------------|-----------------|-------------|
| S-01 | [Role] | [Domain knowledge, experience, frame] | [Knowledge boundaries] | [What they optimize for] | [champion / neutral / skeptic / unspecified] |
| S-02 | [Role] | [Domain knowledge, experience, frame] | [Knowledge boundaries] | [What they optimize for] | [champion / neutral / skeptic / unspecified] |
[Add S-03 and beyond if needed.]

---

## INTERVIEW: S-01 [Role]

Questions must be open-ended. At least one follow-up must respond to a specific prior
answer. Label follow-ups: FOLLOW-UP on A[N]. Minimum 3 exchanges.

Q1: [Open-ended question -- not leading, not yes/no]
A1 (S-01): [Answer in S-01's voice -- vocabulary, concerns, and framing match the declared
            role and prior knowledge. The answer is recognizably S-01's. References declared
            prior knowledge or knowledge gaps in S-01's own terms.]

Q2: [FOLLOW-UP on A1: (what you are following up on)] OR [Next question]
A2 (S-01): [Answer]

Q3: [Question or follow-up]
A3 (S-01): [Answer]

Surprising moment: [One sentence: an unexpected answer, tension, or reveal. Or write:
"None detected -- interview confirmed declared profile."]

Evidence extracted:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Concrete insight, concern, requirement, contradiction, or signal. Specific enough that it could not have come from a persona with different declared knowledge.] | insight / concern / requirement / contradiction / signal | HIGH / MEDIUM / LOW | [One line: why this confidence? Reference S-01's declared domain knowledge or role.] |
[Add E-02 and beyond. At least one row required per subject.]

---

## INTERVIEW: S-02 [Role]

Q1: [Open-ended question -- grounded in S-02's declared profile and concerns]
A1 (S-02): [Answer in S-02's voice -- distinct vocabulary, frame, and concerns from S-01.
            If S-01's and S-02's answers are interchangeable, the persona declarations failed.]

Q2: [FOLLOW-UP on A1 or next question]
A2 (S-02): [Answer]

Q3: [Question or follow-up]
A3 (S-02): [Answer]

Surprising moment: [One sentence or "None detected."]

Evidence extracted:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence item] | [type] | [confidence] | [rationale anchored in S-02's role] |
[Add E-02 and beyond.]

---

[Repeat INTERVIEW and EVIDENCE EXTRACTED sections for S-03 and beyond if declared above.]

---

## CONTRADICTION INVENTORY

[Complete before synthesis. List all contradictions ranked from most to least evidentially
significant. A contradiction is any place where evidence from two subjects conflicts in a
way that changes the meaning of the composite signal. Minimum one row required when N >= 2
subjects. Rank 1 requires the Evidential Weight field. Lower ranks do not.]

| Rank | Contradiction | Subjects in tension | Evidential weight (Rank 1 only) |
|------|--------------|---------------------|---------------------------------|
| 1 | [Name the contradiction: what specifically did S-X claim that S-Y's evidence contradicts or reframes?] | [e.g., S-01 vs S-02] | [Required for Rank 1 only: what does this contradiction confirm, undermine, or leave unresolved? Why does it matter more than the others? Which E-IDs from each side are load-bearing?] |
| 2 | [Next most significant contradiction, if present] | [Subjects] | -- |
| 3 | [Next, if present] | [Subjects] | -- |

Write "None detected" with a one-line rationale if subjects produced no contradictions.
If only one contradiction exists, it is Rank 1 by default -- Evidential Weight is still required.

---

## SYNTHESIS

[Required when N >= 2 subjects. Read the Contradiction Inventory before writing this section.
Synthesis claims must be consistent with the Inventory's Rank 1 finding.]

| Dimension | Finding |
|-----------|---------|
| Convergence | [What multiple subjects pointed toward, even from different angles. Name the E-IDs that contribute.] |
| Critical contradiction | [Restate Rank 1 from the Inventory. Synthesis version: what does this contradiction *mean* for the interview question -- not just which subjects disagreed, but what it changes about the answer.] |
| Dominant arc signal | [If dispositions declared: was convergence or contradiction dominant? What does that mean for the topic? If no dispositions declared: "Disposition arc: N/A -- no disposition labels declared."] |
| Strongest signal | [The single most important evidence item from the whole session. Name the E-ID, subject, and why it is more important than the others.] |
| Open question | [What the interviews surfaced but no subject fully answered] |

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count, evidence_count, surprising_moments (count),
             contradiction_count (rows in Contradiction Inventory),
             critical_contradiction_named (true/false),
             synthesis_present (true/false), prior_signals_found (true/false).
```

---

## V-03: Lifecycle -- Two-Phase Synthesis (C-11 + C-12 via dedicated arc phase)

**Axis:** Lifecycle emphasis -- synthesis splits into two sequential phases. Phase 4A covers
traditional cross-evidence synthesis (C-09 content: patterns, convergences, strongest signal).
Phase 4B covers arc analysis (C-11/C-12 content: disposition relationship, dominant arc signal,
ranked critical contradiction). Phase 4B cannot begin until Phase 4A is complete, and Phase 4B
questions cannot be answered by restating Phase 4A content.

**Hypothesis:** A single synthesis table can satisfy C-09 while leaving C-11 and C-12 as
shallow bullets. When arc analysis is a named phase with distinct structural questions, separate
from evidence synthesis, the model must engage with what the *relationship* between dispositions
means as evidence. Phase 4B questions are not answerable by evidence summary alone: "Was
convergence despite skepticism the dominant signal?" requires reasoning about the arc, not
restating what subjects said. The phase separation forces this reasoning before the artifact
is written. Tests whether lifecycle separation alone (without role-sequence enforcement) can
produce reliable C-11/C-12 coverage -- a more format-neutral test than V-01.

```
You are running /prove-interview. The skill runs in five phases. Complete each phase before
beginning the next. Synthesis splits into Phase 4A (evidence patterns) and Phase 4B (arc
analysis). Complete Phase 4A before Phase 4B. Phase 4B questions cannot be answered by
restating Phase 4A content.

---

## PHASE 1: SETUP + ROSTER

Goal: Establish session context and declare all subjects. Profiles are locked after Phase 1.

Prior signals: [Search simulations/prove/ for prior artifacts on this topic. List files
with one-line summaries. Write "None -- starting fresh" if nothing found.]
Interview question: [One sentence: what question does this session answer?]
Disposition note: [Do subjects have declared dispositions (champion, neutral, skeptic)?
                  Declare them in the roster. If no, mark "Disposition: unspecified" per
                  subject. C-11 gradability depends on whether dispositions are declared.]

Roster:
| # | Role / Title | Prior knowledge | Knowledge gaps | Primary concern | Disposition |
|---|-------------|-----------------|----------------|-----------------|-------------|
| S-01 | [Role] | [Domain background and experience] | [What they would not know without specific exposure] | [What they optimize for] | [champion / neutral / skeptic / unspecified] |
| S-02 | [Role] | [Domain background and experience] | [What they would not know without specific exposure] | [What they optimize for] | [champion / neutral / skeptic / unspecified] |
[Add rows as needed. Minimum two subjects for synthesis phases to be gradable.]

PHASE 1 GATE: Do not begin Phase 2 until:
[ ] Interview question is one sentence
[ ] At least two subjects declared with role, prior knowledge, gaps, concern, and disposition
[ ] Prior signal state declared (found or not found -- not silent)

---

## PHASE 2: INTERVIEWS

Goal: Conduct each interview. Answers must stay in declared persona voice.
Phase 1 profiles are locked -- do not modify prior knowledge or disposition here.
No evidence extraction in Phase 2. No synthesis in Phase 2.

---

### INTERVIEW: S-01 [Role]

[Minimum 3 exchanges. Questions open-ended. At least one labeled FOLLOW-UP on A[N].]

Q1: [Open-ended question]
A1 (S-01): [Answer in S-01's voice -- vocabulary, concerns, and frame match the Phase 1
            declaration. References S-01's declared prior knowledge. Generic answers that
            could come from any persona are a Phase 1 lock violation.]

Q2: [FOLLOW-UP on A1: (what you are following up on)] OR [Next question]
A2 (S-01): [Answer]

Q3: [Question or follow-up]
A3 (S-01): [Answer]

Surprising moment: [One sentence: what unexpected answer, tension, or reveal emerged?
Write "None detected -- interview confirmed Phase 1 profile" if nothing unexpected appeared.
Do not extract evidence here -- that is Phase 3.]

---

### INTERVIEW: S-02 [Role]

Q1: [Open-ended question grounded in S-02's Phase 1 profile]
A1 (S-02): [Answer in S-02's voice -- distinct from S-01's vocabulary and frame. If S-02's
            declared disposition is Skeptic, resistance must be role-grounded and traceable
            to their declared prior knowledge. Generic reluctance fails the Phase 1 lock.]

Q2: [FOLLOW-UP on A1 or next question]
A2 (S-02): [Answer]

Q3: [Question or follow-up]
A3 (S-02): [Answer]

Surprising moment: [One sentence or "None detected."]

---

[Add INTERVIEW block for S-03 and beyond if declared in Phase 1.]

PHASE 2 GATE: Do not begin Phase 3 until:
[ ] Each declared subject has a completed interview block
[ ] Each interview has at least one labeled FOLLOW-UP
[ ] Each interview has a surprising-moment note (even if "None detected")
[ ] No evidence extraction in Phase 2

---

## PHASE 3: EXTRACT

Goal: Extract discrete evidence items from each interview. Read Phase 2 transcripts only.
Do not modify Phase 2 transcripts. Do not introduce new content not present in Phase 2.

### EVIDENCE: S-01

| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Concrete insight, concern, requirement, contradiction, or signal. Specific enough that it could not have come from a persona with different declared knowledge.] | insight / concern / requirement / contradiction / signal | HIGH / MEDIUM / LOW | [One line: why this confidence? Reference S-01's declared prior knowledge.] |
[Add E-02 and beyond. At least one row required per subject.]

### EVIDENCE: S-02

| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence item] | [type] | [confidence] | [rationale] |
[Add E-02 and beyond.]

[Add EVIDENCE tables for S-03 and beyond if needed.]

PHASE 3 GATE: Do not begin Phase 4A until:
[ ] At least one evidence row per subject
[ ] Each evidence item is specific (not "Subject had concerns" -- name the concern)
[ ] Confidence level declared with one-line rationale for each item
[ ] No new interview content introduced in Phase 3

---

## PHASE 4A: SYNTHESIS -- EVIDENCE PATTERNS

Goal: Connect evidence across subjects. Patterns, convergences, open questions.
Read Phase 3 evidence tables only. Do not introduce new evidence.
Do not write arc analysis in Phase 4A -- that is Phase 4B.

| Dimension | Finding |
|-----------|---------|
| Convergence | [What multiple subjects pointed toward, even from different positions. Name E-IDs that contribute.] |
| Strongest signal | [Most important evidence item -- state E-ID, subject, and why it is most important] |
| Evidence gap | [What question the combined evidence does not answer -- what interviews would fill it] |

PHASE 4A GATE: Do not begin Phase 4B until:
[ ] Convergence finding names at least one E-ID
[ ] Strongest signal names an E-ID and a rationale
[ ] Phase 4A does not contain arc analysis, disposition assessment, or contradiction ranking

---

## PHASE 4B: SYNTHESIS -- ARC ANALYSIS

Goal: Assess what the relationship between dispositions means as evidence. This phase
cannot be answered by restating Phase 4A content. If no dispositions were declared in
Phase 1, answer the N/A fields and skip to the artifact write step.

[For sessions with declared dispositions (at least one champion/skeptic pair):]

Disposition arc present: YES / NO / PARTIAL
[YES: at least one declared advocate and one declared skeptic. PARTIAL: dispositions declared
but advocate/skeptic contrast is asymmetric or one role is missing.]

Arc dominant signal: CONVERGENCE-DOMINANT / CONTRADICTION-DOMINANT / INCONCLUSIVE
[CONVERGENCE-DOMINANT: the skeptic's evidence moved toward the champion's position, or
conditions-for-satisfaction were named that the champion's evidence already meets.
CONTRADICTION-DOMINANT: the skeptic's resistance survived the session intact and directly
undermines the champion's strongest claim. INCONCLUSIVE: the arc did not resolve.]

Arc red flag: [Did the skeptic confirm the champion's view without role-grounded pushback?
              If yes, name this as a profile failure. A skeptic whose resistance was generic
              or whose answers fit any persona fails this check regardless of disposition label.]

Critical contradiction: [Name the single most significant contradiction between interview
                         subjects. State which E-IDs are in tension. Explain its evidential
                         weight: what does this contradiction confirm, undermine, or leave
                         unresolved? Why is this contradiction more important than any others?
                         A synthesis that names multiple contradictions in parallel without
                         ranking them fails this field.]

What the arc means: [One to three sentences: given the dominant arc signal and the critical
                     contradiction, what is the composite signal for the topic under investigation?
                     This is the Phase 4B conclusion -- synthesizes disposition relationship,
                     not evidence items. Should not duplicate Phase 4A content.]

[For sessions with no declared dispositions:]
Arc analysis: N/A -- no disposition labels declared in Phase 1. C-11 scores N/A for this session.

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count, evidence_count, surprising_moments (count),
             dispositions_declared (true/false), arc_outcome (convergence-dominant /
             contradiction-dominant / inconclusive / N/A), critical_contradiction_named (true/false),
             synthesis_present (true), prior_signals_found (true/false),
             phase_gate_failures (count of unchecked gate items across Phases 1-3).
```

---

## V-04: Disposition Arc + Current-Practice Q1 (C-05 + C-11 combination)

**Axes:** Role sequence (Champion/Neutral/Skeptic disposition ordering) + Inertia framing
(declared current-practice field per subject; current-practice Q1 mandatory for every interview).
Direct test of R1's open research question: does grounding each disposition in a declared
current practice produce better C-05 compliance than disposition labeling alone?

**Hypothesis:** The Skeptic is the hardest persona to write with genuine C-05 grounding.
A Skeptic whose profile says "role: compliance officer, concern: data residency" has a
declarative anchor. A Skeptic whose profile adds "current practice: we run manual quarterly
audits because no tool has passed our data residency requirements; three past attempts failed
at vendor questionnaire stage" has a behavioral anchor. The behavioral anchor constrains what
the Skeptic can plausibly say about Q1 -- and what they cannot. Answers that ignore the declared
current practice are structurally visible as C-05 failures. Same mechanism for Champion and
Neutral: current practice grounds enthusiasm and pragmatism in declared behavior, not just
declared knowledge. The combination addresses both R1 essential partial-credit gaps: C-05
(behavioral baseline) and C-11 (disposition arc).

```
You are running /prove-interview. Subjects run in disposition order: Champion, then Neutral,
then Skeptic. Each subject has a declared current practice. Every interview opens with a
current-practice question (Q1) before any feature or change question is asked.
The contrast between current practice and feature reaction is where the evidence lives.

---

## SETUP

Prior signals: [Search simulations/prove/ for prior artifacts on this topic. List files
with one-line summaries. Write "None -- starting fresh" if nothing found. Prior interviews
reveal which current-practice baselines are missing from the record.]
Interview question: [One sentence: what question does this session answer?]

---

## SUBJECT PROFILES

Declare all subjects before any interviews begin. The current-practice field is
load-bearing -- it determines what each subject can plausibly say in response to Q1.
"Senior engineer" is not enough: name their domain, their experience, and what they do
today to handle the problem this feature or change addresses.

**S-01 -- CHAMPION**
Role: [Title and specific domain]
Disposition: Champion -- [specific reason for advocacy: what problem does their current
             practice have that this addresses? What have they seen work?]
Current practice: [What they do today to handle the problem this feature addresses. Specific
                  enough that Q1's answer is constrained by it. If they have no current
                  practice for this problem: "No current practice -- this problem goes
                  unaddressed today."]
Prior knowledge: [What they know from domain experience]
Gaps: [What they would not know without specific exposure]
Stakes: [What they gain or lose from a change to current practice]

**S-02 -- NEUTRAL**
Role: [Title and specific domain]
Disposition: Neutral -- [outcome orientation: what are they evaluating the proposed change
             against?]
Current practice: [What they do today. Must differ meaningfully from Champion's --
                  different domain, different tool, or different relationship to the problem.]
Prior knowledge: [What they know]
Gaps: [What they don't know]
Stakes: [What they stand to gain or lose]

**S-03 -- SKEPTIC**
Role: [Title and specific domain]
Disposition: Skeptic -- [role-grounded resistance from:
             (a) a prior failure they witnessed or caused,
             (b) a competing priority their role demands,
             (c) a different model of the problem, or
             (d) a concrete constraint they own.
             Generic change-aversion is not valid.]
Current practice: [What they do today -- what they are defending, what failed before, or
                  the constraint they are enforcing. Most important current-practice
                  declaration in the session. The Skeptic's current practice is where their
                  resistance is grounded, not just their stated stance.]
Prior knowledge: [Experience that built the skeptical frame]
Gaps: [What they don't know -- even skeptics have boundaries]
Stakes: [What they lose from change, or gain if their objection is satisfied]

---

## INTERVIEW: S-01 (CHAMPION)

Q1 is always about current practice. Do not ask about the proposed change until S-01 has
described what they do today. The contrast between Q1 (current practice) and Q3 (feature
reaction) is the core Champion evidence.

Q1 (current practice): Walk me through what you do today when [describe the problem scenario
in neutral terms -- not in terms of the proposed solution].
A1 (Champion): [Answer grounded in declared current practice -- what they actually do,
                including friction, workarounds, and what they have learned. References the
                current-practice and prior-knowledge fields from the profile. If current
                practice is "no current practice," the answer reflects that gap and what
                it costs them.]

Q2: [FOLLOW-UP on current practice -- probe the friction point, the workaround's cost,
     or the condition under which current practice breaks down]
A2 (Champion): [Answer -- approaching current practice's limits. This is where Champion
                enthusiasm is grounded: they have lived the problem.]

Q3: [Introduce the proposed feature or change -- ask for S-01's reaction in light of what
     they just described. Let their current-practice frame do the work.]
A3 (Champion): [Answer -- reaction from current-practice baseline. The contrast between
                A1 and A3 is the core Champion evidence. Recognizably a reaction to what
                they said in A1-A2, not a generic endorsement.]

Surprising moment: [Did S-01's current-practice description reveal a constraint the opening
did not suggest? Did their feature reaction depart from the trajectory their Q1-Q2 answers
set up? Label it, or write: "Current practice confirmed expected Champion baseline."]

Evidence from S-01:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence rooted in what S-01 said about current practice. Grounding test: could this item have been said by a persona with a different declared current practice? If yes, not grounded enough.] | insight / concern / requirement / contradiction / signal | HIGH / MEDIUM / LOW | [One line anchored in S-01's declared current practice or prior knowledge.] |
[Add E-02 and beyond.]

---

## INTERVIEW: S-02 (NEUTRAL)

Q1 is adapted to S-02's domain and declared practice -- not a copy of S-01's Q1.

Q1 (current practice): [Adapt to S-02's domain and current practice declaration]
A1 (Neutral): [Answer grounded in S-02's declared current practice -- different domain,
               different constraints from S-01. Pragmatic voice: what works today, what
               breaks today. Not interchangeable with S-01's Q1 answer.]

Q2: [FOLLOW-UP on S-02's current-practice description -- probe friction or insufficiency]
A2 (Neutral): [Answer]

Q3: [Feature or change question -- from S-02's current-practice baseline]
A3 (Neutral): [Answer -- reaction from current-practice frame. May differ sharply from
               S-01's contrast. The Neutral's current practice determines whether they
               see the proposed change as improvement or disruption.]

Surprising moment: [Label or "Current practice confirmed expected Neutral baseline."]

Evidence from S-02:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence rooted in S-02's current practice] | [type] | [confidence] | [rationale anchored in declared current practice] |
[Add E-02 and beyond.]

---

## INTERVIEW: S-03 (SKEPTIC)

Q1 is adapted to the Skeptic's domain and current practice. The Skeptic's Q1 answer is
the most important current-practice answer in the session: it describes what they are
defending, what failed before, or what constraint they enforce. At least one question
must probe the specific declared resistance reason. Ask whether the objection is
conditional (satisfiable) or fundamental.

Q1 (current practice): [Neutral framing of the problem scenario, adapted to Skeptic's domain]
A1 (Skeptic): [Answer grounded in Skeptic's declared current practice -- describes what
               they do today in terms of their role and experience. The resistance is
               visible here: current practice reflects a past failure, a constraint, or a
               deliberately chosen alternative. Not generic reluctance. Not interchangeable
               with S-01's or S-02's Q1 answer.]

Q2: [FOLLOW-UP: probe the root of the Skeptic's current practice -- why does it exist?
     What problem does it solve that prior attempts didn't?]
A2 (Skeptic): [Answer -- the reason behind their current practice is the root of their
               skepticism. Traceable to their declared prior knowledge and resistance reason.]

Q3: [Introduce the proposed change -- ask for S-03's reaction against their current-practice
     baseline]
A3 (Skeptic): [Answer -- reaction from current-practice frame. The Skeptic's objection
               should be rooted in what they said in A1-A2.]

Q4: [Ask: under what conditions would your objection be fully satisfied?]
A4 (Skeptic): [Answer -- conditional or fundamental resistance. A Skeptic who names
               specific conditions has given the team a requirement. A Skeptic who cannot
               name conditions has named a blocker.]

Surprising moment: [Did the Skeptic's current-practice description reveal a constraint the
Champion did not account for? Did their conditions-for-satisfaction answer open or close the
arc? Label it, or write: "Skeptic confirmed declared resistance -- no arc shift detected."]

Evidence from S-03:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence rooted in Skeptic's current practice and conditions-for-satisfaction answer] | [type] | [confidence] | [rationale anchored in declared current practice] |
[Add E-02 and beyond.]

---

## SYNTHESIS

Current-practice comparison: [How did S-01, S-02, and S-03's current practices differ?
                               Which user population does the proposed change help most?
                               Which does it disrupt or leave unchanged?]

Feature-reaction contrast: [How did each subject's reaction differ? Is the contrast explained
                             by their different current practices -- or does it reveal something
                             about the proposed change that transcends practice differences?]

Dominant arc signal: [Was convergence or contradiction the dominant arc signal across Champion
                      and Skeptic? Did the Skeptic's current-practice grounding make their
                      resistance more or less surmountable than a stance-only Skeptic would have
                      been? Convergence despite role-grounded skepticism = strong signal.
                      Contradiction that survived the current-practice arc = most important finding.]

Critical contradiction: [The single most significant contradiction between subjects. Name
                         which E-IDs are in tension. Explain its evidential weight: what does
                         this contradiction confirm, undermine, or leave unresolved? Why is
                         this the most evidentially consequential contradiction -- not the most
                         dramatic, but the one that most changes the answer to the interview
                         question?]

What leading with current practice revealed: [One key finding invisible if interviews had led
                                               with the feature question instead of the
                                               current-practice question. This is the structural
                                               contribution current-practice anchoring makes
                                               beyond disposition ordering alone.]

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count (3), disposition_order (champion/neutral/skeptic),
             evidence_count, surprising_moments (count), arc_outcome (convergence-dominant /
             contradiction-dominant / inconclusive), critical_contradiction_named (true),
             synthesis_present (true), prior_signals_found (true/false),
             current_practice_anchored (true).
```

---

## V-05: Full R2 Ceiling Candidate (Disposition + Ranked Contradiction + Quote-Anchored Arc)

**Axes:** Role sequence (disposition order) + output format (ranked contradiction inventory
+ quote-required evidence + INTERVIEWER:/SUBJECT: transcript) + inertia framing
(current-practice anchor). All R2 primary mechanisms active simultaneously.

**Hypothesis:** C-11 and C-12 are aspirational criteria -- the rubric grades them as depth
items. The reason they are hard to score reliably: a synthesis can *claim* "convergence despite
skepticism" without citing any Skeptic SUBJECT turn that actually converged. Quote-anchoring the
arc synthesis changes this: a C-11 claim is only structurally gradable when a specific Skeptic
SUBJECT turn is cited as evidence. A C-12 contradiction ranking is only structurally gradable
when both sides of the Rank 1 contradiction are cited by SUBJECT turn. This makes C-11 and
C-12 behave like C-04 and C-10 -- not optional depth items, but claims with required source
citations. Combined with current-practice anchoring (C-05), disposition profiles (C-03),
and ranked contradiction table (C-12), this is the R2 ceiling candidate.

```
You are running /prove-interview. Subjects run in disposition order: Champion, Neutral, Skeptic.
Each subject has a declared current practice. Every interview opens with a current-practice
question before any feature question. After all evidence is extracted, complete the Contradiction
Inventory with ranked rows and Rank 1 requiring both-sides SUBJECT turn quotes. Every arc
synthesis claim -- every statement about convergence, contradiction, or arc signal -- must cite
a direct SUBJECT turn verbatim. No arc claim without a source quote.

---

## SETUP

Prior signals: [Search simulations/prove/ for prior artifacts on this topic. List files
with one-line summaries. Write "None -- starting fresh" if nothing found. Prior interviews
reveal which current-practice baselines are missing from the record.]
Interview question: [One sentence: what question does this session answer?]

---

## SUBJECT PROFILES

Profiles are locked after this section. The current-practice field is load-bearing.
The disposition must be honest: a Champion with no real enthusiasm or a Skeptic with no
role-grounded resistance is a profile failure, not a finding.

**S-01 -- CHAMPION**
Role: [Title and specific domain]
Disposition: Champion -- [specific reason: what problem does their current practice have
             that this addresses? What have they seen succeed?]
Current practice: [What they do today. Specific enough that Q1's answer is constrained by it.]
Prior knowledge: [Domain experience and background]
Gaps: [What they would not know without specific exposure]
Stakes: [What they gain or lose from change]
Assumption to test: [One assumption in their advocacy that the Neutral or Skeptic might challenge]

**S-02 -- NEUTRAL**
Role: [Title and specific domain]
Disposition: Neutral -- [outcome orientation: what are they evaluating against?]
Current practice: [What they do today. Must differ meaningfully from Champion's.]
Prior knowledge: [Domain experience]
Gaps: [What they don't know]
Stakes: [What they stand to gain or lose]
Assumption to test: [One assumption in their pragmatic framing]

**S-03 -- SKEPTIC**
Role: [Title and specific domain]
Disposition: Skeptic -- [role-grounded resistance: prior failure / competing priority /
             different problem model / concrete constraint owned by this role.
             Generic change-aversion is not valid.]
Current practice: [What they do today -- what they are defending, what failed before, or
                  what constraint they are enforcing. Most important current-practice
                  declaration in the session.]
Prior knowledge: [Experience that built the skeptical frame]
Gaps: [What they don't know -- even skeptics have boundaries]
Stakes: [What they lose from change or gain if their objection is satisfied]
Assumption to test: [The specific assumption in their skepticism -- what would have to be
                    true for their resistance to be wrong?]

---

## INTERVIEW: S-01 (CHAMPION)

INTERVIEWER: and SUBJECT: format. Every turn is labeled. Q1 is current practice.
Minimum 3 INTERVIEWER turns. At least one FOLLOW-UP labeled explicitly.

INTERVIEWER: Walk me through what you do today when [describe the problem scenario in
neutral terms -- not in terms of the proposed solution].
SUBJECT (Champion): [Answer grounded in declared current practice -- what they actually do,
                     including friction, workarounds, and what they have learned. Vocabulary
                     is the Champion's role vocabulary. The answer is not interchangeable
                     with any other subject's Q1 answer.]

INTERVIEWER: [FOLLOW-UP on current practice -- probe friction, cost, or failure mode]
SUBJECT (Champion): [Answer -- approaching the limits of current practice.]

INTERVIEWER: [Introduce the proposed change -- ask for reaction in light of current practice]
SUBJECT (Champion): [Answer -- reaction from current-practice baseline. The contrast between
                     this and the Q1 answer is the core Champion evidence.]

SURPRISE: [One SUBJECT turn that contradicted the declared assumption in the profile.
           Quote the turn verbatim. State: "Assumed: [profile assumption]. Revealed: [what
           the answer showed instead]." Write "None -- interview confirmed declared profile"
           if nothing surprising emerged.]

EVIDENCE PULL -- S-01:
| E-ID | Evidence item | Quote from SUBJECT turn | Type | Confidence | Rationale |
|------|--------------|-------------------------|------|------------|-----------|
| E-01 | [Specific insight, concern, requirement, contradiction, or signal] | "[Verbatim SUBJECT (Champion) turn]" | insight / concern / requirement / contradiction / signal | HIGH / MEDIUM / LOW | [One line: why this confidence? Reference declared current practice or prior knowledge.] |
[Add E-02 and beyond. Minimum 2 rows. Quote column must be verbatim SUBJECT text -- not paraphrase.]

---

## INTERVIEW: S-02 (NEUTRAL)

INTERVIEWER: [Current-practice Q1 adapted to S-02's domain and declared practice]
SUBJECT (Neutral): [Answer grounded in S-02's declared current practice -- different domain,
                    different constraints from S-01. Pragmatic voice: what works, what breaks.
                    Vocabulary and concerns are recognizably S-02's, not S-01's.]

INTERVIEWER: [FOLLOW-UP on current practice -- probe friction or insufficiency]
SUBJECT (Neutral): [Answer]

INTERVIEWER: [At least one question must address a tension from Champion's evidence without
             naming the Champion as the source]
SUBJECT (Neutral): [Answer -- may converge with or diverge from Champion's baseline.]

SURPRISE: [Verbatim quote of surprising turn. Or "None -- confirmed Neutral profile."]

EVIDENCE PULL -- S-02:
| E-ID | Evidence item | Quote from SUBJECT turn | Type | Confidence | Rationale |
|------|--------------|-------------------------|------|------------|-----------|
| E-01 | [Evidence rooted in S-02's current practice] | "[Verbatim SUBJECT (Neutral) turn]" | [type] | [confidence] | [rationale] |
[Add E-02 and beyond. Minimum 2 rows.]

---

## INTERVIEW: S-03 (SKEPTIC)

The Skeptic's Q1 answer is the most important current-practice answer in the session.
At least one INTERVIEWER turn must probe the declared resistance reason. Ask whether
the objection is conditional (satisfiable) or fundamental.

INTERVIEWER: [Current-practice Q1 adapted to Skeptic's domain]
SUBJECT (Skeptic): [Answer grounded in Skeptic's declared current practice -- describes
                    what they do today in terms of their role and experience. The declared
                    resistance is visible here: current practice reflects a past failure,
                    a constraint, or a deliberately chosen alternative. Not generic reluctance.
                    Recognizably the Skeptic's answer, not any other persona's.]

INTERVIEWER: [FOLLOW-UP: probe the root of their current practice -- why does it exist?
             What problem does it solve that prior attempts didn't?]
SUBJECT (Skeptic): [Answer -- the reason behind current practice is the root of skepticism.
                   Traceable to declared prior knowledge and resistance reason.]

INTERVIEWER: Under what conditions would your objection be fully satisfied?
SUBJECT (Skeptic): [Answer -- conditional or fundamental resistance. If conditional: the
                   team has a requirement. If fundamental: the team has a blocker. This is
                   the most important SUBJECT turn in the session.]

SURPRISE: [Verbatim quote of surprising turn. Or "None -- confirmed Skeptic profile."]

EVIDENCE PULL -- S-03:
| E-ID | Evidence item | Quote from SUBJECT turn | Type | Confidence | Rationale |
|------|--------------|-------------------------|------|------------|-----------|
| E-01 | [Evidence rooted in Skeptic's current practice and conditions-for-satisfaction answer] | "[Verbatim SUBJECT (Skeptic) turn]" | [type] | [confidence] | [rationale] |
[Add E-02 and beyond. Minimum 2 rows.]

---

## CONTRADICTION INVENTORY

[Complete before synthesis. Rank by evidential significance. A contradiction is any place
where evidence from two subjects conflicts in a way that changes the meaning of the composite
signal. Rank 1 requires Evidential Weight and both-sides SUBJECT quotes. Lower ranks do not.]

| Rank | Contradiction | Subjects in tension | Evidential weight (Rank 1 only) | Quote A (Rank 1 only) | Quote B (Rank 1 only) |
|------|--------------|---------------------|----------------------------------|-----------------------|-----------------------|
| 1 | [What specifically did S-X claim that S-Y's evidence contradicts or reframes?] | [e.g., Champion vs Skeptic] | [Required: what does this contradiction confirm, undermine, or leave unresolved? Why is it more evidentially consequential than the others?] | "[Verbatim SUBJECT turn from first side]" | "[Verbatim SUBJECT turn from second side]" |
| 2 | [Next contradiction, if present] | [Subjects] | -- | -- | -- |

Write "None detected" with a one-line rationale if subjects produced no contradictions.
If only one contradiction exists, it is Rank 1 by default -- all Rank 1 fields are required.

---

## SYNTHESIS

Every arc synthesis claim must cite a direct SUBJECT turn verbatim. No arc claim without
a source quote. Claims about convergence, contradiction, or arc signal not backed by a
SUBJECT turn are assertions, not evidence.

Current-practice comparison: [How did the three declared current practices differ? Which
                               population benefits most from the proposed change? Which
                               is disrupted or left unchanged?]

Dominant arc signal: CONVERGENCE-DOMINANT / CONTRADICTION-DOMINANT / INCONCLUSIVE
Evidence for arc signal: "[Verbatim Skeptic SUBJECT turn that confirms convergence OR
                           maintains contradiction -- the turn that clinches the arc outcome]"
Interpretation: [One sentence: what this turn means for the arc signal]

Arc red flag check: [Did the Skeptic confirm the Champion's view without role-grounded
                    pushback? Cite the Skeptic's SUBJECT turn to support your answer.
                    A confirmed red flag means C-11 has a profile compliance problem
                    regardless of the synthesis conclusion.]

Critical contradiction (from Inventory Rank 1): [What this contradiction *means* for the
interview question -- not just which subjects disagreed, but what it changes about the answer.
Both-sides quotes already cited in Inventory above.]

What leading with current practice revealed: [One key finding invisible if interviews had led
                                               with the feature question instead of the
                                               current-practice question. Cite one SUBJECT
                                               turn from Q1 that supports this finding.]

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count (3), disposition_order (champion/neutral/skeptic),
             evidence_count, surprising_moments (count), arc_outcome (convergence-dominant /
             contradiction-dominant / inconclusive / red-flag),
             arc_quote_cited (true/false), critical_contradiction_named (true),
             contradiction_rank1_quoted (true/false),
             synthesis_present (true), prior_signals_found (true/false),
             current_practice_anchored (true).
```

---

## Round 2 Design Notes

### Variation axis selection

**Single-axis (three):**

- **V-01 (Role sequence + arc diagnosis):** C-11 primary. Inherits R1 V-03's disposition
  ordering but adds a pre-synthesis Arc Diagnosis checkpoint. The checkpoint commits to a
  binary (convergence-dominant / contradiction-dominant) with a one-sentence rationale before
  synthesis begins. This prevents the most common C-11 failure: dispositions present, arc
  signal unnamed. The arc red-flag check targets the rubric's explicit warning about false
  convergence signals (Skeptic confirming Champion without role-grounded resistance).

- **V-02 (Ranked contradiction inventory):** C-12 primary. Minimal change to base structure --
  one new required section (Contradiction Inventory) between evidence extraction and synthesis.
  Key mechanism: Rank 1 has more required columns than lower ranks (Evidential Weight column
  is Rank 1 only). Column asymmetry forces ranking to be structural rather than advisory.
  Does not require disposition ordering -- tests whether C-12 is format-neutral for role
  sequence. If V-02 scores C-12 PASS, C-11 and C-12 are architecturally independent.

- **V-03 (Two-phase synthesis):** C-11 + C-12 via lifecycle separation. Phase 4A is evidence
  synthesis (C-09 content). Phase 4B is arc analysis (C-11/C-12 content). Phase 4A gate
  prevents arc analysis from being merged with evidence summary. Phase 4B questions are
  explicitly unanswerable by restating Phase 4A. Tests whether lifecycle separation alone
  (without role-sequence enforcement) can produce reliable C-11/C-12 coverage.

**Combination (two):**

- **V-04 (Disposition arc + current-practice Q1):** Direct test of R1's open research question.
  Each disposition gets a current-practice field in addition to prior knowledge and stance.
  Targets both R1 essential partial-credit gaps simultaneously: C-05 (behavioral baseline via
  current-practice Q1 per subject) and C-11 (disposition arc via Champion/Neutral/Skeptic
  ordering). Ranked critical contradiction in synthesis targets C-12. Expected to improve on
  R1 V-03's partial C-05 score and confirm whether behavioral anchoring also improves
  disposition authenticity.

- **V-05 (Full ceiling candidate):** All primary R2 mechanisms active. INTERVIEWER:/SUBJECT:
  transcript format (structural C-03), current-practice Q1 (C-05), disposition ordering (C-11),
  ranked Contradiction Inventory with both-sides SUBJECT quotes at Rank 1 (C-12), EVIDENCE PULL
  with verbatim Quote column (C-04/C-10), quote-required arc synthesis (C-11/C-12 structural
  gradability). Structural complexity cost: longer prompt, more required columns. Expected
  benefit: C-11 and C-12 become structurally gradable rather than asserted.

---

### C-11 coverage comparison (v2 rubric)

| V | C-11 mechanism |
|---|---------------|
| V-01 | Disposition ordering + mandatory Arc Diagnosis checkpoint (binary commitment before synthesis) + arc red-flag check |
| V-02 | None structurally -- Disposition column in roster is optional; C-11 not targeted |
| V-03 | Phase 4B arc analysis phase with explicit disposition-arc question and arc outcome field |
| V-04 | Disposition ordering + behavioral grounding per disposition (current-practice field) + arc synthesis |
| V-05 | Disposition ordering + behavioral grounding + quote-required arc synthesis (C-11 claims must cite SUBJECT turns) |

V-05 has the strongest C-11 mechanism (claims must cite SUBJECT turns -- structurally gradable).
V-01 has the cleanest enforcement (binary commitment before synthesis). V-04 is the middle:
behavioral grounding makes disposition authenticity harder to fake, but no quote requirement.

---

### C-12 coverage comparison (v2 rubric)

| V | C-12 mechanism |
|---|---------------|
| V-01 | Named Critical contradiction synthesis field with E-ID citation and evidential weight explanation |
| V-02 | Ranked Contradiction Inventory with Evidential Weight column required at Rank 1 only (column asymmetry) |
| V-03 | Phase 4B Critical contradiction field with required ranking rationale and explicit ranking test |
| V-04 | Named Critical contradiction synthesis field with evidential weight explanation |
| V-05 | Ranked Contradiction Inventory with both-sides SUBJECT turn quotes required at Rank 1 |

V-05 has the strongest C-12 mechanism (Rank 1 requires both-sides SUBJECT quotes -- claims are
source-verified, not just named). V-02 is the isolation test: does ranked table structure alone
produce C-12 compliance? If V-02 scores C-12 PASS, the gap from C-09 to C-12 is a structural
ranking column. If PARTIAL, the gap requires behavioral framing of "evidential weight" as well.

---

### R2 open research questions

1. **Arc Diagnosis checkpoint (V-01) vs. dedicated Phase 4B (V-03):** Two structural approaches
   to forcing C-11 engagement. V-01 inserts a binary commitment before synthesis; V-03 creates
   a separate phase. Hypothesis: V-01's binary is faster to satisfy correctly; V-03 gives more
   reasoning room but adds lifecycle overhead. Which produces more reliable arc analysis?

2. **Does Rank 1 column asymmetry alone produce C-12 compliance (V-02)?** If V-02 scores
   C-12 PASS, the structural gap between C-09 and C-12 is a ranking column. If PARTIAL, the
   gap also requires behavioral framing of what "evidential weight" means -- column presence
   is not sufficient without content quality instruction.

3. **Does SUBJECT quote requirement on arc synthesis improve C-11/C-12 gradability (V-05)?**
   If yes, quote-anchoring should migrate into the v-next canonical spec as a standard mechanism
   for aspirational criteria, not just essential ones. This would be the R2 structural innovation
   with the highest generalization value across all prove-* skills.
