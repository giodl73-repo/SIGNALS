---
skill: scout-competitors
topic: plugin
item: signal-plugin-competitive-brief-full
date: 2026-03-15
skill_version: golden-2026-03-14
run: R7 -- expanded from golden; all 25 findings numbered
input: CLAUDE.md, plugin-plan.md, prior runs (2026-03-14, golden-2026-03-15)
---

# Competitive Brief: Signal Plugin for Claude Code (Full Run)

**The strategic lead:** Signal has one uncontested position -- the pre-build evidence layer
inside the developer's own repo. Every named competitor either activates after the
decision to build has already been made, lives outside the developer's IDE entirely, or
operates on a single axis (code generation, project tracking, web research) rather than
Signal's multi-namespace evidence corpus. The real threat is not any named tool. It is the
combination of Anthropic's first-party /feature-dev plugin (adjacent execution-phase slot),
raw inertia (decision to skip entirely), and raw LLM prompting (80% of the output with
zero friction). Signal must win the "should we?" stage before /feature-dev owns the
"how do we?" stage -- and it must do this while teams feel no pain from skipping.

---

## 1. The Primary Competitor: Inertia

**Threat level: HIGH. Always. Score this one first.**

Inertia is not laziness. It is a rational response to how software teams are incentivized.

**Why teams do nothing:**

- Sprint planning commits the work before the question "should we?" is asked. Evidence
  gathering after a feature is in the sprint feels like asking permission retroactively.
- The cost of skipping is invisible and deferred. A missed competitive signal from March
  shows up as a product gap in September. The decision to skip appears free on the day
  it is made.
- Senior engineers have intuition that performs well on familiar territory. The gap is
  genuinely new territory -- new integrations, new user segments, new platform bets --
  where intuition fails silently and nobody notices until production.
- Velocity culture rewards shipping, not pausing. A team that stops to investigate before
  building is perceived as slow.
- Existing rituals fill the pre-build slot. Sprint planning, design review, and PR review
  already occupy the gate before code ships. Signal must find a new slot or justify
  replacing an existing one.

**What makes inertia sticky:** Survivorship bias. A team that skips Signal once and ships
without disaster interprets that as evidence Signal is not needed. They will never know
what problem they avoided. The counterfactual is invisible by design.

F-01: Inertia is not passivity. It is an active, habitual, socially reinforced choice.
Teams that skip evidence gathering have always shipped and usually shipped successfully
enough that they have no reason to change. Signal wins by being faster than the threshold
of "is this worth the time?" -- not by being more comprehensive than the alternatives.

F-02: The cost inertia imposes is invisible at the time of the skip. The METR study
(July 2025) found developers using AI tools took 19% longer than they perceived -- a
parallel failure mode: teams believe they are moving fast right up until the rework bill
arrives. Signal's job is to make the cost visible before it is incurred. The CTO framing:
"What was the last feature you significantly reworked or sunsetted? That cost is the
budget Signal competes for."

---

## 2. Named Competitors

### Anthropic /feature-dev Plugin

**Feature Overlap: MEDIUM | Positioning: Direct (same IDE, same platform) | Threat: HIGH**

The most dangerous named competitor because it is first-party, ships by default in the
Claude Code plugin catalog, and occupies the adjacent execution-phase slot upstream of
Signal in the developer's mental model.

/feature-dev is a 7-phase structured workflow: requirements gathering, codebase
exploration (parallel agents studying architecture and conventions), architecture design,
implementation, testing, review, and documentation. It deploys three specialized agents:
code-explorer (traces execution paths), code-architect (proposes approaches with
trade-offs), and code-reviewer (catches bugs with confidence scores).

Weakness: Execution-phase only. /feature-dev starts after the decision to build is made.
It never asks "should we build this?" Signal's pre-build evidence stage is upstream and
structurally distinct -- but users who see /feature-dev first may conclude the problem is
solved and never look for Signal.

