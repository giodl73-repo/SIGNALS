# Signal — Know What You Know Before You Commit

Pre-commitment evidence tool for feature teams. 9 namespaces. 69 skills. The primary competitor is always inertia.

## What it is

Signal is a Claude Code plugin for gathering evidence before you commit to building something. You run skills across 9 namespaces — scout the market, draft the spec, trace the runtime behavior, prove the core hypothesis, simulate adoption. When you have enough signals, `/topic-status` tells you you are ready. The primary competitor is always inertia: the first thing every investigation answers is why teams would do nothing instead.

## Install

```bash
# Clone the repo
git clone https://github.com/your-org/signal .signal-src
cd .signal-src
```

### Claude Code

Pick the binding that fits your team's style:

```bash
# Bare — shortest possible names (/decide, /competitors, /hypothesis)
./install/install-bare.sh

# Flat — namespace-prefixed names (/scout-competitors, /draft-spec)
./install/install-flat.sh

# Signal-prefix — /signal-decide, /signal-competitors (multi-plugin repos)
./install/install-signal.sh

# Grouped — namespace menus (/scout shows all scout skills)
./install/install-grouped.sh

# Prefixed — full /signal-scout-competitors names
./install/install-prefixed.sh

# Domains — campaign entry points (/decide, /simulate, /validate)
./install/install-domains.sh
```

### GitHub Copilot

```bash
# Bare — decide.prompt.md, competitors.prompt.md
./install/install-bare-github.sh

# Flat — scout-competitors.prompt.md, draft-spec.prompt.md
./install/install-flat-github.sh

# Signal-prefix — signal-competitors.prompt.md, signal-decide.prompt.md
./install/install-signal-github.sh

# Grouped — namespace dispatch prompts
./install/install-grouped-github.sh

# Prefixed — signal-scout-competitors.prompt.md prompts
./install/install-prefixed-github.sh

# Domains — decide.prompt.md, simulate.prompt.md, validate.prompt.md
./install/install-domains-github.sh
```

### Not sure which to pick?

| If you... | Use |
|-----------|-----|
| Want the simplest possible invocation | `install-bare.sh` -> `/decide`, `/competitors` |
| Want to see which namespace each skill is in | `install-flat.sh` -> `/scout-competitors` |
| Want `signal-` prefix (multi-plugin repos) | `install-signal.sh` -> `/signal-decide` |
| Want namespace menus | `install-grouped.sh` -> `/scout` shows all scout skills |
| Use GitHub Copilot | any `*-github.sh` variant |

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
- **[Namespace guides](docs/guides/)** — Deep coverage of each namespace, all skills, parameters, artifact examples. 11 guides: scout, draft, review, flow, trace, prove, listen, program, topic, corps, crew.
- **[ACHIEVEMENTS.md](docs/ACHIEVEMENTS.md)** — 31 achievements across 7 categories. The most important one is Falsified.
- **[PRINCIPLES.md](PRINCIPLES.md)** — 10 design principles: concurrent by default, append-only artifacts, self-contained skills, namespace = audience, zero barrier to first run.

## Feedback & Issues

Found a bug? Unexpected output? Improvement idea?

- **In Claude Code**: `/signal-feedback` — formats and submits a GitHub issue directly
- **GitHub Issues**: [github.com/gim-home/signal/issues](https://github.com/gim-home/signal/issues)
- **Discussions**: [github.com/gim-home/signal/discussions](https://github.com/gim-home/signal/discussions)

## License / status

v0.1 beta — 2026-03-16

Signal is not released yet. The skill catalog is complete (69 skills, 13 namespaces). The core binding is built and installed. Golden prompt convergence is ongoing.
