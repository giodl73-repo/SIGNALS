# Sim Plugin — Session Handover

**From**: Craftworks session (C:\src\craftworks, branch feature/theseus-the-unifier)
**To**: New Claude session at C:\src\sim
**Date**: 2026-03-14
**Repo**: https://github.com/giodl_microsoft/sim.git

---

## What This Is

**Sim** is a simulation plugin for Claude Code that packages every simulation technique built across the craftworks ecosystem into a single plugin anyone can use. Target audience: 5,000+ developers at an all-hands. Zero barrier to entry — run one skill, get results immediately with stock roles.

## What's Been Done

### 1. Philosophy and Evidence (complete)

- `ai-first-development-philosophy.md` — core philosophy with simulation catalog (12 techniques, 9 principles)
- `techniques/01-09/` — 9 evidence directories, each with README tracing source files from craftworks, panel, agentverse
- `CLAUDE.md` — session driver with directory structure, technique index, cross-references

### 2. Plugin Plan (complete)

- `plugin-plan.md` — the master plan. Contains:
  - **8 namespaces**: scout, draft, review, flow, trace, prove, listen, program
  - **42 skills** across those namespaces
  - **Design principles**: zero barrier, flat skills, namespace=audience, no dashes in skill names
  - **Storage**: namespace/skill subdirectories under `simulations/`
  - **Topics**: `TOPICS.md` registry with `{topic}-{slug}-{date}.md` naming convention. Topic is a prefix that ties artifacts across all directories (e.g., `frogs-toad-2026-03-14.md`, `frogs-green-2026-03-14.md`)
  - **4-phase lifecycle**: setup → execute → findings → amend (common across all skills)
  - **Default modes per namespace**: full (review 4.7, trace 4.7, prove 4.3, flow 4.3, program 4.3) vs lightweight (scout 3.3, draft 3.0, listen 3.7). Every skill supports `--quick` and `--full` flags.
  - **Stock roles** ship with every skill. Custom roles in `.craft/roles/simulate/` unlock depth.
  - **Program orchestrator**: `/program:plan` sequences skills into staged plans with gates, tracked by topic prefix
  - **Technique heritage**: maps each skill to its proven technique from the evidence corpus

### 3. User Testing (complete)

- **Q01** — Tier 3 skill catalog validation. 28 personas (backend 9, frontend 9, developer 10) tested the original 10 skills. Results in `research/Q01/results/inv-a.md`, `inv-b.md`, `inv-c.md`. Key outcomes: 3 skills cut/merged, 5 new skills added, `/flow:` vs `/trace:` namespace split established.
- **Q02** — Common lifecycle validation. Two experiments:
  - **(a) Unified test**: 10 mixed personas. Usefulness 4.20, predictability 4.30, complexity 2.20. Amend most skippable. Execute never skipped. Results in `research/Q02/results/inv-a.md`.
  - **(b) Per-namespace test**: 3 personas per namespace. Review+trace strongest fit (4.7). Draft+scout weakest (3.0-3.3). Lightweight default for PM-facing, full for dev-facing. Results in `research/Q02/results/inv-b.md`.

### 4. Namespace Specs (complete — ready for simulation)

8 detailed specs in `simulations/draft/specs/`:

| Spec | File | Skills | Key Details |
|------|------|--------|-------------|
| Scout | `sim-scout-2026-03-14.md` | 8 | PM-facing, lightweight default, 7 stock roles |
| Draft | `sim-draft-2026-03-14.md` | 3 | Author-facing, lightweight default, spec/proposal/pitch |
| Review | `sim-review-2026-03-14.md` | 4 | Validation, full default, 6 disciplines + 5 advocates + 12 personas |
| Flow | `sim-flow-2026-03-14.md` | 7 | Domain process, full default, lifecycle/conversation/trigger/dataflow/integration/throttle/resilience |
| Trace | `sim-trace-2026-03-14.md` | 7 | System platform, full default, request/state/contract/component/deployment/migration/permissions |
| Prove | `sim-prove-2026-03-14.md` | 8 | Investigation, full default, hypothesis → experiments → synthesize → publish |
| Listen | `sim-listen-2026-03-14.md` | 3 | Post-ship feedback, lightweight default, 12 customer personas |
| Program | `sim-program-2026-03-14.md` | 1 | Orchestrator, full default, sequences all other namespaces |

### 5. Directory Structure (created)

```
simulations/
├── TOPICS.md                    # topic registry
├── scout/{8 skill dirs}/
├── draft/specs/, proposals/, pitches/
├── review/{4 skill dirs}/
├── flow/{7 skill dirs}/
├── trace/{7 skill dirs}/
├── prove/investigations/, publications/
├── listen/{3 skill dirs}/
└── program/plans/
```