Source: [Feature Dev -- Claude Plugin | Anthropic](https://claude.com/plugins/feature-dev)

F-03: Anthropic /feature-dev is the closest structural neighbor to Signal in the Claude
Code plugin catalog. It is first-party, zero-install-friction, and visible to every Claude
Code user. The differentiation must be immediate and obvious: Signal operates before the
decision; /feature-dev operates after. Without this framing, teams will see /feature-dev
as "the AI workflow plugin" and Signal as redundant.

F-04: Anthropic controls Signal's distribution platform. If Anthropic decides to add a
pre-build evidence namespace to /feature-dev (a /scout:requirements phase, a /trace:risk
phase before architecture), Signal's entire positioning is compressed at the platform
layer. The six-month watch trigger: does /feature-dev gain a /scout: or /prove:
equivalent? That event compresses the whitespace from an uncontested space to a
differentiation battle against a first-party feature.

---

### GitHub Copilot Workspace

**Feature Overlap: MEDIUM | Positioning: Adjacent (post-decision planning) | Threat: HIGH**

As of early 2026, Copilot Workspace is available to all paid Copilot subscribers. It
generates a Specification and a Plan from a natural-language task description -- both
user-editable before any code runs. It understands project-wide dependencies and
coordinates changes across frontend, backend, and database schema in one sweep.

Weakness: The Specification Copilot Workspace generates is a build specification -- it
describes how to implement a task. It is not a decision brief. It does not assess
competitive positioning, simulate user behavior, trace technical risk, or ask whether
the task is the right task.

Source: [GitHub Next | Copilot Workspace](https://githubnext.com/projects/copilot-workspace)

F-05: GitHub Copilot Workspace generates a Specification and Plan before code runs --
partial pre-build overlap that users may conflate with Signal's full evidence stage.
Copilot Workspace's scope is a single Issue: "how do I implement this?" Signal's scope
is a topic body: "should we build this, and what do we know across all dimensions before
we commit?" The distinction matters most when a team's first reaction to Signal is "we
already have Copilot Workspace."

---

### GitHub Copilot (Coding Assistant)

**Feature Overlap: LOW on pre-build research; HIGH on in-editor code assistance | Threat: MEDIUM**

4.7 million paying subscribers as of January 2026 (source: Microsoft FY26 Q2 earnings).
No structured "should we build this?" workflow. Writes code on demand, not evidence on
demand. The threat is not overlap -- it is opportunity cost: developers who feel
well-served by Copilot may not perceive a gap Signal fills.

F-06: Copilot's expansion into multiple AI models (Claude 4.6, Codex) as of early 2026
signals that the platform is becoming a multi-model orchestration layer. This opens the
question of whether Copilot could add a research/evidence namespace -- the distribution
moat would make it immediately formidable. Watch the `@workspace` and agent features
as leading indicators.

---

### Raw LLM Prompting (Claude, ChatGPT Direct)

**Feature Overlap: HIGH per interaction | Positioning: Adjacent (unstructured) | Threat: HIGH**

This is not a product. It is a behavior. Developers already ask Claude or ChatGPT "is
this a good idea?" or "what are the risks of building X?" The output is unstructured,
session-ephemeral, and has no artifact discipline, no namespace vocabulary, no amend
loop, and no topic-threading architecture.

F-07: Raw Claude prompting is the 80%-fidelity substitute for Signal with zero installation
friction. A developer who gets a useful answer from a direct prompt will not look for a
plugin that does the same thing more formally. Signal must demonstrate that the formal
version finds things the informal version misses -- and this requires either a case study
or a live demo where Signal surfaces a real gap a raw prompt would not have found. The
qualitative difference is large but invisible until Signal has been used at least once.

---

### ChatGPT Custom GPTs / OpenAI Operator Tools

**Feature Overlap: MEDIUM | Positioning: DIY threat | Threat: MEDIUM**

Any team with a ChatGPT Plus subscription can build a custom GPT that mimics a single
Signal skill. Operator can automate research flows. What custom GPTs cannot do: maintain
a cross-namespace artifact corpus, enforce artifact naming conventions, produce repo-
resident evidence, or synthesize across a topic.

F-08: Teams that have invested in their own GPT library (a "competitive analyzer" GPT,
a "spec writer" GPT) have a switching cost Signal must overcome, not just an inertia.
The cost of the DIY path is assembling and maintaining 10-15 separate custom GPTs each
with no awareness of the others. Signal's namespace system is precisely the integration
layer that DIY GPT workflows lack -- but teams do not know this until they have hit the
DIY wall.

---

### Cursor Plan Mode (Composer 2.0)

**Feature Overlap: LOW-MEDIUM | Positioning: Adjacent (IDE planning) | Threat: MEDIUM**

Cursor 2.5 (released February 2026) separates planning from execution. Plans are
generated as editable in-repo Markdown files with file paths, code references, and a
to-do list. 4M+ developer user base.

Weakness: Plan Mode is single-axis (implementation planning). No competitive analysis,
no user research simulation, no risk hypothesis investigation, no post-ship feedback
simulation. Cursor asks "how should we build this?" never "should we build this?"

Source: [Cursor: The best way to code with AI](https://cursor.com/)

F-09: Cursor Plan Mode (Composer 2.0) stores in-repo Markdown plans -- structural overlap
with Signal's /draft: and /trace: namespaces. Differentiation is multi-axis depth and
audience namespacing: a Cursor plan answers "how do I implement this file set?" A Signal
/draft:spec answers "what are we building and have we validated it against competitive,
technical, customer, and compliance dimensions?"

---

### Windsurf (Codeium)

**Feature Overlap: LOW-MEDIUM | Positioning: Adjacent (agentic coding) | Threat: LOW-MEDIUM**

Windsurf's Cascade architecture (2025) uses a "write-first, then plan" agentic loop with
multi-file awareness and terminal command execution. Free tier accelerates adoption.

Weakness: No namespaced evidence, no hypothesis discipline, no artifact naming convention,
no topic synthesis. Operates on implementation scope, not decision scope.

F-10: Windsurf's free tier (vs. Cursor's paid model) makes it the path-of-least-resistance
agentic coding tool for individual developers -- occupying the same attention slot as
Signal's first-use scenario. The threat is not feature overlap but attention budget
competition. A developer who installed Windsurf this morning will not install Signal this
afternoon unless they understand the tools solve different problems in different phases.

---

### Perplexity AI

**Feature Overlap: MEDIUM | Positioning: Adjacent (web research) | Threat: LOW-MEDIUM**

Perplexity's "answer engine" model produces cited, synthesized web research in seconds.
For /prove:websearch and /scout:market, Perplexity is a credible single-skill substitute.

Weakness: Cannot frame findings against a stated hypothesis, produce a repo-resident
artifact with frontmatter, connect research to a prior competitive brief or system trace,
or synthesize across namespaces. Research is session-ephemeral.

F-11: Teams use Perplexity for competitive research before installing Signal. The risk is
that teams treat Perplexity as a substitute for Signal's research skills and never
install the plugin. The counter: a Signal output that imports Perplexity citations is
better than a Perplexity output that imports nothing. Signal's /prove:websearch and
/scout:competitors produce repo-resident, hypothesis-framed, amend-looped artifacts that
Perplexity cannot.

---

### Google Gemini Code Assist

**Feature Overlap: LOW-MEDIUM | Positioning: Adjacent (enterprise AI) | Threat: MEDIUM for Google-native teams**

Google Gemini Code Assist in 2026 integrates with Google Workspace (Docs, Drive, Meet)
and surfaces enterprise knowledge in the IDE context. For teams whose design artifacts
live in Google Docs, Gemini's "search your workspace from the IDE" overlaps with
/prove:intelligence.

Weakness: Artifacts live in Google Workspace, not in git. Identical structural weakness
to Notion AI and Confluence. Not accessible via slash command at the terminal for
non-Google-native teams.

F-12: Gemini Code Assist is a meaningful threat only in the Google-native enterprise
segment; for the Microsoft Dynamics/Azure/GitHub-dominant teams Signal targets, the
threat is low. The signal to watch: if Gemini Code Assist adds a /feature-research
command that produces repo-resident artifacts with citation tracking, the threat upgrades
to HIGH for Google-native teams.

---

### Notion AI

**Feature Overlap: MEDIUM | Positioning: Adjacent (knowledge management) | Threat: MEDIUM**

Notion AI in 2026 can search Salesforce data alongside workspace content and generate
images, summaries, and action items. Custom Agents (launching at scale May 2026) automate
standups and status reports.

Weakness: Artifacts live in Notion, not in the repo. A Signal artifact committed to git
carries decision context for the team two years from now; a Notion page is invisible to
git blame.

Source: [notion.com/releases/2026-01-20](https://www.notion.com/releases/2026-01-20)

F-13: Notion AI is the primary threat to /prove:intelligence and /draft:proposal for
non-developer personas. PMs who live in Notion may prefer Notion AI's workspace-integrated
output to Signal's terminal-driven workflow. Signal's counter: repo residency and git
history are non-negotiable for any artifact that informs a technical decision. A Notion
doc does not show up in `git log`. A Signal artifact does.

---

### Confluence / Atlassian Intelligence

**Feature Overlap: MEDIUM | Positioning: Adjacent (enterprise knowledge base) | Threat: LOW-MEDIUM**

Atlassian Intelligence (Rovo) in 2026 turns Confluence highlights into Jira tasks and
generates content from Jira, Loom, and the Atlassian teamwork graph. This is the
"PRD to ticket" pipeline formalized.

What it does not do: gather competitive intelligence, simulate system behavior, predict
customer reaction, or synthesize cross-signal stories.

Source: [eesel.ai Atlassian Intelligence overview](https://www.eesel.ai/blog/atlassian-intelligence-confluence-ai-features)

F-14: Enterprise teams that already use Confluence for PRDs are hard to displace. For
these teams, Signal must position as additive -- "run Signal before you write the Confluence
PRD" -- not as a Confluence replacement. The artifact naming convention (`{topic}-spec-
{date}.md`) produces a file that can be referenced from Confluence and committed to git,
serving both audiences.

---

### Linear

**Feature Overlap: LOW | Positioning: Complementary | Threat: LOW-MEDIUM**

Linear's AI workflow for 2026 is explicitly "from drafting PRDs to pushing PRs" and its
MCP server integration with Cursor and Claude means it is moving toward the handoff point
Signal targets.

Weakness: Linear does not gather evidence; it structures and tracks work. No competitive
intelligence, no simulation, no synthesis.

Source: [linear.app/ai](https://linear.app/ai)

F-15: Linear's PRD-to-issue bridge is the closest named workflow to Signal's scout-to-
draft pipeline from the PM side. If Linear adds a /research namespace that produces
structured findings, Signal's PM-facing namespaces face a real challenger with Linear's
distribution advantage in developer-led teams. The watch trigger: does Linear add a
"pre-PRD evidence gathering" step? If yes, the overlap with /scout: becomes direct.

---

### Jira AI / Monday AI / ClickUp AI (PM Tool AI Convergence)

**Feature Overlap: LOW-MEDIUM | Positioning: Adjacent (PM tooling) | Threat: LOW-MEDIUM**

Jira, Monday, and ClickUp have all shipped AI features in 2025-2026 that generate sprint
plans, identify risks in backlog items, and auto-create epics from natural language.

Weakness: None produce repo-resident artifacts. None simulate system behavior. None
synthesize findings across a topic.

F-16: If a PM is already getting "good enough" research scaffolding from their PM tool's
AI, they will not install Signal for the /scout: namespace. Signal's PM-facing skills must
be demonstrably better than what the PM's existing tooling already provides -- or Signal
must explicitly reposition those skills as the developer-facing half of a handoff that
starts in the PM's existing tooling.

---

### Agile Ceremonies / Design Docs / ADRs (Process Competitors)

**Feature Overlap: MEDIUM | Positioning: Status quo institutionalized | Threat: HIGH for process-disciplined teams**

Teams with strong Agile discipline already produce sprint planning artifacts, Architecture
Decision Records (ADRs), and PR templates. These teams are not evidence-free; they have
a process. What their process lacks: competitive research with citations, system failure
simulation, customer persona evaluation, and cross-artifact synthesis.

F-17: "We already do this informally" is the most common objection from senior-engineer
teams. A team with ADRs, design reviews, and sprint planning believes it has covered the
Signal problem space. Signal does not replace their process -- it fills the gaps their
process always had but never noticed. The key demo for process-disciplined teams: run
/scout:competitors on a feature they recently shipped and show them a competitive signal
their informal process missed. That gap closes the objection.

---

### MCP Servers / Raw Tool Ecosystem (Assemble-It-Yourself)

**Feature Overlap: MEDIUM | Positioning: Infrastructure threat | Threat: MEDIUM for technical teams**

The Model Context Protocol (MCP) ecosystem enables Claude to connect to arbitrary tools
and data sources. A technically sophisticated team could assemble a Signal-like workflow
from MCP servers: a web search MCP for /prove:websearch, a GitHub MCP for artifact
storage, a Confluence MCP for /prove:intelligence.

Weakness: Cannot assemble from MCP servers alone: the namespace taxonomy, artifact naming
convention, skill lifecycle (setup-execute-findings-amend), quest loop for golden prompt
discovery, or the synthesis layer (/topic:story, /topic:echo).

F-18: The MCP threat is a sophisticated user problem. Technical teams willing to invest
in custom tooling will build their own Signal equivalent. What they build will cover 70%
of the surface and take months to stabilize. Signal's counter is the quest loop: the
golden prompts, rubric library, and discovery discipline represent institutional knowledge
that a DIY MCP workflow would take 6-12 months to accumulate -- and would never document.
Signal is the shortcut to the curated version of what the DIY team eventually builds.

---

### Productboard (AI tier)

**Feature Overlap: LOW-MEDIUM | Positioning: Complementary (PM-facing) | Threat: LOW**

Productboard's AI tier accelerates feature prioritization with automated feedback
categorization that links user insights to feature ideas. $20/maker/month add-on.

Weakness: PM-facing, SaaS-hosted, not repo-native. Not accessible via slash command.

Source: [Productboard AI](https://www.productboard.com/product/ai-for-product-management/)

F-19: Productboard is an integration target, not a threat. Signal evidence artifacts
could feed Productboard decisions via MCP or export. Signal is upstream: it produces the
evidence that Productboard tracks. The positioning is "run Signal before you update
Productboard" -- not "use Signal instead of Productboard."

---

### Sprig / Dovetail (UX Research)

**Feature Overlap: LOW | Positioning: Adjacent (UX research) | Threat: LOW**

Sprig and Dovetail overlap with Signal's /listen: namespace. Both are UX-team-facing,
SaaS-hosted, require real users to generate data.

Signal's /listen: namespace simulates what feedback will look like before there are real
users to survey. Sprig and Dovetail measure what feedback actually is after real users
exist. Different phases, not the same product.

Source: [Sprig: Modern Research Platform for UX Teams](https://sprig.com/)

F-20: Sprig/Dovetail and Signal's /listen: namespace are sequential, not competing.
Signal predicts the feedback before launch; Sprig/Dovetail measure it after. The
combined workflow: run /listen:adoption before the build commit to predict friction, then
run Sprig/Dovetail post-launch to measure actual friction against the prediction. Signal
is a calibration tool for the research investment that comes after.

---

### Devin / Cognition AI

**Feature Overlap: LOW | Positioning: Adjacent (autonomous execution) | Threat: LOW**

Devin 2.0 at $20/month. Added Devin Wiki (machine-generated codebase documentation)
and Devin Search (natural-language codebase Q&A). Its 83% improvement in junior-level
task completion signals autonomous execution is maturing rapidly.

Weakness: Execution agent. Builds when directed. Does not investigate whether to build.

Source: [Devin AI Guide 2026](https://aitoolsdevpro.com/ai-tools/devin-guide/)

F-21: Devin is a candidate integration target, not a threat. A team using Devin to build
a feature could run Signal's pre-build namespaces first and feed the resulting evidence
package to Devin as context. Signal becomes the upstream input. If Devin adds a research
harness (hypothesis-first investigation, competitive brief generation) before Signal
ships, the integration opportunity narrows -- but the execution architecture is so
different that the products would remain structurally distinct.

---

### LaunchDarkly

**Feature Overlap: NEAR-ZERO | Positioning: Complementary | Threat: LOW**

LaunchDarkly's core value proposition is "separate feature releases from deployments."
Post-build validation: "when do we roll this out and to whom?" Signal's question is
pre-build.

Source: [launchdarkly.com](https://launchdarkly.com/)

F-22: LaunchDarkly is the clearest example of Signal's "pre-build vs. post-build" frame.
The two tools are most powerful in sequence: Signal before the build decision,
LaunchDarkly after. Signal's /listen:adoption predicts the adoption curve; LaunchDarkly
controls the rollout that realizes it. Zero competitive overlap; natural pipeline partners.

---

### Roo Code / Cline (VS Code Agentic Plugins)

**Feature Overlap: LOW | Positioning: Adjacent | Threat: LOW-MEDIUM**

Roo Code's Plan Mode + Act Mode architecture. Can automate a headless browser to gather
documentation. Open-source momentum; multi-model support.

Weakness: No namespaces, no artifact naming, no signal synthesis, no hypothesis
discipline.

Source: [roocode.com](https://roocode.com/)

F-23: Roo Code and Cline occupy the same developer workflow slot as Signal's first-use
scenario. The risk is not current feature overlap but future roadmap convergence: if Roo
Code adds a structured "research before build" mode with repo-native artifacts, it would
be a Signal competitor with a head start in VS Code distribution. The watch trigger: does
Roo Code's Plan Mode gain multi-axis evidence gathering (competitive, technical, customer)?

---

## 3. The Whitespace: What No Competitor Owns

Signal's uncontested position:

> Structured, multi-namespace evidence accumulation that lives as repo-native artifacts,
> runs inside the developer's IDE via slash commands, crosses the PM-dev boundary from
> /scout: through /listen:, and synthesizes per-topic into a decision narrative.

No named competitor owns all four:
1. **Repo-native artifacts** -- not a SaaS dashboard, not a chat transcript, not a
   Notion doc. Evidence lands in git, organized by namespace, discoverable by topic prefix.
2. **Developer-facing UX** -- Claude Code plugin, slash commands, namespace vocabulary
   that maps to what developers already know.
3. **Multi-axis evidence** -- 12 namespaces covering PM (scout, draft), technical (trace,
   flow), research (prove), post-ship (listen), metrics, and goals. No single-axis tool
   spans this.
4. **Topic narrative layer** -- /topic: ties artifacts across directories into a coherent
   story. The answer to "do we have enough evidence to build?" is a synthesis, not a pile
   of documents.

F-24: The whitespace is not a gap in the market -- it is a gap in how the market has
framed the problem. Every competitor has defined the job as either "help me write code
faster" or "help me track work." Signal defines the job as "help me know what I know
before I commit." That reframe is the moat. Every time a competitor enters the pre-build
space, they must either adopt Signal's framing (which validates the category) or define
their own frame (which fractures the category and benefits the most recognized player).
First-mover advantage in category definition is real -- but only if Signal ships before
the category is named by someone else.

---

## 4. --mode risk: The Cost of Building the Wrong Thing

A team commits to Feature X. They spend 6 weeks building. On day 43 they learn:

- The feature duplicates something a competitor ships this quarter (missed: /scout:competitors)
- The data flow fails under weekend batch volumes (missed: /flow:dataflow)
- The permissions model allows data to cross tenant boundaries (missed: /trace:permissions)
- Three of twelve customer personas will never use it (missed: /review:customers)

| Risk | Missed signal | Pre-build cost | Post-ship cost |
|------|--------------|----------------|----------------|
| Competitive duplicate | /scout:competitors | Afternoon of research | 6-12 weeks + roadmap credibility |
| System failure under load | /flow:throttle, /trace:request | 2-hour simulation | Sprint of hotfixes + incident |
| Security / permissions flaw | /trace:permissions | 1-hour trace | Regulatory review + remediation |
| Wrong customer persona | /review:customers | Half-day persona run | Low adoption + redesign cycle |
| Spec misalignment across team | /review:design | Design review session | Rework after first code review |
| Adoption blind spot | /listen:adoption | Half-day simulation | Full engineering sunk cost |

F-25: Signal's most powerful exec argument is not cost savings -- it is decision confidence.
The signal artifacts become the audit trail for "why did we build this?" When a feature
underperforms, the team with Signal artifacts can trace the decision. The team without
them cannot. In regulated industries (finance, healthcare, compliance-heavy enterprise),
the decision audit trail is itself a compliance requirement. /prove:publish and
/scout:compliance address this directly.

---

## 5. Competitive Threat Summary

| Competitor | Threat | Primary overlap dimension |
|------------|--------|--------------------------|
| Inertia / status quo | HIGH (always) | None -- competes on comfort |
| Anthropic /feature-dev | HIGH | Adjacent phase; same platform; first-party |
| GitHub Copilot Workspace | HIGH | /draft:spec, /scout:requirements (single-issue scope) |
| Agile ceremonies / ADRs | HIGH (process teams) | /draft:, /review:design (informal substitute) |
| Raw Claude / ChatGPT prompting | HIGH | All namespaces (80% fidelity, zero friction) |
| Anthropic platform convergence | MEDIUM-HIGH (long-term) | Entire plugin surface if /feature-dev expands |
| GitHub Copilot | MEDIUM | Developer attention budget |
| ChatGPT custom GPTs | MEDIUM | Individual skills (DIY without integration layer) |
| Cursor Plan Mode | MEDIUM | /draft:spec, /trace: (implementation scope) |
| Notion AI | MEDIUM | /prove:intelligence, /draft:proposal (PM-facing) |
| MCP ecosystem (DIY assembly) | MEDIUM (technical teams) | Full surface if team builds own stack |
| Gemini Code Assist | MEDIUM (Google-native) | /prove:intelligence |
| Perplexity AI | LOW-MEDIUM | /prove:websearch, /scout:market (single-skill) |
| Windsurf (Codeium) | LOW-MEDIUM | Attention budget; Plan Mode overlap |
| Linear | LOW-MEDIUM | PRD-to-issue bridge (no simulation) |
| Jira AI / Monday AI | LOW-MEDIUM | PM-facing /scout: namespaces |
| Confluence / Atlassian | LOW-MEDIUM | /draft:spec, /scout:requirements (enterprise) |
| Roo Code / Cline | LOW-MEDIUM | Attention budget; potential roadmap convergence |
| Devin / Cognition | LOW | Integration target; execution vs. evidence |
| Productboard AI | LOW | Integration target; PM-facing |
| LaunchDarkly | LOW | None (different phase) |
| Sprig / Dovetail | LOW | /listen: (post-ship vs. pre-ship simulation) |

---

## 6. Amendments

**AMEND-01: Narrow to Claude Code plugin ecosystem competitors only**

What the user changes: Add `--scope plugin-ecosystem`. Remove SaaS tools (Notion AI,
LaunchDarkly, Linear, Confluence) from the matrix.

What changes in output: Tightens whitespace analysis to "what no Claude Code skill or
MCP server currently owns." Primary competitor shifts from "inertia" to "generic prompting."
Adds distribution section comparing marketplace installation patterns. Anthropic /feature-
dev and raw Claude prompting become the dominant 1-2 threats.

**AMEND-02: Add internal competitor analysis (build vs. buy)**

What the user changes: Add `--include internal` with existing tooling inventory (e.g.,
"we already use Confluence + GitHub Copilot + Linear").

What changes in output: Adds an "internal competitor" section for each tool the team
already has. Reframes the matrix question from "Signal vs. market" to "Signal vs. what
we already pay for." The whitespace becomes specific to the gap in the team's existing
tooling stack. The risk section quantifies redundant tooling cost vs. new investment.

**AMEND-03: Add six-month watch list with early-warning triggers**

What the user changes: Request `--mode watch`.

What changes in output: Replaces static threat assessment for HIGH threats with watch
sections. Early-warning triggers: /feature-dev adds a /scout: or /prove: equivalent;
Copilot Workspace adds multi-namespace evidence modes; Cursor adds competitive analysis
to Plan Mode; Linear adds a pre-PRD research step. Any of these compresses Signal's
whitespace and requires immediate repositioning.

---

## Findings Summary (25 findings)

| # | Finding | Threat | Priority |
|---|---------|--------|----------|
| F-01 | Inertia is an active, habitual, socially reinforced choice -- Signal must beat "doing nothing" on speed, not features | Inertia | P1 |
| F-02 | The cost of skipping is invisible and deferred; CTO frame: "What did your last rework cost?" | Inertia | P1 |
| F-03 | Anthropic /feature-dev is seen first by every Claude Code user; differentiation must be immediate: Signal operates before the decision | Anthropic /feature-dev | P1 |
| F-04 | If /feature-dev adds a /scout: or /prove: phase, Signal's whitespace compresses at the platform layer -- watch for this event | Anthropic platform | P1 |
| F-05 | Copilot Workspace generates Spec + Plan from an Issue -- teams may conflate this with Signal's full evidence stage | GitHub Copilot Workspace | P1 |
| F-06 | Copilot's multi-model expansion signals it could add a research namespace; distribution moat would make it immediately formidable | GitHub Copilot | P2 |
| F-07 | Raw Claude prompting is the 80%-fidelity substitute with zero friction; Signal wins on the other 20%: system, discipline, corpus | Raw prompting | P1 |
| F-08 | Teams with DIY GPT libraries have a switching cost Signal must overcome, not just inertia | ChatGPT GPTs | P2 |
| F-09 | Cursor Plan Mode overlaps /draft: and /trace: at the implementation scope; differentiation is multi-axis depth and audience namespacing | Cursor | P2 |
| F-10 | Windsurf's free tier occupies the same attention slot as Signal's first-use scenario without overlapping on decision scope | Windsurf | P2 |
| F-11 | Teams use Perplexity for competitive research pre-Signal; Signal's counter is repo residency + hypothesis framing that Perplexity cannot produce | Perplexity | P2 |
| F-12 | Gemini Code Assist is a meaningful threat only in Google-native enterprise; watch for repo-native artifact output as the upgrade trigger | Gemini | P2 |
| F-13 | Notion AI is the primary /prove:intelligence and /draft:proposal threat for PM personas; Signal's counter is git residency | Notion AI | P2 |
| F-14 | Confluence teams need "Signal before the PRD" positioning, not "Signal instead of Confluence" | Confluence | P2 |
| F-15 | Linear's PRD-to-issue bridge is the closest named workflow to Signal's scout-to-draft pipeline; watch trigger: does Linear add a pre-PRD evidence step? | Linear | P2 |
| F-16 | PM tool AI features narrow the /scout: territory from the PM side; Signal's PM-facing skills must demonstrably outperform existing PM tooling | Jira/Monday AI | P2 |
| F-17 | "We already do this informally" is the most common objection from senior-engineer teams; the counter is a live demo that finds a gap their informal process missed | Agile ceremonies | P1 |
| F-18 | The MCP DIY path produces 70% of Signal in months; Signal's counter is the quest loop and curated golden prompts that DIY never documents | MCP ecosystem | P2 |
| F-19 | Productboard and Devin are integration targets, not threats; Signal is upstream of both | Productboard / Devin | P3 |
| F-20 | Sprig/Dovetail and Signal's /listen: namespace are sequential: Signal predicts, Sprig/Dovetail measures | Sprig / Dovetail | P3 |
| F-21 | Devin is an integration target; Signal feeds Devin context; the risk is Devin adding pre-build investigation before Signal ships | Devin | P3 |
| F-22 | LaunchDarkly is the clearest "different phase" case; the two tools are most powerful in sequence | LaunchDarkly | P3 |
| F-23 | Roo Code / Cline occupy the attention slot; the watch trigger is Plan Mode gaining multi-axis evidence gathering | Roo Code | P2 |
| F-24 | The whitespace is a category framing gap, not a feature gap; first-mover advantage in category definition is real but finite | Category | P1 |
| F-25 | Signal's exec argument is decision confidence + audit trail, not cost savings; this matters most in regulated industries | Exec positioning | P1 |

---

*Sources consulted (March 2026):*
- [Feature Dev -- Claude Plugin | Anthropic](https://claude.com/plugins/feature-dev)
- [GitHub Next | Copilot Workspace](https://githubnext.com/projects/copilot-workspace)
- [Microsoft FY26 Q2 Earnings -- Copilot subscriber count](https://www.aboutchromebooks.com/github-copilot-statistics/)
- [Cursor: The best way to code with AI](https://cursor.com/)
- [Devin AI Guide 2026](https://aitoolsdevpro.com/ai-tools/devin-guide/)
- [Productboard AI](https://www.productboard.com/product/ai-for-product-management/)
- [Sprig: Modern Research Platform for UX Teams](https://sprig.com/)
- [notion.com/releases/2026-01-20](https://www.notion.com/releases/2026-01-20)
- [linear.app/ai](https://linear.app/ai)
- [launchdarkly.com](https://launchdarkly.com/)
- [roocode.com](https://roocode.com/)
- [eesel.ai Atlassian Intelligence overview](https://www.eesel.ai/blog/atlassian-intelligence-confluence-ai-features)
