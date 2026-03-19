# Signal — Know What You Know Before You Commit

Pre-commitment evidence tool for feature teams. 9 namespaces. 69 skills. The primary competitor is always inertia.

## What it is

Signal is a Claude Code plugin for gathering evidence before you commit to building something. You run skills across 9 namespaces — scout the market, draft the spec, trace the runtime behavior, prove the core hypothesis, simulate adoption. When you have enough signals, `/topic-status` tells you you are ready. The primary competitor is always inertia: the first thing every investigation answers is why teams would do nothing instead.

## Install

```bash
git clone https://github.com/your-org/signal .signal-src && cd .signal-src
```

Choose a binding — each installs the same 60 skills with different invocation names.
Preview what you'll get, then run the install.

---

### Binding A — Bare (shortest names)

```
discover  /competitors  /feasibility  /risk  /inertia  /hypothesis  /websearch
          /analysis  /synthesize  /orchestrate  /brainstorm  /causal  /coherence
          /compare  /competitors-alt  /feasibility-alt
specify   /spec  /proposal  /pitch  /commitment
validate  /design  /code  /users  /customers  /feedback  /support  /adoption  /inertia
simulate  /lifecycle  /conversation  /stress  /contract  /state  /permissions  /request
rhythm    /status  /story  /decide  /behavior  /qa  /brief
roles     /scan  /build  /chart  /generate  /create  /check  /committee
          /product-review  /pull-request
signal    /check
tools     /coverage  /preview  /accept
```

```bash
./install/install-bare.sh            # Claude Code  → .claude/skills/
./install/install-bare-github.sh     # GitHub Copilot → .github/prompts/
```

---

### Binding B — Flat (namespace-prefixed, default)

```
/discover-competitors   /discover-feasibility   /discover-risk   /discover-inertia
/specify-spec           /specify-proposal        /specify-pitch   /specify-commitment
/validate-design        /validate-customers      /validate-users  /validate-adoption
/simulate-contract      /simulate-state          /simulate-lifecycle
/rhythm-status          /rhythm-story            /rhythm-decide
/roles-scan             /roles-build             /roles-pull-request  ...60 total
```

```bash
./install/install-flat.sh            # Claude Code
./install/install-flat-github.sh     # GitHub Copilot
```

---

### Binding C — Signal-prefix (multi-plugin safe)

Same 60 skills, every command prefixed with `signal-`:

```
/signal-competitors   /signal-spec   /signal-decide   /signal-contract  ...60 total
```

```bash
./install/install-signal.sh          # Claude Code
./install/install-signal-github.sh   # GitHub Copilot
```

---

### Binding D — Grouped (namespace menus)

Adds namespace aggregators — type `/discover` to see all discover skills, or go direct:

```
/discover             → shows menu of all 15 discover skills
/discover-competitors → runs directly (also available)
/rhythm               → shows menu of 6 rhythm skills
/roles                → shows menu of 9 roles skills
... + all 60 individual skills
```

```bash
./install/install-grouped.sh         # Claude Code
./install/install-grouped-github.sh  # GitHub Copilot
```

---

### Not sure which to pick?

| If you... | Use |
|-----------|-----|
| Want the shortest possible commands | **bare** — `/decide`, `/competitors` |
| Want to see the namespace on each command | **flat** — `/discover-competitors` |
| Share `.claude/skills/` with other plugins | **signal** — `/signal-competitors` |
| Prefer menus over memorizing names | **grouped** — `/discover` shows all |
| Use GitHub Copilot | add `-github` to any of the above |

## The 9 namespaces

| Namespace | What it answers | Example skill |
|-----------|----------------|---------------|
| `scout` | Who else does this? Is it feasible? What does the market look like? | `/scout-competitors` |
| `draft` | What exactly are we building? | `/draft-spec` |
| `review` | Does this design work for real users and teams? | `/review-design` |
| `flow` | How does this actually behave at runtime? | `/flow-lifecycle` |
| `trace` | Does the implementation match the spec? | `/trace-contract` |
| `prove` | Is our core assumption correct? | `/prove-hypothesis` |
| `listen` | Will teams actually adopt this? What blocks them? | `/listen-adoption` |
| `program` | What are we committing to? What is the staged plan? | `/program-plan` |
| `topic` | Are we ready to commit? What signals are missing? | `/topic-status` |

Two additional namespaces for teams with org configuration:

| Namespace | What it answers |
|-----------|----------------|
| `corps` | Org chart, ROB, PR review through the full org structure |
| `crew` | Review any artifact through your compiled team roles |

## How it works

Four steps from idea to first read on readiness:

```
1. /topic-new payment-reminders      Register topic, plan the investigation
2. /scout-competitors payment-reminders   Scout inertia and named competitors
3. /prove-hypothesis payment-reminders   State the core assumption and what would falsify it
4. /topic-status payment-reminders       See what signals exist, what is missing, readiness %
```

You do not have to start at step 1. Start where the pain is.

