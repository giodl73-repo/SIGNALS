## Round 1 Variations -- prove-interview

Five complete skill body prompts written to `simulations/quest/variations/prove-interview-variations-R1-2026-03-14.md`.

### Design summary

**Three single-axis:**

- **V-01: Output Format** -- Pre-printed tables at every stage: persona profile table (C-01/C-02), per-subject evidence table with type + confidence + rationale (C-04/C-10), synthesis table (C-09). Column-level requirements make invisible skips impossible.

- **V-02: Phrasing Register** -- Conversational, immersive prose. "Who are we talking to? What surprised you?" Control variation. Minimum structural overhead; tests whether question-driven narration alone achieves rubric compliance.

- **V-03: Role Sequence (Disposition Order)** -- Champion → Neutral → Skeptic with disposition declared per subject. The Skeptic's resistance must be role-grounded, not generic. Disposition ordering creates an expected arc against which surprising moments and contradictions are structurally visible.

**Two combination axes:**

- **V-04: Lifecycle Emphasis + Output Format** -- Four hard phases (Setup / Interview / Extract / Synthesize) with gate checklists. Evidence extraction is Phase 3 only -- Phase 2 is transcript only. Gate failure count goes in frontmatter for machine-readable rubric compliance.

- **V-05: Inertia Framing + Phrasing Register** -- Current-practice anchor. Q1 is always "what do you do today without this?" before any feature question. Each persona has a declared `current-practice` field. Evidence items must depart from the declared baseline, making C-05 (grounded, not invented) fail visibly rather than silently.

**Key research question for R2:** Does V-05's behavioral anchor (what they do) produce better C-05 compliance than V-01's declarative anchor (what they know)? Testable on live runs.
 gate checklists between them. Evidence extraction is Phase 3 only -- Phase 2 (interview) is transcript only, no extraction. This enforces C-04 and C-09 as structural phases rather than optional trailing sections. Pre-printed evidence tables with confidence columns in Phase 3 enforce C-10. Gate failures are recorded in artifact frontmatter.

**V-05: Inertia Framing + Phrasing Register** -- The current-practice anchor. Every interview opens with a mandatory Q1: "What do you do today without this?" before any feature question is asked. The status-quo baseline is a declared field in each persona profile (not just role + prior knowledge). Evidence items must be rooted in what the persona said about current practice, not in invented domain facts. This is the strongest structural enforcement of C-05 (grounded, not invented) because it anchors answers in the persona's declared real behavior, not in plausible-sounding domain vocabulary. Phrasing is immersive and stakes-aware.

### Key design decision

C-05 (grounded, not invented) is the rubric's hardest essential. Most prompt formats rely on a behavioral instruction ("answers must reference domain knowledge") with no structural check. V-05's current-practice anchor changes this: every answer must depart from a declared baseline, making generic platitudes structurally visible as failures. V-04's phase separation changes C-04: by making extraction a separate phase with its own gate, it prevents the most common failure mode where evidence is implied in the transcript but never named. That's the open research question for R2: does V-05's current-practice anchor produce materially better C-05 compliance than V-01's persona profile table?

---

## V-01: Output Format (Table-Structured)

**Axis:** Output format -- every stage has a pre-printed table with required columns.
Persona profile table enforces C-01/C-02. Evidence table enforces C-04/C-10. Synthesis
table enforces C-09. Column-level requirements make invisible skips impossible.

**Hypothesis:** Pre-printed tables with column-level requirements prevent the most common
failure modes: undeclared personas (C-01), missing prior knowledge scoping (C-02), implicit
evidence (C-04), and missing confidence ratings (C-10). Each column is a mini-gate. The
synthesis table makes cross-interview comparison structural rather than optional.

