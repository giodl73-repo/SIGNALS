# output/

Generated output from `forge generate`. Do not edit files here directly — they are regenerated on each forge run.

## T1/ — Claude Code format, all bindings

Assembled skill files for all 6 binding variants, ready for deployment.

Structure mirrors the install target: `.claude/skills/` layout per binding.

## Subdirectories by binding

- `binding-flat/` — flat binding output (`/scout-competitors` etc.)
- `binding-bare/` — bare binding output (`/competitors` etc.)
- `binding-grouped/` — grouped binding with namespace menus
- `binding-prefixed/` — prefixed binding (`/signal-scout-competitors`)
- `binding-domains/` — domain campaign entry points

## How to regenerate

```bash
forge generate --stage program
```

Or regenerate a specific binding:

```bash
forge generate --binding flat
```

## How to deploy

After regenerating, use the install scripts to copy to a project:

```bash
./install/install-flat.sh /path/to/my-project
```

See [install/README.md](../install/README.md) for full install instructions.
