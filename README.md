# Signal — Know What You Know Before You Commit

**The primary competitor is always inertia.** Most features compete not against another product but against the world where the team simply doesn't ship anything new. Signal is feature decision intelligence for Claude Code and GitHub Copilot that takes that fact seriously: every `/discover-competitors` run scores "none / status quo" first, and scores it HIGH. If you cannot explain why inertia loses, the feature does not have a clear value case — and you should know that *before* you commit, not after.

62 skills across 9 namespaces, organized around the loop from *is this worth building?* to *what will users say after we ship?*

## Install

```bash
git clone https://github.com/giodl73-repo/SIGNALS
cd your-project
bash ../SIGNALS/install/install-flat.sh
```

Adds Signal context to `CLAUDE.md` automatically. First commands:

```
/discover-competitors <feature>   Scout inertia and named competitors
/discover-inertia <feature>       Why would teams do nothing instead?
/signal                           See all 62 commands
/rhythm-decide <feature>          Full pre-commitment decision campaign
```

Four install variants are available — flat (default), bare, grouped, and a GitHub Copilot binding. See [`install/README.md`](install/README.md) for which to choose.

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
1. /discover-competitors my-feature   Inertia is scored first, and HIGH
2. /discover-inertia my-feature       Why would teams do nothing instead?
3. /specify-spec my-feature           Write the spec
4. /rhythm-status my-feature          See what signals exist, readiness %
```

Start anywhere. Every skill is self-contained.

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
claude plugin marketplace add https://github.com/giodl73-repo/SIGNALS
claude plugin install signal
```

Commands: `/signal:discover competitors`, `/signal:specify spec`, `/signal:validate design`

---

## Docs

- **[QUICKSTART.md](docs/QUICKSTART.md)** — 5-step workflow, what a signal looks like
- **[PRINCIPLES.md](PRINCIPLES.md)** — 11 design principles
- **[docs/ACHIEVEMENTS.md](docs/ACHIEVEMENTS.md)** — 38 achievements. The most important: Falsified.
- **[install/README.md](install/README.md)** — which binding to choose

## Issues

- **GitHub Issues**: [github.com/giodl73-repo/SIGNALS/issues](https://github.com/giodl73-repo/SIGNALS/issues)
- **Discussions**: [github.com/giodl73-repo/SIGNALS/discussions](https://github.com/giodl73-repo/SIGNALS/discussions)

## Status

v1.0 beta · 62 skills · 9 namespaces · 206 domain roles

## License

[MIT](LICENSE) — © 2026 Gio Della-Libera.