```
You are running /prove-interview. Fill in this structured template.
All section headers are fixed. Declare all persona profiles BEFORE any interviews begin.
Do not adjust a persona's declared prior knowledge after their interview starts.

---

## SETUP: PRIOR SIGNALS
[Search simulations/prove/ for any prior hypothesis, analysis, synthesis, or interview
artifacts on this topic.]
Prior signals found: [List files found, or write "None -- starting fresh."]
Topic under investigation: [State the topic or hypothesis this interview session is probing.]
Interview goal: [One sentence: what question do these interviews collectively answer?]

---

## INTERVIEW SUBJECTS

[Declare all subjects before any interviews begin. Minimum two for synthesis to be gradable (C-08/C-09).]

| # | Role / Title | Prior Knowledge (what they know) | Knowledge Gaps (what they don't know) | Key Concerns (what they care about) |
|---|-------------|----------------------------------|---------------------------------------|--------------------------------------|
| S-01 | [Role] | [2-3 sentences: domain knowledge and background] | [What they would not know without specific exposure] | [What they optimize for in their role] |
| S-02 | [Role] | [2-3 sentences: domain knowledge and background] | [What they would not know without specific exposure] | [What they optimize for in their role] |
[Add S-03 and beyond if needed.]

---

## INTERVIEW: S-01 [Role]

[Questions must be open-ended -- not leading, not yes/no. At least one follow-up question
must respond to a specific prior answer within this interview. Label follow-ups as FOLLOW-UP.]

Q1: [Open-ended question]
A1 (S-01): [Answer in S-01's voice -- vocabulary, concerns, and framing match the declared role
            and prior knowledge. Generic answers that could come from any persona fail here.]

Q2: [FOLLOW-UP on A1: (what you are following up on)] OR [Next question]
A2 (S-01): [Answer]

Q3: [Question or follow-up]
A3 (S-01): [Answer]

[Add Q4/A4 if needed. Minimum 3 exchanges.]

Surprising moment: [Label one answer or exchange where S-01's response was unexpected, in tension
with the interview goal, or revealed something the questions did not anticipate. Write "None
detected -- interview confirmed expectations" if genuinely absent.]

## EVIDENCE EXTRACTED: S-01

| E-ID | Evidence Item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Concrete insight, concern, requirement, contradiction, or signal -- not a transcript summary] | insight / concern / requirement / contradiction / signal | HIGH / MEDIUM / LOW | [One sentence: why this confidence level?] |
[Add E-02 and beyond. At least one row required per subject.]

---

## INTERVIEW: S-02 [Role]

Q1: [Open-ended question]
A1 (S-02): [Answer in S-02's voice -- different vocabulary, concerns, and framing from S-01]

Q2: [FOLLOW-UP or next question]
A2 (S-02): [Answer]

Q3: [Question or follow-up]
A3 (S-02): [Answer]

Surprising moment: [Label or write "None detected."]

## EVIDENCE EXTRACTED: S-02

| E-ID | Evidence Item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence item] | [type] | [confidence] | [rationale] |

---

[Repeat INTERVIEW and EVIDENCE EXTRACTED sections for S-03 and beyond if declared above.]

---

## SYNTHESIS

[Required when N >= 2 subjects. Write "N/A -- single subject run" for single-subject sessions.]

| Dimension | Finding |
|-----------|---------|
| Convergence | [What multiple subjects pointed toward, even from different angles] |
| Contradiction | [Where subjects disagreed, or where one subject's evidence undercuts another's] |
| Strongest signal | [The single most important evidence item from the whole session -- name the E-ID and why] |
| Open question | [What the interviews surfaced but no subject fully answered] |

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count, evidence_count, surprising_moments (count),
             synthesis_present (true/false), prior_signals_found (true/false).
```

---

## V-02: Phrasing Register (Conversational/Immersive)

**Axis:** Phrasing register -- conversational, second-person prose replaces imperative
directives and section headers. The skill reads like a thinking partner walking through
a research session, not a compliance checklist.

**Hypothesis:** An immersive register lowers friction for PM and researcher audiences
encountering the skill for the first time. The rubric's essential criteria (C-01 through C-05)
can still be met when the narrative questions are specific enough about persona identity and
grounding. The synthesis section is invited but not gated -- this is the control variation
for C-09/C-10 aspiration coverage. Expected to score full essential and recommended criteria;
aspirational results will vary by model execution.

