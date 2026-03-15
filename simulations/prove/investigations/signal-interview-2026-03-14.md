---
skill: prove-interview
topic: signal
item: interview
date: 2026-03-14
skill_version: 0.1.0
input: plugin-plan.md + signal.skills.yaml + PRINCIPLES.md
---

# /prove:interview -- Signal Plugin: 3 Dynamics Developer Interviews

**Hypothesis**: Dynamics 365 / Power Platform developers will immediately understand
Signal's value and adopt it within their first session.

**Falsification condition**: If 2 of 3 developers cannot articulate what Signal does
after a 5-minute intro, or if they identify a blocker that prevents first-run completion,
the hypothesis is refuted.

**Interview subjects**: 3 developers from the Dynamics/Power Platform ecosystem,
selected to span experience levels and product areas.

---

## Interview 1: Ravi Krishnamurthy
**Role**: Senior Power Platform Developer, Insurance vertical
**Experience**: 6 years. Builds Power Automate flows, Canvas apps, and Dataverse plugins.
Writes specs in Word docs, tracks bugs in DevOps, does almost no simulation before building.
**Prior Signal exposure**: None. Saw the all-hands announcement 10 minutes ago.

### Opening question: "What do you understand Signal to be?"

"So it's like... a set of prompts that help you think through a feature before you build it?
And the prompts are organized by who's asking the question -- like a PM would run /scout and
a developer would run /trace? That part makes sense to me. I always wish I had done more
analysis before I built some things.

But I'm confused about the 'topic' concept. What is a topic? Is it a feature? A sprint? A
user story? The docs say it's a 'topic prefix that ties artifacts together' which doesn't
tell me what it IS."

**Finding 1**: "Topic" as a concept is clear in the system but the word is abstract to a
developer who thinks in terms of features, user stories, and work items. Needs a concrete
analog: "A topic is like a feature branch for your thinking -- just as all your code changes
for Feature X go on one branch, all your Signal signals for Feature X go under one topic."

### Question: "Walk me through how you'd use Signal for your next feature."

"OK, so my next piece of work is adding a new approval workflow to our claims processing
system. I'd probably run... /scout:requirements? To pull out what the feature needs? And
then maybe /trace:state to walk through what happens when a claim goes through the new
approval step. That one I understand immediately -- I hand-compile state transitions ALL
the time in Confluence. If Signal does that with stock roles and produces a file, that saves
me 2 hours.

But I'm looking at the skill list and I'm not sure which one to run FIRST. Is there an
order? Like, does /scout always come before /draft? The /program:plan skill probably tells
me the order but I don't want to run a whole program just to ask my first question."

**Finding 2**: The ordering between skills is implicit (documented in plugin-plan.md stage
lifecycle) but not surfaced on first use. Ravi correctly identified that a new user needs
a recommended starting path without having to run /program:plan first. A simple "Start here"
card per audience in the README would solve this. Developer: start with /trace:state.
PM: start with /scout:requirements. Architect: start with /review:design.

### Question: "What would stop you from adopting this?"

"Honestly? The biggest thing is -- what does my team see? If I run /trace:state and
produce a Markdown file, is that visible to my teammates? Do they have to install Signal
to read it? Is it in the PR? In DevOps? The artifact lands in the repo which is good,
but there's no integration with our actual work tracking. I want to link a Signal artifact
to a work item, not just have it floating in a folder.

Also -- and this is real -- my manager asks me to write specs in a specific format. If
Signal produces a Markdown file and my manager wants a Word doc in our spec template,
that's two artifacts I have to maintain."

**Finding 3 (MAJOR)**: Work item integration gap. Ravi needs Signal artifacts to connect
to Azure DevOps work items. This is not in the current spec. The artifact lands in git,
but the connection to the work item (which is where his manager tracks progress) is missing.

**Finding 4**: Output format lock-in. Markdown is the right internal format, but export
paths to Word, JIRA, ADO matter for enterprise adoption. Not blocking for v0.1 but it is
a clear adoption barrier at the team/org level.

**NPS prediction**: 7/10. Ravi would use Signal personally but struggles to advocate for
it to his team without ADO integration.

