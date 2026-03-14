---
skill: trace-skill
topic: plugin
item: scout-competitors
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md
---

# /trace-skill -- scout-competitors

**Skill under trace**: scout-competitors
**Test invocation**: `/scout-competitors "Signal plugin for Claude Code -- AI-assisted feature investigation"`
**Repo context**: C:\src\sim (Signal plugin repo -- CLAUDE.md, plugin-plan.md, PRINCIPLES.md, signal.program.yaml, 9 namespace specs)
**Scenario**: First-time user, PM persona, wants to understand the competitive landscape before committing to building Signal

---

## Setup Phase

**What the skill should auto-detect:**

Reading repo context signals:
- `CLAUDE.md`: "Signal is a developer tool for feature decision-making"
- `plugin-plan.md`: "Claude Code plugin, 9 namespaces, 48 skills, developer tooling"
- `signal.program.yaml`: plugin name = signal, target_platform = claude-code
- No package.json (not a published npm package yet)
- No prior scout run in `simulations/scout/competitors/`

**Auto-detected domain**: AI developer tooling / Claude Code plugins / simulation and investigation methodology

**Confirmed without prompting**: Yes -- repo context is sufficient. No need to ask the user for domain description.

**Roles loaded**: PM, Strategy, Architect, GTM

**Setup verdict**: PASS. Repo context is rich enough. The skill should proceed to execute without confirmation.

---

## Execute Phase

### PM lens (feature parity scoring)

Competitors for an AI-assisted investigation/simulation plugin for Claude Code:

| Competitor | What they do | Feature parity with Signal |
|------------|-------------|---------------------------|
| Cursor AI | IDE with AI assistance, context-aware code generation | 2/10 -- code generation only, no investigation methodology |
| GitHub Copilot Workspace | Task-to-PR pipeline, multi-file edits | 2/10 -- implementation focused, no pre-build validation |
| Devin / Factory AI | Autonomous coding agents | 1/10 -- fully autonomous, opposite philosophy |
| OpenAI Assistants | Custom GPT agents via API | 3/10 -- general agent, no domain-specific methodology |
| ChatGPT / Claude (bare) | General LLM assistants | 4/10 -- manual workflow, no structured output |
| Panel (academic review) | Panel plugin for paper review in craftworks | 6/10 -- structured review methodology, same ecosystem |
| Custom scripts / ad-hoc | Teams hand-rolling their own investigation prompts | 5/10 -- unstructured version of what Signal formalizes |
| Nothing (the void) | Teams don't do pre-build investigation at all | 0/10 -- the most common competitor |

**PM finding**: The real competition is "nothing" -- most teams skip pre-build investigation entirely. Signal's primary competitive threat is inertia, not another tool.

### Strategy lens (positioning gap)

- **Cursor/Copilot**: positioned as coding accelerators (implementation speed). Signal is positioned before implementation (design confidence). These are adjacent but not competing -- a developer could use both.
- **Panel**: closest to Signal's structured methodology approach. Panel is academic review (post-artifact). Signal is pre-commit investigation. Complementary.
- **Whitespace**: No tool in the Claude Code ecosystem offers structured pre-build investigation with topic narrative management. Signal owns this space entirely within Claude Code.
- **Key positioning insight**: Signal is not "AI does the research for you" (Devin model). It is "AI plays every role in your pre-build review" (structured empathy engine). Different philosophy, different audience.

### Architect lens (technical moat)

- **Techniques corpus** (`techniques/01-09/`): 9 proven simulation techniques with 730+ scenarios of evidence. This is the moat -- years of methodology work that would take a new entrant months to replicate.
- **topic narrative model**: The signal-topic-item-date naming convention + `/topic:` namespace creates a coherent artifact graph across all investigation dimensions. No competitor has this.
- **program.yaml / CREST input**: Generates binding variants from a single definition. Cross-platform (Claude Code, Cursor, Cline/Roo) without rewriting skill content. Technical advantage in distribution.
- **Binding-agnostic design**: Skills designed once, deployed to any AI coding tool. Reduces switching cost for teams already using Cursor or Copilot alongside Claude Code.

### GTM lens (distribution advantage)

- **All-hands install path**: Copy one SKILL.md and run. Zero config. This is the distribution advantage -- no signup, no account, no server, no API key beyond what Claude Code already requires.
- **craftworks ecosystem**: Already deployed in the craftworks monorepo with 730+ simulation scenarios proving the techniques. Built-in case study.
- **Target beachhead**: Dynamics 365 / Power Platform developers who already use craftworks methodology. They know the vocabulary (series, findings, DCR). Signal packages what they already do manually.