```
You are running /prove-interview.

The goal here is to hear from people before you build. These are simulated interviews --
the subjects are not real, but their answers should be. Each subject has a job, a history,
and a perspective shaped by what they know and what they've been burned by. Your job is to
ask good questions, listen to their answers in their voice, and extract what the evidence
actually says.

---

**Before the interviews: check what you already know.**

Look in simulations/prove/ for any prior hypothesis, analysis, synthesis, or interview
artifacts on this topic. If you find them, list them here -- they change what you should ask.
If you find nothing, note that. A fresh-start session and a session with three prior artifacts
ask different questions.

Prior investigation: [list files found or "None found -- this is a fresh session."]
What these interviews are probing: [one sentence -- what question do you need these people to answer?]

---

**Who are we interviewing?**

Before the first question, introduce each subject. Who are they? What's their job? What do
they already know about this domain? What are they unlikely to know? What do they care about
more than anything else in their role? Get this right before you put words in their mouths --
an answer from someone who has lived this problem for ten years sounds very different from an
answer from someone encountering it for the first time.

Subject 1: [Name the role. 3-4 sentences: their background, domain knowledge, knowledge gaps,
            and primary concern. Enough specificity that their answers later are recognizably theirs.]

Subject 2: [Name the role. 3-4 sentences: same fields. Must be a meaningfully different profile
            from Subject 1 -- different role, different knowledge level, or different set of concerns.]

[Add Subject 3 if needed. Two subjects is the minimum for a session that produces variance.]

---

**Interview: Subject 1**

You are now with Subject 1. They've agreed to talk. Start with a question that doesn't lead
anywhere -- something genuinely open-ended that gives them room to surprise you. At some
point in this interview, follow up on something they said rather than moving to a new question.
That's where the real evidence usually lives.

Q: [Open-ended question -- does not imply the answer you want]
Subject 1: [Answer in Subject 1's voice -- their vocabulary, their concerns, their frame of
            reference. A compliance officer does not sound like a senior engineer. A first-time
            user does not sound like a power user. If the answer could come from any persona,
            rewrite it until it couldn't.]

Q: [Next question or follow-up -- if following up, note what you're following up on]
Subject 1: [Answer]

Q: [Continue for at least 3 exchanges total]
Subject 1: [Answer]

Something unexpected happened here: [Describe a moment where Subject 1's answer revealed a
tension, assumption, or concern that the questions didn't anticipate. If nothing surprising
emerged, write "No surprising moment -- the interview confirmed expectations."]

What did you learn? Pull the concrete evidence from this interview:
- [Evidence item: a specific insight, concern, requirement, contradiction, or signal. Not a
  summary of the conversation -- a specific thing this subject said that carries weight and
  could not have come from a generic AI response about this topic.]
- [Add more evidence items if the interview produced multiple distinct findings.]

---

**Interview: Subject 2**

[New voice. The questions may shift based on what Subject 1 revealed.]

Q: [Open-ended question -- grounded in Subject 2's declared profile]
Subject 2: [Answer in Subject 2's voice -- different vocabulary, different concerns, different frame]

Q: [Follow-up or next question]
Subject 2: [Answer]

Q: [Continue for at least 3 exchanges]
Subject 2: [Answer]

Something unexpected: [Surprising moment or "No surprising moment -- confirmed expected profile."]

What did you learn?
- [Evidence item rooted in Subject 2's declared knowledge and role]
- [Add more if needed]

---

[Continue for Subject 3 and beyond if declared above.]

---

**What do the interviews say together?**

[Write this when you have two or more subjects. Skip and mark N/A for single-subject sessions.]

Look across all the evidence. Where do the subjects converge -- even coming from opposite
directions? Where do they contradict each other? Which single piece of evidence is the most
important thing you heard in this session? And what question did the interviews open that
no subject fully answered?

Convergences: [What multiple subjects pointed toward]
Contradictions: [Where subjects disagreed or where one subject's evidence undercuts another's]
Strongest signal: [The single most important evidence item from the whole session, and why]
Unresolved question: [What's still open after all interviews]

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count, evidence_count, surprising_moments (count),
             synthesis_present (true/false), prior_signals_found (true/false).
```

---

## V-03: Role Sequence (Disposition-Ordered: Champion / Neutral / Skeptic)

**Axis:** Role sequence -- subjects run in fixed disposition order: Champion (most favorable,
most informed about the problem) → Neutral (pragmatic, no strong stake) → Skeptic (most
resistant, with a declared role-based reason to push back).

**Hypothesis:** Ordering subjects by disposition creates a natural arc that makes surprising
moments and genuine contradictions structurally easier to surface. The Champion establishes
the strongest-case baseline; the Neutral tests it for practicality; the Skeptic challenges
it with role-grounded resistance. A Skeptic who simply confirms the Champion adds no signal.
A Skeptic whose objection was never visible in the Champion's answers is the most important
evidence in the session. Disposition labeling also forces the simulation author to declare
honest profiles -- a "Skeptic" who agrees with everything is a profile failure, not a finding.

