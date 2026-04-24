# Hypothesis-Driven Investigation (`/research` Skill)

Structured hypothesis → experiment → findings loops. "We think X" → test it → "Actually Y."

## What It Simulates

Design decisions — the designer (or team members) use AI to run experiments and analyze results against a hypothesis.

## Scale

- **Craftworks**: 7+ investigations (Q01-Q07), 16+ sub-investigations, 8+ experiments per Q
- **Agentverse**: 59 research questions, 30 with experiment subdirectories, 8 contributors

## Evidence Files

### The Skill (reusable across any repo)

| File | Purpose |
|------|---------|
| `C:\src\craftworks\.claude\skills\research\SKILL.md` | `/research` skill — 708-line orchestrator for hypothesis-driven investigation |

### Craftworks Investigations

| Path | Content |
|------|---------|
| `C:\src\craftworks\design\admin\focus\Q02\` | Q02 investigation |
| `C:\src\craftworks\design\admin\focus\Q04\` | Q04 investigation |
| `C:\src\craftworks\design\admin\focus\Q05\` | Q05 investigation |
| `C:\src\craftworks\design\admin\focus\Q07\` | Q07 investigation (16 sub-studies) |
| `C:\src\craftworks\design\admin\focus\Q07\README.md` | Investigative journey narrative |

### Agentverse Question Registry (Multi-Contributor)

| File | Purpose |
|------|---------|
| `C:\src\agentverse\designs\questions.md` | Master registry — 59 questions, 8 contributors, P0/P1 priority |
| `C:\src\agentverse\designs\_consensus\questions\` | 59 question files + 30 experiment subdirectories |

### Sample Agentverse Questions (with experiments)

| File | Owner | Topic |
|------|-------|-------|
| `C:\src\agentverse\designs\_consensus\questions\Q01.md` | giodl | Workspace topology |
| `C:\src\agentverse\designs\_consensus\questions\Q02.md` | jamesol | Agent Workspace 1:N |
| `C:\src\agentverse\designs\_consensus\questions\Q04.md` | jamesol | Git-based config UX |
| `C:\src\agentverse\designs\_consensus\questions\Q05.md` | jamesol | Agentverse blueprint |
| `C:\src\agentverse\designs\_consensus\questions\Q11.md` | jeffand | Git vs Dataverse substrate |
| `C:\src\agentverse\designs\_consensus\questions\Q18.md` | giodl | Solution escape path |

## Skill Workflow

1. **Hypothesis first** — "What do we expect to find, and what would change our minds?"
2. **Experiment types**: `exp-` (enterprise search / Work IQ), `inv-` (web/desk inquiry), `exp-` (code experiment)
3. **Result files** in `Qx/results/` with letter labels matching experiment bullets
4. **Synthesis** — answer-first, reverse-experiment format
5. **Diagrams** — ASCII structural/comparative/flow diagrams
6. **Narrative README** — "What we thought we learned" vs "What we actually learned"
7. **Status lifecycle**: Open → In Progress → Proposed → Answered (group ratification)

## Multi-Contributor Model (Agentverse)

Questions owned by individual contributors, prioritized P0/P1, progress through Open → Proposed → Answered. Each resolves a design disagreement through evidence. Questions fork and block each other (dependency graph).

Contributors: giodl, jamesol, edpiva, jeffand, aadkannan, jukoesma, sriknair, alexpeck, rakukeha, singhsidd, sharadbajaj, aarthisk, wucheng