| Situation | Start here |
|-----------|-----------|
| Feature idea, don't know if it's worth building | `/scout-competitors` |
| Spec written, want a design review | `/review-design` |
| Implementation done, want to verify it matches spec | `/trace-contract` |
| Shipped, adoption is low | `/listen-adoption` |
| Core assumption needs testing | `/prove-hypothesis` |

Every skill writes one dated artifact: `simulations/{namespace}/{skill}/{topic}-{signal}-{date}.md`. Two people running the same skill on the same topic produce two files, no collision. Skills are concurrent by default.

## 6 install variants

| Binding | Commands | Invocation | When to use |
|---------|---------|-----------|-------------|
| **bare** | 75 atomic skills, bare stems | `/decide`, `/competitors`, `/hypothesis` | Signal is your only plugin; shortest typing |
| **flat** (default) | 75 atomic skills | `/scout-competitors`, `/campaign-decide` | Default for all installs; teams that know the namespace model |
| **signal** | 75 skills as `/signal-*` | `/signal-decide`, `/signal-competitors` | Multi-plugin workspaces where short names collide |
| **grouped** | 75 skills + namespace menus | `/scout` shows menu, `/campaign` shows campaigns | Onboarding; teams who describe intent and want routing |
| **prefixed** | 75 skills as `/signal-*` + aggregators | `/signal-scout-competitors`, `/signal-decide` | Full namespace + campaign coverage with collision safety |
| **domains** | 6 campaign commands + 75 skills | `/decide`, `/simulate`, `/validate`, `/specify`, `/evidence`, `/track` | PMs and execs who think in outcomes; sprint kickoffs |

Claude Code install scripts: `install/install-bare.sh`, `install/install-flat.sh`, `install/install-signal.sh`, `install/install-grouped.sh`, `install/install-prefixed.sh`, `install/install-domains.sh`

GitHub Copilot install scripts: `install/install-bare-github.sh`, `install/install-flat-github.sh`, `install/install-signal-github.sh`, `install/install-grouped-github.sh`, `install/install-prefixed-github.sh`, `install/install-domains-github.sh`

## The inertia rule

Every `/scout-competitors` run assesses "none / status quo" first, always. Inertia is not one competitor among many — it is the primary competitor, scored threat HIGH by default. The inertia case answers: why would a team do nothing? What does the status quo workaround cost them? Is that cost lower than the switching cost of adopting something new? If you cannot write a paragraph explaining why inertia loses, your feature does not have a clear value case yet. Signal surfaces this in 10 minutes, not 3 weeks.

## Docs

- **[QUICKSTART.md](docs/QUICKSTART.md)** — First run walkthrough. The minimal workflow. What a signal looks like.
- **[Namespace guides](docs/guides/)** — Deep coverage of each namespace, all skills, parameters, artifact examples. 19 guides: 9 namespaces, 2 org namespaces, 4 campaigns, 4 concepts.
- **[ACHIEVEMENTS.md](docs/ACHIEVEMENTS.md)** — 31 achievements across 7 categories. The most important one is Falsified.
- **[PRINCIPLES.md](PRINCIPLES.md)** — 10 design principles: concurrent by default, append-only artifacts, self-contained skills, namespace = audience, zero barrier to first run.
- **[COMMANDS.md](docs/COMMANDS.md)** — Complete skill reference: all 75 skills across 9 namespaces with invocation examples.

## Directory guide

| Directory | What's in it |
|-----------|-------------|
| [docs/](docs/QUICKSTART.md) | Guides, QUICKSTART, COMMANDS, ACHIEVEMENTS, philosophy |
| [install/](install/README.md) | 12 install scripts for 6 bindings x 2 platforms |
| [signals/](signals/README.md) | 75 golden prompt bodies, one per Signal skill |
| [simulations/](simulations/README.md) | Quest loop artifacts, skill outputs, topic registry |
| [bindings/](bindings/README.md) | 6 program.yaml binding variants |
| [tools/](tools/README.md) | Quest loop scripts and generator utilities |
| [.craft/](.craft/README.md) | 206 expert role files organized by domain |
| [experiments/](experiments/README.md) | Parameter study data (S2-04, S2-06) |
| [study/](study/README.md) | A/B/C/D/E navigation test |
| [output/](output/README.md) | Generated forge output — run forge generate to update |

## Research

27+ papers documenting Signal's methodology are in `C:\src\craftworks-research\signals\`. See the [research module README](../../craftworks-research/signals/MODULE.md) for the full index.

## Feedback & Issues

Found a bug? Unexpected output? Improvement idea?

- **In Claude Code**: `/signal-feedback` — formats and submits a GitHub issue directly
- **GitHub Issues**: [github.com/gim-home/signal/issues](https://github.com/gim-home/signal/issues)
- **Discussions**: [github.com/gim-home/signal/discussions](https://github.com/gim-home/signal/discussions)

## License / status

v0.1 beta — 2026-03-16

Signal is not released yet. The skill catalog is complete (69 skills, 13 namespaces). The core binding is built and installed. Golden prompt convergence is ongoing.