```
You are running /prove-interview. Interviews run in disposition order: Champion, then Neutral,
then Skeptic. Declare each subject's disposition before their interview begins. The Skeptic's
resistance must be role-grounded -- "change is hard" does not qualify.

---

## SETUP

Prior signals: [Search simulations/prove/ for prior artifacts on this topic. List files found
or write "None -- starting fresh."]
Interview question: [One sentence: what question does this session collectively answer?]

---

## SUBJECT PROFILES

[Declare all three subjects before any interview begins. Disposition must be honest --
the Champion's enthusiasm must have domain-specific grounding; the Skeptic's resistance
must have a plausible role-based reason, not generic reluctance.]

**S-01 -- CHAMPION**
Role: [Title or role]
Disposition: Champion -- [why they are favorable: they benefit most, or are most informed about the problem]
Prior knowledge: [What they know, what shaped their view, why their stance is informed rather than naive]
Concern: [The one thing that could reduce their enthusiasm -- champions have limits; name the limit]

**S-02 -- NEUTRAL**
Role: [Title or role]
Disposition: Neutral -- [what makes them uncommitted: they care about outcomes, not the idea itself]
Prior knowledge: [Their domain background, what they know from direct experience with this problem space]
Concern: [What they optimize for -- reliability, cost, team load, speed, something concrete]

**S-03 -- SKEPTIC**
Role: [Title or role]
Disposition: Skeptic -- [the specific role-based reason for resistance: past failure, competing priority,
             different model of the problem, or concrete constraint. Not "change aversion."]
Prior knowledge: [Their background -- they are not uninformed; they have a different frame]
Concern: [What specifically drives the skepticism -- name it from their role's perspective]

---

## INTERVIEW: S-01 (CHAMPION)

[Champion sets the favorable baseline. At least one question should probe their declared
concern -- unbounded enthusiasm is not a useful signal. Follow up on their strongest assertion.]

Q1: [Open-ended question -- leave room for both enthusiasm and qualification]
A1 (Champion): [Answer grounded in Champion's declared prior knowledge -- informed, favorable,
                but domain-specific. Not generic advocacy. References what they know about the problem.]

Q2: [FOLLOW-UP on A1 or next question]
A2 (Champion): [Answer]

Q3: [Probe the Champion's declared concern -- what would make them less enthusiastic?]
A3 (Champion): [Answer -- shows limits, not unlimited positivity]

Surprising moment: [Did the Champion reveal a concern or tension that the opening didn't suggest?
Label it. Or: "Champion confirmed favorable baseline -- no tension detected."]

Evidence extracted:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Specific insight, concern, requirement, contradiction, or signal] | [type] | HIGH/MEDIUM/LOW | [one-line rationale] |
[Add E-02 and beyond as needed.]

---

## INTERVIEW: S-02 (NEUTRAL)

[The Neutral has no agenda. They want to know if this actually works. Use what the Champion
revealed to shape questions here -- the Neutral is not in a vacuum. At least one question
should ask the Neutral to evaluate something the Champion claimed, without framing it as
"the Champion said."]

Q1: [Practical, outcome-focused question grounded in Neutral's declared concerns]
A1 (Neutral): [Answer in Neutral voice -- pragmatic, skeptical of abstractions, wants specifics.
               References their domain background.]

Q2: [Follow-up or next question]
A2 (Neutral): [Answer]

Q3: [Ask the Neutral to evaluate the Champion's strongest implicit claim without naming the Champion]
A3 (Neutral): [Answer -- may converge with or diverge from Champion's baseline]

Surprising moment: [Unexpected answer, tension with Champion baseline, or practical concern
the Champion didn't surface. Or: "Neutral confirmed pragmatic framing."]

Evidence extracted:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence] | [type] | [confidence] | [rationale] |

---

## INTERVIEW: S-03 (SKEPTIC)

[Most important interview. Skeptic's objections must be grounded in their declared role-based
concern -- not generic. At least one question must probe their specific declared reason for
resistance. Ask if there are conditions under which the objection would be satisfied.]

Q1: [Open question -- let them frame the problem in their own terms]
A1 (Skeptic): [Answer in Skeptic voice -- a different frame, different vocabulary, different
               concerns from both Champion and Neutral. References their declared background
               and specific resistance reason.]

Q2: [FOLLOW-UP: probe the root of the resistance -- what is it actually about?]
A2 (Skeptic): [Answer -- drill into the specific concern declared in the profile]

Q3: [Ask: under what conditions would your objection be satisfied?]
A3 (Skeptic): [Answer -- the most important evidence item in the session. The answer reveals
               whether the resistance is conditional or fundamental.]

Surprising moment: [Did the Skeptic reveal a latent openness, a deeper concern than declared,
or a direct contradiction with the Champion that changes the interpretation of prior interviews?
This is where the arc pays off. Or: "Skeptic confirmed declared resistance -- no arc detected."]

Evidence extracted:
| E-ID | Evidence item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence -- especially the conditions-for-satisfaction answer] | [type] | [confidence] | [rationale] |

---

## SYNTHESIS

Champion-to-Skeptic arc: [What did the Champion claim that the Skeptic challenged directly?
                           What survived the arc unchanged?]
Neutral verdict: [Did the Neutral's evidence side closer to Champion or Skeptic? Why?]
Convergence across dispositions: [What all three subjects agreed on, even from opposite positions]
Critical contradiction: [The most important place where evidence across subjects conflicts]
Strongest signal: [The single most important thing heard -- name the E-ID from which subject and why]
Open question: [What these three interviews fail to resolve, despite the arc]

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count (3), disposition_order (champion/neutral/skeptic),
             evidence_count, surprising_moments (count), arc_detected (true/false),
             synthesis_present (true), prior_signals_found (true/false).
```

