# Signal — Know What You Know Before You Commit

Feature decision intelligence for Claude Code and GitHub Copilot. 62 skills across 9 namespaces. The primary competitor is always inertia.

## Install

```bash
git clone https://github.com/giodl_microsoft/signals
cd your-project
bash ../signals/install/install-flat.sh
```

Adds Signal context to `CLAUDE.md` automatically. First commands:

```
/discover-competitors <feature>   Scout inertia and named competitors
/discover-inertia <feature>       Why would teams do nothing instead?
/signal                           See all 62 commands
/rhythm-decide <feature>          Full pre-commitment decision campaign
```

---

## 4 install variants

| Binding | Commands | Install |
|---------|----------|---------|
| **flat** (default) | `/discover-competitors`, `/specify-spec` | `install/install-flat.sh` |
| **bare** | `/competitors`, `/spec`, `/design` | `install/install-bare.sh` |
| **grouped** | `/discover` menu + direct | `install/install-grouped.sh` |
| **GitHub Copilot** | `.github/prompts/` | `install/install-flat-github.sh` |

```bash
# Domain roles (optional — richer signal output)
bash install/install-roles.sh --domain dynamics   # Dynamics 365 (13 roles)
bash install/install-roles.sh --domain msft       # MSFT internal (5 roles)
bash install/install-roles.sh --domain flask      # Flask/Python (3 roles)
```

---

## The 9 namespaces

| Namespace | What it answers | Key skills |
|-----------|----------------|------------|
| **discover** | Is this worth building? Who competes with inertia? | competitors, inertia, feasibility, hypothesis, risk |
| **specify** | What exactly are we building? | spec, proposal, pitch, commitment |
| **validate** | Does this hold up under review? Will users adopt it? | design, code, users, customers |
| **simulate** | How does it behave at runtime? | lifecycle, request, state, contract |
| **prove** | Is our core assumption actually true? | hypothesis, websearch, analysis, synthesize |
| **listen** | What will users say after we ship? | adoption, feedback, support |
| **rhythm** | Are we ready to commit? What's the story? | status, decide, story, qa, brief |
| **roles** | What does the org think? | scan, check, product-review, pull-request |
| **tools** | Workspace health and coverage? | health, coverage, layout |

---

## How it works

```
1. /discover-competitors my-feature   The primary competitor is always inertia
2. /discover-inertia my-feature       Why would teams do nothing instead?
3. /specify-spec my-feature           Write the spec
4. /rhythm-status my-feature          See what signals exist, readiness %
```

Start anywhere. Every skill is self-contained.

**The inertia rule**: Every `/discover-competitors` run assesses "none / status quo" first. Inertia is the primary competitor, always scored HIGH. If you cannot explain why inertia loses, the feature does not have a clear value case.

---

## Artifacts

Every skill writes one dated artifact:

```
signals/discover/competitors/my-feature-competitors-2026-03-19.md
```

Use `--output <path>` to write anywhere flat:

```
/discover-competitors my-feature --output ./research
# → ./research/my-feature-competitors-2026-03-19.md
```

---

## Claude Code plugin

```bash
claude plugin marketplace add https://github.com/giodl_microsoft/signals
claude plugin install signal
```

Commands: `/signal:discover competitors`, `/signal:specify spec`, `/signal:validate design`

---

## Docs

- **[QUICKSTART.md](docs/QUICKSTART.md)** — 5-step workflow, what a signal looks like
- **[PRINCIPLES.md](PRINCIPLES.md)** — 11 design principles
- **[docs/ACHIEVEMENTS.md](docs/ACHIEVEMENTS.md)** — 38 achievements. The most important: Falsified.
- **[install/README.md](install/README.md)** — which binding to choose

## Research

35 papers on Signal's methodology in [`craftworks-research/signals/papers/`](https://github.com/gim-home/craftworks-research).

## Issues

- **GitHub Issues**: [github.com/giodl_microsoft/signals/issues](https://github.com/giodl_microsoft/signals/issues)
- **Discussions**: [github.com/giodl_microsoft/signals/discussions](https://github.com/giodl_microsoft/signals/discussions)

## Status

v1.0 beta · 62 skills · 9 namespaces · 206 domain roles

## License

[MIT](LICENSE) — © 2026 Gio Della-Libera.
