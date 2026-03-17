# /persona-walkthrough — Multi-Persona UX Verification

> Installed from sim/techniques/04 + signal:review-users skill.
> For: pacts S05 (progressive levels)

## Usage

```
/persona-walkthrough <topic> <spec>
```

## Protocol

5 persona advocates walk through a design from their user perspective. Each persona
narrates in first person, flags confusion/friction/fear/jargon with exact artifact
quotes, gives usability score 1-5.

### Personas

| Persona | Key Question | Perspective |
|---------|-------------|-------------|
| **Maker** | "Can I do this without reading a manual?" | Zero-config, fast start, no jargon |
| **Developer** | "Are outputs machine-parseable?" | JSON output, exit codes, piping, hooks |
| **Compliance** | "Would an auditor accept this?" | Audit trail, evidence, regulatory mapping |
| **Supervisor** | "Can I intervene in 30 seconds?" | Fleet oversight, approval gates, kill switch |
| **Operator** | "Would a Terraform user be confused?" | Infrastructure patterns, health checks, logs |

### Phase 1 — Walkthrough (per persona)

Each persona walks the feature independently. Narrate in first person:

```markdown
### {Persona Name} Walkthrough

**Starting context**: {what this persona already knows}

1. {First thing I try} → {what happens} → {my reaction}
2. {Next step} → {what happens} → {confusion/friction/fear/delight}
...

**Friction points**:
- F1: "{exact quote from spec/artifact}" — {why this is confusing for me}
- F2: ...

**Usability score**: {1-5}/5
**Would I adopt?**: {yes/no/maybe} — {why}
```

### Phase 2 — Cross-Persona Synthesis

| Finding | Personas | Type | Severity |
|---------|----------|------|----------|
| Universal friction (3+ personas flag same thing) | ... | blocking/major/minor | ... |
| Role-specific friction (1 persona, valid concern) | ... | major/minor | ... |
| Persona conflict (helps one, hurts another) | ... | design tension | ... |

### Phase 3 — Aggregate Score

| Persona | Score | Would Adopt? | Top Friction |
|---------|-------|-------------|-------------|
| Maker | /5 | | |
| Developer | /5 | | |
| Compliance | /5 | | |
| Supervisor | /5 | | |
| Operator | /5 | | |
| **Average** | /5 | | |

**Gate**: No persona below 3/5. If any score below 3, iterate (amend phase).

## Output

Write to the scenario directory:
- `SCENARIO.md` — full walkthrough per persona + synthesis
- `TRACE.md` — aggregate score table + universal friction list
