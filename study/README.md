# Signal Navigation Study — A/B/C/D/E Test

5 participants per variant. Task: use Signal to make a feature decision on a standard topic.

## Variants

| Variant | Binding | Entry | Install |
|---------|---------|-------|---------|
| A | grouped | `/scout` → menu | `cp -r study/variant-grouped/.claude .` |
| B | groups | `/discover` → 5 phases | `cp -r study/variant-groups/.claude .` |
| C | signal | `/signal <intent>` | `cp -r study/variant-signal/.claude .` |
| D | flat | `/scout-competitors` | `cp -r study/variant-flat/.claude .` |
| E | bare | `/competitors` | `cp -r study/variant-bare/.claude .` |

## Task (same for all variants)

> "Your team is considering building a dark mode feature for your product.
>  Use Signal to gather enough evidence to decide whether to build it.
>  You have 30 minutes."

## What to measure

1. **Time to first artifact** — when does simulations/ get its first file?
2. **Skill coverage at 30min** — how many namespaces touched?
3. **Error rate** — wrong command, had to backtrack (observe or ask)
4. **NPS** — "Would you use Signal again? 0-10"
5. **Which skill first** — what was their entry point?

## Study log template

```
Participant: ___  Variant: ___  Date: ___
First command typed: ___
Time to first artifact: ___ min
Artifacts produced: ___
Namespaces covered: ___
Error count: ___
NPS: ___
Notes: ___
```

## Pre-registered predictions (S3-12)

- C wins time-to-first-artifact
- E wins repeat-session speed
- A/B split by role (engineers→A, PMs→B)
- D is lowest error rate
