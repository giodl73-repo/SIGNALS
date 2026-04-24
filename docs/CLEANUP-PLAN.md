# Signal Repo Cleanup Plan

**Goal**: Every file reachable from README.md through transitive closure of README.md files.
**Rule**: If you can't navigate to it from README.md, it either moves or gets deleted.

---

## The mess (audit findings)

### Critical: 90+ stray Python scripts at root
All `_write_*.py`, `_build_*.py`, `_append_*.py`, `_gen_*.py` files are one-off quest loop
helpers that escaped into root. They have no business being at root level.
**Action: archive to `simulations/quest/archive/scripts/` or delete**

### Broken filename paths at root
`C:srcsimsimulationsquestgoldenquest-score-variate-R3-2026-03-16.md` etc — these are
Windows path artifacts from failed writes. Not real files.
**Action: delete**

### Stray root .md files not linked from README
- `ai-first-development-philosophy.md` → should be in `docs/`
- `plugin-plan.md` → should be in `docs/` or archived
- `PROMPT-HANDOVER.md` → archived (was for session handover, now superseded by CLAUDE.md)
- `signal.bindings.md` → should be in `docs/` or `bindings/`
- `SIGNAL.md` → workspace context file, keep at root but link from README
- `signal.program.yaml` → superseded by `program.yaml`, delete or move to `bindings/`

### Test directories at root
- `test-craft-make/` → delete (temporary test)
- `test-craft-new/` → delete
- `output-github/` → temporary, merge into `output/` structure

### Directories with no README
- `simulations/` ← huge, no README
- `signals/` ← 60 golden prompt files, no README
- `install/` ← 12 scripts, no README
- `tools/` ← quest loop scripts, no README
- `experiments/` ← S2-04/S2-06 experiment data, no README
- `findings/` ← signal findings, no README
- `from-contract/`, `from-intent/`, `from-program/` ← future work stubs, no README
- `output/` ← forge generate output, no README
- `.roles/` ← roles registry, no README

---

## The target structure (navigable)

```
README.md                    ← links to: docs/, install/, signals/, simulations/, .roles/
  ↓
docs/
  README.md                  ← links to: QUICKSTART, COMMANDS, guides/, ACHIEVEMENTS, MANIFEST, ROLE-MAPPING
  QUICKSTART.md
  COMMANDS.md
  ACHIEVEMENTS.md
  MANIFEST.md
  ROLE-MAPPING.md
  guides/
    README.md                ← lists all 8 namespace guides
    discover.md  specify.md  validate.md  simulate.md
    rhythm.md    roles.md    signal.md    tools.md    evals.md
  philosophy.md              ← moved from root ai-first-development-philosophy.md
  bindings.md                ← moved from root signal.bindings.md

install/
  README.md                  ← explains all 12 install scripts + role installer
  install-bare.sh ... (12 scripts)
  install-roles.sh

signals/
  README.md                  ← "60 golden prompt bodies, one per skill"
  discover-competitors.md ... (60 files)

bindings/
  README.md                  ← already exists ✓
  binding-flat.program.yaml ... (6 files)

simulations/
  README.md                  ← explains quest/discover/specify/validate/etc subdirs
  quest/
    README.md                ← golden prompts, rubrics, variations, scorecards
    golden/
    rubrics/
    variations/
    scorecards/
    archive/                 ← stray scripts moved here
  ai-simulation-techniques/  ← external research
  discover/  specify/  validate/  simulate/  (skill artifacts)

.roles/
  README.md                  ← explains roles/ structure, how to add roles
  roles/                     ← 206 role files
  compiler.yaml
  craft.json

tools/
  README.md                  ← quest-run-one.sh, quest-resume.sh, gen-commands.py
  quest-run-one.sh
  quest-resume.sh
  gen-commands.py
  claude-run.py

experiments/
  README.md                  ← S2-04 and S2-06 experiment data
  S2-04-floor-variation/
  S2-06-confidence-floor/

study/
  README.md                  ← already exists ✓ (A/B/C/D/E navigation study)

output/
  README.md                  ← "forge generate output, see install/ to use these"
  T1/
```

---

## Actions (in order)

1. **Delete**: test dirs, broken path filenames, `output-github/`
2. **Archive**: 90 root Python scripts → `simulations/quest/archive/scripts/`
3. **Move**: root .md files to `docs/` (`ai-first-development-philosophy.md` → `docs/philosophy.md`, `signal.bindings.md` → `docs/bindings.md`, `plugin-plan.md` → `docs/history/plugin-plan.md`)
4. **Delete**: `PROMPT-HANDOVER.md`, `signal.program.yaml` (superseded)
5. **Add README.md** to: `simulations/`, `signals/`, `install/`, `tools/`, `experiments/`, `findings/`, `.roles/`, `output/`
6. **Update root README.md** to link all major directories
7. **Customer test**: simulate new user navigating from README.md, verify they can find everything

---

## Customer test protocol

A new user lands at README.md. They should be able to answer these questions by following links:
1. How do I install Signal? (README → install/README → install-bare.sh)
2. What skills are available? (README → docs/COMMANDS.md)
3. What is inertia-first? (README → docs/QUICKSTART.md → docs/guides/discover.md)
4. How do I create a role? (README → docs/guides/roles.md → .roles/README → .roles/)
5. What are the golden prompts? (README → signals/README → signals/discover-competitors.md)
6. How do I run a product review? (README → docs/guides/rhythm.md)
7. What is the A/B navigation study? (README → study/README)
8. What research papers exist? (README → ??? ← GAP: no link to craftworks-research)

---

## Estimated scope
- Delete: ~100 files (stray scripts + test dirs + broken paths)
- Move: ~8 files
- Add README.md: ~9 directories
- Update: README.md (root), docs/README.md
- Time: 30 min

**Status**: PLAN (not yet applied)