---

## V-04: Lifecycle Emphasis + Output Format (Phase-Gated with Tables)

**Axes:** Lifecycle emphasis (four hard phases with gate checklists) + output format
(pre-printed tables enforce C-04/C-10 in Phase 3; synthesis table enforces C-09 in Phase 4).

**Hypothesis:** Separating interview transcript (Phase 2) from evidence extraction (Phase 3)
prevents the most common failure mode: evidence implied in dialogue but never explicitly named.
When extraction is a separate phase with its own gate, C-04 is unavoidable -- a blank Phase 3
table is a visible gate failure, not a silent omission. Phase 4 synthesis with a table structure
makes C-09 structural rather than aspirational. Gate failure counts in frontmatter make rubric
compliance machine-readable across runs.

```
You are running /prove-interview.
Four phases execute in order. Complete each phase before proceeding.
Persona profiles are locked after GATE 1 -- do not modify prior knowledge after interviews begin.
Evidence extraction is Phase 3 only -- do not extract in Phase 2 (transcript only).

---

## PHASE 1: SETUP

Goal: Establish context and declare all interview subjects before any interviews run.

Prior signals: [Search simulations/prove/ for prior hypothesis, analysis, synthesis, or interview
artifacts on this topic. List files with one-line summaries. Write "None -- fresh session" if
nothing found.]

Interview question: [One sentence: what question does this session collectively answer?]

Interview subjects:
[Declare all subjects. Minimum two for synthesis phase to be gradable.]

| # | Role / Title | Prior knowledge (what they know) | Gaps (what they don't know) | Primary concern |
|---|-------------|----------------------------------|-----------------------------|-----------------|
| S-01 | [Role] | [Domain knowledge and background] | [Knowledge boundaries] | [What they optimize for] |
| S-02 | [Role] | [Domain knowledge and background] | [Knowledge boundaries] | [What they optimize for] |
[Add rows as needed.]

GATE 1 -- required before PHASE 2:
[ ] Prior signal state declared (found or not found -- not silent)
[ ] Interview question is one sentence
[ ] At least two subjects declared with role, prior knowledge, gaps, and concern
[ ] No interview transcript content in Phase 1

---

## PHASE 2: INTERVIEW

Goal: Conduct each interview. Answers must stay in the declared persona's voice.
Phase 1 profiles are locked -- do not modify prior knowledge descriptions here.
Evidence extraction is Phase 3 only. No evidence bullets or tables in Phase 2.

[Run one interview block per subject declared in Phase 1.]

---

### INTERVIEW BLOCK: S-01 [Role]

[At least 3 question-answer exchanges. Questions are open-ended, not leading. At least one
follow-up must respond to a specific prior answer. Label: FOLLOW-UP on A[N].]

Q1: [Open-ended question]
A1 (S-01): [Answer in S-01's voice -- vocabulary, concerns, and framing match the Phase 1 profile.
            The answer references S-01's declared prior knowledge or knowledge gaps. Generic
            answers that fit any persona fail this phase.]

Q2: [FOLLOW-UP on A1: (what you are responding to)] OR [Next question]
A2 (S-01): [Answer]

Q3: [Question or follow-up]
A3 (S-01): [Answer]

Surprising moment: [One sentence labeling an unexpected answer, tension, or reveal.
Write "None detected -- interview confirmed Phase 1 profile" if nothing unexpected emerged.
Do not extract evidence here -- that is Phase 3.]

---

### INTERVIEW BLOCK: S-02 [Role]

Q1: [Open-ended question]
A1 (S-02): [Answer in S-02's voice -- distinct from S-01's vocabulary and frame]

Q2: [FOLLOW-UP or next question]
A2 (S-02): [Answer]

Q3: [Question or follow-up]
A3 (S-02): [Answer]

Surprising moment: [One sentence or "None detected."]

---

[Add INTERVIEW BLOCK for S-03 and beyond if declared in Phase 1.]

GATE 2 -- required before PHASE 3:
[ ] Each declared subject has a completed interview block
[ ] Each interview has at least one labeled follow-up (FOLLOW-UP on A[N])
[ ] Each interview has a surprising-moment note (even if "None detected")
[ ] No evidence extraction in Phase 2 -- only transcript and surprising-moment notes

---

## PHASE 3: EXTRACT

Goal: Extract discrete evidence items from each interview. Evidence lives here only.
Do not modify Phase 2 transcript. Read Phase 2 to extract -- do not introduce new content.

[Complete one evidence table per subject.]

### EVIDENCE: S-01

| E-ID | Evidence Item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Concrete insight, concern, requirement, contradiction, or signal -- specific, not a transcript summary] | insight / concern / requirement / contradiction / signal | HIGH / MEDIUM / LOW | [One sentence: why this confidence? Reference S-01's declared domain knowledge.] |
[Add E-02 and beyond. At least one row required per subject.]

### EVIDENCE: S-02

| E-ID | Evidence Item | Type | Confidence | Rationale |
|------|--------------|------|------------|-----------|
| E-01 | [Evidence item] | [type] | [confidence] | [rationale] |

[Add EVIDENCE tables for S-03 and beyond if needed.]

GATE 3 -- required before PHASE 4:
[ ] At least one evidence row per subject
[ ] Each evidence item is specific (not "Subject had concerns" -- name the concern)
[ ] Confidence level declared for each item with a one-line rationale
[ ] No new interview content introduced in Phase 3

---

## PHASE 4: SYNTHESIZE

Goal: Connect evidence across subjects. Required when N >= 2. Mark N/A for single-subject runs.
Read Phase 3 evidence tables only. Do not introduce new evidence in Phase 4.

| Dimension | Finding |
|-----------|---------|
| Convergence | [What multiple subjects pointed toward, even from different positions] |
| Contradiction | [Where subjects disagreed or where one subject's evidence undercuts another's] |
| Dominant signal | [Most important evidence item across the session -- state E-ID, subject, and why] |
| Arc | [How evidence shifted or developed from first interview to last] |
| Open question | [What the interviews surfaced but did not resolve] |

GATE 4 (artifact write check):
[ ] All Phase 3 evidence tables have at least one row
[ ] Synthesis table is complete (or marked N/A for single-subject run)
[ ] Gate failures from Gates 1-3 counted for frontmatter

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count, evidence_count, surprising_moments (count),
             synthesis_present (true/false), prior_signals_found (true/false),
             gate_failures (count of unchecked gate items across all gates -- 0 means clean run).
```

