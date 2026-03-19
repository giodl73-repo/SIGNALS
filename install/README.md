# install/

12 install scripts for 6 bindings x 2 platforms (Claude Code + GitHub Copilot), plus a role installer.

## Prerequisites

- Claude Code installed and available on PATH
- Repository cloned: `git clone https://github.com/your-org/signal .signal-src`

## Which binding to choose

See the [binding table in QUICKSTART.md](../docs/QUICKSTART.md#the-minimal-workflow) or pick from this summary:

| Script | Commands installed | Use when |
|--------|--------------------|----------|
| `install-bare.sh` | `/decide`, `/competitors`, `/hypothesis` | Signal is your only plugin; shortest typing |
| `install-flat.sh` | `/scout-competitors`, `/draft-spec` | Default; teams that know the namespace model |
| `install-signal.sh` | `/signal-decide`, `/signal-competitors` | Multi-plugin repos where short names collide |
| `install-grouped.sh` | `/scout` (shows menu), `/campaign` | Onboarding; describe intent and get routing |
| `install-prefixed.sh` | `/signal-scout-competitors` | Full namespace + campaign coverage, collision-safe |
| `install-domains.sh` | `/decide`, `/simulate`, `/validate` | PMs and execs who think in outcomes |

GitHub Copilot variants: `install-*-github.sh` — same 6 bindings, installs `.prompt.md` files instead.

## What a successful install looks like

After running any `install-*.sh`:

- Skills are written to `.claude/skills/` in the current project directory
- Run `ls .claude/skills/ | wc -l` — expect 75 skill files (plus namespace menus for grouped/prefixed)
- Test with `/topic-status test-topic` — should produce a coverage readout with no errors

## Role installer

`install-roles.sh` installs expert role files from `.craft/roles/` into your project.

```bash
# Install all 206 roles
./install/install-roles.sh

# Install a domain subset
./install/install-roles.sh --domain engineering
./install/install-roles.sh --domain product
```

See [.craft/README.md](../.craft/README.md) for the full roles structure.
