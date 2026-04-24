# simulations/

All signal artifacts and quest loop history. This directory grows as skills run.

## Subdirectories

### quest/ — Quest loop artifacts

The quest loop iterates skill prompts through rubric scoring to convergence. All intermediate state lives here.

- **`quest/golden/`** — Final golden prompts: the best-scoring variation for each skill, promoted from variations/. These are the source of truth for `signals/`.
- **`quest/rubrics/`** — Rubric evolution history: every rubric version for every skill, date-stamped. Shows how evaluation criteria improved.
- **`quest/variations/`** — All variation files (N per skill per round): the raw output of each quest loop iteration before scoring.
- **`quest/scorecards/`** — Scoring results: rubric-scored outputs, one per round per skill. Shows score progression toward convergence.
- **`quest/archive/scripts/`** — Historical quest loop helper scripts (Python). Provenance record of how the loop was built.

### Skill artifact directories

Each namespace has a subdirectory matching the signal artifact path:

- **`discover/`**, **`specify/`**, **`validate/`**, **`simulate/`** — Skill outputs organized by namespace and skill name
- **`rhythm/`**, **`roles/`** — Campaign and org workflow artifacts

Artifact naming: `{topic}-{signal}-{date}.md`. Glob `{topic}-*` to find all signals for a topic across all directories.

### Research

- **`ai-simulation-techniques/`** — External research on AI simulation techniques. Background material for technique design.

## TOPICS.md

`simulations/TOPICS.md` is the topic registry. `/topic-new` registers here. `/topic-status` reads here for strategy vs. coverage comparison.