---

## V-05: Inertia Framing + Phrasing Register (Current-Practice Anchor)

**Axes:** Inertia framing (each persona has a declared current-practice field; every interview
opens with a mandatory current-practice question before any feature question) + phrasing
register (immersive and stakes-aware, not directive).

**Hypothesis:** C-05 (grounded, not invented) fails most often when persona answers sound
domain-plausible but are not grounded in declared knowledge -- they are invented domain
vocabulary rather than role-specific behavior. Anchoring every interview in current practice
forces answers to depart from a declared behavioral baseline. An answer about what someone
does today (not what they think about a feature) draws directly from declared prior knowledge
and cannot be fabricated without that fabrication being visible against the declared baseline.
This is the strongest structural enforcement of C-05 without adding a compliance gate. The
current-practice contrast also sharpens surprising moments (C-06): a reaction that contradicts
current practice is structurally visible; a reaction that merely comments on it is not.

```
You are running /prove-interview.
Before asking any subject about the proposed feature, you must ask what they do today without it.
The current-practice question is always Q1. Evidence is only as credible as the baseline it departs from.

---

**Context**

Check simulations/prove/ for prior artifacts on this topic. If prior interviews exist, read
their evidence sections before declaring subjects -- prior evidence reveals which voices and
current-practice baselines are missing from the record.

Prior artifacts found: [list with one-line summaries, or "None."]
What this session is probing: [one sentence]

---

**Who we're talking to**

Declare each subject before any interviews run. The current-practice field is load-bearing --
it determines what the subject could plausibly say in response to Q1. "Senior engineer" is not
enough: name their domain, their experience with the problem space, and what tools or workflows
they use today to handle the problem this feature addresses. A declared current practice of
"spreadsheet + weekly sync" produces different answers than "automated pipeline with manual
exception handling." That difference is the evidence.

Subject 1:
Role: [Title and specific domain]
Current practice: [What they do today to handle the problem this feature addresses -- specific
                   enough that Q1's answer is constrained by it. If they have no current practice
                   for this problem, say so: "No current practice -- this problem goes unaddressed."]
Prior knowledge: [What they know from experience in this domain]
Gaps: [What they would not know without specific exposure]
Stakes: [What they would gain or lose from a change to current practice]

Subject 2:
Role: [Title and specific domain]
Current practice: [Same specificity as Subject 1. Must differ meaningfully -- different domain,
                   different tool, or different relationship to the problem.]
Prior knowledge: [What they know]
Gaps: [What they don't know]
Stakes: [What they stand to gain or lose]

[Add Subject 3 if needed.]

---

**Interview: Subject 1 -- [Role]**

The first question is always about current practice. Do not ask about the proposed feature
until Subject 1 has described what they do today. The contrast between current practice and
feature reaction is where the evidence lives.

Q1 (current practice): Walk me through what you do today when [describe the problem scenario
in neutral terms -- not in terms of the proposed solution].
Subject 1: [Answer grounded in declared current practice -- what they actually do, including
            friction, workarounds, and what they've learned from doing it this way. The answer
            draws from the "current practice" and "prior knowledge" fields declared above.
            If current practice is "no current practice," the answer should reflect that gap.]

Q2: [Follow-up on current practice -- based on what Subject 1 said, probe the friction point,
     the workaround's cost, or the condition under which current practice breaks down]
Subject 1: [Answer -- still grounded in current practice, approaching its limits or failure modes]

Q3: [Introduce the proposed feature or change -- ask for Subject 1's reaction in light of what
     they just described. Do not reframe the feature; let their current-practice frame do the work.]
Subject 1: [Answer -- reaction from current-practice baseline. The contrast between Q1-A1 and
            this answer is the core evidence. The contrast should be visible.]

Q4 (optional follow-up): [If Subject 1's reaction was surprising, qualified, or contradicted
their current-practice description, follow up on the gap]
Subject 1: [Answer]

Surprising moment: [Did Subject 1's current-practice description reveal a constraint or concern
that changes the feature question? Did their reaction to the feature depart from the trajectory
their current-practice answers suggested? Label it, or write "Current practice confirmed
expected baseline -- no arc detected."]

Evidence from Subject 1:
[Each evidence item must be rooted in what Subject 1 said about current practice -- not in
invented domain vocabulary. The grounding test: could this item have been said by someone
with a different declared current practice? If yes, it's not grounded enough.]
- [Evidence item 1: what Subject 1's current-practice description revealed]
  Confidence: HIGH / MEDIUM / LOW -- [one sentence rationale, referencing their declared current practice or prior knowledge]
- [Evidence item 2 if present]
  Confidence: [level] -- [rationale]

---

**Interview: Subject 2 -- [Role]**

Q1 (current practice): [Adapt to Subject 2's domain and declared practice -- not the same
question as Subject 1's Q1 unless their domains are identical]
Subject 2: [Answer grounded in Subject 2's declared current practice -- different domain,
            different constraints, different friction from Subject 1]

Q2: [Follow-up on Subject 2's current-practice description]
Subject 2: [Answer]

Q3: [Feature or change question -- from Subject 2's current-practice baseline]
Subject 2: [Answer -- the contrast between Subject 2's current practice and the proposed
            change. May differ sharply from Subject 1's contrast.]

Surprising moment: [Label or "Current practice confirmed expected baseline."]

Evidence from Subject 2:
- [Evidence item rooted in Subject 2's current practice]
  Confidence: [level] -- [rationale anchored in their declared current practice]
- [Add more if present]

---

[Continue for Subject 3 if declared above.]

---

**What the session says**

[Required for N >= 2. Compare current-practice baselines, not just feature reactions.]

Current-practice comparison: [How did Subject 1's and Subject 2's current practices differ?
                               The differences reveal which user populations the feature helps
                               most and which it disrupts or leaves unchanged.]

Feature-reaction contrast: [How did each subject's reaction to the feature differ? Is the
                             contrast explained by their different current practices -- or does
                             it reveal something about the feature that transcends practice differences?]

Strongest signal: [The most important evidence item from the whole session. Name it and say
                   why it is more important than the others.]

What leading with current practice revealed: [One key finding that would have been invisible
                                              if you had led with the feature question instead
                                              of the current-practice question.]

---

Write artifact: simulations/prove/investigations/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, subject_count, evidence_count, surprising_moments (count),
             synthesis_present (true/false), prior_signals_found (true/false),
             current_practice_anchored (true -- all interviews opened with Q1 current-practice).
```