---

## Interview 2: Amara Osei
**Role**: D365 Finance Architect, Banking vertical
**Experience**: 12 years. Architects ledger designs, defines data models, leads enterprise
implementations. Writes extensive specs. Very methodical.
**Prior Signal exposure**: None. Heard about it from a colleague.

### Opening question: "What do you understand Signal to be?"

"I've read the plugin-plan.md. Signal is a structured investigation methodology packaged
as Claude Code skills. The architecture is sound -- 9 namespaces covering the full
pre-build lifecycle, each namespace mapped to an audience. The topic naming convention
is clean. I like that artifacts are append-only and dated.

My question is about reproducibility. If I run /trace:state on a spec today and another
architect runs the same command next week on the same spec, will we get materially different
results? How deterministic is this?"

**Finding 5 (MAJOR)**: Reproducibility concern. Amara, as an architect, needs to understand
the determinism model before she can approve Signal for her team's methodology. The current
specs don't address this explicitly. Need to add to spec and PRINCIPLES.md: "Signal produces
advisory artifacts, not deterministic outputs. Two runs on the same input will find the
same structural issues but may phrase them differently. The finding categories (P1/P2/P3) and
phase coverage (setup/execute/findings) are deterministic; the specific wording is not."

### Question: "Which Signal skills would you use for your work?"

"Definitely /trace: -- all of it. State validation, contract testing, deployment tracing.
I hand-compile these today in Confluence using my own templates. If Signal produces
equivalent output with less setup, I will use it.

/review:design is interesting. The auto-selected domain expert feature -- will it actually
select a D365 Finance expert or will it select a generic 'financial systems architect'?
The quality of the review depends entirely on the quality of the expert selection.

/prove: is appealing for the research questions I bring to architecture reviews. Currently
I write hypothesis documents in OneNote. If Signal formalizes that into a prove:hypothesis
→ prove:websearch → prove:synthesize pipeline, that is genuinely useful."

**Finding 6**: Domain expert selection quality is the key adoption gate for /review:design
in enterprise contexts. Amara's specific concern: will the auto-selected expert know the
difference between a D365 Finance ledger and a generic financial database? Custom roles
in `.craft/roles/signal/` are the answer, but the path to creating them needs to be clear.

### Question: "What would stop you from adopting this?"

"Two things. First: our firm has a model risk management requirement (SR 11-7). Any AI
tool that influences design decisions needs to be approved. Signal's compliance story is
actually very good -- it's methodology, not a model, git-native, no data persistence --
but I need the compliance argument written up in a format I can hand to our model risk
committee. A one-page Signal Compliance Brief for regulated industries would remove the
gate entirely.

Second: the skill bodies are stubs right now. I looked at the generated SKILL.md files.
'Implementation for trace-state.' That's not useful. I understand they will be filled in,
but my assessment of Signal depends on seeing an actual skill that works, not a scaffold."

**Finding 7 (MAJOR)**: The stub SKILL.md bodies are visible to sophisticated evaluators and
will kill adoption among architects who evaluate the actual output before recommending it.
This confirms: shipping with stub bodies is not an option. Golden prompts must be in the
SKILL.md files before any external demo.

**Finding 8**: Signal Compliance Brief needed. A one-pager specifically for SR 11-7 and
SOC 2 compliance reviewers: Signal is methodology, not a model. Git-native, no telemetry,
no data persistence beyond the repo. Artifacts are advisory, not automated decisions.

**NPS prediction**: 9/10 -- IF the skill bodies are real. 3/10 on stubs.

---

## Interview 3: Preethi Sundar
**Role**: Copilot Studio Developer, Microsoft Healthcare Solutions
**Experience**: 3 years. Builds agent conversations, designs topic graphs, tests dialog
flows. Relatively new to structured methodology.
**Prior Signal exposure**: Saw the all-hands slide deck.

### Opening question: "What do you understand Signal to be?"

"I think I get it? It's like... a way to stress-test your design before you build it.
You describe what you're building and Signal plays all the different roles -- PM, user,
compliance person, architect -- and tells you what's wrong before you've written any code.

