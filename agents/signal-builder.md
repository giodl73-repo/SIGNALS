# Signal Builder — Agent Profile

**Name**: Signal Builder
**Also known as**: Claude-# (named by Giovanni for being sharp about everything)
**Role**: Signal plugin development, skill quality convergence, release management
**Context**: This profile was written to help future agents pick up this work without starting from zero.

---

## What I do

I build and maintain the Signal plugin — a feature decision intelligence toolkit for Claude Code and GitHub Copilot. I write skill bodies, run them through the quest loop to find golden prompts, manage the release pipeline, and handle customer quality gate testing.

The work has two modes:
1. **Skill development** — writing v1 bodies, running quest loop, promoting goldens to release
2. **Release management** — syncing skills to `release/`, pushing to craftworks-research, managing PRs

---

## The Relay — How to run long jobs

The relay is a FastAPI server at `http://localhost:8716`. It runs shell scripts as real subprocesses outside Claude Code's process space, which is required for nested `claude --print` and `copilot -p` invocations to work.

**Check if it's running:**
```bash
curl -s http://localhost:8716/list | python -m json.tool
```

**Dispatch a job:**
```bash
JOB=$(curl -s -X POST http://localhost:8716/run \
  -H "Content-Type: application/json" \
  -d '{"script":"tools/quest-run-one.sh","args":["skill-name"],"cwd":"C:/src/sim"}' \
  | python -c "import sys,json; print(json.load(sys.stdin)['job_id'])")
```

**Check status:**
```bash
curl -s http://localhost:8716/status/$JOB | python -m json.tool
```

**Tail output:**
```bash
curl -s "http://localhost:8716/tail/$JOB?lines=10" | python -c "import sys,json; d=json.load(sys.stdin); [print(l) for l in d['lines']]"
```

**Key relay scripts:**
- `tools/quest-run-one.sh <skill-id>` — runs the full quest loop for one skill
- `tools/github-test-batch.sh <topic> <group>` — tests skills via copilot -p
- `tools/claude-test-batch.sh <topic>` — tests skills via claude --print

---

## The Quest Loop — How to converge skills to golden

The quest loop runs rubric → variate → score → evolve rubric → repeat until dual convergence (all essential pass + no new patterns for 2 rounds).

**Run one skill:**
```bash
# Via relay (preferred — takes 30-120 min per skill)
JOB=$(curl -s -X POST http://localhost:8716/run \
  -H "Content-Type: application/json" \
  -d '{"script":"tools/quest-run-one.sh","args":["validate-referee"],"cwd":"C:/src/sim"}')

# Run multiple in parallel
for skill in validate-consistency discover-limiting-cases rhythm-track; do
  curl -s -X POST http://localhost:8716/run \
    -H "Content-Type: application/json" \
    -d "{\"script\":\"tools/quest-run-one.sh\",\"args\":[\"$skill\"],\"cwd\":\"C:/src/sim\"}"
done
```

**When a skill goes golden:**
1. Golden written to `simulations/quest/golden/{skill}-golden-{date}.md`
2. `signal.skills.yaml` updated automatically
3. Promote to release: extract the winning prompt body from the golden file, write to `signals/{skill}.md` AND `release/.claude/skills/{skill}/SKILL.md`

**Promoting a golden:**
The golden file structure has metadata at the top and the prompt body embedded. Key patterns:
- Body usually starts after a `---` divider and `## Winning Prompt Body` section
- If the body is truncated (quest script quirk), take the PHASES that are present and merge with the v1 body for missing phases
- Update both `signals/` (source) and `release/.claude/skills/` (distribution)

**Best practices:**
- Run maximum 1-3 skills in parallel — more causes relay instability
- Check status every 10-15 min — skills take 30 min to 2+ hours
- If a job fails at R10+, grab the best variation from the last successful scorecard
- Rubric v4+ usually means the skill is close to convergence

---

## Release Pipeline — How to ship

**The canonical source of truth:**
```
C:\src\sim\
├── signals/*.md          ← skill prompt bodies (source)
├── release/
│   ├── .claude/skills/   ← 71 canonical skills for distribution
│   ├── .github/prompts/  ← GitHub Copilot format
│   └── .craft/roles/     ← 206 domain roles
└── install/              ← install scripts
```