### 6. Dogfooding (in progress)

Topic `sim` registered in TOPICS.md. The plugin is being built using its own methodology:
- Specs drafted (step 4 above) ← **you are here**
- Next: simulate against the specs (review:users, review:customers, listen:adoption)
- Then: build the actual skills as Claude Code skills (`.claude/skills/{namespace}-{skill}/SKILL.md`)

---

## What Needs To Be Done

### Immediate Next Steps

1. **Simulate against the specs** — Run the plugin's own simulation skills against its own specs:
   - `/review:users` — 5 persona advocates (maker, developer, compliance, supervisor, operator) walk through the plugin experience
   - `/review:customers` — 12 customer personas (C-01 through C-12) evaluate the plugin
   - `/listen:adoption` — simulate adoption curves and friction points for 5,000 person rollout
   - Write results to `simulations/review/users/sim-*.md`, `simulations/review/customers/sim-*.md`, `simulations/listen/adoption/sim-*.md`

2. **Synthesize Q01 cross-role findings** — `research/Q01/results/inv-d.md` (cross-persona synthesis of inv-a/b/c) has not been written yet. Update Q01.md findings and answer sections.

3. **Build the skills** — Implement each namespace as Claude Code skills:
   - Skills go in `.claude/skills/{namespace}-{skill}/SKILL.md` (e.g., `.claude/skills/scout-competitors/SKILL.md`)
   - Each skill is a prompt file that drives E2E workflow using the spec as its blueprint
   - Stock roles embedded in each skill's prompt
   - Lifecycle phases (setup/execute/findings/amend) built into the prompt flow

4. **Build program orchestrator** — `/program:plan` generates `program.yaml` from intent, sequences skills across stages with gates and topic tracking

5. **Package as plugin** — `.claude-plugin/manifest.json` with all skills registered

### Key Design Decisions (already made)

- **No dashes in skill names** — `/scout:competitors` not `/scout:competitor-analysis`
- **Namespace = audience** — PM knows `/scout:`, dev knows `/trace:`
- **Stock roles for everything** — zero setup required for first use
- **Topic prefix** — `{topic}-{slug}-{date}.md` ties artifacts across directories
- **Lightweight vs full** — PM-facing defaults to lightweight, dev-facing to full
- **`--quick` and `--full` flags** — override default mode on any skill

### Source Material (in craftworks)

The specs reference techniques and roles from the craftworks monorepo at `C:\src\craftworks`:

| What | Where |
|------|-------|
| Backend roles (OLE format) | `craft-cli/config/roles/backend/*.md` |
| Frontend roles | `craft-cli/config/roles/frontend/*.md` |
| Developer roles | `craft-cli/config/roles/developer/*.md` |
| PM roles | `craft-cli/config/roles/pm/*.md` |
| 12 customer personas | `design/admin/focus/Q07/data/customer-personas.md` |
| 51 academic reviewers | `panel/.craft/roles/panel-reviewer/` |
| Research skill | `.claude/skills/research/SKILL.md` |
| Simulation guides | `design/astro/scenarios/SIMULATION.md`, `design/agent/scenarios/SIMULATION.md`, `design/flash/scenarios/SIMULATION.md` |
| Persona walkthrough pipeline | `.craft/pipelines/suite/simulate.md` |
| Review standards | `design/astro/reviews.md` |
| Panel scoring | `panel/config/scoring.yaml` (4-point and 10-point scales) |

### User Preferences

- **Giovanni** — 40+ Microsoft patents, ADO.NET DiffGram inventor. Deep BIC platform knowledge.
- **Always `mode: "bypassPermissions"`** when launching agents
- **Agents write to disk**, not inline (saves context)
- **`--body-file` for GitHub CLI**, never heredoc
- **ASCII only** for clipboard/Teams output
- **`git mv` for renames**, never plain `mv`
- **Windows permanently** — Git Bash, `python` not `python3`
- **Don't touch git state without asking** — parallel sessions running

---

## Validation Contract

When this session's work is done, bring it back to the craftworks session for the **ultimate test**: use the built plugin to simulate itself. The craftworks session will validate:
1. Does each skill produce the artifact it promises?
2. Does the topic system tie artifacts together across namespaces?
3. Does the program orchestrator sequence skills correctly?
4. Do stock roles produce useful results with zero setup?
5. Does the lightweight/full mode distinction feel right?

---

*Generated by the craftworks session. Good luck building it.*