---

## Round 1 Design Notes

### Variation axis selection

Three single-axis variations from the five candidate axes:

- **Output format** (V-01): Maximum structural coverage of rubric criteria. Pre-printed tables
  with required columns make C-01/C-02 (persona profile), C-04 (evidence per subject), C-09
  (synthesis table), and C-10 (confidence column) unavoidable. Chosen as the structural
  enforcement baseline.

- **Phrasing register** (V-02): Control variation. Tests whether immersive, question-driven
  prose achieves full rubric compliance without structural enforcement. If V-02 scores as well
  as V-01 on essentials, structural overhead in V-01 is unnecessary cost. If V-02 underperforms
  on C-09/C-10, that quantifies the structural enforcement benefit.

- **Role sequence** (V-03): Tests disposition ordering as a mechanism for producing genuine
  arc (C-06) and cross-interview contradiction (C-09). The hypothesis is that ordering by
  disposition -- Champion to Skeptic -- makes surprising moments structurally more likely
  because the Skeptic must respond to the established favorable baseline. Most interview
  simulations run subjects in arbitrary order; this tests whether order matters for signal quality.

Two combination variations:

- **V-04 (Lifecycle emphasis + output format)**: Phase separation is the direct structural
  enforcement of C-04. When extraction is a separate phase with its own gate, evidence items
  cannot be implied and left implicit. Gate failure counting makes rubric compliance observable
  across model runs without manual inspection. This is the highest-oversight variation.

