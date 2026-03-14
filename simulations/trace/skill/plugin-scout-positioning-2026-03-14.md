---
skill: trace-skill
topic: plugin
item: scout-positioning
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md
prior_run: simulations/trace/skill/plugin-scout-competitors-2026-03-14.md
---

# /trace-skill -- scout-positioning

**Invocation**: `/scout-positioning "Signal plugin" --audiences "developers, PMs, architects, team leads"`
**Scenario**: Lead preparing all-hands pitch, needs per-audience positioning

## Phase 1: Setup

Prior competitors run loaded from trace file. Key data: primary competitor = inertia, whitespace = no tool owns pre-build investigation in Claude Code, table stakes = CLI-only/Markdown/zero accounts/cross-platform.

**SF-01 (MAJOR)**: Spec says "if available" with no fallback. If no prior run exists, skill degrades silently -- misses the "inertia is primary competitor" finding. Must add explicit fallback: note degradation, run competitor identification inline, flag "run /scout-competitors for richer positioning."

## Phase 2: Execute

**Category**: Pre-commit investigation tool. Not a coding assistant, not a testing framework, not an AI agent.

**Core differentiation**: Coding assistants prevent bad code. Signal prevents bad decisions.

### Per-audience positioning statements

**Developers**: "Signal finds spec bugs the way TDD finds code bugs -- before you write a line of implementation. You hand-compile through the system, surface the gaps in the design, and fix them in the spec. The time you spend in Signal is the time you don't spend untangling a bad decision six weeks later."

**PMs**: "Signal turns pre-build investigation into a structured afternoon, not a two-week research sprint. Run 12 customer personas against your spec, map your stakeholders, size the market -- all in one session. Walk into the all-hands with evidence, not intuition."

**Architects**: "Signal is a formal verification methodology for designs that don't have formal languages yet. Hand-compile your specs the way you'd hand-compile a parser: systematically, with findings, with severity scores. You've been the critic before the room has a chance to be."

**Team leads**: "Signal turns the heroic one-person deep-dive into a repeatable team process. Every investigation lands as artifacts in the repo, tied by topic prefix, discoverable by grep. When the next team inherits this feature, they grep the topic prefix and see every investigation that ran before them."

### PM reality check

| Claim | Reality | Verdict |
|-------|---------|---------|
| 12 customer personas | /review:customers C-01 through C-12 | VALID |
| Stakeholder map | /scout:stakeholders power/interest grid | VALID |
| Market sizing | /scout:market TAM/SAM/SOM | VALID |
| One afternoon | Lightweight default for /scout: | VALID |
| Quantified confidence score | Per-skill scores, no composite | PARTIAL -- claim ahead of spec |

## Phase 3: Findings

**Anti-positioning**: NOT a testing framework. NOT a code generator. NOT an autonomous agent. NOT a replacement for building.

**Messaging hierarchy**:
1. Primary: Signal makes the gap between idea and spec visible before you build
2. Supporting: 9 structured investigation namespaces, zero config, artifacts in repo as institutional memory
3. Proof: 9 proven techniques, 730+ scenarios from craftworks corpus

## Phase 4: Amend

1. Soften "quantified confidence score" to "evidence-backed brief with scored dimensions"
2. Add zero-config proof point to architect statement to preempt "heavyweight process" objection
3. Make team lead statement concrete: "grep the topic prefix" not abstract "trail" metaphor

## Verdict

**Result**: USEFUL. PM reality-check pass caught one ahead-of-spec claim. Cross-skill dependency (prior competitors run) is load-bearing -- the "inertia is primary competitor" finding changes the entire pitch.

### Findings Register

| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | No fallback for missing prior /scout:competitors run -- silent degradation | MAJOR |
| SF-02 | "Quantified confidence score" claim ahead of spec capability | MINOR |
| SF-03 | Artifact path consistent across spec and plugin-plan.md | INFO |
