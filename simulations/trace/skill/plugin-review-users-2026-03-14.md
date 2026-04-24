---
skill: trace-skill
topic: plugin
item: review-users
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-review-2026-03-14.md
---

# /trace-skill -- review-users

**Invocation**: `/review-users plugin-plan.md --journey "install Signal and run first skill"`
**Scenario**: 5 persona advocates walk through installing Signal and running /scout-competitors

## Phase 1: Setup

Target artifact: plugin-plan.md + output/T1/.claude/skills/scout/SKILL.md
User-facing surface: CLI invocation (/scout-competitors), SKILL.md file, artifact output
Entry points per persona:
- Maker: README first, then tries to copy SKILL.md
- Developer: finds SKILL.md directly, reads it, runs it
- Compliance: reads plugin-plan.md for data handling
- Supervisor: asks team lead, gets a link
- Operator: checks if it works in CI, reads the SKILL.md like a config file

## Phase 2: Execute

### Maker (C-01 Maria equivalent)
"I clicked the link in the all-hands email and found a GitHub repo. There's a SKILL.md
file I'm supposed to copy to .claude/skills/scout/. I don't know what .claude/skills/ is.
There's no README telling me where that folder goes. I asked my developer colleague.
He copied the file for me. Then I typed /scout-competitors in Claude Code and... it
worked! The output was Markdown which I had to open in VS Code to read nicely."
Score: 2/5. Delight: it ran. Friction: install required developer help.

### Developer
"Found the repo. Saw the folder structure. Copied output/T1/.claude/skills/scout/SKILL.md
to my .claude/skills/scout/SKILL.md. Ran /scout-competitors 'my feature'. Clean output,
good structure. The frontmatter on the artifact was a nice touch -- I can grep it.
One issue: the SKILL.md body still says 'Implementation for scout.' -- it's a stub.
The output was generic, not useful. The SKILL.md needs the golden prompt body."
Score: 3/5. Critical finding: stub body produces generic output.

### Compliance Officer
"I read the plugin-plan.md looking for data handling. Found P-09 (frontmatter provenance)
and P-01 (concurrent by default). No mention of what data leaves the machine. I know
Claude Code sends repo content to Anthropic -- that's my primary concern. Signal doesn't
make this worse but the README doesn't say that explicitly."
Score: 3/5. Finding: compliance brief missing from install docs.

### Supervisor
"My team told me they installed something called Signal. I asked what it does. They showed
me a Markdown file with competitive analysis. I asked if I could see what they've run.
They said 'it's in the simulations/ folder.' I looked -- it was there, dated, with
frontmatter. That's good. I can audit what was run. But I can't stop them from running
things without approval -- there's no gate."
Score: 4/5. Finding: no approval gate, but append-only artifacts satisfy audit need.

### Operator
"Looks like a Claude Code skill. Copies like any other SKILL.md. I checked if it runs
in our CI pipeline. It does -- claude -p with the skill prompt works headless.
The --json flag for structured output is documented but not implemented yet (it's in the spec
as a flag but the stub SKILL.md doesn't produce JSON). That would have been useful for CI."
Score: 3/5. Finding: --json flag documented but not implemented in stub.

## Phase 3: Findings

Universal friction (3+ personas):
- P1: SKILL.md bodies are stubs -- all personas who ran the skill got generic output
- P2: No README with install steps -- Maker needed developer help
- P2: No compliance brief -- Compliance found the right principles but had to dig

Role-specific:
- Developer: stub body is the blocker (F-07 from interview -- critical)
- Operator: --json not implemented in stub

Aggregate usability score: 3/5

## Phase 4: Amend

1. Ship with golden prompt bodies (F-07 critical -- no stub bodies)
2. Write a README with 3-step install (copy file, open Claude Code, run /scout-competitors)
3. Add compliance one-pager to repo root (signal-compliance-brief.md)

## Verdict

**Result**: USEFUL design, BLOCKED by stubs.
The 5-persona structure works perfectly -- Compliance and Operator perspectives caught
issues Developer alone would have missed. The skill is sound; the implementation gap is stubs.

### Findings Register
| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | Stub SKILL.md bodies produce generic output for all personas | CRITICAL |
| SF-02 | No README with install steps -- Maker required developer help | MAJOR |
| SF-03 | --json flag documented but not implemented in stub | MAJOR |
| SF-04 | Compliance brief not in repo root | MAJOR |
| SF-05 | Supervisor found append-only artifacts satisfy audit need -- delight | DELIGHT |
