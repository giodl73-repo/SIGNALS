---
skill: scout-competitors
topic: plugin
item: competitors
date: 2026-03-15
skill_version: v1
input: auto-detected from CLAUDE.md + plugin-plan.md
---

# Competitive Brief: Signal Plugin

**Topic**: plugin
**Product statement**: Know what you know before you commit. Signal helps teams gather evidence for feature decisions and synthesizes it into a story.
**Target**: Developers, architects, SREs, data scientists — anyone who makes feature decisions.
**Platform**: Claude Code plugin (skill-based, artifact-to-repo, YAML-configured).

**The strategic lead**: Signal has one uncontested position — the pre-build evidence layer
inside the developer's own repo. Every named competitor either activates after the decision
to build has already been made, or lives outside the developer's IDE entirely. The real
threats are: (1) Anthropic's first-party /feature-dev plugin (adjacent execution-phase slot),
(2) GitHub Copilot Workspace (pre-build spec generation at GitHub scale), and (3) raw inertia
(the decision to skip entirely). Signal must win the "should we?" stage before /feature-dev
owns the "how do we?" stage — and it must do this while teams feel no pain from skipping.

---

## 1. The Primary Competitor — Inertia / Status Quo

**Threat level: HIGH (always)**

The most dangerous competitor to Signal has no product page, no funding round, and no feature set to compare against. It is the choice to do nothing.

**Why teams do nothing:**

- Teams believe they already know enough. ("We've built this kind of thing before.")
- Research feels like overhead on a sprint that is already behind.
- The cost of being wrong is not visible until after the build — and by then, the team has shipped and moved on.
- No one is accountable for evidence that was never gathered.
- The skill of "structured pre-build research" has no job title. No one owns it, so no one defends it.
- Survivorship bias: teams that shipped without Signal once and avoided disaster interpret that as evidence Signal is not needed. The counterfactual is invisible by design.
- "We already do this informally." Senior engineers run ad hoc versions of what Signal formalizes. The informal version feels like it works. The formal version feels like documentation overhead.

**What makes inertia sticky:**
- Zero friction. Doing nothing requires no install, no prompt, no artifact, no review.
- Evidence-gathering has no deadline. There is always a reason to skip it today and do it later.
- Perceived cost is immediate (time in sprint). Actual cost is deferred (rework 6 weeks later).
- Teams that have shipped without research before will do so again. The miss has to be painful enough to change behavior.
- Velocity culture rewards shipping, not pausing. A team that stops to investigate before building is perceived as slow.

**What Signal must eliminate to win:**
- First-run friction. If setup requires configuration, inertia wins before the first artifact.
- Ambiguity about who this is for. If developers and PMs both look at it and think "that's for someone else," no one uses it.
- The "we'll do it later" trap. The tool must be fast enough that later becomes now.

F-01: Inertia is not passivity. It is an active, habitual, socially reinforced choice. Teams that skip evidence gathering have always shipped and usually shipped successfully enough that they have no reason to change. Signal wins by being faster than the threshold of "is this worth the time?" — not by being more comprehensive than the alternatives.

F-02: The cost inertia imposes is invisible at the time of the skip. The METR study (July 2025) found developers using AI tools took 19% longer than they perceived — a parallel failure mode: teams believe they are moving fast right up until the rework bill arrives. Signal's job is to make the cost visible before it is incurred.

F-03: "We already do this informally" is the most dangerous objection because it is partially true. Signal needs a demo that surfaces a gap the informal version misses — specifically something a P1-tier finding in `/trace:permissions` or `/flow:throttle` would catch that a PM brief never mentions.

---

## 2. The Whitespace — What No Competitor Owns

No current tool owns the space Signal occupies: **structured pre-build evidence gathering, organized by audience, producing repo-resident artifacts, delivered as a zero-setup developer tool.**

The whitespace breaks into four dimensions:

