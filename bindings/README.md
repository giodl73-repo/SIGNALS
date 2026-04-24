# Signal Bindings

Four program.yaml variants for different invocation models. All bindings are complete,
standalone files. Pick one, copy it to program.yaml (or point --config at it), and
generate the plugin.

---

## Variants

### binding-flat.program.yaml

The canonical binding. Exact copy of program.yaml with a header comment.

Commands: 62 atomic skills + 9 namespace aggregators + trace-skill + 4 quest skills = 76 total

Usage:
  /scout-competitors
  /trace-contract
  /draft-spec
  /flow-lifecycle

When to use:
- You know the specific skill you want
- Teams that have learned the namespace model
- Default for all new installs
- Reference for all other bindings (if in doubt, diff against this one)

---

### binding-grouped.program.yaml

Namespace aggregators as primary entry points with full sub-skill menus in the body.
All 62 atomic skills are still present and directly invokable.

Commands: 12 namespace aggregators (with sub-skill menus) + 62 atomic skills = 74 total

Usage:
  /scout             -> shows menu of 8 scout sub-skills, routes to most relevant
  /scout-competitors -> runs directly (still works)
  /flow              -> shows menu of 7 flow sub-skills
  /quest             -> shows menu of 4 quest sub-skills

When to use:
- Onboarding new users who do not know the skill names yet
- Teams where users describe intent and want the plugin to route
- Demos where discoverability matters more than precision
- Exploratory use: "I want to do something in the trace namespace"

The aggregator body describes each sub-skill in one line. Typing the namespace command
without a specific skill will present the menu and run the most contextually appropriate
sub-skill, or prompt the user to choose.

---

### binding-prefixed.program.yaml

Every skill and namespace aggregator prefixed with "signal-".
scout-competitors becomes signal-scout-competitors, trace-contract becomes
signal-trace-contract, etc. Namespace aggregators become signal-scout, signal-trace, etc.

Commands: 13 prefixed namespace aggregators + 62 prefixed atomic skills = 75 total

Usage:
  /signal-scout-competitors
  /signal-trace-contract
  /signal-draft-spec
  /signal-scout

When to use:
- Multi-plugin environments where "scout", "draft", "review" collide with another plugin
- Craftworks workspaces that already define /scout or /trace for other purposes
- Any environment where you need to make Signal's namespace explicit
- CI/automation scripts that call skills by name and need unambiguous routing

Workers in this binding are updated to reference prefixed command names so
worker->command associations remain consistent.

---

### binding-domains.program.yaml

Six cross-namespace domain commands for workflow-level invocation, plus all 62 atomic
skills and 9 namespace aggregators unchanged.

Domain commands: 6
Namespace aggregators: 9 + trace-skill + 4 quest skills = 14
Atomic skills: 62
Total: 82 commands

Domain commands and what they span:

  /decide    -> scout-competitors + scout-feasibility + scout-market +
                prove-hypothesis + prove-websearch + prove-synthesize
               Output: decision brief with market landscape, viability, evidence, recommendation

  /simulate  -> flow-lifecycle + flow-conversation + trace-state +
                trace-contract + trace-permissions
               Output: simulation findings report with gaps, exception paths, anomalies

  /validate  -> review-design + review-users + review-customers +
                listen-feedback + listen-adoption
               Output: validation brief with expert findings, usability scores, NPS forecast

  /specify   -> draft-spec + draft-proposal + draft-pitch
               Output: spec package (technical spec + decision record + pitch)

  /evidence  -> full prove suite: hypothesis -> websearch -> intelligence ->
                prototype -> analysis -> interview -> synthesize -> publish -> topic
               Output: complete evidence dossier with hypothesis verdict

  /track     -> topic-new + topic-plan + topic-status + topic-story + topic-echo
               Output: topic dashboard with coverage, narrative, readiness statement

When to use:
- Executives and PMs who think in outcomes, not skill names
- Sprint kickoffs where you want to run the full decision workflow in one command
- Teams new to Signal who want guided workflows before learning individual skills
- When the goal is "am I ready to commit?" rather than "run this specific analysis"

Individual skills remain available alongside domain commands. Users who know the skill
they want can still type it directly.

---

## Generating the Plugin

All bindings assume the craft generate pipeline. To use a specific binding:

Option A: Copy to program.yaml before generating
  cp bindings/binding-grouped.program.yaml program.yaml
  craft generate --stage program

Option B: Point --config at the binding (if your craft version supports it)
  craft generate --stage program --config bindings/binding-domains.program.yaml

Option C: Symlink for active development
  # On Unix:
  ln -sf bindings/binding-prefixed.program.yaml program.yaml

The generated output lives in .claude/commands/ as one .md file per skill.
Namespace aggregators and domain commands get their own .md files with the body
text from body_file resolved and parameters injected.

---

## Binding Selection Guide

  Single developer, learning Signal      -> flat (the default)
  Team onboarding, discoverability       -> grouped
  Shared workspace, multiple plugins     -> prefixed
  PM-driven, workflow orientation        -> domains
  Production install, no ambiguity       -> flat or prefixed
  Demo / showcase                        -> grouped or domains

---

## Adding a New Binding

1. Copy binding-flat.program.yaml as the base
2. Change the header comment to describe the variant
3. Modify the commands section only (entities, workers, roles, state are stable)
4. Name the file binding-<variant>.program.yaml
5. Add an entry to this README under Variants
