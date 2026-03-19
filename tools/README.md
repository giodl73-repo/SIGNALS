# tools/

Quest loop scripts and utility tools for Signal development.

## Quest loop scripts

**`quest-run-one.sh`** — Run a single skill through one quest loop round.

```bash
./tools/quest-run-one.sh scout-inertia
./tools/quest-run-one.sh flow-ratelimit --round 21
```

Produces: variation file in `simulations/quest/variations/`, rubric score in `simulations/quest/scorecards/`.

**`quest-resume.sh`** — Resume quest loop from the best available state for a skill.

```bash
./tools/quest-resume.sh scout-inertia
```

Finds the highest-scoring variation and round, then continues from there.

**`quest-run-all.sh`** — Run one round for all skills (batch mode). Slow; use for scheduled runs.

**`quest-test.sh`** — Run a quick smoke test on a skill without saving artifacts.

## Generator scripts

**`gen-commands.py`** — Regenerate `docs/COMMANDS.md` from `signal.skills.yaml`.

```bash
python tools/gen-commands.py
```

Run this whenever `signal.skills.yaml` changes (skills added, renamed, or retired).

**`claude-run.py`** — Claude `--print` wrapper that bypasses shell ARG_MAX limits.

Used internally by quest scripts when prompt bodies exceed shell argument length limits. Not typically called directly.

**`gen-binding-flat.py`** — Generate the flat binding variant from `program.yaml`.

## Other files

`build_v7_rubric.py` — legacy rubric builder, archived here for reference (do not use).
`qu5-standalone.sh` — standalone Q05 listen-adoption runner (historical).