1. **Pre-build, not post-build.** Feature flags (LaunchDarkly, Unleash) operate after the code is written. Testing frameworks (Jest, Playwright) operate after the code is written. Code review tools (GitHub Copilot, CodeRabbit) operate after the code is written. Signal operates before. The question it answers is "should we build this and how?" not "did we build it correctly?"

2. **Evidence-to-repo, not evidence-in-SaaS.** Notion AI, Confluence, and Linear keep evidence in their own databases — outside the repo, outside git history, invisible to the team that inherits the codebase two years later. Signal artifacts land in the repo alongside the code they inform. The decision trail lives where the decision matters.

3. **Namespace = audience, zero taxonomy overhead.** No tool has solved the "who is this for?" problem at the navigation level. PMs know `/scout:` is theirs. Developers know `/trace:` is theirs. The namespace is the routing. No tags, no folders, no project setup required.

4. **The synthesis layer.** Copilot writes code on demand. Linear tracks issues. Confluence stores documents. No tool synthesizes cross-namespace signals into a coherent story of "here is what we know, here is what we do not know, here is what surprised us." `/topic:story` and `/topic:echo` own this space outright.

F-04: The whitespace is not a gap in the market — it is a gap in how the market has framed the problem. Every competitor has defined the job as either "help me write code faster" or "help me track work." Signal defines the job as "help me know what I know before I commit." That reframe is the moat.

---

## 3. The Table Stakes — What Any Entrant Must Have

To be taken seriously in the developer tooling segment:

| Requirement | Why |
|-------------|-----|
| Zero-setup first run | Developers will not configure a tool before they trust it |
| Repo-native artifacts | Evidence that lives outside git is evidence that gets lost |
| CLI / editor integration | Developer workflow is terminal or editor; no browser pivot |
| AI model quality at the skill level | The output quality must exceed what a developer could produce with a raw prompt |
| Namespace or domain organization | Flat output lists are unusable at scale |
| Citeable sources in research output | Claims without sources are rejected by architects and PMs alike |

F-05: The "zero-setup first run" requirement is a filter that eliminates most research tools from developer consideration. Tools that require workspace setup, team invites, or configuration files before producing a first artifact will not survive the first-five-minutes test with a developer who has a sprint deadline.

---

## 4. The Competitive Matrix

### 4.1 Anthropic /feature-dev Plugin (first-party)

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | MEDIUM — execution-phase coverage; adjacent planning steps overlap with `/draft:spec` |
| Positioning | Direct (same IDE, same platform, adjacent phase) |
| Technical moat | First-party, bundled, default Claude Code plugin catalog; zero install friction |
| Distribution | Claude Code official plugin catalog — seen by every Claude Code user |
| Threat | HIGH — most dangerous named competitor due to default visibility |

F-06: Anthropic's /feature-dev is a 7-phase structured workflow (requirements, codebase exploration via parallel agents, architecture design, implementation, testing, review, documentation). It deploys three specialized agents: code-explorer, code-architect, and code-reviewer. It activates after the decision to build is made. Signal is upstream — but users who see /feature-dev first may conclude the problem is solved. Signal must position explicitly as "pre-/feature-dev" or as the upstream input that makes /feature-dev's architecture agent more effective.

F-07: /feature-dev is the first thing developers see when searching for structured workflow plugins in the Claude Code catalog. Signal's go-to-market cannot assume discovery by search — it requires a clear category name that separates pre-build from build. The early-warning trigger: if /feature-dev adds a `/scout:` or `/prove:` equivalent, Signal's whitespace compresses immediately.

### 4.2 GitHub Copilot Workspace

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | MEDIUM — generates Specification and Plan before code runs; partial pre-build overlap |
| Positioning | Direct (post-decision planning at GitHub scale) |
| Technical moat | GitHub platform integration; enterprise contracts; 100M+ developer accounts |
| Distribution | Bundled with Copilot Free/Pro/Enterprise — zero incremental friction |
| Threat | HIGH — strongest structural competitor at distribution scale |

