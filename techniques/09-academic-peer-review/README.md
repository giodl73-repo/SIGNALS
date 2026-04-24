# Three-Tier Academic Peer Review (Panel)

Full academic paper review lifecycle with simulated expert reviewers at three tiers: paper → module → board.

## What It Simulates

Academic peer review — 51 AI expert personas across 10 categories review papers, modules, and the full research program.

## Scale

51 reviewers, 10+ research papers, 3 tiers, 4-point and 10-point scoring scales.

## Evidence Files

### Commands (Operations)

| File | Tier | Purpose |
|------|------|---------|
| `C:\src\panel\commands\paper.md` | Paper | Individual paper lifecycle — setup, author, review, status, show, promote |
| `C:\src\panel\commands\module.md` | Module | Cross-portfolio panel review — design, review, curate, status |
| `C:\src\panel\commands\board.md` | Board | Monorepo-level review — cross-module synthesis |

### Configuration

| File | Purpose |
|------|---------|
| `C:\src\panel\config\scoring.yaml` | Scoring rubrics — 4-point (paper) and 10-point (module/board) scales |
| `C:\src\panel\config\stages.yaml` | 8-stage lifecycle (draft → panel → synthesis → revision → recheck → ready → submit → accepted) |

### Shared Engines

| File | Purpose |
|------|---------|
| `C:\src\panel\shared\synthesis-engine.md` | Consolidate reviews → SYNTHESIS.md with P1/P2/P3 classification |
| `C:\src\panel\shared\reviewer-profile-loader.md` | 5-tier resolution chain + session caching for reviewer profiles |
| `C:\src\panel\shared\score-utils.md` | Score aggregation, consensus metrics |
| `C:\src\panel\shared\stage-machine.md` | Stage progression with gates |
| `C:\src\panel\shared\reviewer-selector.md` | Match reviewers to papers by expertise |
| `C:\src\panel\shared\panel-utils.md` | Module-level utilities |
| `C:\src\panel\shared\board-utils.md` | Board-level utilities |
| `C:\src\panel\shared\quality-checker.md` | Paper validation (baselines, limitations) |

### Reviewer Personas (51 reviewers)

| Path | Format | Content |
|------|--------|---------|
| `C:\src\panel\.roles\roles\panel-reviewer\R-1.md` through `R-51.md` | OLE frontmatter | 51 reviewer personas with orientation/lens/expertise |
| `C:\src\panel\context\panel\reviewers\profiles\` | Cached profiles | ~2KB each, session-cached for token efficiency |
| `C:\src\panel\context\panel\reviewers\_index.yaml` | Registry | Maps names to R-N IDs |

### Reviewer Categories (10)

1. Systems & Infrastructure
2. Compilers & PL Theory
3. AI Agents & Orchestration
4. Prompting & LLM Capabilities
5. Human-AI Interaction (HCI)
6. ML Systems & Efficiency
7. ML Research / Learning
8. Software Engineering & DevOps
9. NLP & Information Retrieval
10. Security & Safety

### Templates

| File | Purpose |
|------|---------|
| `C:\src\panel\templates\review-template.md` | Individual review structure |
| `C:\src\panel\templates\synthesis-template.md` | Synthesis document structure |
| `C:\src\panel\templates\revision-plan-template.md` | Revision plan structure |
| `C:\src\panel\templates\reviewer-profile-template.md` | Reviewer profile structure |

### Research Papers (self-documenting)

| Paper | Topic |
|-------|-------|
| `C:\src\panel\research\panel-review-methodology\` | AI-Simulated Expert Review methodology |
| `C:\src\panel\research\panel-reviewer-calibration\` | Calibrating AI personas without fine-tuning |
| `C:\src\panel\research\panel-revision-dynamics\` | Multi-round revision impact measurement |
| `C:\src\panel\research\panel-portfolio-assessment\` | Cross-portfolio expert panels |
| `C:\src\panel\research\panel-synthesis-methods\` | From reviews to revisions: automated synthesis |
| `C:\src\panel\research\panel-reviewer-profiles\` | Token-efficient persistent profiles |

## Architecture

```
Tier 3: Board (monorepo)     — 7-member board, 10-point scale, B1/B2/B3
  ├── Tier 2: Module (portfolio) — 7-member panel, 10-point scale, PP1/PP2/PP3
  │     └── Tier 1: Paper (individual) — 5-7 reviewers, 4-point scale, P1/P2/P3
```

## Token Efficiency

Persistent profiles reduce per-paper cost by 34.7%, module-level by 37.3%.
