# /rhythm — Governance Cadences

## The short version

The rhythm namespace runs your governance cadences — the recurring reviews and decisions that
keep a feature on track. Status checks, story synthesis, decision campaigns, quality gates,
and brief generation. These are the beats your team keeps.

## Skills

| Command | Bare | Description |
|---------|------|-------------|
| `/rhythm-status` | `/status` | Topic coverage and commitment readiness check |
| `/rhythm-story` | `/story` | Synthesize all signals into a narrative arc |
| `/rhythm-decide` | `/decide` | Full pre-commitment decision campaign |
| `/rhythm-behavior` | `/behavior` | Behavioral simulation campaign (flow + trace) |
| `/rhythm-qa` | `/qa` | Quality assurance gate before commitment |
| `/rhythm-brief` | `/brief` | Campaign brief and narrative summary |

## When to use this namespace

Use rhythm skills at the **end of a signal-gathering session** or at regular cadences:
- Weekly: `/rhythm-status` to see coverage and gaps
- Before committing: `/rhythm-decide` to run the full decision campaign
- After shipping: `/rhythm-story` to capture the narrative arc

## Example workflow

```
/rhythm-status dark-mode      # What signals do we have? What's missing?
/rhythm-decide dark-mode      # Run the full decision campaign
/rhythm-qa dark-mode          # Quality gate: is evidence strong enough?
/rhythm-story dark-mode       # Synthesize the narrative for stakeholders
```

## What it produces

Artifacts in `simulations/rhythm/{topic}-{skill}-{date}.md`

## What's next

- [discover/](discover.md) — gather the signals before running rhythm
- [roles/](roles.md) — set up your org structure for governance reviews
- [validate/](validate.md) — validate with users before the decision rhythm