I'm most excited about /flow:conversation. I build conversation flows all day and the
hardest part is finding the dead ends and the weird edge cases before we go to testing.
If Signal can simulate a multi-turn conversation and find where the topic graph breaks, I
would use that every sprint."

**Finding 9 (DELIGHT)**: /flow:conversation resonates immediately with Copilot Studio
developers. Preethi immediately understood the value without explanation. This is the
skill with the most natural product-market fit in the Dynamics ecosystem.

### Question: "Walk me through how you'd use it."

"I'd run /flow:conversation on my topic graph spec. But wait -- how does Signal know
what my topic graph looks like? Does it read my Copilot Studio export? Or do I describe
it in text? I can't paste a YAML export into a Claude prompt easily.

And for /trace:contract -- I have expected outputs that I've already written in test cases.
Can I point Signal at my existing test cases and have it compare against those? Or does it
generate its own expected outputs from scratch?"

**Finding 10**: Input format ambiguity for technical skills. Preethi needs to know what
format to provide her topic graph in. The specs say "product concept (1-2 sentences)" for
most inputs but technical skills like /flow:conversation and /trace:contract need richer
input. The spec should clarify: plain text description is always valid, but Signal can also
read spec files, YAML exports, or existing test files if you provide a path.

### Question: "What would stop you from adopting this?"

"Honestly nothing technical. I'd try it today if the skills were real. My concern is
time. I'm already behind on my current sprint. If running Signal adds 2 hours to my
pre-build process, my manager will push back. But if it saves me 4 hours of post-build
rework -- which it probably would -- then it pays for itself.

The thing that would make me an evangelist: if I could show my manager a Signal artifact
and say 'here is the conversation flow I validated before I built it, and here are the 3
edge cases I caught that we didn't have test cases for.' That's the before/after story
that sells it."

**Finding 11**: The ROI story needs a before/after artifact comparison. "Here's what
Signal found vs. what we would have caught in testing" is the adoption narrative for
individual contributors selling it up to their managers.

**NPS prediction**: 9/10 -- IF the skills work and the learning curve is under 15 minutes.

---

## Synthesis

### Hypothesis verdict: PARTIALLY CONFIRMED

Dynamics developers DO immediately grasp Signal's value for their specific pain points.
Ravi saw /trace:state as 2 hours saved. Amara wants /review:design with domain experts.
Preethi immediately connected /flow:conversation to her daily work.

But "adopt within their first session" is REFUTED. Three blockers prevent first-session
adoption:

1. **Stub skill bodies** (Amara) -- cannot evaluate what isn't there
2. **Work item integration gap** (Ravi) -- ADO/JIRA connection missing
3. **Input format ambiguity** (Preethi) -- unclear how to feed technical specs into skills

### New findings

| ID | Finding | Severity | Persona |
|----|---------|----------|---------|
| F-01 | "Topic" concept needs a concrete analog (feature branch for thinking) | MINOR | Ravi |
| F-02 | No "start here" path per audience | MAJOR | Ravi |
| F-03 | ADO/work item integration gap | MAJOR | Ravi |
| F-04 | Output format lock-in (Markdown only) | MINOR | Ravi |
| F-05 | Reproducibility model not documented | MAJOR | Amara |
| F-06 | Domain expert selection quality is adoption gate for /review:design | MAJOR | Amara |
| F-07 | Stub SKILL.md bodies kill sophisticated evaluators | CRITICAL | Amara |
| F-08 | Signal Compliance Brief needed for regulated industries | MAJOR | Amara |
| F-09 | /flow:conversation resonates immediately with Copilot Studio devs | DELIGHT | Preethi |
| F-10 | Input format ambiguity for technical skills | MAJOR | Preethi |
| F-11 | ROI story needs before/after artifact comparison | MAJOR | Preethi |

### What this changes for shipping

**Critical (before any demo)**: F-07 -- ship with real skill bodies or don't ship.
**High (before all-hands)**: F-02 (start here paths), F-08 (compliance brief), F-10 (input format docs)
**Post-launch backlog**: F-03 (ADO integration), F-04 (export formats)
