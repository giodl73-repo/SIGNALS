# Signal Release Plan — craftworks-research

## What exists today

| Location | What it is | Status |
|----------|-----------|--------|
| `C:\src\sim` | Signal source repo (skills, signals, install scripts, tests) | DONE |
| `craftworks-research/signals/papers/` | 35 research papers (S1-S4, T5 tracks) | DONE |
| `craftworks-research/signals/MODULE.md` | Research module design doc | DONE |
| `craftworks-research/README.md` | Research portfolio overview | NEEDS UPDATE |

## What to create

### 1. `craftworks-research/signal/` — the distributable plugin

One new top-level directory. Users clone craftworks-research and run the install from here.

```
craftworks-research/
└── signal/                          ← NEW (the plugin home)
    ├── README.md                    ← What it is + 3-step install
    ├── QUICKSTART.md                ← From sim/docs/QUICKSTART.md
    ├── PRINCIPLES.md                ← From sim/PRINCIPLES.md
    ├── ACHIEVEMENTS.md              ← From sim/docs/ACHIEVEMENTS.md
    │
    ├── install/                     ← Copy from sim/install/
    │   ├── install-flat.sh          ← Claude Code flat binding
    │   ├── install-flat-github.sh   ← GitHub Copilot flat binding
    │   ├── install-bare.sh
    │   ├── install-grouped.sh
    │   ├── install-prefixed.sh
    │   └── README.md               ← Which binding to choose
    │
    ├── .claude/
    │   └── skills/                  ← Copy from sim-test/.claude/skills/
    │       ├── discover-competitors/
    │       │   └── SKILL.md
    │       └── ... (62 skills)
    │
    ├── .github/
    │   └── prompts/                 ← Copy from sim-test/.github/prompts/
    │       ├── discover-competitors.prompt.md
    │       └── ... (219 .prompt.md files)
    │
    ├── .roles/
    │   └── roles/                   ← Copy from sim/.roles/
    │       ├── architect.md
    │       └── ... (206 role files)
    │
    └── docs/                        ← From sim/docs/
        ├── QUICKSTART.md
        ├── guides/
        └── philosophy.md
```

### 2. Update `craftworks-research/README.md`

Add two sections:

**A) Under "How the research fits together" box** — upgrade the "Signals" line to reference both the research AND the plugin:

```
Signals — enforcement archetypes, quest loop, AI-first dev methodology, Signal plugin (62 skills)
```

**B) Add a new "Using Signal" section** (after the existing research sections) that:
- Links to `signal/` as the installable plugin
- Shows the 3-command quick start
- Links to the research papers that explain why it works
- Notes GitHub Copilot compatibility (71% pass, 85% with --compact)

**C) Expand the "Prompt Engineering & Skill Design — Signals" section** to document our research body:

From MODULE.md, we have 4 tracks + T5:
- Track 1 (S1): 4 papers on enforcement archetypes
- Track 2 (S2): 10 papers on the quest loop
- Track 3 (S3): 12 papers on the plugin design (pre-commitment, inertia, flow simulation, org-as-code, achievements)
- Track 4 (S4): 3 papers on mock infrastructure and fidelity gaps
- Track T5: 4 papers on signal as evaluation methodology

Plus the customer quality gate work (5 rounds, 60 customers, 87 bugs fixed) and the GitHub Copilot relay tests.

## Steps to execute

1. **Copy source files** from sim → craftworks-research/signal/
   - Install scripts (sim/install/*.sh)
   - Skill files (sim-test/.claude/skills/)
   - GitHub Copilot prompts (sim-test/.github/prompts/)
   - Role registry (sim/.roles/)
   - Docs (sim/docs/QUICKSTART.md, sim/PRINCIPLES.md, sim/docs/ACHIEVEMENTS.md)

2. **Write craftworks-research/signal/README.md** — the plugin landing page

3. **Update craftworks-research/README.md** — add Signal sections

4. **Do NOT copy**: sim/simulations/ (quest artifacts), sim/tools/ (dev tools), sim/signal.skills.yaml (internal), sim/bindings/ (forge inputs)

## What the install looks like (from a user's perspective)

```bash
# Clone the research repo
git clone https://github.com/your-org/craftworks-research
cd your-project

# Install Signal (flat binding — recommended)
bash ../craftworks-research/signal/install/install-flat.sh

# OR install GitHub Copilot prompts
bash ../craftworks-research/signal/install/install-flat-github.sh

# First commands
/discover-competitors my-feature
/signal-health
```

## Notes on what NOT to include

- `sim/simulations/` — quest loop artifacts, test scorecards (internal research, not user-facing)
- `sim/tools/` — relay test scripts, quest-run-one.sh (dev tools, not user-facing)
- `sim/bindings/*.program.yaml` — forge inputs (users don't need to compile)
- `sim/signal.skills.yaml` — skill registry tracker (internal)
- `sim-test/` — test workspace (internal)
- `.github/prompts/*.prompt.md` > 4.5KB without --compact instruction may OOM copilot CLI
