# Signal Achievements

Achievements are not grinding. They are milestones that teach good evidence practice by
rewarding it. Each one marks a moment when a team did something worth doing: ran their
first skill, falsified a hypothesis, covered all nine namespaces before committing.

The most culturally important achievement in this list is **Falsified**. It is earned when
a hypothesis does not hold. That is not a failure. In Signal's evidence philosophy, a
hypothesis that cannot be falsified is not a hypothesis -- it is an assertion. A team that
earns Falsified has demonstrated intellectual honesty: they investigated rather than
confirmed. No other achievement says more about a team's evidence posture than that one.

The unearned achievements are the curriculum. Look at what you have not yet earned. That
is what Signal can do that you have not tried yet.

Achievements are a menu, not a ramp. You can ship great features using only 3 namespaces. The achievement system exists to show you what's possible, not to require you to earn it.

---

## EXPLORATION

*First time in each namespace. Nine achievements. Every team earns the first one.*

**First Signal**
Run any Signal skill for the first time.
*Trigger: any skill completes successfully.*
*Why it matters: every evidence campaign starts with a single run. This is yours.*

**Discover Pioneer**
Run your first scout skill.
*Trigger: any discover-* skill completes (discover-competitors, discover-feasibility, discover-naming,
discover-compliance, discover-market, discover-stakeholders, discover-positioning, discover-requirements).*
*Why it matters: the scout namespace is where you answer "why would teams do nothing?" --
the question Signal exists to surface. Eight scout skills remain after this one.*

**Specify Founder**
Run your first draft skill.
*Trigger: any specify-* skill completes (specify-spec, specify-proposal, specify-pitch, discover-brainstorm).*
*Why it matters: drafting without prior signals is guessing. With them, it is grounded authorship.*

**Validate Reviewer**
Run your first review skill.
*Trigger: any validate-* skill completes (validate-design, validate-code, validate-users, validate-customers).*
*Why it matters: review is the first point where someone other than the author looks at the work.
Signal routes this through structured personas, not ad-hoc feedback.*

**Simulate Tracer**
Run your first flow skill.
*Trigger: any simulate-* skill (flow) completes (simulate-lifecycle, simulate-conversation, simulate-trigger,
simulate-dataflow, simulate-integration, simulate-throttle, simulate-stress).*
*Why it matters: you have described what you are building. Now you have simulated how it
actually behaves at runtime. These are different questions.*

**Verify Tracer**
Run your first trace skill.
*Trigger: any simulate-* skill (trace) completes (simulate-request, simulate-state, simulate-contract, simulate-component,
simulate-deployment, simulate-migration, simulate-permissions).*
*Why it matters: tracing by hand finds what testing misses -- the gap between what the spec says
and what the implementation does.*

**Evidence Investigator**
Run your first prove skill.
*Trigger: any discover-* skill (evidence) completes (discover-hypothesis, discover-websearch, prove-intelligence,
prove-prototype, discover-analysis, prove-interview, discover-synthesize, prove-publish).*
*Why it matters: you have a feature idea. prove asks whether the assumption underneath it is
actually true. Most teams skip this. You did not.*

**Adoption Listener**
Run your first listen skill.
*Trigger: any validate-* skill (adoption) completes (validate-feedback, validate-support, validate-adoption).*
*Why it matters: you have simulated your users before they arrived. The support tickets you
predict now are cheaper than the ones filed after ship.*

**Commitment Planner**
Run your first program or topic skill.
*Trigger: any program-* or topic-* skill completes.*
*Why it matters: signals without a narrative are noise. program and topic are the namespaces
that turn a pile of artifacts into a decision.*

---

## DEPTH

*Run multiple skills in the same namespace on one topic. Deliberate, not accidental.*

**Full Scout**
Run all 8 scout skills on one topic.
*Trigger: discover-competitors, discover-feasibility, discover-naming, discover-compliance, discover-market,
discover-stakeholders, discover-positioning, and discover-requirements all completed for the same topic.*
*Why it matters: full scout is the most complete market and technical intelligence available
before a spec is written. This is the intended practice for high-stakes features.*

**Full Prove**
Run all prove skills on one topic. The hardest evidence campaign in Signal.
*Trigger: discover-hypothesis, discover-websearch, prove-intelligence, prove-prototype, discover-analysis,
prove-interview, and discover-synthesize all completed for the same topic.*
*Why it matters: a team that has done full prove has exhausted the hypothesis space before
committing. They have not just believed a thing -- they have tested it.*