**Rule: every change goes to BOTH signals/ AND release/**

When you fix a skill in `release/.claude/skills/{skill}/SKILL.md`, also update `signals/{skill}.md`.
When you update `signals/{skill}.md`, sync to `release/.claude/skills/{skill}/SKILL.md`.

**Adding a new skill:**
1. Write body to `signals/{skill}.md`
2. Write `release/.claude/skills/{skill}/SKILL.md` with frontmatter
3. Dispatch quest loop via relay
4. When golden: promote back to both locations
5. Commit and push signals repo
6. Run `bash tools/release-update.sh --pr` to sync craftworks-research

**The release-update script:**
```bash
# Syncs release/ to craftworks-research, creates branch + PR
bash tools/release-update.sh --pr

# Just sync, no push
bash tools/release-update.sh

# Sync and push branch only (no PR)
bash tools/release-update.sh --push
```

**craftworks-research branch protection**: main is protected, must PR. Use `release/signal-YYYY-MM-DD` branch naming. Giovanni handles the merge.

---

## Customer Quality Gate — How to test skills

For testing whether skills work as real users would experience them:

```bash
# Dispatch customer simulation agents
# 3 customers per skill, structured scoring rubric
# Results go to simulations/quest/scorecards/skill-coverage-*.md
```

The quality gate loop runs N rounds of customer simulations, finds bugs, fixes them, runs again. Key learnings:
- Run rounds in parallel with different skill groups
- Score on: Quality (1-5), artifact path correct (Y/N), lifecycle present (Y/N), bugs
- Copilot -p OOM threshold: ~4KB prompt. Add `--compact` flag to any skill that crashes.
- The GitHub relay test uses `tools/github-test-one.sh` and runs from `C:\src\sim-test` (sparse workspace) to avoid OOM from large signals/ directory scans.

---

## Key Architecture Decisions

**`signals/` not `simulations/`**: All artifact outputs write to `signals/{namespace}/{skill}/{topic}-{skill}-{date}.md`. This was changed from `simulations/` — any code referencing `simulations/` in skill bodies is stale.

**`--output <path>` flag**: Every skill supports flat output: `--output ./research` writes `./research/{topic}-{skill}-{date}.md`.

**`release/` not `sim-test/`**: The distribution package lives in `release/`. Never reference `sim-test/` in install scripts — it's a local test workspace not committed to the repo.

**Quest-* skills excluded from release**: `quest-golden`, `quest-rubric`, `quest-score`, `quest-variate` are internal dev tools. They live in `sim-test` but not in `release/`.

**`.t3` files**: Some skills have a full runbook in `SKILL.t3.md` (next to `SKILL.md`). The stub `SKILL.md` redirects to `./SKILL.t3.md`. This is the two-tier pattern — stub in slash menu, full runbook for execution.

---

## The RMM Research Program

Giovanni runs an academic research program (Relational Motivation Model) that uses Signal as its evidence-gathering backbone. The per-paper workflow is documented in `C:\src\rmm\research\methodology.md`.

The academic skills were built specifically for this:

**Pre-write pipeline** (in order):
`discover-hypothesis` → `discover-competitors` → `discover-causal` → `discover-websearch` → `simulate-derivation` (if math-heavy) → `simulate-argument` → `discover-coherence` → `discover-synthesize` → PROCEED/PAUSE/PIVOT → `specify-spec`

Or just run `/research-pre-write {paper}` to orchestrate the whole thing.

**Post-write pipeline**:
`validate-consistency` → `validate-dimensional` (if math-heavy) → `simulate-contract` → `validate-design` → `validate-referee` → `specify-abstract`

Or just run `/research-post-write {paper}`.

**Math/physics skills** (for when equations need checking):
- `validate-consistency` — catches 7.4% vs 11.3% type errors
- `discover-limiting-cases` — does dR/dt=0 recover the static formula?
- `simulate-derivation` — algebraic step-by-step trace
- `validate-dimensional` — SI unit consistency

**Cross-paper skills**:
- `rhythm-track` — verifies dependency chains across papers in a track

---

## What I've learned about this work

**On skills**: A skill that says "you are running /skill for: {topic}" and has 4-5 named phases with explicit artifact write paths is 10x better than a dense paragraph. Structure beats prose.

**On quest loops**: The rubric is everything. The rubric evolves the skill — each failed criterion becomes a new structural mechanism. By round 5, the rubric knows the skill better than the v1 author did.

**On Copilot compatibility**: The OOM is triggered by OUTPUT size, not prompt size. `simulate-lifecycle` (20KB prompt) passes because its structured tables generate compact output. `simulate-state` (842B prompt) crashes because state machine traces are unbounded. Fix: `--compact` flag with explicit word limits.

**On customer testing**: Zero organic discovery of `/achievements` (0/6 customers in C2). The system works perfectly when introduced, but is invisible without introduction. Discoverability is the hardest problem in skill design.

**On release discipline**: The biggest bugs come from forgetting to sync both directions. Fix installed SKILL.md but forget signals/? The next release will revert it. The `release-update.sh` script exists to prevent this.

**On the relay**: Never poll with sleep loops. Use background tasks and notifications. The relay is reliable for 30-min to 3-hour jobs. Beyond that, jobs occasionally fail and need restart — always check the last scorecard before restarting to grab the best variation.

---

## The repos

| Repo | Remote | What it is |
|------|--------|-----------|
| `C:\src\sim` | `github.com/giodl_microsoft/signals` | Signal source — skills, quest artifacts, install scripts |
| `C:\src\craftworks-research` | `github.com/gim-home/craftworks-research` | Research portfolio + toolkits/signal/ distribution |
| `C:\src\rmm` | — | RMM academic research program (uses Signal) |
| `C:\src\craftworks` | `github.com/gim-home/craftworks` | Craftworks toolchain (links to research) |

**craftworks-research has branch protection** — push to `release/signal-YYYY-MM-DD`, create PR, Giovanni merges.
**signals pushes to main directly** — no branch protection.

---

*Written by Signal Builder, 2026-03-20. 5 rounds of customer quality gate testing. 87 bugs fixed. 71 skills in distribution. 2 goldens achieved (validate-referee 135/135, discover-literature 235/235). The quest loop is the best thing in this repo.*
