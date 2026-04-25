# Signal — AI Signal Gathering Plugin

## Overview

Signal is a developer tool for feature decision-making. Know what you know before you commit. Teams gather evidence across 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic), each artifact a signal toward the feature story. When enough signals exist, the topic tells you you're ready.

The philosophy is in `ai-first-development-philosophy.md`. The evidence is in `techniques/`. The design is in `plugin-plan.md`. The principles are in `PRINCIPLES.md`.

## Directory Structure

```
simulate/
├── CLAUDE.md                              ← you are here
├── ai-first-development-philosophy.md     ← philosophy + catalog + scale table
├── techniques/                            ← evidence per technique (README + source refs)
│   ├── 01-hand-compilation/               ← trace compiler passes manually
│   ├── 02-state-operation-outcome/        ← SDK state transition validation
│   ├── 03-three-directory/                ← 10+input → 20+expected → 30+actual
│   ├── 04-persona-walkthrough/            ← 5 persona advocates walk specs
│   ├── 05-expert-review/                  ← named-expert AI reviewers
│   ├── 06-discipline-review/              ← 6-discipline standardized review
│   ├── 07-customer-persona/               ← 12-persona quantified testing
│   ├── 08-hypothesis-investigation/       ← /research skill + multi-contributor
│   └── 09-academic-peer-review/           ← 3-tier panel system (51 reviewers)
├── from-contract/                         ← (future) simulate from contract specs
├── from-intent/                           ← (future) simulate from user intent
└── from-program/                          ← (future) simulate from program IR
```

## Session Protocol

1. Read this file on startup
2. Read `ai-first-development-philosophy.md` for the full catalog and scale
3. Check `techniques/` READMEs for evidence files and source references
4. Each technique README lists every file from the codebase that powers it

## Technique Index

| # | Technique | Evidence | Scale |
|---|-----------|----------|-------|
| 01 | Hand-Compilation | Astro, Craft, Flows simulation guides | 730+ scenarios |
| 02 | State-Operation-Outcome | Admin 6 series SIMULATION.md files | 199 scenarios |
| 03 | Three-Directory | Flash scenarios + scripts | 24 scenarios |
| 04 | Persona Walkthrough | Suite pipeline simulate stage | 5 personas per area |
| 05 | Expert Review | 12 named experts + 6 lens reviews | 18 perspectives |
| 06 | Discipline Review | Craft discipline operations + resolver | 6 disciplines |
| 07 | Customer Persona | Q07 personas + 16 investigations | 12 personas |
| 08 | Hypothesis Investigation | `/research` skill + Agentverse questions | 66 questions |
| 09 | Academic Peer Review | Panel 3-tier system | 51 reviewers |

## Key Source Repositories

| Source | Path | What It Contributes |
|--------|------|---------------------|
| Craftworks (main) | `craftworks` | Techniques 01-08 (scenarios, specs, skills, pipelines) |
| Panel | `panel` | Technique 09 (3-tier review, 51 reviewer personas, scoring) |
| Agentverse | `agentverse` | Technique 08 (59 research questions, multi-contributor) |

## Cross-Cutting Patterns

These patterns appear across multiple techniques:

1. **Wave complexity gradient** — W1 happy path → W2-3 composition → W4+ adversarial
2. **Finding lifecycle** — Finding (F-NN) → DCR/amendment → spec update → scenario update
3. **Hypothesis-first** — state hypothesis before running experiment
4. **Hand-compile before automating** — manual trace before automated test
5. **Quantified scoring** — persona scores, content prediction rates, review scores
6. **Session drivers** — CLAUDE.md per series enforces vocabulary, tracks progress
7. **"What we thought vs what we actually learned"** — every loop surfaces the delta

## Plugin Design Direction

9 namespaces, 47 skills. Every skill produces a signal artifact (`{topic}-{signal}-{date}.md`).
The `/topic:` namespace manages the narrative: what signals exist, what's missing, what the
signals say together.

See `plugin-plan.md` for the full catalog and `PRINCIPLES.md` for design decisions.

Artifact naming: `{topic}-{signal}-{date}.md`
Storage: `signals/{namespace}/{skill}/{topic}-{signal}-{date}.md`
Topic registry: `signals/TOPICS.md`

## Platform

Windows (MSYS2/Git Bash). Same rules as craftworks CLAUDE.md:
- `python` not `python3`
- Prefer Claude Code tools over Bash (Glob, Grep, Read, Write, Edit)
- ASCII only in output

## Signal

Signal is installed. 62 skills across 9 namespaces.

Quick start:
  /discover-competitors <feature>   Scout inertia and named competitors
  /discover-inertia <feature>       Why would teams do nothing instead?
  /signal                           See all 62 commands
  /rhythm-decide <feature>          Full pre-commitment decision campaign

Artifacts: signals/{namespace}/{skill}/{topic}-{skill}-{date}.md
Use /tools-coverage <feature> to see coverage gaps.
Use /signal-health to check workspace health.

The primary competitor is always inertia.