**Full Flow**
Run all 7 flow skills on one topic. You simulated the whole system.
*Trigger: simulate-lifecycle, simulate-conversation, simulate-trigger, simulate-dataflow, simulate-integration,
simulate-throttle, and simulate-stress all completed for the same topic.*
*Why it matters: a spec with full flow coverage has had its behavior -- state machine, data
path, triggers, throttle behavior, failure modes -- played out before a line of implementation
is written.*

**Full Trace**
Run all trace skills on one topic. Complete implementation verification.
*Trigger: simulate-request, simulate-state, simulate-contract, simulate-component, simulate-deployment,
simulate-migration, and simulate-permissions all completed for the same topic.*
*Why it matters: every failure mode class has been checked. This is the post-commitment
analog of Full Scout -- as thorough as you can get on the implementation side.*

**Deep Listen**
Run all 3 listen skills on one topic. You know what users will say before they say it.
*Trigger: validate-feedback, validate-support, and validate-adoption all completed for the same topic.*
*Why it matters: you have predicted the feedback before the feature ships, the support tickets
before they are filed, and the adoption curve before the rollout begins.*

**Signal Saturated**
Run 10 or more skills on a single topic across any namespaces.
*Trigger: 10+ skills completed for the same topic, regardless of namespace.*
*Why it matters: this is the gateway between casual use and committed investigation. More
than casual, less than complete. A topic that has reached Signal Saturated has been seriously examined.*

---

## COVERAGE

*Cross-namespace coverage on one topic. Signal's core argument made visible.*

**Evidence Starter**
Cover 3 or more namespaces on a single topic.
*Trigger: skills from 3 distinct namespaces completed for the same topic.*
*Why it matters: you have moved past single-skill use into coordinated evidence gathering.
The feature is being investigated, not just specced.*

**Evidence Builder**
Cover 5 or more namespaces on a single topic.
*Trigger: skills from 5 distinct namespaces completed for the same topic.*
*Why it matters: more than half the namespaces on one topic. The feature has been scouted,
drafted, reviewed, and investigated in some combination. This is substantive coverage.*

**Critical Path**
Cover the 3 critical namespaces on one topic: discover-feasibility, any trace skill, and any listen skill.
*Trigger: discover-feasibility + any trace-* + any listen-* all completed for the same topic.*
*Why it matters: these three namespaces answer the questions that matter most for Tier 2 features --
can we build it, does the implementation hold, and will teams adopt it.*

**Fast Coverage**
Reach 5 namespaces within 24 hours on one topic.
*Trigger: skills from 5 distinct namespaces completed for the same topic within a 24-hour window.*
*Why it matters: evidence gathering does not have to be slow. Signal is designed for a morning
of investigation before a commit, not a month of research. This is that morning.*

**Pre-Commitment Ready**
Cover 7 or more namespaces on a single topic.
*Trigger: skills from 7 distinct namespaces completed for the same topic.*
*Why it matters: near-complete coverage. A team at 7+ namespaces has the evidence density
that Signal's inertia model says is required before committing to a feature with significant
implementation cost.*

**Full Coverage**
Cover all 9 namespaces on a single topic.
*Trigger: at least one skill from each of the 9 namespaces completed for the same topic.*
*Why it matters: this is rare and deliberate. Earning Full Coverage is a statement: we examined
this feature from every angle before committing. Nothing was left unexamined.*

---

## QUALITY

*Output quality, not just completion. Tied to rubric scores and specific findings.*

**First Gold**
Any skill achieves essential-pass on the first run -- no prior run on this topic with this skill.
*Trigger: a skill scores >= 80 on its golden rubric on the first invocation for a topic.*
*Why it matters: first-run quality is the signal that a topic was well-scoped and the context
was rich. No iteration required. This is the aspirational standard.*

**Inertia Identified**
discover-competitors scores inertia as the primary or co-primary competitor.
*Trigger: any discover-competitors run returns inertia / status quo as the primary competitive threat.*
*Why it matters: this should be every run. Inertia is always the primary competitor for internal
features. Earning it once is a reminder of the rule -- and a prompt to check if you understood it.*

**Sharp Hypothesis**
discover-hypothesis produces a hypothesis assessed as specific and falsifiable.
*Trigger: discover-hypothesis output includes a hypothesis that names a specific mechanism and
declares a specific, observable prediction (rubric criterion: hypothesis is falsifiable).*
*Why it matters: a sharp hypothesis can be wrong in a specific way. "Teams with 5+ namespaces
covered are 2x more likely to pass first code review" is sharp. "More coverage is better" is not.*

