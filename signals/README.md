# signals/

75 golden prompt bodies — one per Signal skill.

## What these are

Each file is the prompt body for one Signal skill. The skill wrapper in `program.yaml` (or any binding variant in `bindings/`) references these files via `body_file:` — the forge tool assembles the full skill from wrapper + body at generate time.

These are the convergent outputs of the quest loop: dozens of rubric-scored variation rounds, each improving on the last, until the prompt reliably produces high-quality signal artifacts.

## How they are used

`program.yaml` references each file:

```yaml
- name: scout-competitors
  body_file: signals/scout-competitors.md
  ...
```

Forge assembles the full skill file at install time. You do not edit these directly during normal use — run a quest loop round if a skill needs improvement.

## How to update

1. Run the quest loop for the skill (`tools/quest-run-one.sh <skill-name>`)
2. Score variations with the rubric (`simulations/quest/rubrics/`)
3. When a variation scores higher, promote it: copy the body into this directory
4. Re-run `forge generate --stage program` to rebuild the output

## Full skill list

See [docs/COMMANDS.md](../docs/COMMANDS.md) for the complete list of 75 skills across 9 namespaces.
