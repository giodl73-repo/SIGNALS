# Simulate — AI Simulation Plugin Project

## Overview

Simulate is the plugin that exposes every simulation technique we've built across the craftworks ecosystem. This directory is both the evidence corpus and the future plugin source.

The philosophy is in `ai-first-development-philosophy.md`. The evidence is in `techniques/`. The plugin will make these techniques available as composable, reusable simulation commands.

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
| Craftworks (main) | `C:\src\craftworks` | Techniques 01-08 (scenarios, specs, skills, pipelines) |
| Panel | `C:\src\panel` | Technique 09 (3-tier review, 51 reviewer personas, scoring) |
| Agentverse | `C:\src\agentverse` | Technique 08 (59 research questions, multi-contributor) |

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

The simulate plugin will expose these techniques as composable commands:

```
simulate scenario <technique> [options]    # Run a simulation scenario
simulate review <target> --experts         # Expert review simulation
simulate walkthrough <specs> --personas    # Persona walkthrough
simulate research <question>               # Hypothesis investigation
simulate panel <paper>                     # Academic peer review
```

Each command wraps the methodology documented in the technique README, making it reusable across any project — not just craftworks.

## Platform

Windows (MSYS2/Git Bash). Same rules as craftworks CLAUDE.md:
- `python` not `python3`
- Prefer Claude Code tools over Bash (Glob, Grep, Read, Write, Edit)
- ASCII only in output