- **V-05 (Inertia framing + phrasing register)**: Current-practice anchoring is the strongest
  available mechanism for C-05 (grounded, not invented) without adding a compliance gate. Every
  answer must depart from a declared behavioral baseline, making invented domain vocabulary
  visible as a departure. The immersive register keeps friction low while the structural
  current-practice Q1 requirement does the grounding work.

### C-05 (grounded, not invented) coverage comparison

| V | How C-05 is enforced |
|---|---------------------|
| V-01 | Persona profile table: prior knowledge is a required column, making answers checkable against declared scope |
| V-02 | Behavioral instruction: "the answer should not be universally applicable platitudes" |
| V-03 | Profile declaration: prior knowledge and knowledge gaps declared per subject; Skeptic's resistance must be role-grounded |
| V-04 | Phase 1 profile table locked at Gate 1; Phase 2 answers must match Phase 1 declarations |
| V-05 | Current-practice Q1 anchor: every answer departs from declared behavioral baseline, not declared vocabulary |

V-05 has the strongest grounding mechanism (behavioral baseline). V-04 has the most auditable
enforcement (gate checklist + locked profiles). V-01 and V-03 rely on declared prior knowledge
as a check surface. V-02 relies on behavioral instruction -- weakest enforcement.

### C-06 (surprising moment) surface comparison

| V | How surprising moments are surfaced |
|---|-------------------------------------|
| V-01 | Per-subject "Surprising moment" field after each interview block |
| V-02 | Per-subject "Something unexpected happened here" narrative field |
| V-03 | Per-subject field + arc-level synthesis: "Champion confirmed vs Skeptic challenged" |
| V-04 | Per-interview-block field in Phase 2 (transcript only) -- surprise is noted, not extracted |
| V-05 | Per-subject field + structural trigger: current-practice-to-feature-reaction contrast is a built-in arc |

V-03 has the richest surprising-moment surface: disposition ordering creates an expected arc
against which surprises are measured. V-05's current-practice Q1 creates a structural trigger
for contrast that V-01/V-02 lack.

### Open research question for R2

Does V-05's current-practice anchor produce materially better C-05 compliance than V-01's
persona profile table? Both enforce grounding structurally, but V-05 forces behavioral
anchoring while V-01 forces declarative anchoring. The hypothesis is that behavioral
(what they do) is harder to invent plausibly than declarative (what they know), making
C-05 failures more visible in V-05. Testable on live model runs.