**Simplified**
A skill output passes QU5 simplification: 20%+ word reduction with all essential criteria preserved.
*Trigger: a skill's output is verified to have reduced length by >= 20% while passing the
essential rubric criteria.*
*Why it matters: clarity is a quality signal. A shorter output that passes every criterion is
more useful than a longer one that does too.*

**Evidence Grounded**
discover-websearch produces 5 or more sources, all with direct quotes, using --confidence strict.
*Trigger: discover-websearch run with --confidence strict returns >= 5 sources, each with a
directly quoted passage and URL.*
*Why it matters: grounded evidence is evidence you can check. No paraphrase, no training data
as fact -- only claims you can trace to a source.*

**High-Fidelity Spec**
specify-spec scores >= 75 on its rubric in the first run, with discover-feasibility and
discover-requirements artifacts available as context.
*Trigger: specify-spec run with both discover-feasibility and discover-requirements present for the same
topic, first-run score >= 75.*
*Why it matters: a high-quality spec with prior context demonstrates the chain. Feasibility
constraints and requirements were grounded, not assumed.*

---

## CHAIN

*Run prerequisite skills before dependent skills on the same topic. Skill ordering matters.*

**Scout-First Spec**
Run discover-feasibility AND discover-requirements before specify-spec on the same topic.
*Trigger: discover-feasibility and discover-requirements both completed before specify-spec runs on
the same topic, with those artifacts available as context.*
*Why it matters: this is the intended pre-spec workflow. Scout-first specs have feasibility
constraints and requirements grounded in investigation, not assumption.*

**Evidence-Based Draft**
Run discover-hypothesis before specify-spec on the same topic.
*Trigger: discover-hypothesis completed before specify-spec runs on the same topic, with the
hypothesis artifact available as context.*
*Why it matters: a spec that starts from an investigated hypothesis asserts tested assumptions,
not untested ones. "We hypothesized X and found it holds under Y conditions" is a stronger spec.*

**Grounded Review**
Run specify-spec before validate-design on the same topic, with the draft artifact passed as context.
*Trigger: specify-spec completed before validate-design runs on the same topic, draft artifact
available to the review.*
*Why it matters: the entire pre-commitment workflow depends on reviewing real artifacts, not
feature descriptions. This is the minimum chain: have something real to review before reviewing it.*

**Simulation-Before-Build**
Run simulate-lifecycle before any trace skill on the same topic.
*Trigger: simulate-lifecycle completed before any simulate-* skill (trace) runs on the same topic.*
*Why it matters: simulating behavior before tracing implementation catches design flaws before
they are built in. Trace finds what was implemented. Flow found what should have been.*

**Full Pre-Commit Chain**
Run skills from scout, draft, and review namespaces on the same topic, in that order.
*Trigger: at least one skill from each of scout, draft, and review namespaces completed in
sequence (scout artifacts available to draft, draft artifact available to review) on the same topic.*
*Why it matters: the complete pre-commitment chain through the three highest-value namespaces.
Scouted, specced, reviewed. Evidence-before-commitment at its most direct.*

---

## DISCOVERY

*Unexpected findings. The category aligned most directly with Signal's epistemological principles.*

**The Echo**
Complete rhythm-reflect. You found something you did not expect.
*Trigger: rhythm-reflect completes successfully for any topic.*
*Why it matters: rhythm-reflect asks "what did we learn that we did not expect?" The echo is
institutional memory -- what the next team finds when they search for prior work on this path.*

**Unexpected Signal**
Any skill run produces a finding the team tagged as unexpected -- a changed prior.
*Trigger: a skill output includes a finding marked as "unexpected" that contradicts a stated
prior (e.g., a competitor the team thought was irrelevant is actually the primary market player).*
*Why it matters: Signal's evidence-gathering is most valuable when it finds things you did not
expect. An achievement system that only rewards planned coverage misses this class of value entirely.*

**Falsified**
discover-hypothesis returns INCONCLUSIVE or REJECTED on any topic.
*Trigger: discover-hypothesis output contains an outcome field of INCONCLUSIVE or REJECTED.*
*Why it matters: this is the most important achievement in Signal. A hypothesis that is
falsified is not a failed feature -- it is a learning that redirects effort before commitment,
when redirection is cheap, not after, when it is expensive. A team that has never earned
Falsified has never truly tested a hypothesis. By naming this achievement "Falsified" rather
than something softer, Signal forces a vocabulary confrontation: negative results are evidence
events, not failures. Earn this. Mean it.*