F-08: GitHub Copilot Workspace GA'd a plan agent with sub-agent orchestration in early 2026 that now reads AGENTS.md and CLAUDE.md instruction files. "Project Padawan" — where Copilot executes an issue autonomously and the developer reviews the output — is the scenario where Signal's evidence layer either feeds the agent upstream or gets bypassed entirely. Workspace's Specification is a build specification (how to implement) not a decision brief (whether to build and what the risks are). But users conflate the two. Signal must name the distinction explicitly.

F-09: Copilot's expansion into multiple AI models (Claude 4.6, Codex) as of early 2026 signals that the platform is becoming a multi-model orchestration layer. This opens the question of whether Copilot could add a research/evidence namespace. The distribution moat would make it immediately formidable. Watch the `@workspace` and agent features as leading indicators. 4.7M paying subscribers (Microsoft FY26 Q2, Jan 2026).

### 4.3 OpenAI Codex CLI

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | MODERATE — o3 reasoning on local repo; iterative review; ad-hoc research via prompt |
| Positioning | Substitute (informal Signal via raw prompting of a capable reasoning model) |
| Technical moat | Open source (openai/codex); o3/o4-mini reasoning quality; zero cost |
| Distribution | GitHub install; any developer with an OpenAI key |
| Threat | MODERATE-HIGH — substitution via convenience, not capability |

F-10: OpenAI Codex CLI is open-source, runs on o3 and o4-mini, and is designed for "longer, more complex coding tasks" including iterative review of local repositories. A developer can use it today as an informal Signal substitute by prompting "research feasibility of X before we build it" with zero setup cost. The threat is not that Codex CLI is better than Signal — it is that it is good enough and already installed. Signal must produce an artifact that Codex CLI's ad-hoc prompting cannot: structured, namespace-organized, repo-resident, citable findings with a named rubric that accumulates over time.

### 4.4 Cursor (Plan Mode / Composer 2.0)

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | LOW-MEDIUM — Plan Mode overlaps lightly with `/draft:spec`; no namespace for evidence |
| Positioning | Adjacent (editor-native AI; competes for developer attention, not research output) |
| Technical moat | Deep editor integration; multi-model; agentic planning (Plan Mode); 4M+ users |
| Distribution | Direct install; strong developer following |
| Threat | MEDIUM — Plan Mode is the closest surface to Signal's pre-build territory |

F-11: Cursor's Plan Mode (Composer 2.0, released February 2026) generates editable in-repo Markdown plans with file paths, code references, and a to-do list. This is structurally similar to Signal's setup phase — but Plan Mode operates on implementation scope ("what files do I change") not feature decision scope ("should we build this and what do we know"). It is single-axis (implementation planning): no competitive analysis, no user research simulation, no risk hypothesis investigation, no post-ship feedback simulation. The risk is not current feature overlap but future roadmap convergence.