---

## Findings Phase

### Competitive Matrix

| Competitor | Feature Parity | Positioning Gap | Technical Moat | Distribution | Threat Level |
|------------|---------------|-----------------|----------------|--------------|-------------|
| Cursor AI | 2/10 | Complementary | Editor lock-in | VS Code fork | LOW |
| GitHub Copilot | 2/10 | Complementary | GitHub lock-in | GitHub native | LOW |
| Panel (craftworks) | 6/10 | Complementary | Same ecosystem | craftworks only | NONE (ally) |
| Custom ad-hoc | 5/10 | Direct | None | None | MEDIUM |
| Nothing (inertia) | 0/10 | Direct | Habit | Everywhere | HIGH |

### Whitespace

No tool in the Claude Code / AI coding assistant ecosystem offers:
1. Structured pre-build investigation methodology (9 namespaces covering every pre-commit dimension)
2. Topic narrative management across investigation artifacts
3. Binding-agnostic packaging (same methodology, multiple invocation targets)

### Table stakes

For Signal to be taken seriously as a developer tool:
- T-01: CLI-only operation (no GUI, no server, no setup beyond file copy)
- T-02: Markdown output that lands in git (artifacts are first-class repo citizens)
- T-03: Zero new accounts or API keys (uses Claude Code's existing auth)
- T-04: Works on Windows, macOS, Linux (cross-platform from day one)

### Key finding

**F-01 (MAJOR)**: The strongest competitor is "doing nothing." The competitive brief
should be framed as "why bother at all?" before "why Signal vs. X?" The go/no-go
framing must address inertia first: what does a team lose by skipping pre-build
investigation? (Answer: post-ship rework, spec bugs caught late, customer adoption
friction that could have been predicted.)

**F-02 (MINOR)**: Panel is positioned as an ally, not a competitor. Signal generates
the inputs (investigations, specs) that Panel reviews. The two skills are adjacent
in the craftworks ecosystem and should reference each other.

---

## Amend Phase

Three things the user (PM persona) could change:

1. **Narrow to "Claude Code plugin ecosystem only"** -- the current scope includes
   general AI tools (Cursor, Copilot) which dilutes the competitive signal. A PM
   building within the craftworks ecosystem would want competitors scoped to "other
   Claude Code plugins" and "other craftworks tools."

2. **Add the "time cost" dimension** -- the matrix scores feature parity but not
   the time a team spends on investigation manually vs. with Signal. Adding a
   "hours saved per investigation cycle" row would make the competitive case more
   concrete for an executive audience.

3. **Focus on the beachhead segment** -- the Dynamics 365 / craftworks developer
   audience is the beachhead. Scoring competitors from their specific perspective
   (do these tools work in a Windows/MSYS2 Dataverse development environment?)
   would produce a more actionable brief for the target launch audience.

---

## Verdict

**Result**: USEFUL -- the skill produces a genuinely valuable competitive brief.

**What worked well**:
- Auto-detection from repo context worked perfectly. No user prompting needed.
- The 4 stock roles (PM, Strategy, Architect, GTM) cover all the right dimensions.
- "Nothing / inertia" as the primary competitor is a real and important finding that
  manual competitive analysis often misses.
- The whitespace finding (no tool owns pre-build investigation in Claude Code) is
  the core strategic insight -- Signal should lead with this.

**What needs fixing in the spec**:
- SF-01: The artifact naming in the spec uses `sim-competitors-{slug}-{date}.md`
  but our convention is `{topic}-{item}-{date}.md`. The spec predates the naming
  decision. Update: artifact should be `{topic}-competitors-{date}.md` in
  `simulations/scout/competitors/`.
- SF-02: The spec says "infer 5-10 competitors by name" in setup. For this repo,
  the skill correctly identified that "nothing" is the primary competitor -- but
  the spec doesn't explicitly tell the skill to consider the zero-tool scenario.
  Add to spec: "Include 'none / status quo' as a competitor row."
- SF-03: The spec mentions `WebSearch` as a tool but the program.yaml has
  WebSearch in the tools list for `scout`. Confirm this is correct -- the
  competitive analysis should use web search to verify competitor features, not
  just reason from training data.

**Skill finding severity**: SF-01 MAJOR (naming convention), SF-02 MINOR (spec gap),
SF-03 INFO (tool confirmation)