**Inertia Wins**
Your inertia analysis concludes the status quo is sufficient. Stop. Pivot.
*Trigger: discover-competitors run for a topic returns a finding that explicitly concludes the
current status quo or workaround is sufficient and the feature does not clear the adoption bar.*
*Why it matters: this is the bravest achievement in Signal. Stopping before building because
the evidence says to is harder than building anyway. The teams that earn this protect their
organization from features that would have shipped flat.*

---

## CORP AND CREW

*Governance achievements. Signal at the org level.*

**First Review**
Run roles-review for the first time.
*Trigger: roles-review completes successfully on any artifact.*
*Why it matters: the first time your org's roles see an artifact, you learn whether your
role definitions are calibrated to the actual work. Every subsequent review gets sharper.*

**Full Corp**
Run corp-rob --stage all.
*Trigger: corp-rob completes with --stage all, producing artifacts for all ROB stages.*
*Why it matters: leadership, teams, PM, TPM, Arch Board, Exec Office -- all stages reviewed.
This is not an artifact check. It is an org-level readiness check.*

**PR Reviewed**
Run corp-pr on a real pull request.
*Trigger: corp-pr completes on a real PR number, with findings from relevant org roles.*
*Why it matters: every relevant role reviewed the PR. The security architect found the access
control gap the PM reviewer never looked for. This is what org-level code review looks like.*

**Simulation Rehearsal**
Run corp-rob before a real committee meeting, then compare findings after.
*Trigger: corp-rob completed on a topic before the corresponding real committee meeting;
team recorded a comparison of simulated findings vs. actual meeting outcomes.*
*Why it matters: Signal's ROB is a rehearsal, not a replacement. The gap between what the
simulation predicted and what the meeting actually surfaced is itself a signal about your
role definitions and org configuration.*

---

## TEAM (v2)

*These achievements require multiple contributors. Proposed for v2 implementation.*

**First Team Signal**
Two people run skills on the same topic.
*Trigger: two distinct contributors complete skills on the same topic (first occurrence).*
*Why it matters: Signal becomes more valuable as shared practice. The transition from individual
evidence gathering to team evidence gathering is a qualitative shift, not just a headcount change.*

**Shared Coverage**
A topic reaches 5 or more namespaces with contributions from 2 or more people.
*Trigger: topic has skills from 5+ namespaces with >= 2 distinct contributors.*
*Why it matters: five namespaces covered by one PM looks different than five namespaces covered
by a PM, an engineer, and a designer. Perspective diversity is evidence diversity.*

**Debate Starter**
Two team members run the same skill on the same topic and reach different findings on a key dimension.
*Trigger: two distinct contributors run the same skill on the same topic; their outputs contain
divergent assessments of the same feature dimension.*
*Why it matters: divergence is information. Two validate-design runs that disagree about a section
indicate either genuine ambiguity in the section or different interpretive frames in the reviewers.
Either case is worth surfacing, not averaging away.*

---

## Achievement Record

An achievement record is not just a gamification artifact. It is a compact form of practice
documentation.

A team that has earned **Full Pre-Commit Chain** on a topic has documented that the feature
was scouted, specced, and reviewed in sequence. A team that has earned **Falsified** has
documented that they investigated rather than confirmed. A team that has earned **Pre-Commitment
Ready** has documented that coverage was deliberate and complete.

The achievement list is the curriculum. The unearned achievements are the path.

Start with any skill. The first achievement costs nothing.

## Calibration

A focused session of 4-8 skills on one topic typically earns **11-15 achievements**. The
EXPLORATION group (9 achievements) fills almost automatically once you cover 5 or more
namespaces. The CHAIN group earns for free when you run skills in the recommended order.
The DEPTH group rewards breadth within a namespace — running all 8 scout skills earns
Full Scout without extra effort.

The achievements that require deliberate attention are:

- **Falsified** — requires an honest investigate-then-report on a hypothesis, not a confirmation
- **The Echo** — requires running rhythm-reflect after the session ends
- **Inertia Wins** — requires that your competitors scan actually conclude "do not build" (rare, brave, right when true)
- **Full Coverage** — requires touching all 9 namespaces, which means intentionally covering rhythm/roles

Run `/achievements <topic>` after any skill session to see your current count and the 2
skills that would unlock the most remaining achievements.