### 4.5 Windsurf (Codeium, acq. Cognition)

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | LOW-MODERATE — Cascade agent persistent session memory; workflow markdown files |
| Positioning | Adjacent (IDE-native agentic coding with memory) |
| Technical moat | Acquired by Cognition (Devin's parent) for ~$250M, Dec 2025; #1 in LogRocket AI Dev Tool Power Rankings (Feb 2026) |
| Distribution | Free tier + Pro/Teams; VS Code-style IDE |
| Threat | MODERATE — persistent memory inches toward "what we know about this feature" territory |

F-12: Windsurf's Cascade agent stores codebase context and workflow patterns persistently across sessions — it is building a memory of what the codebase has become, not of what the team decided and why. Signal's value is in the decision evidence layer Cascade does not touch. The Cognition acquisition is the signal to watch: if Cognition merges Devin's autonomous execution with Windsurf's persistent memory and adds a structured research phase, it would be Signal's most complete competitor. Monitor Windsurf Q3 2026 roadmap for "planning" or "research" features.

### 4.6 Devin / Cognition

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | LOW — Devin executes tasks; Signal gathers evidence |
| Positioning | Adjacent (autonomous execution vs. deliberate pre-build research) |
| Technical moat | Agentic architecture; multi-Devin concurrency; $20/month entry (Devin 2.0) |
| Distribution | Direct; enterprise via Goldman Sachs / IBM partnerships |
| Threat | LOW — different job to be done; integration target not a competitor |

F-13: Devin 2.0 can "generate draft architecture in 15 minutes for others to react to" — but this is architecture generation, not evidence gathering. Devin does not state a hypothesis, gather competitive intelligence, simulate failure modes, or produce a story of what is known. Its 83% improvement in junior-level task completion signals the autonomous execution space is maturing rapidly. **Partnership potential**: Signal is upstream of Devin. A team running Signal pre-build and then handing evidence artifacts to Devin as context is the most powerful integration story for both products.

### 4.7 Linear

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | LOW — Linear tracks work; Signal informs work |
| Positioning | Complementary (Linear is where decisions land; Signal is where decisions are made) |
| Technical moat | Best-in-class issue tracker; AI triage; MCP server for Cursor/Claude integration |
| Distribution | PLG with strong developer and startup adoption |
| Threat | LOW-MEDIUM — Linear is adding AI that bridges "research → issue" gap |

F-14: Linear's AI workflow for 2026 is explicitly "from drafting PRDs to pushing PRs" — and its MCP server integration with Cursor and Claude means it is moving toward the handoff point Signal targets. Linear does not gather evidence; it structures and tracks work. But its PRD-to-issue bridge is the closest named workflow to Signal's scout-to-draft pipeline. If Linear adds a `/research` namespace that produces structured findings, Signal's PM-facing namespaces face a real challenger.

### 4.8 Notion AI

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | MEDIUM — Notion AI can draft documents and search internal data; overlaps with `/draft:` and `/prove:intelligence` |
| Positioning | Adjacent (knowledge management with AI assist; not structured evidence gathering) |
| Technical moat | Massive installed base; Salesforce/CRM integration; Custom Agents (May 2026) |
| Distribution | Bottom-up SaaS; team-level purchase |
| Threat | MEDIUM — the primary threat to `/prove:intelligence` and `/draft:proposal` |

F-15: Notion AI in 2026 can search Salesforce data alongside workspace content and generate images, summaries, and action items from meetings. Custom Agents (launching at scale May 2026) can automate daily standups and status reports. But Notion's artifacts live in Notion, not in the repo. A Signal artifact committed to git carries decision context for the team two years from now; a Notion page is invisible to git blame. That is the structural moat Signal holds over Notion AI. Signal should lean into this in enterprise conversations: "your evidence never leaves your codebase."

### 4.9 Confluence / Atlassian Intelligence (Rovo)

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | MEDIUM — PRD templates, requirements management, Rovo AI search overlap with `/draft:spec` and `/scout:requirements` |
| Positioning | Adjacent (enterprise knowledge base with AI assist) |
| Technical moat | Enterprise distribution; Jira integration; Atlassian teamwork graph |
| Distribution | Top-down enterprise; bundled with Jira |
| Threat | LOW-MEDIUM — enterprise teams that already use Confluence for PRDs are hard to displace |

F-16: Atlassian Intelligence (Rovo) in 2026 turns Confluence highlights into Jira tasks and generates content from Jira, Loom, and the Atlassian teamwork graph. This is the "PRD to ticket" pipeline formalized. What it does not do: gather competitive intelligence, simulate system behavior, predict customer reaction, or synthesize cross-signal stories. The gap is the entire Signal namespace surface outside of `/draft:`. In enterprise positioning, Signal complements Atlassian rather than competing: "Signal feeds the decision that Confluence documents."

### 4.10 Sourcegraph Cody

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | LOW — whole-repo code understanding; batch changes; no pre-build evidence workflow |
| Positioning | Adjacent (code navigation and generation within existing codebase) |
| Technical moat | SOC 2, GDPR/CCPA, BYOK, zero code retention — enterprise procurement baseline |
| Distribution | Free tier + Enterprise; VS Code and JetBrains marketplace |
| Threat | LOW-MODERATE — enterprise compliance posture sets procurement expectations |

F-17: Cody's enterprise compliance stack (SOC 2, zero retention, BYOK) sets a procurement baseline that developer-tool buyers in regulated industries now expect. Signal's artifact storage model — local markdown files, no data leaves the repo — is a compliance advantage by default. This is a positioning win Signal should name explicitly in enterprise conversations: "your evidence never leaves your codebase and never touches a third-party server."

### 4.11 Productboard AI / Jira PD / Miro AI (PM-side discovery tools)

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | LOW-MODERATE — AI synthesis of user feedback, feature scoring, roadmap prioritization |
| Positioning | Upstream of Signal (PM discovery → Signal technical evidence → build decision) |
| Technical moat | Jira PD has Atlassian install base; Productboard is standalone SaaS; Miro owns visual PM workflow |
| Distribution | Enterprise SaaS; team-level purchase via PM organization |
| Threat | LOW-MODERATE for Signal directly; integration targets for Signal PM namespaces |

F-18: Productboard, Jira PD, and Miro AI are the 2026 consolidation anchors for PM-side discovery. None produce structured technical evidence artifacts — no feasibility assessments, architecture traces, or compliance checks. Signal's `/scout:`, `/draft:`, and `/trace:` namespaces are the gap these tools explicitly leave open. The strategic positioning: Signal is downstream of PM discovery, feeding the technical evidence layer that PM tools cannot produce. In enterprise deals, Signal should integrate with Productboard/Jira PD as the "technical depth layer" rather than competing for the PM budget.

### 4.12 LaunchDarkly

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | NEAR-ZERO — LaunchDarkly is post-build; Signal is pre-build |
| Positioning | Complementary (LaunchDarkly controls rollout; Signal informs the decision to build) |
| Technical moat | Market leader in feature flags; enterprise SDK distribution; experimentation layer |
| Distribution | Enterprise sales + developer self-serve |
| Threat | LOW — operates in an entirely different decision window |

F-19: LaunchDarkly's core value proposition is "separate feature releases from deployments" — gradual rollouts, kill switches, A/B tests. This is post-build validation: "when do we roll this out and to whom?" Signal's question is pre-build: "should we build this at all, and do we understand it well enough to commit?" Zero overlap on the research problem. The two tools are most powerful in sequence: Signal before the build decision, LaunchDarkly after. This is the clearest positioning statement against a named competitor.

### 4.13 Roo Code / Cline (VS Code Agentic Plugins)

| Dimension | Assessment |
|-----------|------------|
| Feature overlap | LOW — agentic coding (Plan + Act); no structured evidence namespace |
| Positioning | Adjacent (same Claude Code / VS Code developer footprint; different job) |
| Technical moat | Open-source momentum; multi-model support; VS Code marketplace distribution |
| Distribution | Free VS Code extension; GitHub stars-driven adoption |
| Threat | LOW-MEDIUM — occupy the same developer workflow slot; could add research mode |

F-20: Roo Code's architecture is Plan Mode (context gathering, architecture discussion) followed by Act Mode (implementation). It can automate a headless browser to gather documentation. The Plan Mode surface is structurally similar to Signal's setup phase — but Roo Code has no concept of namespaces, no artifact naming convention, no signal synthesis, and no hypothesis discipline. The risk is not current feature overlap but future roadmap convergence: open-source tools in this segment ship quickly when the community identifies a gap.

---

## 5. The MCP Ecosystem — Distribution and Noise

**Not a named competitor — a structural threat to discoverability.**

The MCP marketplace has 18,548 servers listed on mcp.so and 1,265 on the Claude Code Marketplace as of March 2026. Popular servers include GitHub, Figma, Playwright, Supabase. Claude Code's lazy-loading MCP Tool Search reduces context usage by up to 95%, enabling large server sets without performance penalty.

F-21: Signal enters a marketplace where 1,265+ Claude Code plugins already exist. Discovery is the primary go-to-market challenge. Signal's differentiation cannot rest on "it's a Claude Code plugin" — that is table stakes. The differentiation must be the artifact schema and the evidence-gathering workflow, which no other listed plugin provides. The path to discoverability is landing page positioning ("the only Claude Code plugin for pre-build feature decisions") and a single zero-friction install that produces a named artifact in under 5 minutes. The category name — not the feature list — is what surfaces in marketplace search.

---

## 6. The Vibe Coding Headwind

**Cultural threat, not a named product.**

Vibe coding (coined 2025) explicitly advocates skipping formal planning: describe intent in natural language, accept AI output, iterate. Promoted by Replit, Cursor, and Windsurf positioning. Amplified on social media and developer communities throughout 2025.

F-22: Vibe coding is the explicit counter-narrative to Signal's premise. If the dominant developer culture in 2025-2026 is "ship first, debug later," then pre-build evidence gathering reads as friction. However: critics document vibe coding as producing "bug-prone code lacking complete architectural structure" that is "difficult to debug and integrate into enterprise systems." Signal's counter-positioning is reactive, not preventive — and that is honest: Signal is what teams reach for after their first vibe-coded feature collapses in production. The positioning: "Signal is not about slowing down. It is about knowing which shortcuts are safe."

---

## 7. Raw LLM Prompting (ChatGPT, Claude direct)

**Not a product — a behavior. And a real threat.**

F-23: Developers already ask Claude or ChatGPT "is this a good idea?" or "what are the risks of building X?" The output is unstructured, session-ephemeral, and has no artifact discipline, no namespace vocabulary, no amend loop, and no topic-threading architecture. The threat: it requires zero installation, zero learning, and is already running in every developer's IDE. A developer who gets a useful answer from a direct prompt will not look for a plugin that does the same thing more formally. Signal's answer: a direct prompt produces one answer once. Signal produces a body of evidence that accumulates across namespaces, persists in the repo as git artifacts, is organized by topic, and synthesizes into a readiness narrative. The qualitative difference is large — but it is invisible until Signal has been used at least once.

---

## 8. --mode risk — The Cost of Building Wrong

**Reframed for executive audiences.**

A team commits to building Feature X on intuition, prior experience, and a PM brief that has not been reviewed by a compliance analyst, a system architect, or a customer persona. They spend 6 weeks building. On day 43, they learn:
- The feature duplicates something LaunchDarkly already does (missed by `/scout:competitors`)
- The data flow through the ETL pipeline fails under weekend batch volumes (missed by `/flow:dataflow`)
- The permissions model allows data to cross tenant boundaries (missed by `/trace:permissions`)
- Three of the twelve customer personas will never use it because the UX assumes a workflow they do not have (missed by `/review:customers`)

None of these findings are hard to surface. They are hard to find after the fact.

**The cost structure:**

| Risk | Missed signal | Cost if caught pre-build | Cost if caught post-ship |
|------|--------------|--------------------------|--------------------------|
| Duplicates existing capability | `/scout:competitors` | Afternoon of research | 6 weeks of engineering + PM time |
| System failure under load | `/flow:throttle`, `/trace:request` | 2-hour simulation | Sprint of hotfixes + incident |
| Security/permissions flaw | `/trace:permissions` | 1-hour trace | Regulatory review + remediation |
| Wrong customer persona | `/review:customers` | Half-day persona run | Low adoption + redesign cycle |
| Spec misalignment across team | `/review:design` | Design review session | Rework after first code review |

F-24: The risk Signal addresses is not "will the code work?" — that is what testing frameworks and code review solve. The risk Signal addresses is "are we building the right thing, for the right people, in the right way?" No tool in the current landscape owns this question with the specificity Signal provides. The exec framing: "What is the cost of a six-week sprint on the wrong feature?" That is the number Signal competes against, not the cost of a competing tool.

F-25: Signal's most powerful exec argument is not cost savings — it is decision confidence. The signal artifacts become the audit trail for "why did we build this?" When a feature underperforms, the team with Signal artifacts can trace the decision. The team without them cannot. In regulated industries (finance, healthcare, compliance-heavy enterprise), the decision audit trail is itself a compliance requirement. `/prove:publish` and `/scout:compliance` address this directly.

The sharp question for any CTO: "What was the last feature your team built and then significantly reworked or sunsetted? What did that cost? That number is the budget Signal competes for."

---

## 9. AMEND — 3 Specific Adjustments

**AMEND-01: Narrow to Claude Code plugin ecosystem competitors only**
- What the user changes: Add `--scope plugin-ecosystem` or instruct "focus only on Claude Code plugins and similar agent framework extensions (Roo Code, Cline, Cursor extensions, MCP servers)."
- What changes in the output: Removes SaaS tools from the matrix. Tightens whitespace analysis to "what no Claude Code skill or MCP server currently owns." The primary competitor shifts from "inertia" to "generic prompting." Adds /feature-dev as the dominant named threat. Adds a distribution section comparing marketplace installation patterns.

**AMEND-02: Add internal competitor analysis (build vs. buy)**
- What the user changes: Add `--include internal` and provide the organization's existing tooling inventory (e.g., "we already use Confluence + GitHub Copilot + Linear").
- What changes in the output: Adds an "internal competitor" section for each tool the team already has. Reframes from "Signal vs. market" to "Signal vs. what we already pay for." The whitespace analysis becomes specific to the gap in the team's existing tooling stack.

**AMEND-03: Add a six-month watch list with early-warning signals**
- What the user changes: Request cadence recommendation and early-warning signals for each HIGH threat.
- What changes in the output: A watch section replaces the static threat assessment for /feature-dev and Copilot Workspace. Early-warning signals: /feature-dev adds a pre-build research phase; Copilot Workspace adds multi-namespace evidence modes; Cursor adds competitive analysis to Plan Mode. Any of these would compress Signal's whitespace significantly.

---

## Summary

| Section | Key Insight |
|---------|-------------|
| Primary competitor | Inertia wins on comfort, not capability. Signal must beat "doing nothing" on speed, not features. |
| Cultural headwind | Vibe coding is the 2025-2026 counter-narrative. Position Signal as "what you reach for after vibe coding fails in production." |
| Whitespace | Pre-build evidence gathering, repo-resident, audience-namespaced, with synthesis layer. No one owns this. |
| Table stakes | Zero-setup first run is the filter. Tools that require configuration before trust lose developers before first use. |
| Highest-threat first-party | Anthropic /feature-dev — bundled, default, same IDE; but execution-phase only. Signal is upstream. |
| Highest-threat third-party | GitHub Copilot Workspace — plan agent + CLAUDE.md support + Project Padawan create direct pre-build overlap at GitHub scale |
| Substitution threat | OpenAI Codex CLI and raw LLM prompting — zero setup, already installed, good enough for ad hoc use |
| Distribution threat | MCP ecosystem noise (18K+ servers); Signal needs a category name, not just a listing |
| Integration targets (not threats) | Devin (execution downstream), Productboard/Jira PD (PM discovery upstream), LaunchDarkly (rollout downstream) |
| Exec risk frame | "What is the cost of six weeks on the wrong feature?" That is the number Signal competes against. |
| AMEND priority | AMEND-02 (internal competitor analysis) produces the highest-value output for teams evaluating whether to adopt Signal alongside existing tooling |

**Findings count: 25 (F-01 through F-25)**
